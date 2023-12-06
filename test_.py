import pytest
import class_shapeObject
from class_shapeObject import ShapeObject

@pytest.fixture
def object():
    so = ShapeObject(32, 43)

    return so
def test_height(object):
    assert object.get_height() == 43

def test_width(object):
    assert object.get_width() == 32

def test_square(object):
    assert object.get_square() == 1849

def test_diameter(object):
    object.set_diameter(7)
    assert object.get_diameter() == 7

def test_circumference(object):
    object.set_diameter(7)
    assert object.get_circumference() == 10.99

def test_area(object):
    assert object.get_area() == 1376

def test_cubedArea(object):
    #object.get_square()
    assert object.get_cubeArea() == 11094