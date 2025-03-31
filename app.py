# calculate formula define
def calculate_bmi(weight, height):
    try:
        bmi = weight / (height ** 2)
        return bmi
    except ZeroDivisionError:
        return "Height cannot be zero."
# main define for input and calculate 
def main():
    try:
        weight = float(input("Enter your weight in kilograms:"))
        height = float(input("Enter your height in meters:"))
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is: {bmi:.2f}")
        if bmi < 18.5:
            print("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            print("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            print("You are overweight.")
        else:
            print("You are obese.")
    except ValueError:
        print("Please enter valid numbers for weight and height.")

if __name__ == "__main__":
    main()

