heights = input()


def valid_mountain_array(heights):
    heights = list(map(int, heights.split()))
    i = 0
    n = len(heights)
    if n < 3:
        return False
    while i + 1 < n and heights[i] < heights[i + 1]:
        i += 1
    if i == 0 or i == n - 1:
        return False
    while i + 1 < n and heights[i] > heights[i + 1]:
        i += 1
    return i == n - 1


if __name__ == '__main__':
    print(valid_mountain_array(heights))
