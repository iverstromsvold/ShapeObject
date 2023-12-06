class ShapeObject:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # self._diameter = diameter
        # self.get_circ_diameter = diameter + circumference
        self.square = height ** 2

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_diameter(self):
        return self._diameter

    def get_circumference(self):
        self._circumference = (self._diameter / 2) * 3.14
        return self._circumference

    def get_circ_diameter(self):
        return self.get_circ_diameter

    def get_square(self):
        self.square = self.height ** 2
        return self.square

    def get_cubeArea(self):
        cubeArea = self.square * 6
        return cubeArea

    def get_area(self):
        area = self.width * self.height
        return area

    def set_diameter(self, x):
        self._diameter = x

    def set_circumference(self, x):
        self._circumference = x

    def validate_square(self, square):
        if square == self.get_square():
            return True
        else:
            return False
