#! /usr/bin/env python3

bottles = 99

for item in range(bottles, 0, -1):
    #
    print(f"{item}bottles of beer on the wall ")
    print(f"{item} bottles of beer on the wall! {item} bottles of beer! You take one down, pass it around!")
    print(f"{item - 1} bottles of beer on the wall!")
    