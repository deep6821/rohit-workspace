import yaml
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructType, StructField


def load_schema(schema_file, schema_name):
    """
    Loads a schema definition from a YAML file.

    Args:
        schema_file (str): The path to the YAML file containing schema definitions.
        schema_name (str): The name of the schema definition to load from the YAML file.

    Returns:
        pyspark.sql.types.StructType: The schema loaded from the YAML file.

    Raises:
        FileNotFoundError: If the specified YAML file does not exist.
        KeyError: If the specified schema name is not found in the YAML file.
        ValueError: If the schema definition contains invalid data types.
    """
    try:
        with open(schema_file, "r", encoding="utf-8") as file:
            schemas = yaml.safe_load(file)

        fields = [
            StructField(field["name"], eval(field["type"].capitalize() + "Type()"), nullable=True)
            for field in schemas[schema_name]["fields"]
        ]
        return StructType(fields)
    except FileNotFoundError:
        raise FileNotFoundError(f"Schema file '{schema_file}' not found.")
    except KeyError:
        raise KeyError(f"Schema name '{schema_name}' not found in the schema file.")
    except Exception as e:
        raise ValueError(f"Error loading schema: {str(e)}")


def validate_schema(input_df, expected_schema):
    """
    Validates a Spark DataFrame against an expected schema.

    Args:
        input_df (pyspark.sql.DataFrame): The DataFrame to validate.
        expected_schema (pyspark.sql.types.StructType): The expected schema.

    Returns:
        pyspark.sql.DataFrame: The validated DataFrame containing only valid records.

    Raises:
        ValueError: If the schema of the DataFrame does not match the expected schema.
    """
    spark = SparkSession.getActiveSession()  # Get the active session within the function
    if not spark:
        raise ValueError("SparkSession not found. Please ensure a SparkSession is active.")

    try:
        # Sort the fields in both actual and expected schemas by field name
        actual_fields_sorted = sorted(input_df.schema.fields, key=lambda f: f.name)
        expected_fields_sorted = sorted(expected_schema.fields, key=lambda f: f.name)

        # Create new schemas with sorted fields
        actual_schema_sorted = StructType(actual_fields_sorted)
        expected_schema_sorted = StructType(expected_fields_sorted)

        # Compare the sorted schemas
        if actual_schema_sorted != expected_schema_sorted:
            raise ValueError("Schema validation error: DataFrame schema does not match the expected schema.")

        # Data schema is valid
        return input_df
    except Exception as e:
        raise ValueError(f"Error validating schema: {str(e)}")
