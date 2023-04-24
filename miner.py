import random
from termcolor import colored

# Ask user for number of wallets to test
num_wallets = int(input("How many wallets do you want to test? "))

# Define empty list to store wallet values
values = []

# Loop over the number of wallets requested
for i in range(num_wallets):
    # Generate a random name for each wallet
    wallet_name = ''.join(random.choices('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_', k=48))

    # Define the probabilities for obtaining different values
    zero_prob = 0.9999
    small_prob = 0.0001
    big_prob = 0.000001

    # Generate a random value for each wallet based on the defined probabilities
    value = 0
    if random.random() < small_prob:
        value = random.uniform(0, 5)
    elif random.random() < big_prob:
        value = random.uniform(5, 1000)
    else:
        value = 0

    # Color the value based on its amount
    if value == 0:
        value_str = colored("$0.00", "red")
    elif value <= 20:
        value_str = colored("${:.2f}".format(value), "white")
    else:
        value_str = colored("${:.2f}".format(value), "green")
        values.append((wallet_name, value_str))

    # Print the name and value of each wallet
    print("Wallet:", colored(wallet_name, "cyan"), "|", "Value:", value_str)

# Print wallets with a value over $5
print("=========================")
print("Wallets with value over $5.00:")
for wallet, value in values:
    print(f"{wallet}: {value}")
print("=========================")
