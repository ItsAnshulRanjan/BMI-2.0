# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight/(height*height)
BMI_ROUND = round(BMI)
if BMI <= 18.5:
  print(f"Your BMI is {BMI_ROUND} ,you are underweight")
elif BMI <= 25:
   print(f"Your BMI is {BMI_ROUND} ,you have a normal weight")
elif BMI <= 30:
   print(f"Your BMI is {BMI_ROUND} ,you are overweight")
elif BMI <= 35:
   print(f"Your BMI is {BMI_ROUND} ,you are obese")
else:
   print(f"Your BMI is {BMI_ROUND} ,you are clinically obese")





