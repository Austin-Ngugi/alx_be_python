FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(temperature):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    final_temp = (temperature-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return final_temp
def convert_to_fahrenheit(temperature):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    final_temp = (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return final_temp
while True:
    try:
        temperature = float(input("Enter the temperature to convert:"))
        break
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
 
if choice == "C":
    final_temp = convert_to_celsius(temperature)
    print(f"{temperature}\u2070C is {final_temp}\u2070F") 
    

elif choice =="F":
    final_temp = convert_to_fahrenheit(temperature)
    print(f"{temperature}\u2070F is {final_temp}\u2070C") 

else:
    print("Enter the correct Temperature unit")


    

    


