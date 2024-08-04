from flask import Flask, jsonify, render_template

from database import load_jobs_from_db

app = Flask(__name__)





#app.route decorator,with '/' as the argument
@app.route("/")
def home():
  jobs_list = load_jobs_from_db()
  return render_template('home.html',jobs=jobs_list)

@app.route("/about")
def about():
  return render_template('about.html')
  
#api for the jobs
@app.route("/api/jobs")
def api_jobs():
  jobs_list = load_jobs_from_db()

  return jsonify(jobs_list)

if __name__ == '__main__':
  app.run(host = '0.0.0.0',debug = True)