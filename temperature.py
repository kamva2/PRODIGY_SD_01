# Autor: Kamva Poswa
# 17 June 2024

def spliting(x):
    return x.split()

def main():
    
    temp = spliting(input("Enter your temperature:"))
    
    float_temp = float(temp[0])
    str_temp = str(' '.join(temp[1:]).lower())
    
    if str_temp == "degree celsius":
        
        kelvin = float_temp + 273.15
        fahrenheit = (float_temp * 9/5) + 32
        
        print(f"The temperature is {round(kelvin,2)}K in Kelvin.")
        print(f"The temperature is {round(fahrenheit,2)}F in Fahrenheits.")
        
    elif str_temp == "kelvin":
        
        degree_c = float_temp - 273.15
        fahrenheit = (float_temp -273.15) * 5/9 + 32
        
        print(f"The temperature is {round(degree_c,2)}C in degree celsius.")
        print(f"The temperature is {round(fahrenheit,2)}F in Fahrenheits.")
        
    elif str_temp == "fahrenheit":
    
        degree_c = (float_temp - 32) * 5/9
        kelvin = (float_temp - 32) * 5/9 + 273.15
        
        print(f"The temperature is {round(degree_c,2)}C in degree celsius.")
        print(f"The temperature is {round(kelvin,2)}K in kelvin.")
        
    else:
        print("Please enter (kelvin, fahrenheit, degree celsius) temperature!!!")
    
main()