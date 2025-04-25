from fastapi import FastAPI
from pydantic import BaseModel
import json
import os


app = FastAPI()
DATA_FILE = "jobs.json"


class Job(BaseModel):
    title:str
    company:str
    location:str
    description:str





def load_jobs():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)
    



def save_jobs(jobs):
    with open(DATA_FILE, 'w') as f:
        json.dump(jobs, f, indent=4)




@app.get('/')
def home():
    return {"message":"Welcome to the Job Board API"}




@app.get('/jobs', summary='Get all Job Listings.')
def get_jobs():
    return load_jobs()



@app.post('/jobs', summary='Create a new Job Listing')
def create_job(job: Job):
    jobs = load_jobs()

    new_job = {
        "id":len(jobs) + 1,
        "title": job.title,
        "company": job.company,
        "location": job.location,
        "description": job.description
    }

    jobs.append(new_job)
    save_jobs(jobs)
    return new_job

