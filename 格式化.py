# 占位符1
date = "11.21"
day = "monday"
weather = "rainy"
message = "today is %s, it is %s, a %s day" % (date, day, weather)
print(message)

# 占位符2
date = "11.21"
day = "monday"
weather = "rainy"
print(f"today is {date}, it is {day}, a {weather} day")

# 精度控制
num_1 = 11
num_2 = 11.345
print("数字宽度限制为5，结果是%5d" %num_1)
print("数字宽度限制为1，结果是%1d" %num_1)                          #宽度限制小于字符本身宽度则无效
print("数字宽度限制为7，小数点精度为2，结果为%7.2f" %num_2)         #小数点也算一单位的宽度
print("小数点精度为1，结果是%.1f" %num_2)

# 占位符作业
name = "elon"
stock_price = 1
stock_code = "123456"
stock_price_daily_growth_factor = 1.5
growth_days = 30
npv = stock_price * stock_price_daily_growth_factor ** growth_days
print(
    f"公司:{name}, 股票代码:{stock_code}, 当前股价:{stock_price}"
      "每日增长系数是:%.2f, 经过%d天的增长，股价达到了%d" %(stock_price_daily_growth_factor, growth_days, npv)
)

