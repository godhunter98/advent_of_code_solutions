from get_input import fetch_input

calorie_list = fetch_input(2022,1)

cals = calorie_list.splitlines()

# Part-1 Logic

total_cals = []
total = 0
for i in cals:
    if i !='':
        x = int(i)
        total+=x

    elif i =='':
        total_cals.append(total)
        total = 0

print("Part-1 Answer")
print("Total: ",max(total_cals),"indice: ",total_cals.index(max(total_cals)))
print("-----*****-----*****-----*****-----*****-----*****-----")
# Part-2 Logic
print("Part-2 Answer")
top3 = sorted(total_cals,reverse=True)[:3]
print("Total of Top 3 calories: ",sum(top3))
print()
        