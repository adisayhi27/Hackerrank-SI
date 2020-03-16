def findWater(arr, n):

    left = [0]*n
    right = [0]*n
    water = 0

    left[0] = arr[0]
    for i in range( 1, n):
        left[i] = max(left[i-1], arr[i])

    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i + 1], arr[i]);

    for i in range(0, n):
        water += min(left[i], right[i]) - arr[i]

    print(water)

if __name__ == "__main__":
    m = int(input())
    for i in range(m):
        n = int(input())
        arr = list(map(int, input().split()))[:n]
        findWater(arr, n)
