arr = [3, 1, 9, 8, 11, 6]

choice_arr = input('Hello, choose an array option, t - test array, n - new (yours array) \n')
if choice_arr == 'n':
    arr =  list(map (int, input().split()))

for j in range(len(arr) - 1, 0, -1):
    counter = 0
    for i in range(j):
          if arr[i] > arr[i + 1]:
              arr[i], arr[i + 1] = arr[i + 1], arr[i]
              counter += 1
    if counter == 0:
       break
print(arr)
input('Press Enter to end \n')