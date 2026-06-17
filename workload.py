import random
from typing import List

LOCALITY_BIAS = 0.8
UNIFORM = 0.0

def generate_workload(length: int, num_pages: int, locality: float = LOCALITY_BIAS, seed: int = None) -> List[int]:
    if seed is not None:
        random.seed(seed)
    refs = []
    working_set_size = max(1, int(num_pages * (1 - locality) + 3))
    working_set = random.sample(range(1, num_pages + 1), min(working_set_size, num_pages))
    for _ in range(length):
        if random.random() < locality:
            page = random.choice(working_set)
        else:
            page = random.randint(1, num_pages)
        refs.append(page)
    return refs

def mobile_scenario(name: str = "default") -> List[int]:
    scenarios = {
        "default": [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5],
        "social_media": [1, 1, 2, 1, 3, 2, 1, 4, 1, 2, 3, 1, 5, 1],
        "gaming": [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7, 1, 2],
        "multitasking": [1, 2, 3, 4, 5, 1, 6, 2, 7, 3, 8, 4, 9, 5, 10],
    }
    return scenarios.get(name, scenarios["default"])
