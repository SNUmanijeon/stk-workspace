from decimal import Decimal, localcontext
import math
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from stk_toolkit.two_body import hohmann_transfer, ideal_burn, orbital_period


class TwoBodyTests(unittest.TestCase):
    def test_dimensionless_reference_and_reversal(self):
        # mu=1, radii 1 and 4: transfer a=2.5; vis-viva gives sqrt(1.6), sqrt(.1).
        up = hohmann_transfer(1, 1, 4)
        down = hohmann_transfer(1, 4, 1)
        self.assertAlmostEqual(up.departure_delta_v_m_s, math.sqrt(1.6)-1, places=14)
        self.assertAlmostEqual(up.arrival_delta_v_m_s, .5-math.sqrt(.1), places=14)
        self.assertAlmostEqual(up.coast_time_s, math.pi*math.sqrt(2.5**3), places=14)
        self.assertAlmostEqual(down.departure_delta_v_m_s, -up.arrival_delta_v_m_s)
        self.assertAlmostEqual(down.arrival_delta_v_m_s, -up.departure_delta_v_m_s)
        self.assertEqual(down.total_delta_v_m_s, up.total_delta_v_m_s)

    def test_no_transfer_and_kepler_scaling(self):
        self.assertEqual(hohmann_transfer(1, 3, 3).coast_time_s, 0)
        self.assertEqual(hohmann_transfer(1, 3, 3).total_delta_v_m_s, 0)
        self.assertAlmostEqual(orbital_period(1, 4)/orbital_period(1, 1), 8)

    def test_small_raise_against_high_precision_vis_viva(self):
        with localcontext() as context:
            context.prec = 60
            r1 = Decimal('7000000')
            r2 = Decimal('7000000.000001')
            # Use the exact binary float supplied to the public API.
            r2 = Decimal.from_float(float(r2))
            mu = Decimal('398600441800000')
            a = (r1+r2)/2
            expected = (mu*(2/r1-1/a)).sqrt()-(mu/r1).sqrt()
        actual = hohmann_transfer(float(mu), float(r1), float(r2)).departure_delta_v_m_s
        self.assertTrue(math.isclose(actual, float(expected), rel_tol=1e-14))

    def test_rocket_equation_mass_and_staging(self):
        # delta-v = ve*ln(2) halves mass. Constant 10 N / 1000 m/s = .01 kg/s.
        burn = ideal_burn(1000*math.log(2), 100, 10, 1000, dry_mass_kg=40)
        self.assertAlmostEqual(burn.final_mass_kg, 50)
        self.assertAlmostEqual(burn.propellant_kg, 50)
        self.assertAlmostEqual(burn.duration_s, 5000)
        first = ideal_burn(100, 100, 10, 1000)
        second = ideal_burn(-200, first.final_mass_kg, 10, 1000)
        total = ideal_burn(300, 100, 10, 1000)
        self.assertAlmostEqual(second.final_mass_kg, total.final_mass_kg)
        self.assertAlmostEqual(first.propellant_kg+second.propellant_kg, total.propellant_kg)
        self.assertAlmostEqual(first.duration_s+second.duration_s, total.duration_s)

    def test_small_burn_and_zero(self):
        burn = ideal_burn(1e-12, 100, 10, 1000)
        self.assertGreater(burn.propellant_kg, 0)
        self.assertAlmostEqual(burn.propellant_kg/1e-13, 1, places=14)
        zero = ideal_burn(0, 100, 10, 1000, dry_mass_kg=100)
        self.assertEqual((zero.duration_s, zero.propellant_kg, zero.final_mass_kg), (0, 0, 100))

    def test_invalid_inputs_and_fuel_exhaustion(self):
        for bad in (0, -1, math.nan, math.inf):
            for args in ((bad, 1, 4), (1, bad, 4), (1, 1, bad)):
                with self.subTest(args=args), self.assertRaises(ValueError):
                    hohmann_transfer(*args)
        for args in ((math.nan, 100, 10, 1000), (1, 0, 10, 1000),
                     (1, 100, -10, 1000), (1, 100, 10, math.inf)):
            with self.assertRaises(ValueError):
                ideal_burn(*args)
        with self.assertRaises(ValueError):
            ideal_burn(1000, 100, 10, 1000, dry_mass_kg=90)


if __name__ == '__main__':
    unittest.main()
