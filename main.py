import addition as add
import substraction as sub
import division as div
import multiplication as mul

a, b = [int(x) for x in input("Enter two integers: ").split(' ')]

printf("Addition :", add(a, b))
printf("Substraction :", sub(a, b))
printf("Division :", div(a, b))
printf("Multiplication :", mul(a, b))