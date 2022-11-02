"""
Program: student_test.py
Author: Alex Heinrichs
Date Created: 11/2/2022

Contains tests for the Student class in Student.py
"""
import unittest
from class_definitions import Student as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = t('Heinrichs', 'Alex', 'CIS', 4.0)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Heinrichs')
        self.assertEqual(self.student.first_name, 'Alex')
        self.assertEqual(self.student.major, 'CIS')

    def test_object_created_all_attributes(self):
        s = t('Heinrichs', 'Alex', 'CIS')
        self.assertEqual(s.last_name, 'Heinrichs')
        self.assertEqual(s.first_name, 'Alex')
        self.assertEqual(s.major, 'CIS')
        self.assertEqual(s.gpa, 0.0)

    def test_student_str(self):
        self.assertEqual(str(self.student), "Heinrichs, Alex has major CIS with gpa: 4.0")

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = t('123', 'Alex', 'CIS')

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            p = t('Heinrichs', '123', 'CIS')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            p = t('Heinrichs', 'Alex', '123')

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            p = t('Heinrichs', 'Alex', 'CIS', 'Perfect')
            p = t('Heinrichs', 'Alex', 'CIS', -2.0)
            p = t('Heinrichs', 'Alex', 'CIS', 5.0)


# Driver
if __name__ == '__main__':
    unittest.main()
