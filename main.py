import addition
import substraction
import division
import multiplication

a, b = [int(x) for x in input("Enter two integers: ").split(' ')]

print("Addition :", addition.add(a, b))
print("Substraction :", substraction.sub(a, b))
print("Division :", division.div(a, b))
print("Multiplication :", multiplication.mul(a, b))