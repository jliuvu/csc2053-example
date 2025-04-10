# Date: 1/21/25

# Lists
cart = ["apples", "bananas", "cherries"]
print(cart)

# Add elements to list:
cart.append("donuts")
cart.append("eggs")
cart.append("flour")
print(cart)

# Remove elements from a list (searches from index 0 to index n):
# Will only remove ONE instance of the entered prompt; You must iterate it or use some remove all function to get rid of all instances
cart.remove("cherries")
print(cart)

# Check if item is in list first before you remove it:
if "pineapple" in cart:
    cart.remove("pineapple")

# Another way to remove is to remove by the index, as shown in the following:
cart.pop(3) # removes whatever is at index 3 (in this case, 'eggs')
print(cart)

# If you do cart.pop(), it will remove the LAST element in the list (last in first out), sort of like a stack
cart.pop() # i.e. flour gets removed
print(cart)

# You may also reverse a list and sort it alphabetically using the following.
cart.reverse()
print(cart)
cart.sort()
print(cart)

# You may slice existing lists and store them in new lists:
cart.append("bananas")
cart.append("grapes")
cart.append("oranges")
print(cart)

# syntax: cart[startIndex : endIndex]
fruit_basket = cart[3:]
print(fruit_basket)

# Declaring a list:
squares = []
for i in range(1,10): # 1 thru 10, non-inclusive of 10
    squares.append(i**2)
print(squares)

 # You may also do it within a list (list comprehension)
squares2 = [x*x for x in range(1, 10)]
print(squares2)

# Store items into b_items in cart that start with 'b':
b_items = [item for item in cart if item.startswith("b")]
print(b_items)

# Create a list with 'n' zeroes
inventory = [0] * len(cart)
print(inventory)

# Sets: 
number_set = set()
number_set = {1, 1, 2, 3, 4, 0, 10, 5}
print(number_set)
number_set.add(-10) # Note, the -10 will be stored near the 10
print(number_set)

# You may sort sets as well:
print(sorted(number_set))

# Dictionaries:
# It is comprised of a 'key' and an associated 'element'
fav_snacks = {} # create an empty dictionary
fav_snacks = {
    'kathleen' : 'tortilla chips',
    'maggie' : 'pretzels',
    'emily' : 'buffalo chicken dip',
    'ava' : 'chocolate'
}
print(fav_snacks)

# You may also add to the dictionary
fav_snacks['wade'] = 'popcorn'
print(fav_snacks)

# Using the dictionary:
if 'kathleen' in fav_snacks:
    print("kathleen's favorite snack is " + fav_snacks['kathleen'])

# To iterate through the entire dictionary, we do:
for key in fav_snacks:
    print(key + "'s favorite snack is " + fav_snacks[key]) 
    print(f"{key}'s favorite food is {fav_snacks[key]}") # you may also use a fstring, which results in the exact outcome as above

# Extract the key and value in the dictioanry:
for key, value in fav_snacks.items():
    print(key, value)

# These functions will return the keys/values into variables:
keys = fav_snacks.keys()
values = fav_snacks.values()

fav_snacks['alice'] = ['chips', 'nuts']
print(fav_snacks)

# YOU MAY HAVE DUPLICATE VALUES, BUT NOT DUPLICATE KEYS! There can only be ONE unique key per dictionary