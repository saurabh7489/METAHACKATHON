import random

class Agent:
    def act(self, state):

        # 🚑 Critical injuries
        if state["injured"] > 25:
            return random.choice([0, 4, 5]), "High injuries → ambulance / doctors / medical camp"

        elif state["injured"] > 0:
            return random.choice([0, 4, 7]), "Treat injured → ambulance / doctors / medicines"

        # 🍲 Food / water
        elif state["food_needed"]:
            return random.choice([1, 6, 18]), "Food/water shortage → supply or shelter"

        # 🚤 Rescue
        elif state["rescue_needed"]:
            return random.choice([2, 8, 9]), "People trapped → rescue operations"

        # ⚡ Infrastructure issues
        elif random.random() < 0.3:
            return random.choice([16, 17, 19]), "Infrastructure damage → restore power / network / roads"

        # 🦠 Pandemic scenario
        elif random.random() < 0.3:
            return random.choice([10, 11, 12, 13]), "Health safety → quarantine / sanitize / masks / vaccination"

        # 📢 Emergency alert
        elif random.random() < 0.2:
            return 14, "Alerting authorities"

        # 👀 Default monitoring
        else:
            return random.choice([3, 15]), "Monitoring situation"
