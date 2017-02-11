#Write python program to enter principal amount, time and interest rate. Create simple_interest(principle,time,rate) function to calculate simple interest.
principle=input("enter principle amount: ")
time=input("enter time  in years: ")
rate=input("enter the interest rate per year in percentage: ")
def simple_interest(principle,time ,rate):
    s=principle*rate*time
    return s
print "simple interest is %f"%simple_interest(principle,rate,time)
