a = int(input(Input mod ))
b = int(input(Input Exponent ))
m = int(input(Input mod ))


ab_ex = ab
ab_modm = ab_ex % m


'''
ab_ex = pow(a,b)
ab_modm = pow(a,b,m)
'''


print(ab_ex)
print(ab_modm)
