
#===========================================================================================================================================
#Bubble sort
#Best  case : sorted         O(n)
#Worst case : inverse sorted O(n^2)
#Ave        :                O(n^2)
#Stable     : Yes
from turtle import right


bubble_sort_info=["O(n)","O(n^2)","O(n^2)","Stable"]
def bubble_sort(data):#最大放最後
    n=len(data)
    for i in range(n-1):
        for j in range(n-i-1):
            if data[j]>data[j+1]:
                tem=data[j]
                data[j]=data[j+1]
                data[j+1]=tem
    return data
#===========================================================================================================================================
#Insertion sort
#Best  case : sorted         O(n)
#Worst case : inverse sorted O(n^2)
#Ave        :                O(n^2)
#Stable     : Yes
def Insertion_sort(data):
    n = len(data)
    for i in range(n-1):
        key = data[i+1]
        j = i
        while j >=0 and key < data[j] :#前面小往前比
                data[j+1] = data[j]#往後放
                j -= 1
        data[j+1] = key # 做完j=-1 所以+1
    return data
#===========================================================================================================================================
#Selection sort
#Best  case : sorted         O(n^2)
#Worst case : inverse sorted O(n^2)
#Ave        :                O(n^2)
#Stable     : No
def Selection_sort(data):
    n=len(data)
    for i in range(n):
        t=i
        for j in range(i+1,n):#找最小的
            if data[t]>data[j]:
                t=j
        if t!=i:#最小的跟最前換
            tem=data[t]
            data[t]=data[i]
            data[i]=tem
    return data


#Merge sort
#Best  case :  O(nlogn)
#Worst case :  O(nlogn)
#Ave        :  O(nlogn)
#Stable     : Yes
def merge(left, right):
    result = []

    while len(left) and len(right):
        if (left[0] < right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result = result+left if len(left) else result+right
    return result

def mergeSort(array):
    if len(array) < 2:
        return array

    mid = len(array)//2
    leftArray = array[:mid]
    rightArray = array[mid:]
    print("left = ",leftArray, " right = ",rightArray)
    return merge(mergeSort(leftArray),mergeSort(rightArray))

#===========================================================================================================================================
#Quick sort
#Best  case :          O(nlogn)
#Worst case :          O(nlogn)
#Ave        :          O(nlogn)
#Stable     : No
def quicksort(data, left, right): # 輸入資料，和從兩邊開始的位置
    if left >= right :            # 如果左邊大於右邊，就跳出function
        return

    i = left                      # 左邊的代理人find bigger than pivot
    j = right                     # 右邊的代理人find smaller than pivot
    key = data[left]                 # 基準點 pivot

    while i != j:                  
        while data[j] > key and i < j:   # 從右邊開始找，找比基準點小的值
            j -= 1
        while data[i] <= key and i < j:  # 從左邊開始找，找比基準點大的值
            i += 1
        if i < j:                        # 當左右代理人沒有相遇時，互換值
            data[i], data[j] = data[j], data[i] 

    # 將基準點歸換至代理人相遇點
    data[left] = data[i] 
    data[i] = key

    quicksort(data, left, i-1)   # 繼續處理較小部分的子循環
    quicksort(data, i+1, right)  # 繼續處理較大部分的子循環



# a=[1,2,3,4,5]
# b=[5,4,3,2,1]
# c=[3,4,4,6,6,0,0,1]
# d=[26,5,77,1,61,11,59,15,48,19]

# quicksort(a,0,len(a)-1)
# quicksort(b,0,len(b)-1)
# quicksort(c,0,len(c)-1)
# quicksort(d,0,len(d)-1)

# print(a)
# print(b)
# print(c)
# print(d)
#===========================================================================================================================================
#heap sort
#Best  case :          O(nlogn)
#Worst case : sorted   O(nlogn)
#Ave        :          O(nlogn)
#Stable     : No

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, N, i):
	largest = i # Initialize largest as root
	l = 2 * i + 1	 # left = 2*i + 1
	r = 2 * i + 2	 # right = 2*i + 2

	# See if left child of root exists and is
	# greater than root
	if l < N and arr[largest] < arr[l]:
		largest = l

	# See if right child of root exists and is
	# greater than root
	if r < N and arr[largest] < arr[r]:
		largest = r

	# Change root, if needed
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i] # swap

		# Heapify the root.
		heapify(arr, N, largest)

# The main function to sort an array of given size
def heapSort(arr):
	N = len(arr)

	# Build a maxheap.
	for i in range(N//2 - 1, -1, -1): #cause it's a tree and index n ~ n/2 has no child so don't waste time ,therefore index from n/2 to 0
		heapify(arr, N, i)

	# One by one extract elements
	for i in range(N-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap first and last
		heapify(arr, i, 0) #heapify again
# arr=[26,5,77,1,61,11,59,15,48,19]
# heapSort(arr)
# print(arr)


#===========================================================================================================================================
#radix sort

# d : how many turns to do
# n : how many datas to do 
# r : how many buckets to take back

#Best  case :          O(d*(n+r))
#Worst case :          O(d*(n+r))
#Ave        :          O(d*(n+r))
#Stable     : Yes
# Radix sort
def radixsort(data):
    length = len(data)
    count = max(data) # 資料裡最大的數值

    # 用最大數來判斷最大位數
    digit = 1
    while count > 9:
        count /= 10
        digit += 1

    tmp = []
    cur = 0
    for i in range(length):    # 資料的大小會決定桶子的數量，會是一個二維陣列
        tmp.append([0] * length)
    order = [0] * length       # 游標行，用來將資料放到同一位數但不同列的桶子

    if digit <= 9:
        '''use LSD(Least significant digit) method '''
        n = 1
        while n <= max(data):
            for i in range(length):
                lsd = int(data[i]/n) % 10  # 將資料用10來取個位數的餘數
                tmp[lsd][order[lsd]] = data[i]
                order[lsd] += 1
            for i in range(length):
                # 如果這個位數的桶子在此行有資料，就丟到同一個位數，但下一列的位置
                if order[i] != 0:
                    for j in range(order[i]):
                        data[cur] = tmp[i][j]
                        cur += 1
                # 將游標行的資料歸零
                order[i] = 0
            n *= 10
            cur = 0
        print(data)
# data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
# radixsort(data)

#===========================================================================================================================================
#shell sort

#Best  case :          O(n^3/2)
#Worst case :          O(n^2)
#Ave        :          O(n^2)
#Stable     : No



def ShellSort(data):
    n = len(data)
    gap = n // 2 
    while gap > 0: 
        for i in range(gap,n): 
            temp = data[i] 
            j = i 
            while  j >= gap and data[j-gap] > temp: 
                data[j] = data[j-gap] 
                j = j - gap 
            data[j] = temp 
        gap = gap // 2
    return data

data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]       
#print(ShellSort(data))



#non_recursive_version
def binarysearch(data,k):
    n=len(data)
    low = 0
    high = n-1
    
    while low <= high:
        mid = (low + high)//2
        if k==data[mid]:
            find=1
            print(data[mid])
        else:
            if k<data[mid]:
                high = mid-1
            else:
                low = mid+1
    

#recursive_version
def binarysearch2(data,k,low,high):
    
    if low <= high:
        mid = (low + high)//2
        if k==data[mid]:
            print(data[mid])
        else:
            if k<data[mid]:
                return binarysearch2(data,k,low,mid-1)
            else:
                return binarysearch2(data,k,mid+1,high)
    

#binarysearch2(data2,26,0,len(data2)-1)


def interpolation_search(data,key):
    low = 0
    high = len(data)-1
    while low <= high:
        mid = round((key-data[low])*(high-low)/(data[high]-data[low]))+low
        if mid>=low & mid<=high:
            if key < data[mid]:
                high = mid-1
                break
            elif key > data[mid]:
                low = mid+1
                break
            else:
                return data[mid]
    return None
data2=[2,4,6,8,9,45,67,89,90]
a=interpolation_search(data2,233)
print(a)