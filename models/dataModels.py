from sqlalchemy import Table, Column
from config.database import metadata, engine_data
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

for table_name in metadata.tables.keys():
    table = Table(table_name, metadata, autoload=True, autoload_with=engine_data)
    
    class_name = table_name.title().replace('_', '')
    columns = [column.name for column in table.columns]
    
    attrs = {'__tablename__': table_name}
    for column in table.columns:
        attrs[column.name] = Column(column.name ,column.type)
        
    model_class = type(class_name, (Base,), attrs)
    
    globals()[class_name] = model_class