from cat import Cat

from unittest import TestCase, main


class CatTest(TestCase):
    def setUp(self):
        # Arrange
        self.cat = Cat('Gato')

    def test_cat_init_values(self):
        self.assertEqual('Gato', self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_m_eat_fed_exception(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        expected = 'Already fed.'
        self.assertEqual(expected, str(ex.exception))

    def test_m_eat_fed_sleepy_size_increment(self):
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

        # Act
        self.cat.eat()

        # Assert
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_m_sleep_exceptions(self):
        self.assertFalse(self.cat.fed)
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        expected = 'Cannot sleep while hungry'
        self.assertEqual(expected, str(ex.exception))

    def test_m_sleep_change_sleepy_status(self):
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()
