'''Write a program to Get Only unique items from two sets'''

s1={1,2,3}
s2={1,7,5}

# us=s1.union(s2) - s1.intersection(s2)
us = s1.symmetric_difference(s2)
print("The only Unique elements are :", us)



# Python Set symmetric_difference() method is used to get the elements
#  present in either of the two sets, but not common to both sets. 
# In this article, we are going to learn about the Python Set symmetric_difference() function.