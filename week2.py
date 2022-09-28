#Q1
def calculate(min, max, step):
    sum = 0 
    for x in range(min,max+1,step):
        sum+=x
    return print(sum)
calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0

#Q2
def avg(data):
    count = 0;
    sum = 0;
    for x in data['employees']:
        if x['manager'] == False:
            sum+=x['salary']
            count+=1
    return print(round(sum/count))        
avg({
    "employees":[
        {
        "name":"John",
        "salary":30000,
        "manager":False
        },
        {
        "name":"Bob",
        "salary":60000,
        "manager":True
        },
        {
        "name":"Jenny",
        "salary":50000,
        "manager":False
        },
        {
        "name":"Tony",
        "salary":40000,
        "manager":False
        }
    ]
}) # 呼叫 avg 函式

#Q3
def func(a):
    def addMultiple(b,c):
        return print(a+b*c)
    return addMultiple
    
func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

#Q4
def selection_sort(list_a):
    indexing_length = range(0, len(list_a)-1)

    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value]: 
                min_value = j

        if min_value != i:
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]

    return list_a
    
def slectionSort(data):
    for i in range(0, len(data)-1):
        min_value = i
        
        for x in range(i+1,len(data)):
            if (data[x] < data[min_value]):
                min_value = x
        
        if min_value != i:
            data[min_value], data[i] = data[i], data[min_value]
            
    return data    
        
def maxProduct(nums):
    sorted_result = slectionSort(nums)
    list_len = len(sorted_result)
    posProduct = sorted_result[list_len-1]*sorted_result[list_len-2]
    negProduct = sorted_result[0]*sorted_result[1]
    if (posProduct>=negProduct):
        return print(posProduct)
    else:    
        return print(negProduct)
    
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10

#Q5
def twoSum(nums, target):
    list = {}
    for x in range(0, len(nums)):
        complement = target - nums[x]
        if (complement in list):
            return [list[complement],x]
        list[nums[x]] = x
    return None   
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

#Q6
def maxZeros(nums):
    result = 0
    maxNum = 0
    for i in nums:
        if i == 0:
            result+=1
            maxNum = max(result,maxNum)
        else:
            result = 0
    return print(maxNum)        
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3