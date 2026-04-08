import random

class Agent:
    def act(self, state):

        actions = []

        # Critical injury
        if state["injured"] > 20:
            actions.append((0, "Critical injuries → ambulance"))
            actions.append((4, "Deploy doctors for support"))

        # Food needed
        if state["food_needed"]:
            actions.append((1, "Food shortage → supply food"))
            actions.append((6, "Send water supply"))

        # Rescue needed
        if state["rescue_needed"]:
            actions.append((2, "Rescue needed → boat"))
            actions.append((8, "Helicopter rescue"))

        # If nothing urgent
        if not actions:
            actions.append((15, "Monitoring situation"))

        # 🔥 RANDOMLY PICK ONE
        return random.choice(actions)
