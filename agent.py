class Agent:
    def act(self, state):
        if state["zone"] == "Zone A" and state["injured"] > 20:
            return 0, "Critical injuries in Zone A → sending ambulance"
        elif state["injured"] > 0:
            return 0, "Injuries detected → ambulance"
        elif state["rescue_needed"]:
            return 2, "Rescue needed → boat"
        elif state["food_needed"]:
            return 1, "Food needed → sending food"
        else:
            return 3, "No urgent need → waiting"


