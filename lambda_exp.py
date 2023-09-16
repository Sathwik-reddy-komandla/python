# mysquare=lambda x: x**2


# print(mysquare(22))

mysquare=lambda *args: sum(args)


print(mysquare(22,4,6,67,8,9,0))

# n=[1,2,34,5,7,8,9,7]

# def filter_f(x):
#     return x%2==0

# even=list(filter(lambda x:x%2==0,n))
# print(even)

# squared=list(map(lambda x:x**2 ,n))
# print(squared)

