import random


class RandomAgent:
    """Baseline: picks a random action every step."""

    def act(self, state):
        action = random.randint(0, 19)
        return action, "Random action selected"


class RuleBasedAgent:
    """
    Priority-driven rule-based agent.
    Handles all 20 actions with state-aware decision making.
    """

    def act(self, state):
        injured = state.get("injured", 0)
        food = state.get("food_needed", False)
        rescue = state.get("rescue_needed", False)
        power = state.get("power_outage", False)
        infra = state.get("infrastructure_damage", False)
        disease = state.get("disease_outbreak", False)
        people = state.get("people", 0)

        # P1: Active disease outbreak → contain immediately
        if disease:
            action = random.choice([10, 11, 12, 13])
            reasons = {
                10: "Disease outbreak → quarantine zone",
                11: "Disease outbreak → sanitize area",
                12: "Disease outbreak → distribute masks",
                13: "Disease outbreak → vaccination drive",
            }
            return action, reasons[action]

        # P2: Critical injuries (>25) → heavy medical response
        if injured > 25:
            action = random.choice([0, 4, 5, 8])
            reasons = {
                0: "Critical injuries → ambulance dispatch",
                4: "Critical injuries → deploy doctors",
                5: "Critical injuries → medical camp",
                8: "Critical injuries → helicopter rescue",
            }
            return action, reasons[action]

        # P3: Moderate injuries
        if injured > 0:
            action = random.choice([0, 4, 7])
            reasons = {
                0: "Injuries present → ambulance",
                4: "Injuries present → deploy doctors",
                7: "Injuries present → distribute medicines",
            }
            return action, reasons[action]

        # P4: Food / water shortage
        if food:
            action = random.choice([1, 6])
            reasons = {
                1: "Food shortage → food supply",
                6: "Food shortage → water supply",
            }
            return action, reasons[action]

        # P5: Rescue needed
        if rescue:
            action = random.choice([2, 8, 9])
            reasons = {
                2: "Rescue needed → rescue boat",
                8: "Rescue needed → helicopter",
                9: "Rescue needed → evacuation bus",
            }
            return action, reasons[action]

        # P6: Power outage
        if power:
            action = random.choice([16, 17])
            reasons = {
                16: "Power outage → restore electricity",
                17: "Power outage → setup communication",
            }
            return action, reasons[action]

        # P7: Infrastructure damage
        if infra:
            action = random.choice([17, 19])
            reasons = {
                17: "Infrastructure damage → setup network",
                19: "Infrastructure damage → clear roads",
            }
            return action, reasons[action]

        # P8: Large population → shelter support
        if people > 100:
            return 18, "Large population → temporary shelter"

        # P9: Alert authorities if borderline
        if random.random() < 0.3:
            return 14, "Alerting authorities as precaution"

        # P10: Stable → monitor
        return 15, "Situation stable → monitoring"


class GreedyAgent:
    """
    Greedy agent: always picks the action most likely to
    maximise immediate reward given the current state.
    """

    def act(self, state):
        injured = state.get("injured", 0)
        food = state.get("food_needed", False)
        rescue = state.get("rescue_needed", False)
        power = state.get("power_outage", False)
        infra = state.get("infrastructure_damage", False)
        disease = state.get("disease_outbreak", False)
        people = state.get("people", 0)

        scores = {}

        scores[8] = 9.0 if (rescue or injured > 20) else -2.0   # helicopter
        scores[0] = 8.0 if injured > 0 else -1.0                 # ambulance
        scores[10] = 7.0 if disease else 0.5                     # quarantine
        scores[13] = 6.0 if disease else 1.0                     # vaccination
        scores[4] = 6.0 if injured > 10 else 1.0                 # doctors
        scores[16] = 6.0 if power else -1.0                      # electricity
        scores[2] = 6.0 if rescue else -1.0                      # boat
        scores[5] = 5.0 if (injured > 5 or disease) else 0.5     # medical camp
        scores[1] = 5.0 if food else -1.0                        # food
        scores[9] = 5.0 if (rescue or people > 100) else 0.5     # evac bus
        scores[19] = 5.0 if infra else -1.0                      # clear roads
        scores[7] = 4.0 if (injured > 0 or disease) else 0.5     # medicines
        scores[17] = 4.0 if (power or infra) else 0.5            # comms
        scores[18] = 4.0 if (people > 80 or rescue) else 0.5     # shelter
        scores[14] = 3.0 if (injured > 20 or rescue) else 0.5    # alert
        scores[11] = 3.0 if (disease or injured > 10) else 0.5   # sanitize
        scores[6] = 3.0 if food else 0.5                         # water
        scores[12] = 3.0 if disease else 0.5                     # masks
        scores[15] = 0.5                                          # monitor
        scores[3] = 1.0 if (injured == 0 and not food and not rescue) else -2.0

        best_action = max(scores, key=scores.get)
        return best_action, f"Greedy selection (expected reward: {scores[best_action]:.1f})"