from collections import Counter

mylist=[1,21,21,3,42,1,2,5,2,31,1,3,2,1,35,5,4,2,4,5,54,3,2,1]

# counter=Counter(mylist)
# print(counter.most_common())
# print(counter.most_common(3))


print(min(mylist,key=mylist.count))

