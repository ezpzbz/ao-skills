import os
import tempfile
import unittest

from tasklist import store


class StoreTest(unittest.TestCase):
    def setUp(self):
        fd, self.path = tempfile.mkstemp(suffix=".json")
        os.close(fd)
        os.remove(self.path)

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_add_and_load(self):
        store.add("first", self.path)
        store.add("second", self.path)
        titles = [t["title"] for t in store.load(self.path)]
        self.assertEqual(titles, ["first", "second"])


if __name__ == "__main__":
    unittest.main()
