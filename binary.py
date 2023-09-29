def binarys(a,ele):
    start=0
    end=len(a)-1
    flag=0
    count=0
    while(start<=end and flag==0):
       count+=1
       mid=(start+end)//2
       if (ele==a[mid]):
          flag=1
          print("element found at ",str(mid+1))
          print("no. of iterations are: ",str(count))
          return
       else:
          if (ele<a[mid]):
               end=mid-1
          else : 
              start=mid+1
    print("not present")

a=[2,88,3,9,1,7,23]
binarys(a,23)
            