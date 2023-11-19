from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Beijing, China',
    'salary': '￥100,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Shanghai, China',
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Chicago, USA',
    'salary': '$130,000'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Chicago, USA',
    'salary': '$120,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, companyname="Jovian")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
