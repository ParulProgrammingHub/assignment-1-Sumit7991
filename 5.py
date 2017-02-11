#Write python program to enter value in days and convert in form of years, months and days(assuming all months has 30 and year is of 360).
d=input("enter number of days: ")
y=d/360
tmp=d%360
m=tmp/30
rem_days=tmp%30
print"%d days have %d years ,%d months and %d remaining days"%(d,y,m,rem_days)

