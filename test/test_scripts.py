import unittest
import scripts


class TestScripts(unittest.TestCase):
    data = {
        1: [2, 3, 4, 5],
        2: [4, 5, 6, 7],
        3: [2, 4, 5],
        4: [9, 10],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
    }

    def test_empty_input(self):
        result = scripts.schedule_scripts({})
        self.assertEqual(result, [])

    def test_sorting_ok(self):
        a = scripts.schedule_scripts(self.data)
        b = [10, 9, 8, 7, 6, 5, 4, 2, 3, 1]
        self.assertListEqual(a, b)

    def test_no_dependencies(self):
        a = scripts.schedule_scripts({5: [], 6: [], 7: [], 8: [], 9: [], 10: []})
        b = [10, 9, 8, 7, 6, 5]
        self.assertListEqual(a, b)

    def test_duplicate_dependencies(self):
        data_duplicate = {
            1: [2, 3, 4, 5],
            2: [4, 5, 6, 7],
            3: [2, 4, 5],
            4: [9, 10, 10],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
            10: [],
        }
        a = scripts.schedule_scripts(data_duplicate)
        b = [10, 9, 8, 7, 6, 5, 4, 2, 3, 1]
        self.assertListEqual(a, b)

    def test_sorting_wrong_order(self):
        a = [1, 9, 8, 7, 6, 5, 4, 2, 3, 10]
        b = scripts.schedule_scripts(self.data)
        self.assertNotEqual(a, b)

    def test_cyclic_dependency(self):
        cycled_data = {
            1: [2, 3],
            2: [3, 4, 5],
            3: [2, 4, 5],
        }
        with self.assertRaises(Exception) as context:
            scripts.schedule_scripts(cycled_data)
        self.assertEqual(str(context.exception), "Cycle or unlisted dependency detected")

    def test_unlisted_dependency(self):
        unlisted_data = {
            1: [2, 3, 4, 5],
            2: [3, 4, 5],
            3: [2, 4, 5],
        }
        with self.assertRaises(Exception) as context:
            scripts.schedule_scripts(unlisted_data)
        self.assertEqual(str(context.exception), "Cycle or unlisted dependency detected")


if __name__ == '__main__':
    unittest.main()
