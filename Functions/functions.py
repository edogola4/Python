# Control Flow and Functions in Python 

'''
1. Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
2. Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.
'''

# function to calculates discount
def calculate_discount(price, discount_percent):
## check if discount is 20% or higher
 if discount_percent >= 20:
    ## apply discount and calculate the final price
    discount_amount = ( discount_percent / 100) * price
    final_price = price - discount_amount
    return final_price
 else:
    ## No discount applied, return original price
    return price

## prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))


## calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percentage)

## display the results
if final_price != original_price:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${original_price:.2f}")
