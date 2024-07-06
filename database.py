from sqlalchemy import create_engine
from sqlalchemy import text
import os

db_connection_string = os.environ['MY_SECRET']


engine = create_engine(
    url=db_connection_string
)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = [u._asdict() for u in result.all()]
    return jobs