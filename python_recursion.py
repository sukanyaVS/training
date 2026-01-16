
def table(n,m = 1):
  if(n < 1):
    print("Enter positive integer")
    return
  if m > 12:
    return
  else:
    print(m,'*',n,'=', m*n)
    table(n,m+1)


x = int(input("Enter a number: "))
table(x)
