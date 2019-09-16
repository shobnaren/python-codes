
def Bubble_sort(arr):
    for k in range(0,len(arr)-2):
        for i in range(0,len(arr)-k-1):
            if arr[i+1] < arr[i]:
                temp = arr[i+1]
                arr[i+1]=arr[i]
                arr[i]=temp
                print(arr)
    print("Sorted array using Buble sort:",arr)


if __name__ == '__main__':
    Arr = [0,3,4,5,1,6,7,8]
    print(Arr)
    Bubble_sort(Arr)
