let totalScore = 0;

function getActionName(action) {
    return [
        "🚑 Ambulance Dispatch",
        "🍲 Food Supply",
        "🚤 Rescue Boat",
        "⏳ Wait / Monitor",
        "👨‍⚕️ Deploy Doctors",
        "🏥 Setup Medical Camp",
        "💧 Water Supply",
        "💊 Distribute Medicines",
        "🚁 Helicopter Rescue",
        "🚌 Evacuation Bus",
        "🔒 Quarantine Zone",
        "🧴 Sanitize Area",
        "😷 Distribute Masks",
        "💉 Vaccination Drive",
        "📢 Alert Authorities",
        "👀 Monitor Situation",
        "⚡ Restore Electricity",
        "📡 Setup Communication Network",
        "🏠 Provide Temporary Shelter",
        "🚧 Clear Road Blockages"
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

        console.log(data);  // 🔍 debug (important)

        // ✅ Update state safely
        document.getElementById("zone").innerText = data.state.zone;
        document.getElementById("people").innerText = data.state.people;
        document.getElementById("injured").innerText = data.state.injured;
        document.getElementById("food").innerText = data.state.food_needed ? "Yes" : "No";
        document.getElementById("rescue").innerText = data.state.rescue_needed ? "Yes" : "No";

        // ✅ Fix action issue
        document.getElementById("action").innerText = getActionName(data.action);

        document.getElementById("reason").innerText = data.reason || "No reason";

        document.getElementById("reward").innerText = data.reward;

        // ✅ Optional fields (safe)
        if (data.priority && document.getElementById("priority")) {
            document.getElementById("priority").innerText = data.priority;
        }

        if (document.getElementById("done")) {
            document.getElementById("done").innerText = data.done ? "Completed" : "Running";
        }

        totalScore += data.reward;
        document.getElementById("score").innerText = totalScore;
    })
    .catch(err => {
        console.error("ERROR:", err);
        document.getElementById("action").innerText = "Error";
        document.getElementById("reason").innerText = "Check console";
    });
}

function resetEnv() {
    fetch('/reset', {
        method: 'POST'
    })
    .then(res => res.json())
    .then(() => {

        totalScore = 0;
document.getElementById("done").innerText = "No Data";

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
