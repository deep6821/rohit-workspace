"""
### File Description: `tableau_connector.py`

This module provides a comprehensive solution for connecting to and querying data from Tableau Server. It includes functionality for loading configuration files, reading data from files, extracting and merging workbook data, and retrieving view data from Tableau Server.

### Imports
- `pandas as pd`: For data manipulation and analysis.
- `yaml`: For parsing YAML configuration files.
- `sqlalchemy.create_engine`: For creating SQLAlchemy engine connections (not used directly in this script but included).
- `tableau_api_lib.TableauServerConnection`: For creating and managing Tableau Server connections.
- `tableau_api_lib.utils.querying`: For querying data from Tableau Server.
- `tableau_api_lib.utils.common.flatten_dict_column`: For flattening dictionary columns in DataFrames.

### Utility Functions

#### `replace_special_characters(text)`
Replaces spaces in the input text with '%20' for URL encoding.

#### `get_encoded_params(param_dict)`
Encodes the values of the input dictionary by replacing special characters.

### Class: `TableauConnector`

A class designed to manage connections and perform various querying operations with Tableau Server.

#### `__init__(self, environment="prod")`
Initializes the `TableauConnector` instance with the specified environment (default is "prod").

#### `_create_tableau_connection(self, tableau_configuration)`
Creates and signs into a Tableau Server connection using the provided configuration dictionary.

#### `_close_tableau_connection(self)`
Signs out of the Tableau Server connection.

#### `load_yaml_config(self, file_path)`
Loads and parses a YAML configuration file from the specified file path and returns it as a dictionary.

#### `read_file(self, file_name, file_type="xlsx")`
Reads a file (either Excel or CSV) and returns its content as a DataFrame. Supports `xlsx` and `csv` file types.

#### `extract_workbook_data(self, config)`
Extracts workbook data from the provided configuration dictionary and returns it as a DataFrame. The data includes project name, workbook name, view name, filters, and measure aliases.

#### `extract_filter_info(self, row)`
Extracts filter field name and value from the filters dictionary in the provided DataFrame row. Returns the filter field name and value.

#### `extract_query_desc(self, row)`
Extracts the query description from the measure aliases dictionary in the provided DataFrame row.

#### `merge_dataframes(self, excel_data_df, workbooks_df)`
Merges two DataFrames (`excel_data_df` and `workbooks_df`) based on 'workbook_name' and 'view_name' columns. Adds `filter_field_name`, `filter_field_value`, and `measure_name` columns to the merged DataFrame.

#### `get_workbook_id(self, project_name, workbook_name)`
Retrieves the workbook ID for the specified project and workbook name. Uses Tableau's querying utility to get workbooks and flattens the result to find the target workbook ID.

#### `generate_filter_params(self, field_name, field_value)`
Generates filter parameters based on the provided field name and value. The parameters are URL encoded for use in Tableau queries.

#### `get_view_data(self, tableau_configuration, df, is_filter=False)`
Retrieves the view data for the specified project, workbook, and view name from the Tableau configuration. Optionally applies filters if `is_filter` is True. Merges the retrieved view data with the input DataFrame and includes additional columns such as `dash_board_value`, `is_match`, and `created_at`.

### Detailed Functionality:

1. **Initialization and Configuration Loading:**
   - The `TableauConnector` class is initialized with an environment (defaulting to "prod").
   - The `load_yaml_config` method loads a YAML configuration file, which is used to configure Tableau Server connections.

2. **File Reading:**
   - The `read_file` method supports reading data from both Excel and CSV files, returning the content as a DataFrame.

3. **Data Extraction:**
   - The `extract_workbook_data` method extracts relevant workbook data from the configuration dictionary, including project names, workbook names, view names, filters, and measure aliases.

4. **Filtering and Merging Data:**
   - The `extract_filter_info` and `extract_query_desc` methods are used to extract specific filter and query description information from DataFrame rows.
   - The `merge_dataframes` method merges two DataFrames based on workbook and view names, integrating additional filter and measure information.

5. **Tableau Server Interaction:**
   - The `_create_tableau_connection` and `_close_tableau_connection` methods manage the lifecycle of Tableau Server connections.
   - The `get_workbook_id` method retrieves the workbook ID using project and workbook names.
   - The `generate_filter_params` method creates filter parameters for querying Tableau views.
   - The `get_view_data` method retrieves view data from Tableau Server, optionally applying filters, and merges it with the existing DataFrame.

6. **Data Processing:**
   - The `get_view_data` method also processes the retrieved view data, adding columns for `dash_board_value`, `is_match`, and `created_at` to track the data value and timestamp.

### Summary
The `tableau_connector.py` file is a robust module for managing connections and querying data from Tableau Server. It includes utility functions for encoding parameters, methods for reading configuration and data files, and comprehensive functionalities for extracting, filtering, merging, and processing workbook and view data from Tableau. This module is essential for integrating Tableau data with other data processing pipelines or applications.


"""
import pandas as pd
import yaml
from sqlalchemy import create_engine
from tableau_api_lib import TableauServerConnection
from tableau_api_lib.utils import querying
from tableau_api_lib.utils.common import flatten_dict_column


def replace_special_characters(text):
    text = text.replace(' ', '%20')
    return text


def get_encoded_params(param_dict):
    encoded_dict = {}
    for key in param_dict.keys():
        encoded_dict[key] = replace_special_characters(str(param_dict[key]))
    return encoded_dict


class TableauConnector:
    """
    A class to handle the connection and querying operations with Tableau Server.
    """

    def __init__(self, environment="prod"):
        """
        Initialize the TableauConnector with the environment.

        Parameters:
            environment (str): The environment to connect to (default is "prod").
        """
        # self.connection, self.tableau_configuration = self._create_tableau_connection(config_path, environment)
        self.connection = None
        self.environment = environment
        self.tableau_configuration = None

    def _create_tableau_connection(self, tableau_configuration):
        """
        Create and sign in to a Tableau Server connection.

        Parameters:
            tableau_configuration (dict): The configuration details for Tableau Server.

        Returns:
            TableauServerConnection: The established Tableau Server connection.
        """
        config = {self.environment: tableau_configuration[self.environment]}
        self.connection = TableauServerConnection(config, env=self.environment)
        self.connection.sign_in()

    def _close_tableau_connection(self):
        """Sign out Tableau Server connection"""
        self.connection.sign_out()

    def load_yaml_config(self, file_path):
        """
        Load and parse a YAML configuration file.

        Parameters:
            file_path (str): The path to the YAML file.

        Returns:
            dict: The parsed YAML content as a dictionary.
        """
        with open(file_path, "r") as file:
            config = yaml.safe_load(file)
        return config

    def read_file(self, file_name, file_type="xlsx"):
        """
        Read a file and return its content as a DataFrame.

        Parameters:
            file_name (str): The name of the file to read.
            file_type (str): The type of the file ("xlsx" or "csv").

        Returns:
            pd.DataFrame: The content of the file as a DataFrame.
        """
        if file_type == "xlsx":
            return pd.read_excel(file_name, sheet_name="Sheet1")
        elif file_type == "csv":
            return pd.read_csv(file_name)
        return None

    def extract_workbook_data(self, config):
        """
        Extracts workbook data from the configuration dictionary.

        Args:
            config (dict): The configuration dictionary.

        Returns:
            pandas.DataFrame: A DataFrame containing project_name, workbook_name, and view_name.
        """
        workbook_data = []
        for project in config['projects']:
            for workbook in project['workbooks']:
                workbook_name = workbook['name']
                for view in workbook.get('views', []):
                    view_name = view['name']
                    filters = view.get('filters', {})
                    measure_aliases = view.get('measure_aliases', {})
                    workbook_data.append({
                        'project_name': project['name'],
                        'workbook_name': workbook_name,
                        'view_name': view_name,
                        'filters': filters,
                        'measure_aliases': measure_aliases
                    })

        workbook_df = pd.DataFrame(workbook_data)
        return workbook_df

    def extract_filter_info(self, row):
        """
        Extracts filter field name and value from the filters dictionary.

        Args:
            row (pd.Series): DataFrame row containing filter information.

        Returns:
            str, str: Filter field name and value.
        """
        filter_value = row['filter']
        filters = row['filters']
        for key, values in filters.items():
            if filter_value in values:
                return key, filter_value
        return None, None

    def extract_query_desc(self, row):
        """
        Extracts query description from the measure_aliases dictionary.

        Args:
            row (pd.Series): DataFrame row containing measure aliases information.

        Returns:
            str: Query description.
        """
        return row['measure_aliases'].get(row['query_desc'])

    def merge_dataframes(self, excel_data_df, workbooks_df):
        """
        Merges two DataFrames based on 'workbook_name' and 'view_name' columns.

        Args:
            excel_data_df (pandas.DataFrame):  excel_data DataFrame.
            workbooks_df (pandas.DataFrame):  workbooks DataFrame.

        Returns:
            pandas.DataFrame: A DataFrame containing the merged data.
        """
        excel_data_df.rename(columns={"dashboard_name": "workbook_name", "tab_name": "view_name"}, inplace=True)
        merged_df = pd.merge(excel_data_df, workbooks_df, on=['workbook_name', 'view_name'], how='inner')
        merged_df['filter_field_name'], merged_df['filter_field_value'] = zip(
            *merged_df.apply(self.extract_filter_info, axis=1))
        merged_df['measure_name'] = merged_df.apply(self.extract_query_desc, axis=1)
        return merged_df

    def get_workbook_id(self, project_name, workbook_name):
        """
        Get the workbook ID for a specific project and workbook name.

        Parameters:
            project_name (str): The name of the Tableau project.
            workbook_name (str): The name of the workbook.

        Returns:
            str: The ID of the workbook.
        """
        workbooks_df = querying.get_workbooks_dataframe(self.connection)
        workbooks_df = flatten_dict_column(workbooks_df, keys=['name', 'id'], col_name='project')

        target_workbook_df = workbooks_df[
            (workbooks_df["project_name"] == project_name) &
            (workbooks_df["name"] == workbook_name)
            ].dropna()

        workbook_id = target_workbook_df["id"].values[0]
        return workbook_id

    def generate_filter_params(self, field_name, field_value):
        """
        Generate filter parameters based on field name and value.

        Args:
            field_name (str): The name of the field to filter on. Ex: Education
            field_value (str): The value of the field to filter on. EX: Bachelor's Degree

        Returns:
            dict: A dictionary containing the filter parameter.
        """
        # https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_filtering_and_sorting.htm#Filter-query-views
        param_dict = {f"filter_for_{field_value.lower().replace(' ', '_')}": f"vf_{field_name}={field_value}"}
        return param_dict

    def get_view_data(self, tableau_configuration, df, is_filter=False):
        """
        Retrieve the view data for a given project, workbook, and view name from tableau_configuration.

        Parameters:
            tableau_configuration (dict): Configuration details for Tableau.
            df (pd.DataFrame): DataFrame containing project_name, workbook_name, view_name, and other columns.
            is_filter (bool): Whether to apply filters to the query.

        Returns:
            pd.DataFrame: DataFrame containing the original columns from df and additional columns from view data.
        """
        workbook_cache = {}
        output_df_list = []

        self._create_tableau_connection(tableau_configuration)

        for _, row in df.iterrows():
            project_name = row["project_name"]
            workbook_name = row["workbook_name"]
            view_name = row["view_name"]
            cache_key = (project_name, workbook_name)
            if cache_key not in workbook_cache:
                workbook_id = self.get_workbook_id(project_name, workbook_name)
                workbook_cache[cache_key] = {
                    "workbook_id": workbook_id,
                    "views_df": querying.get_views_for_workbook_dataframe(self.connection, workbook_id=workbook_id)
                }

            target_views_df = workbook_cache[cache_key]["views_df"]
            filtered_df = target_views_df[target_views_df["name"] == view_name]

            for _, value in filtered_df.iterrows():
                view_id = value["id"]
                if is_filter:
                    filter_param_dict = {"filter_dict": f"vf_{row['filter_field_name']}={row['filter_field_value']}"}
                    filter_param_dict = get_encoded_params(filter_param_dict)
                    view_data_df = querying.get_view_data_dataframe(self.connection, view_id=view_id,
                                                                    parameter_dict=filter_param_dict)
                else:
                    view_data_df = querying.get_view_data_dataframe(self.connection, view_id=view_id)

                view_data_columns = list(view_data_df.columns)
                view_data_df = view_data_df.set_index(view_data_columns[0]).transpose().reset_index(drop=True)

                for _, view_data_row in view_data_df.iterrows():
                    combined_row = row.to_dict()
                    combined_row['view_id'] = view_id
                    # Adding the dashboard value
                    combined_row["dash_board_value"] = view_data_row.get(row["measure_name"], None)
                    # Adding the match result
                    combined_row["is_match"] = "Yes" if combined_row.get("result") == combined_row[
                        "dash_board_value"] else "No"
                    # Adding date and time 
                    combined_row["created_at"] = pd.Timestamp.now()
                    # Combining the data
                    combined_data = pd.DataFrame([combined_row])
                    output_df_list.append(combined_data)

        output_df = pd.concat(output_df_list, ignore_index=True)
        output_df.drop(['filters', 'measure_aliases'], axis=1, inplace=True)
        return output_df


if __name__ == "__main__":
    tableau_connector_obj = TableauConnector()
    config_file_path = "C:\\office\\rohit-workspace\\tableau\\parameters.yml"
    input_file_path = "C:\\office\\rohit-workspace\\tableau\\sample_dashboard.xlsx"
    configuration_data = tableau_connector_obj.load_yaml_config(config_file_path)
    excel_data_df = tableau_connector_obj.read_file(input_file_path)
    workbooks_df = tableau_connector_obj.extract_workbook_data(configuration_data["tableau_configuration"])
    merged_df = tableau_connector_obj.merge_dataframes(excel_data_df, workbooks_df)
    view_df = tableau_connector_obj.get_view_data(
        configuration_data["tableau_configuration"],
        merged_df,
        is_filter=False
    )

    db_user = "postgres"
    db_password = "root"
    db_host = "localhost"
    db_port = "5432"
    db_name = "rohit"
    db_table_name = "tableau_dashboard_data"

    # Replace the connection string with your PostgreSQL connection details
    engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

    view_df.to_sql(db_table_name, engine, if_exists='replace', index=False)
