def cooldown(arr,c):
    counter = 0
    res = []

    for i in range(len(arr)):
        if res==[]:
            res.append(arr[i])

        else:
            if res[-1] == arr[i]:
                counter+=1
            if res[-1]!=arr[i]:
                counter=0
            if counter>=c:
                res.append("_")

            res.append(arr[i])
            
        
    return res
print("ashutsiohgs")
arr=[1,1,1,1,2,3,5,5,5,5,1]
c = 3
print(cooldown(arr,c))