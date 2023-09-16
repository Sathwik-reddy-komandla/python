age=12

# print("you are an adult" elif age>18 if "you are not")

x=[[11 ,2, 4],
[4, 5, 6],
[10 ,8 ,-12]]




def diagonalDifference(arr):
    # Write your code here
    # left to right diagonal
    l_r=0
    r_l=0
    for x in range(len(arr)):
        l_r+=arr[x][x]
        r_l+=arr[x][len(arr)-1-x]
    print(abs(l_r-r_l))

diagonalDifference(x)