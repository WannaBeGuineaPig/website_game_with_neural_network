__all__ = [
    'get_all_topic'
]

from sqlalchemy import create_engine, MetaData, Table, select
from .config import get_db_url

DATABASE_URL = get_db_url()
engine = create_engine(DATABASE_URL)
metadata = MetaData()
table = Table('topic', metadata, autoload_with=engine)

def get_all_topic():
    with engine.connect() as conn:
        stmt = select(table.c.name_topic)
        return conn.execute(stmt).scalars().all()