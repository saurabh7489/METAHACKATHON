from env import DisasterEnv

# Create global environment instance
env = DisasterEnv()

def reset():
    """
    Reset environment and return initial state as dict
    """
    state = env.reset()
    if not isinstance(state, dict):
        raise TypeError("Reset must return a dictionary")
    return state

def step(action):
    """
    Take an integer action and return a dictionary:
    {
        'state': dict,
        'reward': float,
        'done': bool,
        'info': dict
    }
    """
    if not isinstance(action, int):
        raise TypeError("Action must be an integer")

    state, reward, done, info = env.step(action)

    # Type checks
    if not isinstance(state, dict):
        raise TypeError("State must be a dictionary")
    if not isinstance(reward, (int, float)):
        raise TypeError("Reward must be a number")
    if not isinstance(done, bool):
        raise TypeError("Done must be boolean")
    if not isinstance(info, dict):
        raise TypeError("Info must be a dictionary")

    return {
        "state": state,
        "reward": float(reward),
        "done": done,
        "info": info
    }
