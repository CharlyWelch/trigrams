from trigrams import book_slice, dict_create, new_builder
import unittest

class TestIt1(unittest.TestCase):
    """ test book_slice """
    def test_1(self):
        self.assertEqual(book_slice('test.txt'), ["This", "is", "a", "test", "file", "for", "trigrams"])

class TestIt2(unittest.TestCase):
    """ test dict_create """
    def test_1(self):
        self.assertEqual(dict_create(["Testing", "text", "for", "dictionary", "creation"]), { "" : [""], "Testing text": ["for"], "text for": ["dictionary"], "for dictionary": ["creation"]} )

# class TestIt3(unittest.Testcase):
#     """ test new_builder """
#     def test_1(self):
#         self.assertEqual(new_builder({"testing text": "for", "text for": "dictionary", "for dictionary": "creation"}))