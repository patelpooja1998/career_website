from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 0,
  'title': 'Data Analyst',
  'location': 'Toronto,CA',
  'salary': '$60,000'
}, {
  'id': 1,
  'title': 'Data scientist',
  'location': 'Ottawa,CA',
  'salary': '$160,000'
}, {
  'id': 2,
  'title': 'Machine Learning Engineer',
  'location': 'Ottawa,CA',
  'salary': '$160,000'
}, {
  'id': 3,
  'title': 'Data Engineer',
  'location': 'Ottawa,CA',
  'salary': '$160,000'
}, {
  'id': 4,
  'title': 'Software Engineer',
  'location': 'Ottawa,CA',
  'salary': '$160,000'
}]


@app.route("/")
def helloworld():
  return render_template('home.html', jobs=JOBS, company_name='Jovian')

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
