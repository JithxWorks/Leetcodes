
class Solution:
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):

        # Find the closest x-coordinate in the rectangle
        if xCenter < x1:
            closestX = x1
        elif xCenter > x2:
            closestX = x2
        else:
            closestX = xCenter

        # Find the closest y-coordinate in the rectangle
        if yCenter < y1:
            closestY = y1
        elif yCenter > y2:
            closestY = y2
        else:
            closestY = yCenter

        # Distance from circle center to closest point
        dx = xCenter - closestX
        dy = yCenter - closestY

        return dx * dx + dy * dy <= radius * radius
