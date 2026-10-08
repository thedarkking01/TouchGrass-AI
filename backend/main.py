from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

FAKE_MISSIONS = {
    "nature": [
        {
            "title": "The 30-Minute Nature Detective",
            "description": "Head outside and investigate the natural world around you.",
            "tasks": ["Find 3 different plants", "Spot 1 bird or insect", "Touch something rough and something smooth"],
        },
        {
            "title": "Cloud Watcher",
            "description": "Find a good spot and just look up.",
            "tasks": ["Identify 2 cloud shapes", "Lie on the grass for 5 minutes", "Notice the wind direction"],
        },
    ],
    "fitness": [
        {
            "title": "The Explorer Sprint",
            "description": "Pick a direction and walk as fast as you can.",
            "tasks": ["Walk 10 minutes without stopping", "Find a hill and climb it", "Do 10 jumping jacks outside"],
        },
    ],
    "explore": [
        {
            "title": "Uncharted Street",
            "description": "Walk down a street you've never been on.",
            "tasks": ["Find something you've never noticed before", "Read 3 street signs", "Discover one new thing about your neighborhood"],
        },
    ],
    "photo": [
        {
            "title": "The Texture Hunt",
            "description": "Go outside and photograph interesting textures.",
            "tasks": ["Photograph bark on a tree", "Find an interesting shadow", "Capture something colorful"],
        },
    ],
    "surprise": [
        {
            "title": "Random Adventure",
            "description": "Flip a mental coin at every corner — left or right.",
            "tasks": ["Walk for 20 minutes with no destination", "Say hi to one stranger", "Find something that makes you smile"],
        },
    ],
}


class MissionRequest(BaseModel):
    time: str
    energy: str
    interest: str


@app.post("/generate-mission")
def generate_mission(req: MissionRequest):
    pool = FAKE_MISSIONS.get(req.interest, FAKE_MISSIONS["surprise"])
    mission = random.choice(pool)
    return {
        "title": mission["title"],
        "description": mission["description"],
        "tasks": mission["tasks"],
        "time": req.time,
        "energy": req.energy,
    }
