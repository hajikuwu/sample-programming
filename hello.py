#1. create empty list
shopping_list = []


#2. define the function using the 'item' parameter
def add_item(item):
    shopping_list.append(item)

#3. call the function and pass data into it
# We can use input() right inside the paranthesis

print("Add to list: ")
add_item(input())

print("Add to list: ")
add_item(input())

print("Add to list: ")
add_item(input())

#4. print the final list using a loop at the very end
print("\nYour final shopping list:")
for thing in shopping_list:
    print(f"- {thing}")
    