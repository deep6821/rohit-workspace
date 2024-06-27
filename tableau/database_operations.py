from sqlalchemy import BigInteger, Column, create_engine, Float, Table, MetaData, Text, TIMESTAMP


def create_table(engine, table_name):
    """
    Create a table in the database using SQLAlchemy's Table object.
    :param engine: SQLAlchemy engine object
    :param table_name: Name of the table
    """
    # Create a MetaData instance
    metadata = MetaData()
    
    # Define the table with columns
    table = Table(
        table_name, metadata,
        Column('qc_id', BigInteger),
        Column('region', Text),
        Column('priority_type', Text),
        Column('workbook_name', Text),
        Column('view_name', Text),
        Column('filter', Text),
        Column('query_desc', Text),
        Column('query', Text),
        Column('result', BigInteger),
        Column('project_name', Text),
        Column('filter_field_name', Text),
        Column('filter_field_value', Text),
        Column('measure_name', Text),
        Column('view_id', Text),
        Column('dash_board_value', Float),
        Column('is_match', Text),
        Column('created_at', TIMESTAMP)
    )

    # Create the table in the database
    table.create(engine, checkfirst=True)

def ingest_data(engine, table_name, data):
    """
    Insert data into the specified table.
    :param engine: SQLAlchemy engine object
    :param table_name: Name of the table
    :param data: Pandas DataFrame containing data to insert
    """
    data.to_sql(table_name, engine, if_exists='replace', index=False)

# if __name__ == '__main__':
#     db_user = "postgres"
#     db_password = "root"
#     db_host = "localhost"
#     db_port = "5432"
#     db_name = "rohit"
#     db_table_name = "tableau_dashboard_data"

#     # Replace the connection string with your PostgreSQL connection details
#     engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

#     create_table(engine, db_table_name)
