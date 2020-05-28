accounts = {"Artur": 10, "Magda": 1000, "Adam": 1500}
accounts1 = {}
#dictionary.items() - returns tuples('key','value')
for person, account_balance in accounts.items():

    accounts1[person] = account_balance * 1.01

print(accounts1)

#Dict comprehension
#we have to mention where the values should be unpacked!!!

accounts2 = {name: balance * 1.01 for (name, balance) in accounts.items()}

print(accounts2)

