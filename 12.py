#Write python program that accepts an integer (n) and computes the value of n+nn+nnn.
n=input("enter vakue of n: ")
nn=str(n)+str(n)
nnn=nn+str(n)
r=n+int(nn)+int(nnn)
print "result is %d"%r
