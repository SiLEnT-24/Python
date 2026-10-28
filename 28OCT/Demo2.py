prev=int(input("Enter your percentage: "))
yrs=int(input("Enter your passing years: "))

res=(prev>=75 and yrs==2024)
# res=(prev>=75 or yrs==2024)
# res=not(prev>=75 and yrs==2024)
# res=not(prev>=75 or yrs==2024)

print(res)
