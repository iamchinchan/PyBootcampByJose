import unittest
import cap


class TestCap(unittest.TestCase):
    def test_one_words(self):
        text = "python"
        result = cap.cap_words(text)
        self.assertEqual(result, "Python")

    def test_multiple_words(self):
        text = "jAtin ka phOne"
        result = cap.cap_words(text)
        self.assertEqual(result, "Jatin Ka Phone")

    def test_with_extra_chars(self):
        text = "jAtin's phonE is damaged!hehe"
        result = cap.cap_words(text)
        self.assertEqual(result, "Jatin's Phone Is Damaged!hehe")


if __name__ == "__main__":
    unittest.main()
