"""Print a caller-parameterized two-body transfer and optional ideal burn budget."""
import argparse
from dataclasses import asdict
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from stk_toolkit.two_body import hohmann_transfer, ideal_burn


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mu-m3-s2', type=float, required=True)
    parser.add_argument('--departure-radius-m', type=float, required=True)
    parser.add_argument('--arrival-radius-m', type=float, required=True)
    parser.add_argument('--mass-kg', type=float)
    parser.add_argument('--thrust-n', type=float)
    parser.add_argument('--exhaust-velocity-m-s', type=float)
    parser.add_argument('--dry-mass-kg', type=float, default=0)
    args = parser.parse_args()
    burn_inputs = (args.mass_kg, args.thrust_n, args.exhaust_velocity_m_s)
    if any(x is not None for x in burn_inputs) and not all(x is not None for x in burn_inputs):
        parser.error('Specify mass, thrust and exhaust velocity together')
    if args.dry_mass_kg and args.mass_kg is None:
        parser.error('Dry mass requires the burn-budget inputs')
    transfer = hohmann_transfer(args.mu_m3_s2, args.departure_radius_m, args.arrival_radius_m)
    result = dict(model='coplanar_circular_impulsive_two_body', **asdict(transfer),
                  total_delta_v_m_s=transfer.total_delta_v_m_s)
    if args.mass_kg is not None:
        result['ideal_burn_budget'] = asdict(ideal_burn(transfer.total_delta_v_m_s,
            *burn_inputs, dry_mass_kg=args.dry_mass_kg))
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
