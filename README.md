# 🌱 TouchGrass AI

> An open-source AI experiment designed to solve an unusual problem: **getting people to stop using AI and go outside.**

Built for the [Hacktoberfest Open-Source AI Challenge: Week 1](https://dev.to/challenges/hacktoberfest) — Theme: **Touch Grass** 🌿

---

## What is it?

TouchGrass AI generates personalized outdoor missions using an open-weight AI model. You tell it how much time you have, your energy level, and what you're into — it gives you a mission and sends you outside.

The core loop:

```
Tell TouchGrass what you have
        ↓
   AI creates a mission
        ↓
    Go outside
        ↓
  Come back & reflect
```

The goal is for the screen to be the **shortest** part of the experience.

---

## Demo

| Step | Screen |
|------|--------|
| 1. Pick your preferences | Time · Energy · Interest |
| 2. Get your AI mission | Title · Description · 3 tasks |
| 3. Go outside | Timer screen |
| 4. Come back & reflect | Journal your adventure |

---

## Tech Stack

| Layer | Tech |
|-------|------|
| Frontend | React + Vite |
| Backend | FastAPI (Python) |
| AI | Gemma (via Gemini API) |
| Inference | Google AI Studio (free tier) |

### Why open-source AI?

This project uses **Gemma**, Google's open-weight model family. That matters because:

- The same model can run **locally with no internet** (via Ollama) — your outdoor mission data never leaves your machine
- You can **swap or fine-tune** the model — want missions tuned to your city or trail system? You can do that
- It **costs nothing to run** on the free tier, and nothing extra to self-host
- The entire stack is open — React, FastAPI, and Gemma are all open source

---

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- A free [Google AI Studio](https://aistudio.google.com) API key

### Backend

```bash
cd backend
python -m pip install -r requirements.txt

# copy the example env and add your key
cp .env.example .env
# edit .env and set GEMINI_API_KEY=your_key_here

python -m uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173` and go touch grass. 🌱

---

## Project Structure

```
TouchGrass AI/
├── backend/
│   ├── main.py          # FastAPI + Gemini AI mission generator
│   ├── requirements.txt
│   └── .env.example
└── frontend/
    └── src/
        ├── App.jsx      # All 4 screens: form → mission → outside → reflect
        └── App.css
```

---

## Roadmap

- [x] Phase 1 — React UI + FastAPI + fake mission JSON
- [x] Phase 2 — Gemma/Gemini AI-generated missions
- [ ] Phase 3 — Reflection journal with local persistence
- [ ] Phase 4 — Offline mode with local Ollama + Gemma

---

## Contributing

PRs welcome. If you take it outside and use it, open an issue and tell us what mission you got. 🌳

---

## License

MIT
