from random import randint

def random_color():
    return (randint(0,255), randint(0,255), randint(0,255))

def random_pastel_color():
    return (randint(0,255), randint(0,255), randint(0,255), 100)