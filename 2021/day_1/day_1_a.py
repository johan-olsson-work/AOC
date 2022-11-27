from aocd import get_data

input = get_data(day=1, year=2021)

print(f"input: {input}")

# Day 1
counter = 0
last = input[0]
for val in input:
    if val > last:
        counter += 1
    last = val
    #print(f"input:{val}")
print(f"counter:{counter}")

# Day 1_2
counter = 0

slider = [input[0], input[1], input[2]]
print(f"slider:{slider}")
print(f"sum of slider:{sum(slider)}")

for val in input[3:]:
    current_sum = sum(slider)
    #print(f"input:{val}")
    slider.append(val)
    slider.pop(0)
    #print(f"slider:{slider}")
    # print(f"all vals:{val_1}, {val_2}, {val_3}")
    if sum(slider) > current_sum:
        counter += 1

print(f"counter:{counter}")
