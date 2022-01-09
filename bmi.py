heigth = float(input("請輸入您的身高(m):"))
weight = float(input("請輸入您的體重:"))
bmi = float(weight / heigth ** 2)
if bmi < 18.5:
    print("您的bmi:", bmi, "您屬於:過輕")
elif 18.5 <= bmi < 24:
    print("您的bmi:", bmi, "您屬於:正常")
elif 24 <= bmi < 27:
    print("您的bmi:", bmi, "您屬於:過重")
elif 27 <= bmi < 30:
    print("您的bmi:", bmi, "您屬於:輕度肥胖")
elif 30 <= bmi < 35:
    print("您的bmi:", bmi, "您屬於:中度肥胖")
else:
    print("您的bmi:", bmi, "您屬於:重度肥胖")
