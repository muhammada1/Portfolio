import math

pi = 3.14159265359

l_AB = float(input("Length AB: "))
l_BC = float(input("Length BC: "))
l_AC = (((l_AB**2)+(l_BC**2))**.5)
 
l_MC = (l_AC/2)
l_MB = (((l_BC**2)-(l_MC**2))**.5)


a_ABC_p = l_AB/l_BC
a_ABC_rad = math.atan(a_ABC_p)
a_ABC = ((a_ABC_rad * 180)/ pi)
a_ABC_round = round(a_ABC)
a_ABC_str = str(a_ABC_round)

print(a_ABC_str + "°")



'''
a_MBC_p = l_MC/l_BC
 
a_MBC_rad = math.asin(a_MBC_p)

a_MBC = ((a_MBC_rad * 180)/ pi)

a_MBC_round = round(a_MBC)
#a_MBC_int = int(a_MBC_round)

a_MBC_str = str(a_MBC_round)
#a_MBC_str = str(a_MBC_int)


print(a_MBC_str + "°")
'''

