# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141.    10^(-1) ≤ d ≤10^(-10)

N = 100
list = []
list1 =[]  
for i in range(1,N+1):  
        list.append (round((1+1/i)**i,3))   
print(list)  
i=0
d = 0.01
for list[i+1] in list:  
        if (list[i+1])-(list[i])>=d:
                list1.append (list[i])    
                i=i+1
print(list1)