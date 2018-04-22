import unittest

import bill

class InsultTestCase(unittest.TestCase):

    def test_insult(self):
        words = bill.insult().split(' ')
        for word, bill_words in zip(words, bill.words):
            self.assertIn(word, bill_words)
