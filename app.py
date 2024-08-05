from flask import Flask, jsonify, render_template, request

from database import load_jobs_from_db
from database import get_job_from_db

app = Flask(__name__)





#app.route decorator,with '/' as the argument
@app.route("/")
def home():
  jobs_list = load_jobs_from_db()
  return render_template('home.html',jobs=jobs_list)

@app.route("/about")
def about():
  return render_template('about.html')

@app.route("/job/<id>")
def job_detail(id):
  job = get_job_from_db(id)
  return render_template('job_detail.html',job=job)


@app.route('/job/<id>/applyform')
def apply_form(id):
  return render_template('apply_form.html',id = id)

@app.route('/submit_application', methods=['post'])
def submit_application():
  return request.form


#api for the jobs
@app.route("/api/jobs")
def api_jobs():
  jobs_list = load_jobs_from_db()

  return jsonify(jobs_list)

if __name__ == '__main__':
  app.run(host = '0.0.0.0',debug = True)