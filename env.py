import random

class DisasterEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.state = {
            "zone": random.choice(["Zone A", "Zone B", "Zone C"]),
            "people": random.randint(50, 200),
            "injured": random.randint(10, 50),
            "food_needed": random.choice([True, False]),
            "rescue_needed": random.choice([True, False])
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

        # ⏳ Wait / other
        else:
            reward += 0

        # 🔥 DYNAMIC CHANGE (important)
        self.state["injured"] = max(0, self.state["injured"] + random.randint(-3, 5))

        # Random new needs
        if random.random() < 0.3:
            self.state["food_needed"] = True

        if random.random() < 0.3:
            self.state["rescue_needed"] = True

        # Random zone change (rare)
        if random.random() < 0.2:
            self.state["zone"] = random.choice(["Zone A", "Zone B", "Zone C"])

        # ✅ Reward never negative
        reward = max(0, reward)

        done = False  # continuous simulation

        return self.state, reward, done, {}

