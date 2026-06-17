import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from simulator import Simulator
from workload import generate_workload, mobile_scenario

def test_integration_generated_workload():
    refs = generate_workload(length=100, num_pages=15, locality=0.7, seed=42)
    sim = Simulator(frames=4, reference_string=refs)
    results = sim.run_all()
    assert len(results) == 4
    assert results["Optimal"]["faults"] <= results["FIFO"]["faults"]
    for name, data in results.items():
        assert 0.0 <= data["hit_rate"] <= 1.0

def test_integration_preset_scenario():
    refs = mobile_scenario("multitasking")
    sim = Simulator(frames=3, reference_string=refs)
    results = sim.run_all()
    assert results["Optimal"]["faults"] <= results["FIFO"]["faults"]
