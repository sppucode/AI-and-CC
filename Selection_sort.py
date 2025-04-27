def selection_sort(arr,size):
    for i in range(size):
        min_index = i
        for j in range (i+1,size):
            if arr[j] < arr[min_index]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
        print(f"after {i+1}th iteration {arr}")

    print("FINAL SORTED ARRAY IS ",arr)




size = input("How many elemnts you want to sort : ")
arr =[]
for i in range(int(size)):
    num = int(input("Enter Element : "))
    arr.append(num)

selection_sort(arr,int(size))