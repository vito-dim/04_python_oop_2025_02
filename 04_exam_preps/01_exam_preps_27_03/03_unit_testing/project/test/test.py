from project.senior_student import SeniorStudent

from unittest import TestCase, main


class TestSeniorStudent(TestCase):
    stud_id = 'E34354567'
    stud_name = 'Jorje'
    stud_gpa = 5.75

    def setUp(self):
        self.student = SeniorStudent(self.stud_id, self.stud_name, self.stud_gpa)

    def test_init_var_types(self):
        self.assertIsInstance(self.student.student_id, str)
        self.assertIsInstance(self.student.name, str)
        self.assertIsInstance(self.student.student_gpa, float)
        self.assertIsInstance(self.student.colleges, set)

    def test_init_var_values(self):
        self.assertEqual(self.stud_id, self.student.student_id)
        self.assertEqual(self.stud_name, self.student.name)
        self.assertEqual(self.stud_gpa, self.student.student_gpa)
        self.assertSetEqual(set(), self.student.colleges)

    def test_set_student_id_lt_4_error(self):
        self.assertEqual(self.stud_id, self.student.student_id)
        with self.assertRaises(ValueError) as ex:
            self.student.student_id = 'a33'
        expected = 'Student ID must be at least 4 digits long!'
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(self.stud_id, self.student.student_id)

    def test_set_student_id_eq_4_success(self):
        new_id = 'E004'
        self.student.student_id = new_id
        self.assertEqual(new_id, self.student.student_id)

    def test_set_student_id_gt_4_success(self):
        new_id = 'E00456'
        self.student.student_id = new_id
        self.assertEqual(new_id, self.student.student_id)

    def test_set_student_id_gt_4_with_strip_success(self):
        new_id = '  E00456  '
        self.student.student_id = new_id
        self.assertEqual(new_id.strip(' '), self.student.student_id)

    def test_set_student_name_empty_error(self):
        self.assertEqual(self.stud_name, self.student.name)
        with self.assertRaises(ValueError) as ex:
            self.student.name = ''
        expected = 'Student name cannot be null or empty!'
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(self.stud_name, self.student.name)

        with self.assertRaises(ValueError) as ex:
            self.student.name = '    '
        expected = 'Student name cannot be null or empty!'
        self.assertEqual(expected, str(ex.exception))

    def test_set_student_name_success(self):
        new_name = 'Pesho'
        self.student.student_name = new_name
        self.assertEqual(new_name, self.student.student_name)

    def test_set_student_gpa_lt_1_error(self):
        gpa = 0.5
        self.assertEqual(self.stud_gpa, self.student.student_gpa)
        with self.assertRaises(ValueError) as ex:
            self.student.student_gpa = gpa
        expected = 'Student GPA must be more than 1.0!'
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(self.stud_gpa, self.student.student_gpa)

    def test_set_student_gpa_eq_1_error(self):
        gpa = 1.0
        self.assertEqual(self.stud_gpa, self.student.student_gpa)
        with self.assertRaises(ValueError) as ex:
            self.student.student_gpa = gpa
        expected = 'Student GPA must be more than 1.0!'
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(self.stud_gpa, self.student.student_gpa)

    def test_set_student_gpa_gt_1_success(self):
        gpa = 5.0
        self.student.student_gpa = gpa
        self.assertEqual(gpa, self.student.student_gpa)

    def test_mod_apply_to_college_error(self):
        required_gpa = 6.0
        college = 'Oxford'
        result = self.student.apply_to_college(required_gpa, college)
        expected = 'Application failed!'
        self.assertEqual(expected, result)
        self.assertSetEqual(set(), self.student.colleges)

    def test_mod_apply_to_college_success(self):
        required_gpa = 5.0
        college = 'BsUni'
        result = self.student.apply_to_college(required_gpa, college)
        expected = f'{self.stud_name} successfully applied to {college}.'
        self.assertEqual(expected, result)
        self.assertIn(college.upper(), self.student.colleges)

    def test_mod_update_gpa_lt_1_case(self):
        new_gpa = 0.3
        result = self.student.update_gpa(new_gpa)
        expected = 'The GPA has not been changed!'
        self.assertEqual(expected, result)

    def test_mod_update_gpa_eq_1_case(self):
        new_gpa = 1.0
        result = self.student.update_gpa(new_gpa)
        expected = 'The GPA has not been changed!'
        self.assertEqual(expected, result)

    def test_mod_update_gpa_gt_1_case(self):
        new_gpa = 6.0
        self.assertEqual(self.stud_gpa, self.student.student_gpa)
        result = self.student.update_gpa(new_gpa)
        expected = 'Student GPA was successfully updated.'
        self.assertEqual(expected, result)
        self.assertEqual(new_gpa, self.student.student_gpa)

    def test_cls_not_eq_for_gpa_override(self):
        stud2 = SeniorStudent('F333556', 'Pesho', 1.3)
        self.assertFalse(self.student == stud2)

    def test_cls_eq_for_gpa_override(self):
        stud2 = SeniorStudent('F333556', 'Pesho', self.stud_gpa)
        self.assertTrue(self.student == stud2)

if __name__ == '__main__':
    main()
