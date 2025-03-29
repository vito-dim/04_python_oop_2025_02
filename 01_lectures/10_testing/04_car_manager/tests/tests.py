from car_manager import Car

from unittest import TestCase, main


class TestCar(TestCase):
    make = 'm'
    model = 'skoda'
    consumption = 1
    fuel_cap = 120

    def setUp(self):
        self.c = Car(self.make, self.model, self.consumption, self.fuel_cap)

    def test_init_values(self):
        self.assertEqual(self.make, self.c.make)
        self.assertEqual(self.model, self.c.model)
        self.assertEqual(self.consumption, self.c.fuel_consumption)
        self.assertEqual(self.fuel_cap, self.c.fuel_capacity)
        self.assertEqual(0, self.c.fuel_amount)

    def test_set_make_empty_error(self):
        self.assertEqual(self.make, self.c.make)
        with self.assertRaises(Exception) as ex:
            self.c.make = ''
        expected = 'Make cannot be null or empty!'
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(self.make, self.c.make)

    def test_set_make_none_error(self):
        self.assertEqual(self.make, self.c.make)
        with self.assertRaises(Exception) as ex:
            self.c.make = None
        expected = 'Make cannot be null or empty!'
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(self.make, self.c.make)

    def test_set_make_success(self):
        new_value = 'take'
        self.assertEqual(self.make, self.c.make)
        self.c.make = new_value
        self.assertEqual(new_value, self.c.make)

    def test_set_model_empty_error(self):
        new_value = ''
        with self.assertRaises(Exception) as ex:
            self.c.model = new_value
        expected = 'Model cannot be null or empty!'
        self.assertEqual(expected, str(ex.exception))

    def test_set_model_none_error(self):
        new_value = None
        with self.assertRaises(Exception) as ex:
            self.c.model = new_value
        expected = 'Model cannot be null or empty!'
        self.assertEqual(expected, str(ex.exception))

    def test_set_model_success(self):
        new_value = 'opel'
        self.c.model = new_value
        self.assertEqual(new_value, self.c.model)

    def test_set_fuel_consumption_lt_0_error(self):
        with self.assertRaises(Exception) as ex:
            self.c.fuel_consumption = -1
        expected = 'Fuel consumption cannot be zero or negative!'
        self.assertEqual(expected, str(ex.exception))

    def test_set_fuel_consumption_eq_0_error(self):
        with self.assertRaises(Exception) as ex:
            self.c.fuel_consumption = 0
        expected = 'Fuel consumption cannot be zero or negative!'
        self.assertEqual(expected, str(ex.exception))

    def test_set_fuel_consumption_success(self):
        self.c.fuel_consumption = 5
        self.assertEqual(5, self.c.fuel_consumption)

    def test_set_fuel_capacity_lt_0_error(self):
        with self.assertRaises(Exception) as ex:
            self.c.fuel_capacity = -5
        expected = 'Fuel capacity cannot be zero or negative!'
        self.assertEqual(expected, str(ex.exception))

    def test_set_fuel_capacity_eq_0_error(self):
        with self.assertRaises(Exception) as ex:
            self.c.fuel_capacity = 0
        expected ='Fuel capacity cannot be zero or negative!'
        self.assertEqual(expected, str(ex.exception))

    def test_set_fuel_capacity_success(self):
        self.c.fuel_capacity = 120
        self.assertEqual(120, self.c.fuel_capacity)

    def test_set_fuel_amount_lt_0_error(self):
        with self.assertRaises(Exception) as ex:
            self.c.fuel_amount = -3
        expected = 'Fuel amount cannot be negative!'
        self.assertEqual(expected, str(ex.exception))

    def test_set_fuel_amount_eq_0_success(self):
        self.assertEqual(0, self.c.fuel_amount)

    def test_set_fuel_amount_gt_0_success(self):
        self.c.fuel_amount = 20
        self.assertEqual(20, self.c.fuel_amount)

    def test_mod_refuel_error(self):
        added_fuel = -3
        with self.assertRaises(Exception) as ex:
            self.c.refuel(added_fuel)
        expected = 'Fuel amount cannot be zero or negative!'
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(0, self.c.fuel_amount)

    def test_mod_refuel_success_normal_fuel_amount(self):
        self.c.fuel_capacity = 50
        self.c.fuel_amount = 10
        added_fuel = 5
        expected = self.c.fuel_amount + added_fuel
        self.c.refuel(added_fuel)
        self.assertEqual(expected, self.c.fuel_amount)

    def test_mod_refuel_success_gt_fuel_amount(self):
        self.c.fuel_capacity = 50
        self.c.fuel_amount = 40
        added_fuel = 30
        self.c.refuel(added_fuel)
        self.assertEqual(self.c.fuel_capacity, self.c.fuel_amount)

    def test_mod_drive_eq_0_error(self):
        self.assertEqual(0, self.c.fuel_amount)
        distance = 100
        with self.assertRaises(Exception) as ex:
            self.c.drive(distance)
        expected = 'You don\'t have enough fuel to drive!'
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(0, self.c.fuel_amount)

    def test_mod_drive_gt_0_error(self):
        fuel = 5
        distance = 999
        self.c.fuel_amount = fuel
        with self.assertRaises(Exception) as ex:
            self.c.drive(distance)
        expected = 'You don\'t have enough fuel to drive!'
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(fuel, self.c.fuel_amount)

    def test_mod_drive_success(self):
        fuel = 100
        distance = 10
        self.c.fuel_amount = fuel
        expected = fuel - ((distance / 100) * self.consumption)
        self.c.drive(distance)
        self.assertEqual(expected, self.c.fuel_amount)



if __name__ == '__main__':
    main()
