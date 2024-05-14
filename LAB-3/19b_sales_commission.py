def compute_commission(sales_amount, commission_rate):
    commission = sales_amount * commission_rate
    return commission


sales_amount = float(input("Enter the sales amount: "))
commission_rate = float(input("Enter the commission rate (as a decimal): "))

commission = compute_commission(sales_amount, commission_rate)
print("The commission is: $", commission)

