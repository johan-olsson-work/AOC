input_data = [1,1,1,3,3,2,1,1,1,1,1,4,4,1,4,1,4,1,1,4,1,1,1,3,3,2,3,1,2,1,1,1,1,1,1,1,3,4,1,1,4,3,1,2,3,1,1,1,5,2,1,1,1,1,2,1,2,5,2,2,1,1,1,3,1,1,1,4,1,1,1,1,1,3,3,2,1,1,3,1,4,1,2,1,5,1,4,2,1,1,5,1,1,1,1,4,3,1,3,2,1,4,1,1,2,1,4,4,5,1,3,1,1,1,1,2,1,4,4,1,1,1,3,1,5,1,1,1,1,1,3,2,5,1,5,4,1,4,1,3,5,1,2,5,4,3,3,2,4,1,5,1,1,2,4,1,1,1,1,2,4,1,2,5,1,4,1,4,2,5,4,1,1,2,2,4,1,5,1,4,3,3,2,3,1,2,3,1,4,1,1,1,3,5,1,1,1,3,5,1,1,4,1,4,4,1,3,1,1,1,2,3,3,2,5,1,2,1,1,2,2,1,3,4,1,3,5,1,3,4,3,5,1,1,5,1,3,3,2,1,5,1,1,3,1,1,3,1,2,1,3,2,5,1,3,1,1,3,5,1,1,1,1,2,1,2,4,4,4,2,2,3,1,5,1,2,1,3,3,3,4,1,1,5,1,3,2,4,1,5,5,1,4,4,1,4,4,1,1,2]

test_data = [3,4,3,1,2]

def create_smart_input(data_list):
    smart_list = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0}
    for data in data_list:
            smart_list[str(data)] += 1

    return smart_list

#Initial state: 3,4,3,1,2 [{1:1}, {2: }]
#After  1 day:  2,3,2,0,1
#After  2 days: 1,2,1,6,0,8
#After  3 days: 0,1,0,5,6,7,8

def one_day_increase(data):
    new_data = []
    for fish in data:
        if fish == 0:
            new_data.append(8)
            fish = 7
        fish -= 1
        new_data.append(fish)
    return new_data

def smarter_one_day_increase(data_dict):
    new_data = {}
    new_data['0'] = data_dict['1']
    new_data['1'] = data_dict['2']
    new_data['2'] = data_dict['3']
    new_data['3'] = data_dict['4']
    new_data['4'] = data_dict['5']
    new_data['5'] = data_dict['6']
    new_data['6'] = data_dict['7'] + data_dict['0']
    new_data['7'] = data_dict['8']
    new_data['8'] = data_dict['0']

    return new_data

smart_list = create_smart_input(input_data)
print(f"smart_list: {smart_list}")

for i in range (0,256):
    print(f"Day {i+1} {smart_list}")
    smart_list = smarter_one_day_increase(smart_list)

result = 0
for key, val in smart_list.items():
    result += val

print(f"Result: {result}")
