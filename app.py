from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [
  {'id':1,
  'title':'Data Analyst',
   'location':'Islamabad',
  'salary':'Rs.10,00,000'},
  {'id':2,
    'title':'Data Scientist',
     'location':'Karachi'}
]

#app.route decorator,with '/' as the argument
@app.route("/")
def home():
  return render_template('home.html',jobs=JOBS)

@app.route("/about")
def about():
  return render_template('about.html')
  
#api for the jobs
@app.route("/api/jobs")
def api_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host = '0.0.0.0',debug = True)