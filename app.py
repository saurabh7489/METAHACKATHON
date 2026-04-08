from flask import Flask, render_template, jsonify
from env import DisasterEnv
from agent import Agent

app = Flask(__name__)

env = DisasterEnv()
agent = Agent()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/step", methods=["POST"])
def step():
    state = env.get_state()
    action, reason = agent.act(state)

    new_state, reward, done, _ = env.step(action)

    # 🔥 Add priority (simple logic)
    priority = "Low"
    if new_state["injured"] > 20:
        priority = "Critical"
    elif new_state["food_needed"] or new_state["rescue_needed"]:
        priority = "Medium"

    return jsonify({
        "state": new_state,
        "action": action,
        "reason": reason,
        "reward": reward,
        "priority": priority   # ✅ IMPORTANT
    })


@app.route("/reset", methods=["POST"])
def reset():
    env.reset()
    return jsonify({"msg": "reset"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)

