from flask import Flask, jsonify, request
from infrastructure import Jobs

# Global Objects
jobs = Jobs()
app = Flask(__name__)

"""
This API return the list of jobs Category  
"""


@app.route("/job_categories", methods=['GET'])
def jobs_category():
    data = jobs.jobs_category()
    return jsonify(data)


"""
This API return the list of Jobs by Locations 
 
"""


@app.route("/job_locations", methods=['GET'])
def jobs_locations():
    data = jobs.job_locations()
    return jsonify(data)


"""
This API return the list of jobs Category  
"""


@app.route("/jobs", methods=['GET'])
def all_jobs():
    if request.method == "GET":
        params = dict(request.values)
        data = jobs.all_jobs(params["by"], params["values"])
    return jsonify(data)


if __name__ == "__main__":
    app.run()
