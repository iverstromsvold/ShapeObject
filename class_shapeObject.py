class ShapeObject:
    def __init__(self, width, height, diameter, circumference):
        self.width = width
        self.height = height
        self._diameter = diameter
        self.get_circ_diameter = diameter + circumference
        self.square = height**2
    def get_height(self):
        return self.height
    def get_width(self):
        return self.width
    def set_diameter(self, 7):
        self._diameter = 7
    def get_circ_diameter(self):
        return self.get_circ_diameter
    def get_square(self):
        return self.square



shapeObject_ = ShapeObject()

