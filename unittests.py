import unittest
import maths
class testVector2(unittest.TestCase):
    def testDot(self):
        self.assertEqual(maths.Vector2.dot(maths.Vector2(5, 0), maths.Vector2(-2, 3)), -10)
    def testNormalized(self):
        self.assertAlmostEqual(maths.Vector2(5, 2).normalized().x, 0.9284766908852594)
unittest.main()