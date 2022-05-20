# a = input('Введите число: ')
# l=[]
# for i in range(len(a)):
#     if a[i] != a[-1]:
#         if a[i] <= a[i+1]:
#             print(a ,'False')
#             l.append(a)
#             print(*l,'False')
#             break
#         else:
#             print(a, 'True')
#             l.append(a)
#             print(*l,'True')
#             break

# n=5
# ls=''
# for i in range(n):
#     for y in range(i):
#         ls = (str(i) + ' ') * i
#     print(ls)

# def greet_me(**kwargs):
#     for key, value in kwargs.items():
#         print("{0}={1}".format(key, value))
#     greet_me(name="yasoob")
# name=yasoob
# def test_args_kwargs(arg1, arg2, arg3):
#     print("arg1:", arg1)
#     print("arg2:", arg2)
#     print("arg3:", arg3)
# args=("two", 3, 5)
# test_args_kwargs(*args)
# kwargs={"arg3": 3, "arg2": "two", "arg1": 5}
# test_args_kwargs(**kwargs)

# some_func(farg, *args, **kwargs)
# import  someclass
# def get_info(self, *args):
#     return "Test data"
# someclass.get_info = get_info
# class Factory:
#     def engine(self):
#         print("Двигател создан")
#     def bridge(self):
#         print("Ходовая часть создана")
# class Toyota(Factory):
#     def wheels(self):
#         print("Калеса готовы")
#     def windows(self):
#         print("Стекло готовы")
# car=Toyota()
# car.engine()
# car.bridge()
# car.wheels()
# car.windows()
# print(17 % 5)
# print(10+ int('20'))

# nums=[8, 1, 2, 2, 3]
# lst=[]
# for i in range(len(nums)):
#     count1=[]
#     for j in range(len(nums)):
#         if nums[i]>nums[j]:
#             count1.append(nums[j])
#             lst.append(len(count1))
# print(lst)
# l=sorted(nums)
# r=[]
# for i in range(len(nums)):
#     r.append(l.index(nums[i]))
# print(r)
# nums = [1,2,1]
# print(nums*2)
# n=nums[::]
# n=[]
# for i in nums:
#     n.append(i)
# print(n)
# words=["a"]

# n=['a':".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# words = ["gin","zen","gig","msg"]
# n = {'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
# old = []
# t = 0
# while t < len(words):
#     one = []
#     for i in words[t]:
#         one.append(n[i])
#     old.append(''.join(one))
#     one = []
#     t+=1
# new = []
# for i in old:
#     if i not in new:
#         new.append(i)
#     return len(new)


# nums = [5, 4, 2, 1, 0, 3]
# res = [nums[0], nums[nums[1]], nums[nums[1]] , nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
# res = [nums[5], nums[4], nums[2], nums[1], nums[0], nums[3]]
# res = [3, 0, 2, 4, 5, 1]

# print(len(nums))
# new=[]
# for i in range(len(nums)):
#     new.append(nums[nums[i]])
# print(new)

# nums=[1, 2, 3, 4]

# for i in range(1, len(nums)):
#     nums[i] += nums[i-1]
# print(nums)
# accounts = [[1,2,3],[3,2,1]]
# # print(accounts+accounts)


# sums = [sum(i) for i in accounts]
# sums.sort()
# print(sums[-1])

# a= "1,2,3,4,5,6"

# print(a.replace(",", "[,]"))

#  sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

# class Solution(object):
#     def mostWordsFound(self, sentences):
#         """
#         :type sentences: List[str]
#         :rtype: int
#         """
#         result = []
#         for element in sentences:
#             result.append(len(element.split()))
#             result.sort()
#         print(result[-1])
# n=Solution()
# n.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])

# import instaloader 
Profile =input ("Введите ваш аккаунть ")
# insta=instaloader.instaloader()
# insta.download_profile(profile_pic_only=True)
