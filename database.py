#this whole code is available on sqlalchemy website.

import sqlalchemy
from sqlalchemy import create_engine,text
import os
engine = create_engine(os.environ['DB_CONNECTION_STRING'])


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    columns_names = result.keys()
    results = result.fetchall()
    jobs_dict_list = []
    for i in range(len(results)):
      row = dict(zip(columns_names,results[i]))
      jobs_dict_list.append(row)
    return jobs_dict_list
    

def get_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM jobs WHERE id = :val"),{'val':id})
    columns = result.keys()
    row = result.fetchone()
    if row:
      return dict(zip(columns,row))
    else:
      return None