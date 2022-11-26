# 基本格式
age = 10
if age >= 18:                                           # 冒号不能忘记
   print("我已经成年了")
   print("即将步入大学生活")
else:                                                   # 冒号不能忘记
   print("我还是未成年")
print("时间过的真快呀")

# 作业
height = int(input("请输入你的身高(Cm)："))
vip_level = int(input("请输入你的vip级别(1~5)："))
day = int(input("请输入今天的日期(1~30)："))            # input输入的都是字符串，需要转换成数字

if height < 120:
   print("您的身高小于120CM，可以免费游玩。")
elif day == 1:
   print("今天是1号免费日，可以免费")
elif vip_level >3:
   print("您的vip级别大于了，可以免费游玩。")           # 多条件判断，所有if依次判断，当遇到第一个True即结束，所有if都False则运行else
else:
   print("不好意思，所有条件都不满足，需要购票10元。")
print("祝您游玩愉快。") 

"""
判断是互斥且有顺序的。
满足第一个条件，将不会理会之后的条件
第一个不满足，再判断第二个条件，以此类推
均不满足，进入else
else也可以省略不写，效果等同三个独立的if判断
"""

# 作业改进版，把int集成到if语句
if int(input("请输入你的身高(Cm)：")) < 120:
   print("您的身高小于120CM，可以免费游玩。")
elif int(input("请输入今天的日期(1~30)：")) == 1:
   print("今天是1号免费日，可以免费")
elif int(input("请输入你的vip级别(1~5)：")) >3:
   print("您的vip级别大于了，可以免费游玩。") 
else:
   print("不好意思，所有条件都不满足，需要购票10元。")
print("祝您游玩愉快。") 

# 嵌套语句1：
if int(input("你的身高是多少：")) > 120:
   print("身高超出限制，不可以免费")
   print("但是，如果vip级别大于了，可以免费")

   if int(input("你的vip级别是多少：")) > 3:
      print("恭喜你，vip级别达标，可以免费")
   else: 
      print("Sorry你需要买票10元")
else:
    print("欢迎小朋友，免费游玩。")

# 嵌套语句2：
if age > 18:
   print("继续判断")
   if age < 30:
      print("年龄达标，判断入职年限")
      if year > 2:
         print("可以领取礼物")
      elif level > 3:
         print("可以领取礼物")
   else:
       print("年龄不达标")
else: 
    print("年龄不达标")          