def inserttion_sort(arr):
    for i in range (1,len(arr)):
        value = arr[i]
        part = i
        while part>0 and arr[part-1]>value:
            arr[part]=arr[part-1]
            part-=1
        arr[part]=value
    print("Insertion sort method:",arr)

if __name__ == '__main__':
    arr = [5,9,3,2,1,0,4]
    print(arr)
    inserttion_sort(arr)




