from project.vehicle import Vehicle

from unittest import TestCase, main


class TestVehicle(TestCase):
    _fuel = 60.5
    _horse_p = 140.5

    def setUp(self):
        self.v = Vehicle(self._fuel, self._horse_p)

    def test_init_correct_value_types(self):
        self.assertIsInstance(self.v.fuel, float)
        self.assertIsInstance(self.v.capacity, float)
        self.assertIsInstance(self.v.horse_power, float)
        self.assertIsInstance(self.v.DEFAULT_FUEL_CONSUMPTION, float)

    def test_init_values(self):
        self.assertEqual(self._fuel, self.v.fuel)
        self.assertEqual(self._fuel, self.v.capacity)
        self.assertEqual(self._horse_p, self.v.horse_power)
        self.assertEqual(1.25, self.v.DEFAULT_FUEL_CONSUMPTION)

    def test_mod_drive_lt_fuel_needed_error(self):
        kilometers = 500
        with self.assertRaises(Exception) as ex:
            self.v.drive(kilometers)
        expected = 'Not enough fuel'
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(self._fuel, self.v.fuel)

    def test_mod_drive_gt_fuel_needed(self):
        kilometers = 20
        self.assertEqual(self._fuel, self.v.fuel)
        self.v.drive(kilometers)
        expected = self._fuel - (1.25 * kilometers)
        self.assertEqual(expected, self.v.fuel)

    def test_mod_refuel_gt_fuel_cap_error(self):
        fill = 100
        self.assertEqual(self._fuel, self.v.fuel)
        with self.assertRaises(Exception) as ex:
            self.v.refuel(fill)
        expected = 'Too much fuel'
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(self._fuel, self.v.fuel)

    def test_mod_refuel_lt_fuel_cap_success(self):
        self.v.fuel = 0
        fill = 20
        self.v.refuel(fill)
        self.assertEqual(20, self.v.fuel)

    def test_printed_class_with_no_changed_attributes(self):
        expected = f'The vehicle has {self._horse_p} horse power with {self._fuel} fuel left and 1.25 fuel consumption'
        result = str(self.v)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()
