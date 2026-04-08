import random

class DisasterEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.state = {
            "people": random.randint(50, 200),
            "injured": random.randint(0, 50),
            "food_needed": random.choice([True, False]),
            "rescue_needed": random.choice([True, False])
        }
        return self.state

    def get_state(self):
        return self.state

    def step(self, action):
        reward = 0

        if action == 0 and self.state["injured"] > 0:
            reward += 5
            self.state["injured"] -= 10

        elif action == 1 and self.state["food_needed"]:
            reward += 3
            self.state["food_needed"] = False

        elif action == 2 and self.state["rescue_needed"]:
            reward += 4
            self.state["rescue_needed"] = False

        else:
            reward -= 2

        done = (
            self.state["injured"] <= 0 and
            not self.state["food_needed"] and
            not self.state["rescue_needed"]
        )

        return self.state, reward, done, {}
