const ACTION_NAMES = [
  "Ambulance Dispatch",       // 0
  "Food Supply",              // 1
  "Rescue Boat",              // 2
  "Wait / Monitor",           // 3
  "Deploy Doctors",           // 4
  "Setup Medical Camp",       // 5
  "Water Supply",             // 6
  "Distribute Medicines",     // 7
  "Helicopter Rescue",        // 8
  "Evacuation Bus",           // 9
  "Quarantine Zone",          // 10
  "Sanitize Area",            // 11
  "Distribute Masks",         // 12
  "Vaccination Drive",        // 13
  "Alert Authorities",        // 14
  "Monitor Situation",        // 15
  "Restore Electricity",      // 16
  "Setup Comms Network",      // 17
  "Temporary Shelter",        // 18
  "Clear Road Blockages",     // 19
];

let totalScore = 0;
let autoRunInterval = null;

function boolBadge(val) {
  return val
    ? '<span class="bool-yes">Yes</span>'
    : '<span class="bool-no">No</span>';
}

function priorityBadge(p) {
  const cls = {
    Critical: "priority-critical",
    High: "priority-high",
    Medium: "priority-medium",
    Low: "priority-low",
  }[p] || "";
  return `<span class="${cls}">${p}</span>`;
}

function updateState(state) {
  document.getElementById("zone").textContent    = state.zone;
  document.getElementById("people").textContent  = state.people;
  document.getElementById("injured").textContent = state.injured;
  document.getElementById("food").innerHTML      = boolBadge(state.food_needed);
  document.getElementById("rescue").innerHTML    = boolBadge(state.rescue_needed);
  document.getElementById("power").innerHTML     = boolBadge(state.power_outage);
  document.getElementById("infra").innerHTML     = boolBadge(state.infrastructure_damage);
  document.getElementById("disease").innerHTML   = boolBadge(state.disease_outbreak);
  document.getElementById("step").textContent    = state.step ?? "-";
  document.getElementById("max-steps").textContent = state.max_steps ?? "-";
}

function runStep() {
  const agent = document.getElementById("agent").value;
  document.getElementById("action").textContent = "Thinking...";
  document.getElementById("reason").textContent = "Processing...";

  fetch("/step", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ agent }),
  })
    .then((r) => r.json())
    .then((data) => {
      updateState(data.state);

      document.getElementById("action").textContent  = ACTION_NAMES[data.action] || "Unknown";
      document.getElementById("reason").textContent  = data.reason || "-";
      document.getElementById("reward").textContent  = data.reward;
      document.getElementById("priority").innerHTML  = priorityBadge(data.priority);
      document.getElementById("done").textContent    = data.done ? "Completed" : "Running";

      const statusEl = document.getElementById("ep-status");
      if (data.done) {
        statusEl.textContent = "Done";
        statusEl.className = "badge badge-done";
        stopEpisode();
      } else {
        statusEl.textContent = "Running";
        statusEl.className = "badge badge-running";
      }

      totalScore += data.reward;
      document.getElementById("score").textContent = Math.round(totalScore * 10) / 10;
    })
    .catch((err) => {
      console.error("Step error:", err);
      document.getElementById("action").textContent = "Error";
      document.getElementById("reason").textContent = "Check console";
    });
}

function resetEnv() {
  stopEpisode();
  totalScore = 0;
  const difficulty = document.getElementById("difficulty").value;
  document.getElementById("diff-label").textContent = difficulty;

  fetch("/reset", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ difficulty }),
  })
    .then((r) => r.json())
    .then((data) => {
      updateState(data.state);
      document.getElementById("action").textContent  = "-";
      document.getElementById("reason").textContent  = "-";
      document.getElementById("reward").textContent  = "-";
      document.getElementById("priority").textContent = "-";
      document.getElementById("done").textContent    = "-";
      document.getElementById("score").textContent   = "0";
      document.getElementById("ep-status").textContent = "Running";
      document.getElementById("ep-status").className = "badge badge-running";
    })
    .catch((err) => console.error("Reset error:", err));
}

function runEpisode() {
  stopEpisode();
  autoRunInterval = setInterval(runStep, 800);
}

function stopEpisode() {
  if (autoRunInterval) {
    clearInterval(autoRunInterval);
    autoRunInterval = null;
  }
}

// Load initial state on page load
window.addEventListener("DOMContentLoaded", () => {
  fetch("/state")
    .then((r) => r.json())
    .then((data) => updateState(data.state))
    .catch(() => {});
});
