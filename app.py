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
            print("You are underweight. 0_0")
            print("Recommendation: Include calorie-rich foods like nuts, seeds, dairy products, and lean protein in your diet. Don't skip meals!")
        elif 18.5 <= bmi < 24.9:
            print("You have a normal weight ^-^")
            print("Recommendation: Maintain your healthy weight with a balanced diet and regular exercise.")
        elif 25 <= bmi < 29.9:
            print("You are overweight 0_-")
            print("Recommendation: Consider reducing sugary and fatty foods, and engage in regular physical activity like walking or swimming.")
        else:
            print("You are obese :0")
            print("Recommendation: Consult a healthcare professional for personalized advice, and focus on a diet high in vegetables, lean proteins, and whole grains. Regular exercise is essential.")
    except ValueError:
        print("Please enter valid numbers for weight and height.")

if __name__ == "__main__":
    main()
       

