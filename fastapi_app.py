import os
import django
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 1. Init Django Environment
# This allows FastAPI to talk to the Django Database
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

# Now we can import Django models!
from portfolio.models import Profile, Skill, Project, Experience

app = FastAPI(title="Code Warlock API", description="Microservice for Portfolio Data")

# 2. Add CORS (So your frontend JS can talk to this API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# === ENDPOINTS ===

@app.get("/api/profile")
def get_profile():
    profile = Profile.objects.first()
    return {
        "name": profile.name,
        "title": profile.title,
        "bio": profile.bio,
        "github": profile.github_link,
        "linkedin": profile.linkedin_link
    }

@app.get("/api/tech-stack")
def get_skills():
    skills = Skill.objects.all()
    return [{"name": s.name, "icon": s.icon_class} for s in skills]

@app.get("/api/resume")
def get_resume():
    experiences = Experience.objects.all()
    data = []
    for job in experiences:
        data.append({
            "role": job.role,
            "company": job.company,
            "start": job.start_date,
            "end": job.end_date if job.end_date else "Present",
            "description": job.description
        })
    return data