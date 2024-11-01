#BMI CHECKER




height=int(input("enter height in cms"))
weight=int(input("enter weight in kg"))

bmi= weight/(height/100)**2

if bmi<=18.4:
  print("you are underweight")
elif bmi<=24.9:
 print("you are healty")
elif bmi<=29.9:
 print("you are overweight")
elif bmi<=34.9:
 print("you are severely overweight")
elif bmi<=39.9:
 print("you are obese")
else:
 print("you are severely obese")