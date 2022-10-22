import unittest


class TrivialTest(unittest.TestCase):
    """Test passes by default so that pytest will pass without any other tests. Remove this test when you add your own tests."""

    def test(self):
        assert True


if __name__ == "__main__":
    unittest.main()
