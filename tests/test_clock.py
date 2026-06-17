import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from algorithms.clock import Clock

def test_clock_basic():
    clock = Clock(frames=3)
    refs = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    faults = 0
    for page in refs:
        if not clock.access(page):
            faults += 1
    assert faults >= 7
    assert faults <= 10

def test_clock_gives_second_chance():
    clock = Clock(frames=2)
    clock.access(1)  # fault
    clock.access(2)  # fault
    clock.access(1)  # hit — ref bit for 1 stays set
    clock.access(3)  # fault — should evict 2, not 1
    assert 1 in clock.memory_set
    assert 2 not in clock.memory_set
