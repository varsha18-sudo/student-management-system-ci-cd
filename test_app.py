import unittest
import app

from app import add_student, get_students


class TestStudentManagement(unittest.TestCase):

    def setUp(self):
        app.students.clear()

    def test_add_student(self):
        result = add_student("Rahul", 101)

        self.assertEqual(result["name"], "Rahul")
        self.assertEqual(result["roll_number"], 101)

    def test_get_students(self):
        add_student("Priya", 102)

        students = get_students()

        self.assertIn(
            {"name": "Priya", "roll_number": 102},
            students
        )


if __name__ == "__main__":
    unittest.main()
