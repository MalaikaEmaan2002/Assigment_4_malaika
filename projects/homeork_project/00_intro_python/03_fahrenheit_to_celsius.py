def temp():
    print("This code is for converting Fahrenheit to Celsius")
    degrees_fahrenheit = float(input("Enter your Fahrenheit degree: "))
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0
    print(f"{degrees_fahrenheit} degrees Fahrenheit is {degrees_celsius} degrees Celsius")

if __name__ == '__main__':
    temp()