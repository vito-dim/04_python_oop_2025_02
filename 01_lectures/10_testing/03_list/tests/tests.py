from extended_list import IntegerList

from unittest import TestCase, main


class TestIntegerList(TestCase):
    data_int = [1, 2, 3, 4, 5]
    data_mix = ['top', {'test': 3}, [1, 3], 6]

    def setUp(self):
        self.int_data = IntegerList(*self.data_int)
        self.mix_data = IntegerList(*self.data_mix)

    def test_init_value_validation_all_ints(self):
        self.assertEqual(self.data_int, self.int_data._IntegerList__data)

    def test_init_value_validation_mixed_data(self):
        self.assertEqual([6], self.mix_data._IntegerList__data)

    def test_get_data_result(self):
        self.assertEqual(self.data_int, self.int_data.get_data())
        self.assertEqual([6], self.mix_data.get_data())

    def test_add_raising_error(self):
        self.assertEqual(self.data_int, self.int_data._IntegerList__data)
        str_value = 'test'
        none_val = None
        lst_val = [3]
        expected = 'Element is not Integer'

        with self.assertRaises(ValueError) as ex:
            self.int_data.add(str_value)
        self.assertEqual(expected, str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.int_data.add(none_val)
        self.assertEqual(expected, str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.int_data.add(lst_val)
        self.assertEqual(expected, str(ex.exception))

        self.assertEqual(self.data_int, self.int_data._IntegerList__data)

    def test_add_success_case(self):
        int_value = 69
        self.assertEqual(self.data_int, self.int_data.get_data())
        self.int_data.add(int_value)
        expected = [*self.data_int, int_value]
        self.assertEqual(expected, self.int_data.get_data())

    def test_removal_index_raise_condition(self):
        self.assertEqual(self.data_int, self.int_data.get_data())
        index = 10
        with self.assertRaises(IndexError) as ex:
            self.int_data.remove_index(index)
        expected = 'Index is out of range'
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(self.data_int, self.int_data.get_data())

    def test_removal_index_success_condition(self):
        self.assertEqual(self.data_int, self.int_data.get_data())
        index = 0
        self.data_int.pop(index)
        self.int_data.remove_index(index)
        self.assertEqual(self.data_int, self.int_data.get_data())

    def test_get_value_raise_condition_gt_case(self):
        index = 10
        with self.assertRaises(IndexError) as ex:
            self.int_data.get(index)
        expected = 'Index is out of range'
        self.assertEqual(expected, str(ex.exception))

    def test_get_value_raise_condition_eq_case(self):
        index = len(self.data_int)
        with self.assertRaises(IndexError) as ex:
            self.int_data.get(index)
        expected = 'Index is out of range'
        self.assertEqual(expected, str(ex.exception))

    def test_get_value_success_case(self):
        index = 0
        result = self.int_data.get(index)
        expected = self.data_int[index]
        self.assertEqual(expected, result)

    def test_insert_index_gt_len_error(self):
        index = 10
        with self.assertRaises(IndexError) as ex:
            self.int_data.insert(index, 30)
        expected = 'Index is out of range'
        self.assertEqual(expected, str(ex.exception))

    def test_insert_index_eq_len_error(self):
        index = len(self.int_data.get_data())
        with self.assertRaises(IndexError) as ex:
            self.int_data.insert(index, 30)
        expected = 'Index is out of range'
        self.assertEqual(expected, str(ex.exception))

    def test_insert_el_not_int(self):
        index = 0
        el = 'por'
        with self.assertRaises(ValueError) as ex:
            self.int_data.insert(index, el)
        expected = 'Element is not Integer'
        self.assertEqual(expected, str(ex.exception))

    def test_insert_success_case(self):
        self.assertNotIn(69, self.int_data.get_data())
        self.int_data.insert(0, 69)
        self.assertIn(69, self.int_data.get_data())

    def test_get_biggest(self):
        self.assertEqual(self.data_int, self.int_data.get_data())
        self.data_int.sort(reverse=True)
        result = self.int_data.get_biggest()
        expected = self.data_int[0]
        self.assertEqual(expected, result)

    def test_get_index(self):
        el = 1
        expected = self.data_int.index(el)
        result = self.int_data.get_index(el)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
