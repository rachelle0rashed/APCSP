def celsius(fahrenheit): 
    celsius = (int(fahrenheit) - 32) / 1.8
    return celsius
    
def fahrenheit(celsius):
    fahrenheit = (1.8 * int(celsius))
    return fahrenheit
    
try: 
    print(fahrenheit(input("Celsius to Fahrenheit: ")))
    print(celsius(input("Fahrenheit to Celsius: ")))

except ValueError:
    print("Sorry man this ain't going to work! ")