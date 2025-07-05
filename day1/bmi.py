#Entering the weight and Height From the keyboard
weight = float(input("Enter Weight(Kgs): "))
height = float(input("Enter Height(m): "))

#Calculating the BMI and printing it
bmi = weight/height**2
print(f"Your BMI is {bmi}")

#Prints when the person Under weight
if bmi < 18.5:
    print("Under weight")

#Prints when the person Healthy weight
elif 18.5 <= bmi <= 24.9:
    print("Healthy weight")

#Prints when the person is Overweight
elif 24.9 < bmi <= 29.9:
    print("Overweight")

#Prints when the person Obesity Class I
elif 29.9 < bmi <= 34.9:
    print("Obesity Class I")

#Prints when Obesity Class II
elif 34.9 < bmi <= 39.9:
    print("Obesity Class II")

#Prints when the person is Obesity Class III (Severe/Morbid Obesity)
else:
    print("Obesity Class III (Severe/Morbid Obesity)")