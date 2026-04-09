from flask import Flask, render_template, jsonify, request
from env import DisasterEnv
from agent import Agent

app = Flask(__name__)

# Create environment and agent
env = DisasterEnv()
agent = Agent()

@app.route("/")
def home():
    # Serve the main page
    return render_template("index.html")

@app.route("/step", methods=["POST"])
def step():
    # Get current state
    state = env.get_state()

    # Agent decides action
    action, reason = agent.act(state)

    # Apply action in environment
    new_state, reward, done, info = env.step(action)

    # Determine priority
    priority = "Low"
    if new_state.get("injured", 0) > 20:
        priority = "Critical"
    elif new_state.get("food_needed") or new_state.get("rescue_needed"):
        priority = "Medium"

    return jsonify({
        "state": new_state,
        "action": action,
        "reason": reason,
        "reward": reward,
        "done": done,
        "priority": priority
    })

@app.route("/reset", methods=["POST"])
def reset():
    # Reset environment and return new state
    new_state = env.reset()
    return jsonify({
        "msg": "Environment reset!",
        "state": new_state
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860, debug=True)
