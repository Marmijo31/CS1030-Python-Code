#= means assign. so "Mason" is =(assigned) to be stored as the firstName 

#first name, last name, and hobby are strings, strings tell to store in memory for refrence. The "text" means it will output as a string of text. 

firstName = "Mason" 

lastName = "Armijo" 

hobby = "Motorcycles" 

#birthYear, currentYear, and currentAge are integers. Integers are numbers (no quotations) 

birthYear = 2000 

currentYear = 2026 

#currentAge calculates by subtracting one integer from the other 

currentAge = currentYear - birthYear 

#fullName is combining 2 strings. No quotations because the 2 variables are already in string.  

fullName = firstName + " " + lastName 

 

#print  

print("My First Python Code") 

print() 

txt = f"My name is {fullName}, one of my hobbies is riding {hobby}. I am {currentAge} years old." 

print(txt) 
print("")
userName=input("What is your name?: ")
print("")
print(f"Hello, {userName}!")
print("")
userAge=int(input("What year were you born?: "))
print("")
print(f"You are {currentYear - userAge} years old.")
