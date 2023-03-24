#6、请对列表nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]使用Python对其进行定义，遍历、增加，访问元素等操作。
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]

#遍历
for item in nums:
    print(item,end=' ')

#增加
nums.append(100)   #append是追加的意思
print(nums)

nums2=[1,2,3,4,5,6,7,8]
nums.append(nums2)  #向列表的末尾一次性添加多个元素
print(nums)

nums.insert(1,90)      #索引为1的位置添加90
print(nums)

nums3=[22,33,44,55,66]
nums[1:]=nums3     #lst从索引为1开始一直到列表的最后(默认步长为1)
print(nums)       #lst被切的部分用lst3替换

#访问
print(nums[2])    #正向索引
print(nums[-3])   #逆向索引