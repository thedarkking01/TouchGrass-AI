import { useState } from "react";
import "./App.css";

const TIME_OPTIONS = ["15m", "30m", "1h", "2h+"];
const ENERGY_OPTIONS = ["Low", "Medium", "High"];
const INTEREST_OPTIONS = ["nature", "fitness", "explore", "photo", "surprise"];

function App() {
  const [time, setTime] = useState("30m");
  const [energy, setEnergy] = useState("Medium");
  const [interest, setInterest] = useState("nature");
  const [mission, setMission] = useState(null);
  const [loading, setLoading] = useState(false);
  const [screen, setScreen] = useState("form"); // form | mission | outside | reflect

  async function generateMission() {
    setLoading(true);
    const res = await fetch("http://localhost:8000/generate-mission", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ time, energy, interest }),
    });
    const data = await res.json();
    setMission(data);
    setScreen("mission");
    setLoading(false);
  }

  if (screen === "form") {
    return (
      <div className="card">
        <h1>🌱 TouchGrass AI</h1>
        <p className="subtitle">What are you up for today?</p>

        <label>Time</label>
        <div className="options">
          {TIME_OPTIONS.map((t) => (
            <button key={t} className={time === t ? "active" : ""} onClick={() => setTime(t)}>
              {t}
            </button>
          ))}
        </div>

        <label>Energy</label>
        <div className="options">
          {ENERGY_OPTIONS.map((e) => (
            <button key={e} className={energy === e ? "active" : ""} onClick={() => setEnergy(e)}>
              {e}
            </button>
          ))}
        </div>

        <label>Interest</label>
        <div className="options">
          {INTEREST_OPTIONS.map((i) => (
            <button key={i} className={interest === i ? "active" : ""} onClick={() => setInterest(i)}>
              {i.charAt(0).toUpperCase() + i.slice(1)}
            </button>
          ))}
        </div>

        <button className="primary" onClick={generateMission} disabled={loading}>
          {loading ? "Generating..." : "🌿 Generate Mission"}
        </button>
      </div>
    );
  }

  if (screen === "mission") {
    return (
      <div className="card">
        <h2>🌳 {mission.title}</h2>
        <p>{mission.description}</p>
        <ul>
          {mission.tasks.map((t, i) => (
            <li key={i}>✓ {t}</li>
          ))}
        </ul>
        <p className="meta">⏱ {mission.time} · ⚡ {mission.energy}</p>
        <button className="primary" onClick={() => setScreen("outside")}>
          🌱 I'm Going Outside
        </button>
        <button className="secondary" onClick={() => setScreen("form")}>
          ← Back
        </button>
      </div>
    );
  }

  if (screen === "outside") {
    return (
      <div className="card center">
        <h2>🌱 You're outside.</h2>
        <p>{mission.time}.</p>
        <p>Go explore.</p>
        <button className="primary" onClick={() => setScreen("reflect")}>
          I'm Back
        </button>
      </div>
    );
  }

  if (screen === "reflect") {
    return (
      <div className="card">
        <h2>Welcome back 🌱</h2>
        <label>What did you discover?</label>
        <textarea placeholder="I found..." rows={3} />
        <label>How did it go?</label>
        <textarea placeholder="It was..." rows={3} />
        <button className="primary" onClick={() => { setScreen("form"); setMission(null); }}>
          Save Adventure
        </button>
      </div>
    );
  }
}

export default App;
