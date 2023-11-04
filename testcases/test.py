import unittest


def request_handler() -> int:
    try:
        request_output = int(input("Type Operation Number: "))
    except ValueError:
        print("Invalid input, the input must be an integer")
        request_handler()
    else:
        return request_output


class TestRequestMethods(unittest.TestCase):

    request = request_handler()

    def test_max(self):
        self.assertLessEqual(self.request, 4, msg="the max number is 4")

    def test_min(self):
        self.assertGreater(self.request, 0, msg="the min number is 1")


if __name__ == '__main__':
    unittest.main()
