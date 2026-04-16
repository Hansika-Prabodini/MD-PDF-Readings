def multiply(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    result = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
    for row in range(3):
        for col in range(3):
            for inner in range(3):
                result[row][col] += a[row][inner] * b[inner][col]
    return result


if __name__ == "__main__":
    a = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
    b = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
    print(multiply(a, b))
