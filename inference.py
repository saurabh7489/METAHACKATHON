from env import DisasterEnv

env = DisasterEnv()


def reset(difficulty: str = "medium") -> dict:
    """
    Reset environment and return initial state.
    difficulty: 'easy' | 'medium' | 'hard'
    """
    state = env.reset(difficulty=difficulty)
    if not isinstance(state, dict):
        raise TypeError("Reset must return a dictionary")
    return state


def step(action: int) -> dict:
    """
    Take an integer action (0–19) and return a result dict:
    {
        'state': dict,
        'reward': float,
        'done': bool,
        'info': dict
    }
    """
    if not isinstance(action, int):
        raise TypeError("Action must be an integer")
    if not (0 <= action <= 19):
        raise ValueError("Action must be between 0 and 19")

    state, reward, done, info = env.step(action)

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
        "info": info,
    }