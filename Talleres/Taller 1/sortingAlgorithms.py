# Basic bubble sort function  
def bubble_sort(list1):  
    # Outer loop for traverse the entire list  
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    return list1  

#list1 = [5, 3, 8, 6, 7, 2]  
#print("The unsorted list is: ", list1)  
# Calling the bubble sort function  
#print("The sorted list is: ", bubble_sort(list1))  

#######
# Bubble sort in Python
def bubbleSort(array):
  # loop to access each array element
  for i in range(len(array)):
    # loop to compare array elements
    for j in range(0, len(array) - i - 1):
      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:
        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

#data = [-2, 45, 0, 11, -9]
#bubbleSort(data)
#print('Sorted Array in Ascending Order:')
#print(data)

#####################
# Insertion sort in Python

def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1        
        # Place key at after the element just smaller than it.
        array[j + 1] = key

#data = [9, 5, 1, 4, 3]
#insertionSort(data)
#print('Sorted Array in Ascending Order:')
#print(data)