from sqlalchemy import inspect, select
from config.database import metadata
from config.database import engine_data as engine

def get_table_names():
    table_name = []
    for table in metadata.tables.values():
        table_name.append(table.name)
    return table_name

def get_table_data(table_name):
    table = metadata.tables.get(table_name)
    if table is None:
        raise Exception("Tabla {} no encontrada".format(table_name))
    conn = engine.connect()
    query = table.select()
    results = conn.execute(query)
    table_data = results.fetchall()
    conn.close()
    return table_data

def get_colnames(table_name):
    table = metadata.tables.get(table_name)
    inspector = inspect(engine)
    columns = inspector.get_columns(table)
    column_names = [column['name'] for column in columns]
    return column_names

def get_onecol_data(table_name, column_name):
    table = metadata.tables.get(table_name)
    query = select([table.c[column_name]])
    conn = engine.connect()
    result = conn.execute(query)
    column_data = [row[column_name] for row in result]
    conn.close()
    return column_data

def get_alltables_data():
    all_table_data = {}
    with engine.connect() as conn:
        for table_name in metadata.tables.keys():
            table = metadata.tables[table_name]
            query = select(table)
            result = conn.execute(query)
            all_table_data[table_name] = [dict(row) for row in result]
    return all_table_data

