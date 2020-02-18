if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())


s_arr = sorted(arr, reverse = True)

while (s_arr[0]) == (s_arr[1]):
    s_arr.remove((s_arr[0]))

print((s_arr[1]))

