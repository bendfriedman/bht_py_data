"""Kleine Werkzeuge für Geometrie."""

# TODO: import math, circle_area(radius) und __main__-Guard
import math

def circle_area(radius: float) -> float:
    return math.pi * radius ** 2

if __name__ == "__main__":
    print(f"circle_area(1) = {circle_area(1):.2f}")
