
def selection_sort(Arr1):
    for i in range(0,len(Arr1)-1):
        min_ind = i
        for j in range(i+1, len(Arr1)):
            if Arr1[j] < Arr1[min_ind]:
                min_ind = j

        temp = Arr1[i]
        Arr1[i]=Arr1[min_ind]
        Arr1[min_ind] = temp

    print("Sorted list",Arr1)


if __name__ == '__main__':
    arr1 = [1,5,2,3,4,1,9,7]
    print("Unsorted array:",arr1)
    selection_sort(arr1)

