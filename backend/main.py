import os
import json
import re
import time as time_module
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

FALLBACK_MISSION = {
    "title": "The Simple Wander",
    "description": "Step outside and walk with no destination in mind.",
    "tasks": ["Walk for at least 10 minutes", "Notice 3 things you've never seen before", "Take one deep breath of fresh air"],
}

PROMPT_TEMPLATE = """
You are TouchGrass AI. Your only job is to get people off their screens and outside.

Generate a personalized outdoor mission for someone with these preferences:
- Available time: {time}
- Energy level: {energy}
- Interest: {interest}

Respond ONLY with a valid JSON object in this exact format, no markdown, no explanation:
{{
  "title": "short catchy mission name",
  "description": "one sentence setting the scene",
  "tasks": ["task 1", "task 2", "task 3"]
}}
"""


class MissionRequest(BaseModel):
    time: str
    energy: str
    interest: str


@app.post("/generate-mission")
def generate_mission(req: MissionRequest):
    prompt = PROMPT_TEMPLATE.format(
        time=req.time,
        energy=req.energy,
        interest=req.interest,
    )
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt,
            )
            raw = response.text.strip()
            raw = re.sub(r"^```(?:json)?\s*", "", raw)
            raw = re.sub(r"\s*```$", "", raw)
            mission = json.loads(raw)
            return {
                "title": mission["title"],
                "description": mission["description"],
                "tasks": mission["tasks"],
                "time": req.time,
                "energy": req.energy,
                "ai": True,
            }
        except Exception as e:
            print(f"Gemini attempt {attempt + 1} failed: {e}")
            if attempt < 2:
                time_module.sleep(2)
    return {**FALLBACK_MISSION, "time": req.time, "energy": req.energy, "ai": False}
