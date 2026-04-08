let totalScore = 0;

function getActionName(action) {
    return [
        "🚑 Ambulance",
        "🍲 Food Supply",
        "🚤 Rescue Boat",
        "⏳ Wait",
        "👨‍⚕️ Deploy Doctors",
        "🏥 Medical Camp",
        "💧 Water Supply",
        "💊 Medicine Distribution",
        "🚁 Helicopter Rescue",
        "🚌 Evacuation Bus",
        "🔒 Quarantine Zone",
        "🧴 Sanitize Area",
        "😷 Distribute Masks",
        "💉 Vaccination Drive",
        "📢 Alert Authorities",
        "👀 Monitor Situation"
    ][action];
}

function runStep() {

    // 🔥 Loading state
    document.getElementById("action").innerText = "Thinking...";
    document.getElementById("reason").innerText = "Processing...";

    fetch('/step', {
        method: 'POST'
    })
    .then(res => res.json())
    .then(data => {

        // ✅ Safe update
        document.getElementById("zone").innerText = data.state.zone;
        document.getElementById("people").innerText = data.state.people;
        document.getElementById("injured").innerText = data.state.injured;
        document.getElementById("food").innerText = data.state.food_needed ? "Yes" : "No";
        document.getElementById("rescue").innerText = data.state.rescue_needed ? "Yes" : "No";

        document.getElementById("action").innerText = getActionName(data.action);
        document.getElementById("reason").innerText = data.reason;
        document.getElementById("reward").innerText = data.reward;

        // ⚠️ Optional priority (only if exists)
        if (data.priority) {
            document.getElementById("priority").innerText = data.priority;
        }

        totalScore += data.reward;
        document.getElementById("score").innerText = totalScore;
    })
    .catch(err => {
        console.error(err);
        alert("Error in API");
    });
}

function resetEnv() {
    fetch('/reset', {
        method: 'POST'
    })
    .then(res => res.json())
    .then(() => {

        totalScore = 0;

        document.getElementById("zone").innerText = "No Data";
        document.getElementById("people").innerText = "No Data";
        document.getElementById("injured").innerText = "No Data";
        document.getElementById("food").innerText = "No Data";
        document.getElementById("rescue").innerText = "No Data";

        document.getElementById("action").innerText = "-";
        document.getElementById("reason").innerText = "-";
        document.getElementById("reward").innerText = "-";
        document.getElementById("score").innerText = "0";
    });
}
