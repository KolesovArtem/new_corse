# a = 10
# b = 5
#
# c1 = a + b
# c2 = a - b
# c3 = a * b
# c4 = a / b
# c5 = a ** b
# c6 = 8 % 3
#
# c7 = [c1, c2, c3, c4, c5]
#
# print("Result1 =", c1)
# print("Result2 =", c2)
# print("Result3 =", c3)
# print("Result4 =", c4)
# print("Result5 =", c5)
# print("Result6 =", c6)
#
#
# for i in c7:
#     check = i % 2
#
#     if check == 0:
#         print("Even =", i)
#     else:
#         print("Odd =", i)


# > <  == >= <= !=

a1 = 10
a2 = 5
a3 = 15
a4 = 50
a5 = 10

result = a1 >= a2
print("Compare ", a1, ">=", a2)
print("Result =", result)


# and or not
print()
result2 = a1 == a2 or a1 < a3 and a1 > a4
r1 = a1 == a2
r2 = a1 < a3
print("R1 a1 == a2", r1)
print("R2 a1 < a3", r2)
print("R =", r1, r2)
print("AND, OR, NOT --> Result =", result2)

print()
if a1 > 10:
    print('TRUE item1')
else:
    print('FALSE item2')