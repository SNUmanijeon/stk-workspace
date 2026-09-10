"""Scalar two-body transfer and ideal rocket calculations in SI units.

Extracted from repeated legacy orbit-transfer helpers. No STK connection,
central-body constants, mission defaults, or propagated results are implicit.
"""
from __future__ import annotations

from dataclasses import dataclass
import math


def _positive(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be finite and positive")
    return value


def orbital_period(mu_m3_s2: float, semimajor_axis_m: float) -> float:
    """Return an elliptic two-body orbital period in seconds."""
    mu = _positive("mu_m3_s2", mu_m3_s2)
    a = _positive("semimajor_axis_m", semimajor_axis_m)
    return 2 * math.pi * math.sqrt(a**3 / mu)


@dataclass(frozen=True)
class HohmannTransfer:
    departure_delta_v_m_s: float
    arrival_delta_v_m_s: float
    coast_time_s: float

    @property
    def total_delta_v_m_s(self) -> float:
        return abs(self.departure_delta_v_m_s) + abs(self.arrival_delta_v_m_s)


def hohmann_transfer(mu_m3_s2: float, departure_radius_m: float,
                     arrival_radius_m: float) -> HohmannTransfer:
    """Coplanar circular-to-circular impulsive transfer; radii from body center.

    Signed burns are along velocity: positive for raising, negative for lowering.
    Equal radii return zero burns and zero coast time (no transfer is needed).
    Excludes plane changes, perturbations and finite-burn trajectory effects.
    """
    mu = _positive("mu_m3_s2", mu_m3_s2)
    r1 = _positive("departure_radius_m", departure_radius_m)
    r2 = _positive("arrival_radius_m", arrival_radius_m)
    if r1 == r2:
        return HohmannTransfer(0.0, 0.0, 0.0)
    # Rationalized forms avoid subtracting almost equal numbers for small raises.
    fraction = (r2 - r1) / (r1 + r2)
    dv1 = math.sqrt(mu / r1) * fraction / (math.sqrt(2*r2/(r1+r2)) + 1)
    dv2 = math.sqrt(mu / r2) * fraction / (1 + math.sqrt(2*r1/(r1+r2)))
    return HohmannTransfer(dv1, dv2, orbital_period(mu, (r1+r2)/2) / 2)


@dataclass(frozen=True)
class IdealBurn:
    duration_s: float
    propellant_kg: float
    final_mass_kg: float


def ideal_burn(delta_v_m_s: float, initial_mass_kg: float, thrust_n: float,
               exhaust_velocity_m_s: float, *, dry_mass_kg: float = 0.0) -> IdealBurn:
    """Constant-thrust rocket-equation mass/time budget using |delta-v|.

    Exhaust velocity is Isp times standard gravity, both caller-selected.
    This is an ideal characteristic-delta-v budget, not a finite-burn targeting
    or trajectory solution. Rejects insufficient propellant and nonfinite inputs.
    """
    dv = float(delta_v_m_s)
    if not math.isfinite(dv):
        raise ValueError("delta_v_m_s must be finite")
    mass = _positive("initial_mass_kg", initial_mass_kg)
    thrust = _positive("thrust_n", thrust_n)
    ve = _positive("exhaust_velocity_m_s", exhaust_velocity_m_s)
    dry = float(dry_mass_kg)
    if not math.isfinite(dry) or not 0 <= dry <= mass:
        raise ValueError("dry_mass_kg must be finite and between zero and initial mass")
    final = mass * math.exp(-abs(dv) / ve)
    if final < dry:
        raise ValueError("Requested delta-v exceeds the available propellant")
    propellant = mass * -math.expm1(-abs(dv) / ve)
    return IdealBurn(propellant * ve / thrust, propellant, final)
