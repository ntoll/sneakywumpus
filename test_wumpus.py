import random

def test_wumpus():
    assert random.randint(1, 10)

    for i in range (random.randint(1, 10)):
        exec ("def test_%d (): assert True" % i)
