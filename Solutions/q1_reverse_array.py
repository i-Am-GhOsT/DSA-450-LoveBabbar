'''
 https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/
'''

list1= [1,2,3,4]
list2= [4,5,6,7]
list3= [8,9,10,11]

'''
HINT 1:

1) Initialize start and end indexes as start = 0, end = n-1 
2) In a loop, swap arr[start] with arr[end] and change start and end as follows : 
start = start +1, end = end – 1
'''

def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
    return A

print("Using List Native Function : "+str(reverseList(list3,0,len(list3)-1)))

'''
HINT 2: Slice The list [::-1]

Means From 0th to including last index in reverse from 
'''

def List_Reverse_Slicing(list_x):
  return list_x[::-1]

print("Using List Slicing : "+str(List_Reverse_Slicing(list1)))

''''
HINT 3 : List reversed Function
'''
def LibFunc_Reverse(list_x):
    list_x.reverse()

LibFunc_Reverse(list2)
print("Using List Library Function : ",list2)