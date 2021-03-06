import unittest

from allennlp.data.tokenizers import SpacyTokenizer


class TestAllenNlp(unittest.TestCase):
    # reference
    # https://github.com/allenai/allennlp/blob/master/allennlp/tests/data/tokenizers/word_tokenizer_test.py
    def test_passes_through_correctly(self):
        tokenizer = SpacyTokenizer()
        sentence = "this (sentence) has 'crazy' \"punctuation\"."
        tokens = [t.text for t in tokenizer.tokenize(sentence)]
        expected_tokens = ["this", "(", "sentence", ")", "has", "'", "crazy", "'", "\"",
                           "punctuation", "\"", "."]
        self.assertSequenceEqual(tokens, expected_tokens)
