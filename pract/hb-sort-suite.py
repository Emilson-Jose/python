# 6-19-23
# suite of homebrew (hb) sort functions for practice

import random       # import random to shuffle lists for reuse

def hb_SelectionSort(li):
    i = 0
    while i < len(li):
        min_index = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_index]:
                min_index = j
        temp = li[i]
        li[i] = li[min_index]
        li[min_index] = temp
        i += 1

def hb_BubbleSort(li):
    i = 1
    while not isOrdered(li):
        for j in range(len(li)-i):
            if li[j] > li[j+1]:
                temp = li[j]
                li[j] = li[j+1]
                li[j+1] = temp
        i += 1

# merge and MergeSort are taken from freeCodeCamp and adjusted to only sort in increasing order
# annotated for understanding 
# https://www.freecodecamp.org/news/sorting-algorithms-explained-with-examples-in-python-java-and-c/
def MergeSort(li):
    if len(li) < 2:
        return li       # if list is 1 element, return list (removed [:] since I'm not sure what it's for)
    else:
        middle = len(li) // 2           # floor division operation to find a middle index
        left = MergeSort(li[:middle])   # recursive call for the list UP TO the middle index
        right = MergeSort(li[middle:])  # recursive call for the list PAST the middle index
        return merge(left, right)       # call merge to append lists

def merge(left, right):
    result = []             # initialize list to append to
    i, j = 0, 0             # indicies
    while (i < len(left) and j < len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def hb_InsertionSort(li):
    i = 1
    while i < len(li):
        key = li[i]
        j = i-1
        while j >= 0 and li[j] > key:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = key
        i += 1

# basically the method from Freecodecamp
def hb_QuickSort(li):
    if len(li) < 2:
        return li[:]        # when an input list is 1 or fewer elements, return input list
    else:
        pivot_index = len(li)//2
        left = [i for i in li if i < li[pivot_index]]           # initialize left list with elements that are less than the pivot
        right = [i for i in li if i > li[pivot_index]]          # initialize right list with elements that are greater than the pivot
        middle = [i for i in li if i == li[pivot_index]]        # initialize middle list with elements that are equal to the pivot
        result = hb_QuickSort(left) + middle + hb_QuickSort(right)  # concatenate the left and right lists to the middle after
                                                                    # recursively sorting the left and right sides
        return result
    
#def quicksort(z):
#    if(len(z)>1):
#        piv=int(len(z)/2)
#        val=z[piv]
#        print("pivot =", val)
#        print("current list =", z)
#        lft=[i for i in z if i<val]
#        mid=[i for i in z if i==val]
#        rgt=[i for i in z if i>val]

#        res=quicksort(lft)+mid+quicksort(rgt)
#        return res
#    else:
#        return z

def hb_HeapSort(ar):
    for x in ar:
        print(x)

# randomize a list to an unordered form
# if list is ordered, re-run
# return shuffled list
def jumbleList(li):
    random.shuffle(li)
    while isOrdered(li):
        random.shuffle(li)
    return li

# check that a list is ordered
def isOrdered(li):
    for x in range(len(li)):
        if x+1 < len(li):
            if li[x] > li[x+1]:
                return False
    return True

def main():
    li1 = [9, 1, 2, 3, 4, 5, 8]
    li2 = [9, 2, 3, 1, 8, 0]
    # li3 = ["Apple", "Banana", "Cantaloupe", "Doug", "Eveline", "Fred"]
    # ar1 = arr.array("i", [9, 1, 2, 3, 4, 5, 8])
    # hb_SelectionSort(ar1)
    print("original list:", li1)
    
    hb_InsertionSort(li1)
    print("insertion sort:", li1)
    jumbleList(li1)
    
    hb_SelectionSort(li1)
    print("selection sort:", li1)
    jumbleList(li1)

    hb_BubbleSort(li1)
    print("bubble sort", li1)
    jumbleList(li1)

    print("merge sort (odd list)", MergeSort(li1))
    jumbleList(li1)
    print("merge sort (even list)", MergeSort(li2))
    jumbleList(li2)

    print("quick sort (odd list)", hb_QuickSort(li1))
    jumbleList(li1)
    print("quick sort (even list)", hb_QuickSort(li2))
    jumbleList(li2)

    hb_HeapSort(li1)
    print("heap sort", li1)

if __name__ == "__main__":
    main()