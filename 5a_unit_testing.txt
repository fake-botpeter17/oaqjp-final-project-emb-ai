import unittest
from EmotionDetection import emotion_detector

def find_max(res):
    current_max_name = ""
    current_max_number = 0
    for emotion in res:
        if res[emotion] >= current_max_number:
            current_max_name = emotion
            current_max_number = res[emotion]
    return current_max_name



class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(find_max(result), "joy")

    def test_anger(self):
        result = emotion_detector("I am really mad about this")
        self.assertEqual(find_max(result), "anger")

    def test_disgust(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(find_max(result), "disgust")

    def test_sadness(self):
        result = emotion_detector("I am so sad about this")
        self.assertEqual(find_max(result), "sadness")

    def test_fear(self):
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(find_max(result), "fear")


if __name__ == "__main__":
    unittest.main()