P=float(input("Enter the Amount:"))
R=float(input("Enter the Rate of interest:"))
T=float(input("Enter the time:"))
SI = (P * R * T) / 100
Amountpayable = P + SI
print(Amountpayable)