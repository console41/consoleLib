# -*- coding: utf-8 -*-

class AABB(object):
    def __init__(self, point1, point2):
        x1, y1, z1 = map(float, point1)
        x2, y2, z2 = map(float, point2)

        self.minX = min(x1, x2)
        self.minY = min(y1, y2)
        self.minZ = min(z1, z2)
        self.maxX = max(x1, x2)
        self.maxY = max(y1, y2)
        self.maxZ = max(z1, z2)

        self.minPoint = (self.minX, self.minY, self.minZ)
        self.maxPoint = (self.maxX, self.maxY, self.maxZ)

        self.width = self.maxX - self.minX
        self.height = self.maxY - self.minY
        self.depth = self.maxZ - self.minZ

        self.centerX = (self.minX + self.maxX) * 0.5
        self.centerY = (self.minY + self.maxY) * 0.5
        self.centerZ = (self.minZ + self.maxZ) * 0.5
        self.center = (self.centerX, self.centerY, self.centerZ)

        self.volume = self.width * self.height * self.depth

    def __contains__(self, item):
        if isinstance(item, tuple):
            x, y, z = map(float, item)
            return (self.minX <= x <= self.maxX and
                    self.minY <= y <= self.maxY and
                    self.minZ <= z <= self.maxZ)
        elif isinstance(item, AABB):
            return (item.minX >= self.minX and
                    item.minY >= self.minY and
                    item.minZ >= self.minZ and
                    item.maxX <= self.maxX and
                    item.maxY <= self.maxY and
                    item.maxZ <= self.maxZ)
        return False

    def __str__(self):
        return "AABB(min=({},{},{}), max=({},{},{}))".format(
            self.minX, self.minY, self.minZ,
            self.maxX, self.maxY, self.maxZ
        )

    def __eq__(self, other):
        return (self.minX == other.minX and
                self.minY == other.minY and
                self.minZ == other.minZ and
                self.maxX == other.maxX and
                self.maxY == other.maxY and
                self.maxZ == other.maxZ)

    def __ne__(self, other):
        return not self.__eq__(other)