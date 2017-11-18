import unittest
import box
import io
import unittest.mock
import random


class TestBox(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, width, height, expected_output, mock_stdout):
        box.drawbox(width, height)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_2x2(self):
        self.assert_stdout(2, 2, '┌┐\n'
                                 '└┘\n')

    def test_2x3(self):
        self.assert_stdout(2, 3, '┌┐\n'
                                 '||\n'
                                 '└┘\n')

    def test_2x4(self):
        self.assert_stdout(2, 4, '┌┐\n'
                                 '||\n'
                                 '||\n'
                                 '└┘\n')

    def test_3x2(self):
        self.assert_stdout(3, 2, '┌ - ┐\n'
                                 '└ - ┘\n')

    def test_4x4(self):
        self.assert_stdout(4, 4, '┌ -  - ┐\n'
                                 '|      |\n'
                                 '|      |\n'
                                 '└ -  - ┘\n')

    def test_random(self):
        min = 5
        max = 15
        w = random.randint(min, max)
        h = random.randint(min, max)

        #Construct the expected output
        '''1st line'''
        expected_output = '┌'
        for i in range(0, w - 2):
            expected_output += ' - '
        expected_output += '┐\n'

        '''middle lines'''
        for i in range(0, h - 2):
            expected_output += '|'
            for j in range(0, w - 2):
                expected_output += '   '
            expected_output += '|\n'

        '''last line'''
        expected_output += '└'
        for i in range(0, w - 2):
            expected_output += ' - '
        expected_output += '┘\n'

        self.assert_stdout(w, h, expected_output)


if __name__ == '__main__':
    unittest.main()
