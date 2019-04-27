def convertFloat(num):
    try:
        num = float(num)
        return num
    except (TypeError, ValueError, ArithmeticError):
       print("num cannot convert float")

print(convertFloat(1))
print(convertFloat("a"))