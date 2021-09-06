'''
Find the maximum and minimum element in an array
https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/
'''


list_a = [1,2,3,4,5]

# Library Functions
def find_minmax(arr):
  return (min(arr),max(arr))


print("Minimum & Maximum element : ",find_minmax(list_a))

# Native Function

def Find_MinMaxPair(arr):
  min_ele,max_ele=arr[0],arr[0] 
  for i in range(1,len(arr)): # start iterating from the second element
      if arr[i]<min_ele: # check if next element is smaller than the previous
          min_ele=arr[i]
      if arr[i]>max_ele: # check if next element is bigger than the previous
          max_ele=arr[i]
  return (min_ele,max_ele)

print("Minimum & Maximum element in : ",Find_MinMaxPair(list_a))