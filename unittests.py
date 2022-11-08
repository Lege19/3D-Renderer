import unittest
import maths
class testVector2(unittest.TestCase):
    def testDot(self):
        self.assertEqual(maths.Vector2.dot(maths.Vector2(5, 0), maths.Vector2(-2, 3)), -10)
    def testNormalized(self):
        self.assertAlmostEqual(maths.Vector2(5, 2).normalized().x, 0.9284766908852594)
class testVector3(unittest.TestCase):
    def testDot(self):
        self.assertEqual(maths.Vector3.dot(maths.Vector3(0, 1, 1), maths.Vector3(1, 0, 0)), 0)
        self.assertEqual(maths.Vector3.dot(maths.Vector3(1, 1, 2), maths.Vector3(-2, -1, 1)), -1)
    def testCross(self):
        self.assertEqual(maths.Vector3.cross(maths.Vector3(1, 0, 0), maths.Vector3(0, 1, 0)).z, 1)
unittest.main()