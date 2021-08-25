import asyncio
import json
from fastapi import FastAPI
from infrastructure import Jobs


jobs = Jobs()
app = FastAPI()


"""
This API return the list of jobs Category  
"""

@app.get("/job_categories")
async def jobs_category():
    data = jobs.jobs_category()
    return data


"""
This API return the list of Jobs by Locations 

"""


@app.get("/job_locations")
async def jobs_locations():
    data = jobs.job_locations()
    return data


@app.get("/jobs")
async def all_jobs(by: str, values: str):
    data = jobs.all_jobs(by, values)
    return data






