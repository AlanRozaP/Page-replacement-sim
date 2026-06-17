#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from simulator import Simulator
from workload import generate_workload, mobile_scenario, LOCALITY_BIAS

def main():
    parser = argparse.ArgumentParser(description="Page Replacement Simulator for Mobile Devices")
    parser.add_argument("--frames", type=int, default=3, help="Number of physical memory frames (default: 3)")
    parser.add_argument("--length", type=int, default=50, help="Length of generated reference string (default: 50)")
    parser.add_argument("--pages", type=int, default=10, help="Number of distinct pages (default: 10)")
    parser.add_argument("--locality", type=float, default=LOCALITY_BIAS, help="Locality bias 0.0-1.0 (default: 0.8)")
    parser.add_argument("--scenario", type=str, default=None, choices=["default", "social_media", "gaming", "multitasking"], help="Use a preset mobile scenario")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducible workloads")
    parser.add_argument("--refs", type=int, nargs="+", default=None, help="Provide a custom reference string (space-separated ints)")

    args = parser.parse_args()

    if args.refs:
        reference_string = args.refs
    elif args.scenario:
        reference_string = mobile_scenario(args.scenario)
    else:
        reference_string = generate_workload(length=args.length, num_pages=args.pages, locality=args.locality, seed=args.seed)

    print(f"Reference string ({len(reference_string)} accesses):")
    print(" ".join(str(p) for p in reference_string))
    print(f"Frames: {args.frames}")

    sim = Simulator(frames=args.frames, reference_string=reference_string)
    results = sim.run_all()
    print(Simulator.format_results(results, title="Page Replacement Comparison"))

    best = min(results, key=lambda k: results[k]["faults"])
    print(f"\nBest algorithm: {best} ({results[best]['faults']} faults)")

if __name__ == "__main__":
    main()
