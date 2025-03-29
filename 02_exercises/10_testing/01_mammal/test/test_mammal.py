from project.mammal import Mammal

from unittest import TestCase, main


class TestMammal(TestCase):
    name = 'foxy'
    type = 'dog'
    sound = 'bark'

    def setUp(self):
        self.animal = Mammal(self.name, self.type, self.sound)

    def test_init_values(self):
        self.assertEqual(self.name, self.animal.name)
        self.assertEqual(self.type, self.animal.type)
        self.assertEqual(self.sound, self.animal.sound)
        self.assertEqual('animals', self.animal._Mammal__kingdom)

    def test_mod_make_sound(self):
        expected = f'{self.name} makes {self.sound}'
        result = self.animal.make_sound()
        self.assertEqual(expected, result)

    def test_mod_get_kingdom(self):
        expected = 'animals'
        result = self.animal.get_kingdom()
        self.assertEqual(expected, result)

    def test_mod_info(self):
        expected = f'{self.name} is of type {self.type}'
        self.assertEqual(expected, self.animal.info())


if __name__ == '__main__':
    main()
