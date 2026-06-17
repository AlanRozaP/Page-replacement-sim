import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from simulator import Simulator

def test_simulator_runs_all():
    sim = Simulator(frames=3, reference_string=[1, 2, 3, 1, 4])
    results = sim.run_all()
    assert "FIFO" in results
    assert "LRU" in results
    assert "Optimal" in results
    assert "Clock" in results
    for r in results.values():
        assert "faults" in r
        assert "hits" in r
        assert "hit_rate" in r

def test_simulator_fifo_match():
    sim = Simulator(frames=3, reference_string=[1, 2, 3, 1, 4])
    results = sim.run_all()
    assert results["FIFO"]["faults"] == 4
