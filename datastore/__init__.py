from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create_all(connectable):
    metadata = Base.metadata
    tables = metadata.sorted_tables
    tables_name = [table.name for table in tables]
    metadata.create_all(bind=connectable)


def drop_all(connectable):
    metadata = Base.metadata
    tables = metadata.sorted_tables
    tables_name = [table.name for table in tables]
    metadata.drop_all(bind=connectable)