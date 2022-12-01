input_test_data = [[1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
                   [1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
                   [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
                   [3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
                   [7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
                   [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
                   [1, 3, 5, 9, 9, 1, 2, 4, 2, 1],
                   [3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
                   [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
                   [2, 3, 1, 1, 9, 4, 4, 5, 8, 1]]





#def increase_all_by_one(data):
#    return_data = []
#    for int_list in data:
#        next_list = [x + 1 for x in int_list]
#        return_data.append(next_list)
#    return return_data
#
#
#def increase_input_points_by_one(data, points):
#    return_data = data
#    additional_flashing_points = []
#    for p in points:
#        return_data[p[0]][p[1]] += 1
#        if return_data[p[0]][p[1]] == 10:
#            additional_flashing_points.append(p)
#            additional_flashing_points.extend(get_adjecent_points(p))
#    if additional_flashing_points:
#        #print_data(return_data, "BEFORE RECURSIVE CALL:")
#        return_data = increase_input_points_by_one(return_data, additional_flashing_points)
#        #print_data(return_data, "AFTER RECURSIVE CALL:")
#    return return_data
#
#
#def fetch_points_that_flashed(data):
#    return_data = []
#    flashes = 0
#    for row_i, row in enumerate(data):
#        for nbr_i, nbr in enumerate(row):
#            if nbr == 10:
#                return_data.append((row_i, nbr_i))
#
#    return return_data
#

#def get_adjecent_points(p):
#    adjecent_points = []
#    first_row = (p[0] == 0)
#    last_row = (p[0] == len(input_test_data) - 1)
#    first_nbr = (p[1] == 0)
#    last_nbr = (p[1] == len(input_test_data[p[0]]) - 1)
#
#    #print(f"VERIFY... point:{p} first_row: {first_row} last_row: {last_row} first_nbr: {first_nbr} last_nbr: {last_nbr}")
#
#    if not first_row and not last_row:
#        if not first_nbr and not last_nbr:
#            adjecent_points.extend([(p[0]-1, p[1]-1), (p[0]-1, p[1]), (p[0]-1, p[1]+1), (p[0], p[1]-1), (p[0], p[1]+1), (p[0]+1, p[1]-1), (p[0]+1, p[1]), (p[0]+1, p[1]+1)])
#        elif first_nbr:
#            adjecent_points.extend([(p[0]-1, p[1]), (p[0]-1, p[1]+1), (p[0], p[1]+1), (p[0]+1, p[1]), (p[0]+1, p[1]+1)])
#        else: # last nbr
#            adjecent_points.extend([(p[0]-1, p[1]-1), (p[0]-1, p[1]), (p[0], p[1]-1), (p[0]+1, p[1]-1), (p[0]+1, p[1])])
#    elif first_row:
#        if not first_nbr and not last_nbr:
#            test = p[1]
#            print(f"test: {test}")
#
#            adjecent_points.extend([(p[0], p[1]-1), (p[0], p[1]+1), (p[0]+1, p[1]-1), (p[0]+1, p[1]), (p[0]+1, p[1]+1)])
#        elif first_nbr:
#            adjecent_points.extend([(p[0], p[1]+1), (p[0]+1, p[1]), (p[0]+1, p[1]+1)])
#        else: # last nbr
#            adjecent_points.extend([(p[0], p[1]-1), (p[0]+1, p[1]-1), (p[0]+1, p[1])])
#    else: # last_row
#        if not first_nbr and not last_nbr:
#            adjecent_points.extend([(p[0]-1, p[1]-1), (p[0]-1, p[1]), (p[0]-1, p[1]+1), (p[0], p[1]-1), (p[0], p[1]+1)])
#        elif first_nbr:
#            adjecent_points.extend([(p[0]-1, p[1]), (p[0]-1, p[1]+1), (p[0], p[1]+1)])
#        else: # last nbr
#            adjecent_points.extend([(p[0]-1, p[1]-1), (p[0]-1, p[1]), (p[0], p[1]-1)])
#
#    return adjecent_points
#

def get_adjecent_points_no_d(p, data, black_list):

    adjecent_points = []
    first_row = (p[0] == 0)
    last_row = (p[0] == len(data) - 1)
    first_nbr = (p[1] == 0)
    last_nbr = (p[1] == len(data[p[0]]) - 1)

    if not first_row and not last_row:
        if not first_nbr and not last_nbr:
            adjecent_points.extend([(p[0]-1, p[1]), (p[0], p[1]-1), (p[0], p[1]+1), (p[0]+1, p[1])])
        elif first_nbr:
            adjecent_points.extend([(p[0]-1, p[1]), (p[0], p[1]+1), (p[0]+1, p[1])])
        else: # last nbr
            adjecent_points.extend([(p[0]-1, p[1]), (p[0], p[1]-1), (p[0]+1, p[1])])
    elif first_row:
        if not first_nbr and not last_nbr:
            adjecent_points.extend([(p[0], p[1]-1), (p[0], p[1]+1), (p[0]+1, p[1])])
        elif first_nbr:
            adjecent_points.extend([(p[0], p[1]+1), (p[0]+1, p[1])])
        else: # last nbr
            adjecent_points.extend([(p[0], p[1]-1), (p[0]+1, p[1])])
    else: # last_row
        if not first_nbr and not last_nbr:
            adjecent_points.extend([(p[0]-1, p[1]), (p[0], p[1]-1), (p[0], p[1]+1)])
        elif first_nbr:
            adjecent_points.extend([(p[0]-1, p[1]), (p[0], p[1]+1)])
        else: # last nbr
            adjecent_points.extend([(p[0]-1, p[1]), (p[0], p[1]-1)])

    return [x for x in adjecent_points if x not in black_list]


#def get_all_points_to_increase(point_list):
#    all_points = []
#    for point in point_list:
#        all_points.append(point)
#        all_points.extend(get_adjecent_points(point))
#
#    return all_points
#
#
#def get_score(reset_data):
#    score = 0
#    for row in reset_data:
#        for val in row:
#            if val == 0:
#                score += 1
#    return score
#
#
#def reset_all_flashed(data):
#    return_data = []
#    for row_i, row in enumerate(data):
#        return_data.append( [0 if x > 10 else x for x in row] )
#
#    score = get_score(return_data)
#
#    return (score, return_data)
#

def print_data(data, string):
    print("")
    print(f"{string}")
    for row in data:
        print(f"row: {row}")


#def take_one_step(data):
#    next_data = increase_all_by_one(data)
#    # print_data(next_data, "substep increase by one:")
#
#    flashed_points = fetch_points_that_flashed(next_data)
#    while flashed_points:
#
#        points_to_increase = get_all_points_to_increase(flashed_points)
#        next_data = increase_input_points_by_one(next_data, points_to_increase)
#        # print_data(next_data, "Flash:")
#        flashed_points = fetch_points_that_flashed(next_data)
#
#    score, next_data = reset_all_flashed(next_data)
#    # print_data(next_data, "STEP DONE")
#    return (score, next_data)
#

def take_step(data, point, black_list, iteration, score_so_far):
    #print(f"iteration: {iteration}")
    iteration += 1

    #print(f"input point: {point}")

    score_so_far += data[point[0]][point[1]]
    best_path_score = 1000

    if point in black_list:
        #print("POINT IN BLACKLIST")

        return 1000

    #print(f"black_list: {new_black_list}")
    new_black_list = []
    new_black_list.extend(black_list)
    new_black_list.append(point)
    #print(f"black_list: {new_black_list}")
    #assert(False)


    if point == (len(data) - 1, len(data) - 1):
        print(f"PATH FOUND: {score_so_far} it: {iteration}")

        return score_so_far

    queue = get_adjecent_points_no_d(point, data, new_black_list)
    #print(f"queue: {queue}")
    #print(f"black_list: {new_black_list}")
    for next_point in queue:
        print(f"for in :")

        score = take_step(input_test_data, next_point, new_black_list, iteration, score_so_far)
        new_black_list.append(next_point)
        if score < best_path_score:
            best_path_score = score


    return best_path_score


#def check_if_all_flashed(data):
#    for row in data:
#        if any(i != 0 for i in row):
#            return False
#    return True

def main():
    total_score = 0
    print_data(input_test_data, "Before any step:")
    next_point = (0, 0)

    #score = take_step(input_test_data, next_point, [], 0, 0)
    total_score += score


    print(f"Total {next_point}):")
    print(f"total_score: {total_score}")

#Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.

if __name__ == '__main__':
    main()
