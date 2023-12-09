from flask import Flask, render_template, jsonify


app = Flask(__name__)

JOBS = [
    {
    'id': 1, 
    'title': 'Data Analyst', 
    'location':'Bengaluru, India', 
    }, 
    {
    'id': 2, 
    'title': 'Data Scientist', 
    'location':'Delhi, India', 
    }, 
    {
    'id': 3, 
    'title': 'Data Statician', 
    'location':'Punjab, India', 
    }, 
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name="Jovian Careers")


@app.route("/api/jobs") #api is used to differentiate from html page
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__": 
    app.run(debug=True)