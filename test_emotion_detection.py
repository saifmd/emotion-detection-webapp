from EmotionDetection import emotion_detector
import unittest

class TestEmotioDetector(unittest.TestCase):
    def test_emotion_detector(self):
        res_1 = emotion_detector("I am glad this happened")
        dominant_emotion = res_1["dominant_emotion"]
        self.assertEqual(dominant_emotion, "joy")

        res_2 = emotion_detector("I am really mad about this")
        dominant_emotion = res_2["dominant_emotion"]
        self.assertEqual(dominant_emotion, "anger")

        res_3 = emotion_detector("I feel disgusted just hearing about this")
        dominant_emotion = res_3["dominant_emotion"]
        self.assertEqual(dominant_emotion, "disgust")

        res_4 = emotion_detector("I am so sad about this")
        dominant_emotion = res_4["dominant_emotion"]
        self.assertEqual(dominant_emotion, "sadness")

        res_5 = emotion_detector("I am really afraid that this will happen")
        dominant_emotion = res_5["dominant_emotion"]
        self.assertEqual(dominant_emotion, "fear")

        res_6 = emotion_detector("I feel very happy today", use_hf=False)
        dominant_emotion = res_6["dominant_emotion"]
        self.assertEqual(dominant_emotion, "joy")


if __name__ == "__main__":
    unittest.main()
