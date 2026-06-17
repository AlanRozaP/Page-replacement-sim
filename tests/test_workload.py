import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from workload import generate_workload, LOCALITY_BIAS

def test_workload_length():
    refs = generate_workload(length=50, num_pages=10, locality=LOCALITY_BIAS)
    assert len(refs) == 50
    assert all(1 <= p <= 10 for p in refs)

def test_workload_locality():
    refs = generate_workload(length=1000, num_pages=20, locality=0.9)
    from collections import Counter
    counts = Counter(refs)
    top5 = sum(v for _, v in counts.most_common(5))
    assert top5 > 500
