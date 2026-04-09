from env import DisasterEnv

# Initialize environment
env = DisasterEnv()

def reset():
    """
    Reset the environment and return initial state.
    """
    return env.reset()

def step(action):
    """
    Take an action and return result in OpenEnv format:
    {
        "state": ...,
        "reward": ...,
        "done": ...,
        "info": {}
    }
    """
    state, reward, done, info = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }
