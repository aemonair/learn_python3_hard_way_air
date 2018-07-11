from nose.tools import *
from ex47.game import Room

def test_room_own():
    room1 = Room('1', "This is room 1")
    room2 = Room('2', "This is room 2")
    room3 = Room('3', "This is room 3")

    room1.add_paths({'room2':room2})
    room1.add_paths({'room3':room3})
    room2.add_paths({'room3':room3})

    assert_equal(room1.go('room3'), room3)
    assert_equal(room1.go('room2'), room2)
    assert_equal(room2.go('room3'), room3)
