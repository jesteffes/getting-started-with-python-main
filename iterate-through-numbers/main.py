years_list = [5,7,12,13,9,21,11,10]
num_eligible = 0

for coworker in years_list:
    if coworker > 9:
        num_eligible = num_eligible + 1

print(num_eligible)