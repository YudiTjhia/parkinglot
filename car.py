class car:
    def __init__(self, number, color):
        self.number = number
        self.color = color

    def __str__(self):
        return "car[number=" + self.number + ",color=" + self.color + "]"
