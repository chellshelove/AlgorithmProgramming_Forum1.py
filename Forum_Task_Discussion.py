import math
 
num = eval(input("Enter a numerator : "))

while num < 1:
    num = eval(input("Please re-enter the numerator. Value must be greater than 0 : "))
else:
    den = eval(input("Enter a denominator : "))
    while den < 1:
        den = eval(input("Please re-enter the denominator. Value must be greater than 0 : "))

formula = math.gcd(num, den)

if num < den:
    print(num, '/', den, "is a proper fraction.")
    if formula == 1:
        print("This proper fraction cannot be reduced any further.")
    else:
        print("This proper fraction can be reduced to : ", num//formula, '/', den//formula)
else:
    print(num, '/', den, "is an improper fraction.")
    if formula == 1:
        print("This improper fraction cannot be reduced any further.")
        if num // den == num:
            print("The whole number is : ", num)
        else:
            print("The mixed number is ", num // den, "and", num//formula - ((num // den) * den), '/', den//formula)
    else:
        print("This improper fraction can be reduced to : ", num//formula, '/', den//formula)
        if num % den == 0:
            print("The whole number is : ", num // den)
        else:
            print("The mixed number is ", num // den, "and", num//formula - ((num // den) * den//formula), '/', den//formula)
