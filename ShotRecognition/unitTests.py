import unittest
import Ball_Tracker.py

pts = [(0,2),(0,4)]
pts2 = [(0,4),(0,2)]
pts3 = [(2,0),(4,0)]
pts4 = [(2,0),(4,0)]
class TestStringMethods(unittest.TestCase):

    def test_angle(self):
        self.assertEqual(Ball_Tracker.angle(10,100,10,200),90)
        self.assertEqual(Ball_Tracker.angle(25,90,200,500),67)
        self.assertEqual(Ball_Tracker.angle(20,200,150,600),72)
        self.assertEqual(Ball_Tracker.angle(0,350,100,400),27)
        self.assertEqual(Ball_Tracker.angle(0,50,300,550),59)

# 2 is down
    # def test_direction(self):
        # self.assertTrue(ball.direction(pts,0,3))
        # self.assertTrue(ball.direction(pts2,0,3))
        # self.assertTrue(ball.direction(pts,1,3))
        # self.assertTrue(ball.direction(pts2,1,3))

        # self.assertTrue(ball.direction(pts,2,3))
        # self.assertTrue(ball.direction(pts2,2,3))
        # self.assertTrue(ball.direction(pts,3,3))
        # self.assertTrue(ball.direction(pts2,3,3))



if __name__ == '__main__':
    unittest.main()


