import math

# # this is what is done under the hood
# class RadiusType():
#     def __get__(self):
#         self.radius
#     def __set__(self, new_radius):
#         self.radius = new_radius
#     def __init__(self, radius):
#         self.radius = radius


class Circle:

    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return f"circle ({self.radius})"

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius < 0:
            raise ValueError("Radius cannott be negative")
        self._radius = new_radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, new_diameter):
        self.radius = new_diameter / 2

    @property
    def areas(self):
        return self.radius ** 2 * math.pi
