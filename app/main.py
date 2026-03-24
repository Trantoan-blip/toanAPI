from fastapi import FastAPI
from app.core.database import Base, engine

from app.api.v1 import auth, users, candidates, jobs, applications, interviews, employees

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Recruitment HR API")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(candidates.router)
app.include_router(jobs.router)
app.include_router(applications.router)
app.include_router(interviews.router)
app.include_router(employees.router)


@app.get("/")
def root():
    return {"message": "Recruitment HR API is running"}