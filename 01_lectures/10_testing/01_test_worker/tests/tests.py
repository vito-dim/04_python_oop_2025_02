from test_worker import Worker

from unittest import TestCase, main


class WorkerTests(TestCase):
    def setUp(self):
        self.w = Worker('Pesho', 100, 0)

    def test_cls_init_checks(self):
        self.assertEqual('Pesho', self.w.name)
        self.assertEqual(100, self.w.salary)
        self.assertEqual(0, self.w.energy)
        self.assertEqual(0, self.w.money)

    def test_m_work_exceptions(self):
        with self.assertRaises(Exception) as ex:
            self.w.energy = 0
            self.w.work()
            self.w.energy = -1
            self.w.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_m_work_increase_money(self):
        self.w.energy = 3
        self.assertEqual(0, self.w.money)
        self.w.work()
        self.assertEqual(100, self.w.money)
        self.w.work()
        self.assertEqual(100 + 100, self.w.money)

    def test_m_work_decrease_energy(self):
        self.w.energy = 3
        self.assertEqual(3, self.w.energy)
        self.w.work()
        self.assertEqual(2, self.w.energy)

    def test_m_rest_increment_energy(self):
        self.assertEqual(0, self.w.energy)
        self.w.rest()
        self.assertEqual(1, self.w.energy)

    def test_m_get_info(self):
        expected_result = f'{self.w.name} has saved {self.w.money} money.'
        result = self.w.get_info()
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()


# from unittest import TestCase, main
#
#
# class TestWorker(TestCase):
#     def setUp(self):
#         self.worker_no_energy = Worker("Test", 100, 0)
#
#     def test_worker_init(self):
#         # Arrange and act
#         worker = Worker("Test", 100, 10)
#
#         # Assert
#         self.assertEqual("Test", worker.name)
#         self.assertEqual(100, worker.salary)
#         self.assertEqual(10, worker.energy)
#         self.assertEqual(0, worker.money)
#
#     def test_worker_has_no_energy_work_raises(self):
#
#         # Act, Assert
#         with self.assertRaises(Exception) as ex:
#             self.worker_no_energy.work()
#
#         # Assert
#         self.assertEqual("Not enough energy.", str(ex.exception))
#         self.assertEqual(self.worker_no_energy.money, 0)
#         self.assertEqual(self.worker_no_energy.energy, 0)
#
#         # Test with negative energy
#         self.worker_no_energy.energy = -1
#         # Act, Assert
#         with self.assertRaises(Exception) as ex:
#             self.worker_no_energy.work()
#
#         # Assert
#         self.assertEqual("Not enough energy.", str(ex.exception))
#         self.assertEqual(self.worker_no_energy.money, 0)
#         self.assertEqual(self.worker_no_energy.energy, -1)
#
#     def test_worker_works(self):
#         worker = Worker("Test", 100, 2)
#
#         self.assertEqual(0, worker.money)
#         self.assertEqual(2, worker.energy)
#
#         # Act
#         worker.work()
#
#         # Assert
#         self.assertEqual(100, worker.money)
#         self.assertEqual(1, worker.energy)
#
#         worker.work()
#         self.assertEqual(200, worker.money)
#         self.assertEqual(0, worker.energy)
#
#     def test_worker_rest_increase_energy(self):
#         self.assertEqual(0,  self.worker_no_energy.energy)
#
#         # Act
#         self.worker_no_energy.rest()
#
#         # Assert
#         self.assertEqual(1,  self.worker_no_energy.energy)
#
#     def test_get_info(self):
#
#         # Act
#         result =  self.worker_no_energy.get_info()
#
#         # Assert
#         self.assertEqual(f'Test has saved 0 money.', result)
#
#
# if __name__ == "__main__":
#     main()