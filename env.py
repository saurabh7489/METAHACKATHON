import random

class DisasterEnv:
    def __init__(self):
        self.reset()
       
    def reset(self):
        self.state = {
            "zone": random.choice(["Zone A", "Zone B", "Zone C"]),
            "people": random.choice([50, 35, 40, 55, 32, 20, 25, 80, 200]),
            "injured": random.choice([5, 8, 12, 15, 20, 25, 30, 48, 50]),
            "food_needed": random.choice([True, False]),
            "rescue_needed": random.choice([True, False]),
            "infrastructure_damage": random.choice([True, False]),
            "power_outage": random.choice([True, False])
        }
        return self.state

    def get_state(self):
        return self.state

    def step(self, action):
        reward = 0

        # 🚑 Ambulance
        if action == 0:
            if self.state["injured"] > 0:
                self.state["injured"] = max(0, self.state["injured"] - random.randint(5, 15))
                reward += 5
            else:
                reward += 1

        # 🍲 Food
        elif action == 1:
            if self.state["food_needed"]:
                self.state["food_needed"] = False
                reward += 3
            else:
                reward += 1

        # 🚤 Rescue
        elif action == 2:
            if self.state["rescue_needed"]:
                self.state["rescue_needed"] = False
                reward += 4
            else:
                reward += 1

        # ⏳ Wait / others
        else:
            reward += 0

        # 🔥 Dynamic changes in environment
        self.state["injured"] = max(0, self.state["injured"] + random.randint(-3, 5))

        # Random new needs appear
        if random.random() < 0.3:
            self.state["food_needed"] = True

        if random.random() < 0.3:
            self.state["rescue_needed"] = True

        # 🔄 Zone change (dynamic)
        if random.random() < 0.3:
            self.state["zone"] = random.choice(["Zone A", "Zone B", "Zone C"])

        # 🧠 Auto logic
        if self.state["injured"] == 0:
            self.state["rescue_needed"] = False

        # 🎯 DONE condition
        done = (
            self.state["injured"] <= 0 and
            not self.state["food_needed"] and
            not self.state["rescue_needed"]
        )

        return self.state, reward, done, {}