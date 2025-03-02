def initialize_image():
    return [[4 - max(abs(i - 4), abs(j - 4)) for j in range(9)] for i in range(9)]

def dilatace(image):
    new_image = [[0] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            neighbors = [image[i][j]]
            if i > 0: neighbors.append(image[i - 1][j])
            if i < 8: neighbors.append(image[i + 1][j])
            if j > 0: neighbors.append(image[i][j - 1])
            if j < 8: neighbors.append(image[i][j + 1])
            new_image[i][j] = max(neighbors)
    return new_image

def eroze(image):
    new_image = [[0] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            neighbors = [image[i][j]]
            if i > 0: neighbors.append(image[i - 1][j])
            if i < 8: neighbors.append(image[i + 1][j])
            if j > 0: neighbors.append(image[i][j - 1])
            if j < 8: neighbors.append(image[i][j + 1])
            new_image[i][j] = min(neighbors)
    return new_image

def print_image(image):
    for row in image:
        print(" ".join(map(str, row)))

image2d = initialize_image()
print_image(image2d)
image2d = dilatace(image2d)
image2d = eroze(image2d)
image2d = eroze(image2d)
image2d = dilatace(image2d)
print_image(image2d)
