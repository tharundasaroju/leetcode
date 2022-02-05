def visiblePoints(points: list[list[int]], angle: int, location: list[int]) -> int:
    max_points = 0
    translateOrigin(points)
    return max_points

def translateOrigin(points: list[list[int]], origin: list[int]) -> list[list[int]]:
    for point in points:
        point[0] -= origin[0]
        point[1] -= origin[1]
    return points

x = [[2,1],[2,2],[3,4],[1,1]]
print(translateOrigin(x, [1,1]))
print(x)