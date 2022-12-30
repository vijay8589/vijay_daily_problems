"""input:
            employees = ['Kelly', 'Emma']
            defaults = {"designation": 'Developer', "salary": 8000}
    output:
            {'Kelly': {'designation': 'Developer', 'salary': 8000}, 
            'Emma': {'designation': 'Developer', 'salary': 8000}}"""

employees = ["Kelly", "Emma"]
defaults = {"designation": 'Developer', "salary": 8000}
res = dict.fromkeys(employees, defaults)
print(res)

print(res["Kelly"])
