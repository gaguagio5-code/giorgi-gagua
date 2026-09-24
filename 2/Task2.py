cart_total = 45.00      # float
is_vip = False          # boolean
is_guest = False        # boolean
promo_code = "SAVE10"   # string, or "" for empty

# Free shipping: cart total is $50 or more OR the customer is a VIP
if cart_total >= 50 or is_vip:
    print("You get Free Shipping!")
else:
    print("Shipping charges apply.")

# Discount: promo code exists (truthy) AND the user is NOT a guest
if promo_code and not is_guest:
    discount = cart_total * 0.10
    cart_total -= discount
    print(f"10% discount applied! You saved ${discount:.2f}.")
else:
    print("No discount applied.")

print(f"Final total: ${cart_total:.2f}")