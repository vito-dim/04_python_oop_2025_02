from project.student import Student

from unittest import TestCase, main


class TestStudent(TestCase):
    name = 'Jorje'
    courses = {
        'python': [],
        'english': []
    }

    def setUp(self):
        self.student = Student(self.name, self.courses)
        self.non_student = Student(self.name, None)

    def test_init_values_none_value(self):
        self.assertEqual(self.name, self.non_student.name)
        self.assertDictEqual({}, self.non_student.courses)

    def test_init_values_default_case(self):
        self.assertEqual(self.name, self.student.name)
        self.assertDictEqual(self.courses, self.student.courses)

    def test_mod_enroll_no_added_courses_and_no_notes(self):
        course_name = 'python'
        notes = []
        add = 'Y'

        self.assertDictEqual(self.courses, self.student.courses)
        result = self.student.enroll(course_name, notes, add)
        self.assertDictEqual(self.courses, self.student.courses)
        expected = 'Course already added. Notes have been updated.'
        self.assertEqual(expected, result)

        add = ''
        self.assertDictEqual(self.courses, self.student.courses)
        self.student.enroll(course_name, notes, add)
        self.assertDictEqual(self.courses, self.student.courses)
        expected = 'Course already added. Notes have been updated.'
        self.assertEqual(expected, result)

        add = 'N'
        self.assertDictEqual(self.courses, self.student.courses)
        self.student.enroll(course_name, notes, add)
        self.assertDictEqual(self.courses, self.student.courses)
        expected = 'Course already added. Notes have been updated.'
        self.assertEqual(expected, result)

    def test_mod_enroll_param_no_added_courses_note_update(self):
        course_name = 'python'
        notes = ['n1', 'n2']

        self.assertDictEqual(self.courses, self.student.courses)
        result = self.student.enroll(course_name, notes)
        self.courses[course_name] = notes
        self.assertDictEqual(self.courses, self.student.courses)
        expected = 'Course already added. Notes have been updated.'
        self.assertEqual(expected, result)

    def test_mod_enroll_new_course_and_no_notes(self):
        new_course = 'history'
        notes = ['n4', 'n5']
        add = 'N'

        self.assertNotIn(new_course, self.student.courses)
        result = self.student.enroll(new_course, notes, add)
        expected = 'Course has been added.'

        self.assertEqual(expected, result)
        self.assertIn(new_course, self.student.courses)
        self.assertEqual([], self.student.courses[new_course])

    def test_mod_enroll_new_course_and_notes_no_arg(self):
        new_course = 'math'
        notes = ['n1', 'n2', 'n3']

        self.assertNotIn(new_course, self.student.courses)
        result = self.student.enroll(new_course, notes)
        expected = 'Course and course notes have been added.'

        self.assertEqual(expected, result)
        self.assertIn(new_course, self.student.courses)
        self.assertEqual(notes, self.student.courses[new_course])

    def test_mod_enroll_new_course_and_notes_with_arg(self):
        new_course = 'Java'
        notes = ['n1', 'n2', 'n3']
        add = 'Y'

        self.assertNotIn(new_course, self.student.courses)
        result = self.student.enroll(new_course, notes, add)
        expected = 'Course and course notes have been added.'

        self.assertEqual(expected, result)
        self.assertIn(new_course, self.student.courses)
        self.assertEqual(notes, self.student.courses[new_course])

    def test_mod_add_notes_course_not_found_error(self):
        course = 'JS'
        note = 'n33'
        with self.assertRaises(Exception) as ex:
            self.student.add_notes(course, note)
        expected = 'Cannot add notes. Course not found.'
        self.assertEqual(expected, str(ex.exception))

    def test_mod_add_notes_course_found_notes_updated(self):
        course = 'python'
        note = 'updated_note'
        self.assertNotIn(note, self.student.courses[course])
        result = self.student.add_notes(course, note)
        expected = 'Notes have been updated'
        self.assertEqual(expected, result)
        self.assertIn(note, self.student.courses[course])

    def test_mod_leave_course_not_found_error(self):
        course = 'test'
        self.assertNotIn(course, self.student.courses)
        with self.assertRaises(Exception) as ex:
            self.student.leave_course(course)
        expected = 'Cannot remove course. Course not found.'
        self.assertEqual(expected, str(ex.exception))
        self.assertNotIn(course, self.student.courses)

    def test_mod_leave_course_left_successfully(self):
        course = 'english'
        self.assertIn(course, self.student.courses)
        result = self.student.leave_course(course)
        expected = 'Course has been removed'
        self.assertEqual(expected, result)
        self.assertNotIn(course, self.student.courses)


if __name__ == '__main__':
    main()
