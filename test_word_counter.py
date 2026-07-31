import unittest

from word_counter import count_words


class WordCounterTests(unittest.TestCase):
    def test_count_words_in_text(self):
        text = "Hola mundo desde Python y Python"
        self.assertEqual(count_words(text), 6)

    def test_count_words_with_punctuation(self):
        text = "Hola, mundo! ¿Desde Python?"
        self.assertEqual(count_words(text), 4)


if __name__ == "__main__":
    unittest.main()
