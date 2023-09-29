def bubble_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    return a
a=[12,55,45,999,23,865,356,554,345435,897]
bubble_sort(a)
for i in range(len(a)):
    print(a[i])