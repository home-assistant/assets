class Area(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
        return self.a * self.b

    def calculate_perimeter(self):
        return (2 * self.a) + (2 * self.b)
