from unittest import TestCase
import alprbd


class TestPreprocess(TestCase):
    def test_all(self):

        file = 'samples/002.jpg'
        image = alprbd.models.Image(file)
        self.assertIsNotNone(image.original, msg="image load failed")
        alprbd.worker.preprocess.process(image)
        self.assertIsNotNone(image.gray, msg="no gray image")
        self.assertEqual(len(image.gray.shape), 2, msg="gray is not 2 dimensional")
        self.assertIsNotNone(image.scaled, msg="scaling failed")
        self.assertEqual(image.scaled.shape[0], alprbd.config.SCALE_DIM[1], msg="scaled height mismatch")
        self.assertEqual(image.scaled.shape[1], alprbd.config.SCALE_DIM[0], msg="scaled width mismatch")
        #cv2.imshow("preprocess test: gray image", image.gray)
        #cv2.imshow("preprocess test: scaled image", image.scaled)
        #cv2.waitKey()

