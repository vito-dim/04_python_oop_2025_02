from project.hero import Hero

from unittest import TestCase, main


class TestHero(TestCase):
    _name = 'Jorje'
    _lvl = 80
    _health = 100.00
    _dmg = 150.00

    def setUp(self):
        self.hero = Hero(self._name, self._lvl, self._health, self._dmg)
        self.enemy_hero = Hero('Poncho', 20, 40, 50)

    def test_validate_init_value_types(self):
        self.assertIsInstance(self.hero.username, str)
        self.assertIsInstance(self.hero.level, int)
        self.assertIsInstance(self.hero.health, float)
        self.assertIsInstance(self.hero.damage, float)

    def test_validate_init_values(self):
        self.assertEqual(self._name, self.hero.username)
        self.assertEqual(self._lvl, self.hero.level)
        self.assertEqual(self._health, self.hero.health)
        self.assertEqual(self._dmg, self.hero.damage)

    def test_mod_battle_self_error(self):
        self.enemy_hero.username = self._name
        self.assertEqual(self.hero.username, self.enemy_hero.username)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)
        expected = 'You cannot fight yourself'
        self.assertEqual(expected, str(ex.exception))

    def test_mod_battle_self_health_lt_0_error(self):
        self.hero.health = -2
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        expected = 'Your health is lower than or equal to 0. You need to rest'
        self.assertEqual(expected, str(ex.exception))

    def test_mod_battle_self_health_eq_0_error(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        expected = 'Your health is lower than or equal to 0. You need to rest'
        self.assertEqual(expected, str(ex.exception))

    def test_mod_battle_enemy_health_lt_0_error(self):
        self.enemy_hero.health = -4
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        expected = f'You cannot fight {self.enemy_hero.username}. He needs to rest'
        self.assertEqual(expected, str(ex.exception))

    def test_mod_battle_enemy_health_eq_0_error(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        expected = f'You cannot fight {self.enemy_hero.username}. He needs to rest'
        self.assertEqual(expected, str(ex.exception))

    def test_mod_battle_draw_rsult(self):
        self.enemy_hero.damage = 500
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual('Draw', result)

    def test_mod_battle_win_result(self):
        self.hero.health = 5000
        self.assertEqual(5000, self.hero.health)
        self.assertEqual(self._lvl, self.hero.level)
        self.assertEqual(self._dmg, self.hero.damage)
        result = self.hero.battle(self.enemy_hero)
        health_after_battle = 5000 - (self.enemy_hero.damage * self.enemy_hero.level)
        self.assertEqual('You win', result)
        self.assertEqual(self._lvl + 1, self.hero.level)
        self.assertEqual(health_after_battle + 5, self.hero.health)
        self.assertEqual(self._dmg + 5, self.hero.damage)

    def test_mod_battle_lose_result(self):
        self.enemy_hero.health = 15000
        self.enemy_hero.damage = 500
        self.assertEqual(15000, self.enemy_hero.health)
        self.assertEqual(20, self.enemy_hero.level)
        self.assertEqual(500, self.enemy_hero.damage)
        result = self.hero.battle(self.enemy_hero)
        enemy_health_after_battle = 15000 - (self.hero.damage * self.hero.level)
        self.assertEqual('You lose', result)
        self.assertEqual(20 + 1, self.enemy_hero.level)
        self.assertEqual(enemy_health_after_battle + 5, self.enemy_hero.health)
        self.assertEqual(500 + 5, self.enemy_hero.damage)

    def test_class_str_repr(self):
        expected = f'Hero {self._name}: {self._lvl} lvl\n' + \
                   f'Health: {self._health}\n' + \
                   f'Damage: {self._dmg}\n'
        result = str(self.hero)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
