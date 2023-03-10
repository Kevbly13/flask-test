from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Farmington, Michigan',
  'salary': '$70,000'
}, {
  'id': 2,
  'title': 'Data Analyst',
  'location': 'El Paso, Texas',
  'salary': '$75,000'
}, {
  'id': 3,
  'title': 'Web Security',
  'location': 'Detroit, Michigan'
}, {
  'id': 4,
  'title': 'Marketing Analyst',
  'location': 'Cleveland, Ohio',
  'salary': '$130,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
