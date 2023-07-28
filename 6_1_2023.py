def two_sum(arr,targ):
    look_for = {}
    for n,x in enumerate(arr, 1):
        print(look_for)
        try: 
            print("look_for[x]", look_for[x])
            return look_for[x], n
            
        except KeyError:
            look_for.setdefault(targ - x,n)

a = (2,1,8,7)
t = 9
print(two_sum(a,t))  # (1,2)