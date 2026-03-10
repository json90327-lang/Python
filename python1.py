#Write a program to find the missing number in an array from 1 to N.
arr=[1,3,4,5]
n=5
total=n*(n+1)//2
result=total-sum(arr)
print(result)

#Write a program to find duplicate elements in a list.
arr=[2,3,4,4,5,5,1,2]
duplicate=set()
for i in arr:
    if arr.count(i)>1:
       duplicate.add(i)
print(duplicate)


#Write a program to find the second largest number in a list without using sort().
arr=[34,67,23,22,21]
largest=max(arr)
arr.remove(largest)
print(arr)
print(max(arr))
