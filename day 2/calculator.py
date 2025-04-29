bill=float(input("what was the total bill ? "))
tip =int(input("How much percent tip you want to give 10 15 20 "))
people =int(input("how many people  to split the bill "))
tip_as_percentage= tip / 100
total_tip_amount =  bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay : {final_amount}")
