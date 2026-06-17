# Page Replacement Simulator for Mobile Devices

A Python simulator comparing FIFO, LRU, Optimal, and Clock page replacement algorithms with workloads inspired by mobile device memory patterns.

## Project Structure

```
page-replacement-sim/
├── algorithms/
│   ├── base.py
│   ├── fifo.py
│   ├── lru.py
│   ├── optimal.py
│   └── clock.py
├── tests/
│   ├── test_fifo.py
│   ├── test_lru.py
│   ├── test_optimal.py
│   ├── test_clock.py
│   ├── test_workload.py
│   ├── test_simulator.py
│   └── test_integration.py
├── simulator.py
├── workload.py
├── main.py
└── README.md
```

## Running the Simulator

```bash
python main.py
python main.py --scenario social_media --frames 3
python main.py --frames 3 --refs 1 2 3 4 1 2 5 1 2 3 4 5
python main.py --frames 4 --length 200 --pages 20 --locality 0.85 --seed 123
```

## Running Tests

```bash
python -m pytest tests/ -v
```

## Algorithms

- **FIFO** — First-In-First-Out
- **LRU** — Least Recently Used
- **Optimal** — Belady's algorithm (theoretical best)
- **Clock** — Second Chance approximation of LRU

## Mobile Workload Model

The workload generator simulates mobile behavior by maintaining a "working set" of active apps. High locality means a small set of apps are accessed repeatedly.
