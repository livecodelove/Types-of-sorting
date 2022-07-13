arr= [3, 14, 1, 7, 9, 8, 11, 6, 4, 2]


choice_arr = input('Hello, choose an array option, t - test array, n - new (yours array) \n')
if choice_arr == 'n':
    arr =  list(map (int, input().split()))
    
l = len(arr)
factor = 1.247
step_factor = l / factor 


while step_factor > 1:
    step = round(step_factor)
    for j in range(step, l):
        for i in range(j):
          if arr[i] > arr[j]:
              arr[i], arr[j] = arr[j], arr[i]
    step_factor = step_factor/factor
print(arr)
input('Press Enter to end \n')
