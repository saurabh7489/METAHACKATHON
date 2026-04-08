class Agent:
    def act(self, state):
        if state["injured"] > 0:
            return 0, "High injuries → sending ambulance"
        elif state["rescue_needed"]:
            return 2, "Rescue needed → sending boat"
        elif state["food_needed"]:
            return 1, "Food shortage → sending food"
        else:
            return 3, "No urgent need → waiting"
