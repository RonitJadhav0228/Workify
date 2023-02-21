from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [{
    "id ": '1',
    "title": "Data Analyst",
    "location": "Banglore",
    "salary": "Rs 10,00,00"
},
{
    "id ": '2',
    "title": "Data Scientist",
    "location": "Delhi NCR",
    "salary": "Rs 20,00,00"
},
{
    "id ": '3',
    "title": "Data Engineer",
    "location": "Navi Mumbai",
    "salary": "Rs 30,00,00"
},
{
    "id":4,
    "title": "Front end dev",
    "location": "Mumbai",
    "salary": "Rs 30,00,00"
}


]

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


@app.route("/")
def hello_world():
    return render_template('home.html' , jobs = JOBS , company_name ='Workify')


if __name__ == "__main__ ":
    app.run(host="0.0.0.0", debug=True)
