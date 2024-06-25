import unittest
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from block_manager import Block_Manager

class TestBreakoutComponents(unittest.TestCase):
    def test_ball_move(self):
        ball = Ball()
        initial_x, initial_y = ball.xcor(), ball.ycor()
        ball.move()
        self.assertNotEqual((initial_x, initial_y), (ball.xcor(), ball.ycor()), "Ball should move to a new position")


    def test_paddle_movement(self):
        paddle = Paddle()
        initial_x = paddle.xcor()
        paddle.right()
        self.assertGreater(paddle.xcor(), initial_x, "Paddle should move right")
        paddle.left()
        paddle.left()
        self.assertLess(paddle.xcor(), initial_x, "Paddle should move left after two left movements")

    def test_scoreboard_update(self):
        scoreboard = Scoreboard()
        initial_score = scoreboard.score
        scoreboard.update_score()
        self.assertEqual(scoreboard.score, initial_score + 1, "Score should increment by 1")

    def test_block_creation(self):
        block_manager = Block_Manager()
        block_manager.create_blocks()
        self.assertGreater(len(block_manager.all_blocks), 0, "Blocks should be created")

# More tests can be added following the structure above.

if __name__ == '__main__':
    unittest.main()