#Write python program to enter 2 angles and using function thirdangle(angle1,angle2) calculate third angle.
angle1=input("enter angle1: ")
angle2=input("enter angle2: ")
def thirdangle(angle1,angle2):
    angle3=180-(angle1+angle2)
    return angle3
print "third angle is : %d"%thirdangle(angle1,angle2)

