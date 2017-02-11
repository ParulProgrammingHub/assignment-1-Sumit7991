#Write python program to enter marks of 5 subjects and find the mean of 5 subjects, calculate percentage. If percentage is less than 35 print fail else print pass.
a=input("enter maximum marks for a subject: ")
t_marks=a*5.0
sub1=input("enter marks of subject 1: ")
sub2=input("enter marks of subject 2: ")
sub3=input("enter marks of subject 3: ")
sub4=input("enter marks of subject 4: ")
sub5=input("enter marks of subject 5: ")
obt_marks=sub1+sub2+sub3+sub4+sub5
avg_marks=obt_marks/5.0
percent=(obt_marks*100)/t_marks
print "average is %f and percentage is %f"%(avg_marks,percent)
if percent<35:
    print "FAIL"
else:
    print "PASS"
