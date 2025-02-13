
hum=int(input("length of humerus in cm= "))
rad=int(input("length of radius in cm= "))
uln=int(input("length of ulna in cm= "))
fem=int(input("length of femur in cm= "))
tib=int(input("length of tibia in cm= "))
fib=int(input("length of fibula in cm= "))

print("NOTE: The above Calculations are based off of a study by Trotter and Gleser in 1958. The result of the above calculations is subject to errors that arise from the fact that the study was conducted on a limited sample size. This tool is only for educational and demonstrational purposes, it is not to be considered as a professional tool for forensic analysis.")
#white males

#humerus
#st=3.574*hum+57.21
whitemalesthum=2.89*hum+78.10
print("Stature from humerus=",whitemalesthum)
a=whitemalesthum

#radius
whitemalestrad=3.79*rad+79.42
print("Stature from radius=",whitemalestrad)
b=whitemalestrad

#ulna
whitemalestuln=3.76*uln+75.55
print("Stature from ulna=",whitemalestuln)
c=whitemalestuln

#femur
whitemalestfem=2.32*fem+65.53
print("Stature from femur=",whitemalestfem)
d=whitemalestfem

#tibia
whitemalesttib=2.42*tib+81.93
print("Stature from tibia=",whitemalesttib)
e=whitemalesttib

#fibula
whitemalestfib=2.60*fib+75.50
print("Stature from fibula=",whitemalestfib)
f=whitemalestfib

avght= (a+b+c+d+e+f)/5


print("Average Stature of the individual=", avght)

#References:
#Jeong, Y., Taylor, R. J., Jung, Y., & Woo, E. J. (2023). Trotter and Gleser’s (1958) equations outperform Trotter and Gleser’s (1952) equations in stature estimation of the US White males. Forensic Sciences Research, 8(1), 16–23. https://doi.org/10.1093/fsr/owad008
# Trotter, M., & Gleser, G. C. (1958). A re‐evaluation of estimation of stature based on measurements of stature taken during life and of long bones after death. American Journal of Physical Anthropology, 16(1), 79–123. https://doi.org/10.1002/ajpa.1330160106

