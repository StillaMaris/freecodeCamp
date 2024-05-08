import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for k, v in kwargs.items():
      self.contents += [k] * v

  def draw(self, num):
    try:
      balls = random.sample(self.contents, num)
    except:
      balls = copy.deepcopy(self.contents)

    for ball in balls:
      self.contents.remove(ball)

    return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  success = 0

  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn_balls = hat_copy.draw(num_balls_drawn)

    exp_list = []
    for k, v in expected_balls.items():
      exp_list += [k] * v

    if contains_balls(exp_list, drawn_balls):
      success += 1

  return success / num_experiments


def contains_balls(expected, actual):
  initial_len = len(actual)
  for ball in expected:
    if ball in actual:
      actual.remove(ball)

  return (len(actual) == initial_len - len(expected))


