
import unittest
from app import get_courses


class TestCourses(unittest.TestCase):

    def test_courses_are_available(self):
        courses = get_courses()
        self.assertGreater(len(courses), 0)

    def test_course_names_are_strings(self):
        for course in get_courses():
            self.assertIsInstance(course, str)


if __name__ == "__main__":
    unittest.main()
