from env import DisasterEnv

# Create environment globally
env = DisasterEnv()

def reset():
    """
    Reset the environment and return initial state as a dict
    """
    state = env.reset()
    return state  # Must be a dictionary

def step(action):
    """
    Take an action (integer) and return dict:
    {
        "state": ...,   # dict
        "reward": ...,  # number
        "done": ...,    # boolean
        "info": {}      # optional dictionary
    }
    """
    state, reward, done, info = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }
