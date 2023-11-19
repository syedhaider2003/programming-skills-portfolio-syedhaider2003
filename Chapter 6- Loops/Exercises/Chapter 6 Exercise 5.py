andwich_orders = ['tuna', 'chicken', 'reuben', 'club', 'ozzie', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

if sandwich_orders.count('pastrami') < 3:
    print("The deli has run out of pastrami.")
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nSandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")