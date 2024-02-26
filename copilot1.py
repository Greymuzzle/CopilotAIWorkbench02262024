# Define a function that has two parameters called subtotal and tax rate. The subtotal and the tax rate will be entered by the user. When you call the function, pass the subtotal and tax rate as arguments to the function. Calculate the total amount, in the function, by adding the subtotal and the product of the subtotal and tax rate. The function should return the total amount.

def calculate_total(subtotal, tax_rate):
    total = subtotal + (subtotal * tax_rate)
    return total

subtotal = float(input("Enter the subtotal: "))
tax_rate = float(input("Enter the tax rate: "))
total = calculate_total(subtotal, tax_rate)
print("The total amount is", total)