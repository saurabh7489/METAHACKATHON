from flask import Flask, render_template, jsonify
from env import DisasterEnv
from agent import Agent

app = Flask(__name__)

env = DisasterEnv()
agent = Agent()

@app.route("/")
def home():
    state = env.reset()
    return render_template("index.html", state=state)

@app.route("/step")
def step():
    state = env.get_state()
    action, reason = agent.act(state)

    new_state, reward, done, _ = env.step(action)

    return jsonify({
        "state": new_state,
        "action": action,
        "reason": reason,
        "reward": reward
    })

@app.route("/reset")
def reset():
    state = env.reset()
    return jsonify(state)

if __name__ == "__main__":
    app.run(debug=True)
