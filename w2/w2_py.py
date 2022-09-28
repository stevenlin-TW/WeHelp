def calculate(min,max,step):
    sum = 0
    for i in range(min,max+1,step):
        sum += i
    print(sum)

calculate(1,3,1)
calculate(4,8,2)
calculate(-1,2,2)

def avg(data):# 請用你的程式補完這個函式的區塊
    count = 0
    sum = 0
    for i in range(len(data["employees"])):
        employee = data["employees"][i]
        if employee["manager"]==False:
            sum += employee["salary"]
            count += 1
    print(sum/count)
    #print(len(data["employees"]))


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


def func(a):
    def sum(b,c):
        print(a + b * c)
    return sum

func(2)(3,4)
func(5)(1,-5)
func(-3)(2,9)


def maxProduct(nums):
    max=0
    #print(type(nums))
    
    if len(nums)==2:
        print(nums[0]*nums[1])
        return
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if (nums[i]*nums[j]<0):
                continue
            else:
                max_temp = nums[i]*nums[j]
                if max_temp > max:
                    max = max_temp
    print(max)


maxProduct([5,20,2,6])    #120
maxProduct([10,-20,0,3])  #30
maxProduct([10,-20,0,-3]) #60
maxProduct([-1,2])        #-2
maxProduct([-1,0,2])      #0
maxProduct([5,-1,-2,0])   #2
maxProduct([-5,-2])       #10


def twoSum(nums,target):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]

result = twoSum([2,11,7,15],9)  # [0,2]
print(result)

def maxZeros(nums):
    count = 0
    max_count = 0
    for i in nums:
        if i == 0:
            count += 1
        else:
            if count>max_count:
                max_count = count
                count = 0

    if count>max_count:
            max_count = count
    print(max_count)
         
maxZeros([0,1,0,0])
maxZeros([1,0,0,0,0,1,0,1,0,0])
maxZeros([1,1,1,1])
maxZeros([0,0,0,1,1])
