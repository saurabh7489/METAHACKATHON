let totalScore = 0;

function getActionName(action) {
    return ["Ambulance", "Food", "Boat", "Wait"][action];
}

function runStep() {
    fetch('/step')
    .then(res => res.json())
    .then(data => {
        document.getElementById("zone").innerText = data.state.zone;
        document.getElementById("people").innerText = data.state.people;
        document.getElementById("injured").innerText = data.state.injured;
        document.getElementById("food").innerText = data.state.food_needed;
        document.getElementById("rescue").innerText = data.state.rescue_needed;

        document.getElementById("action").innerText = getActionName(data.action);
        document.getElementById("reason").innerText = data.reason;
        document.getElementById("reward").innerText = data.reward;

        totalScore += data.reward;
        document.getElementById("score").innerText = totalScore;
    });
}

function resetEnv() {
    fetch('/reset')
    .then(res => res.json())
    .then(data => {
        totalScore = 0;
        location.reload();
    });
}
