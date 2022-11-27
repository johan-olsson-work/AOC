test_input_data = [
    ["dc", "end"],
    ["HN", "start"],
    ["start", "kj"],
    ["dc", "start"],
    ["dc", "HN"],
    ["LN", "dc"],
    ["HN", "end"],
    ["kj", "sa"],
    ["kj", "HN"],
    ["kj", "dc"]]

input_data = [["bm", "XY"],
              ["ol", "JS"],
              ["bm", "im"],
              ["RD", "ol"],
              ["bm", "QI"],
              ["JS", "ja"],
              ["im", "gq"],
              ["end", "im"],
              ["ja", "ol"],
              ["JS", "gq"],
              ["bm", "AF"],
              ["RD", "start"],
              ["RD", "ja"],
              ["start", "ol"],
              ["cj", "bm"],
              ["start", "JS"],
              ["AF", "ol"],
              ["end", "QI"],
              ["QI", "gq"],
              ["ja", "gq"],
              ["end", "AF"],
              ["im", "QI"],
              ["bm", "gq"],
              ["ja", "QI"],
              ["gq", "RD"]]

def get_nodes(data):
    nodes = {}
    for row in input_data:
        for node in row:
            nodes[node] = []
    print(f"nodes: {nodes}")

    for key in nodes:
        for row in input_data:
            for node_idx, data_node in enumerate(row):
                if key == data_node:
                    if node_idx == 0:
                        nodes[key].append(row[1])
                    else:
                        nodes[key].append(row[0])

    return nodes


def handle_blacklist(blacklist, key):
    if len(set(blacklist)) == len(blacklist) and key != "start" and key != "end":
        blacklist.append(key)
    else:
        if key not in blacklist:
            blacklist.append(key)
    return blacklist

def find_all_course_combos(start_key, end_key, nodes, blacklisted_nodes, current_course):
    blacklisted_nodes = blacklisted_nodes[:]
    print("")
    courses = 0
    print(f"start_key: {start_key} end_key: {end_key} blacklisted_nodes: {blacklisted_nodes}")

    if start_key in blacklisted_nodes:
        if start_key == "start" or start_key == "end" or len(set(blacklisted_nodes)) != len(blacklisted_nodes):
            print("RETURN Blacklisted route, return 0")
            return 0
    if start_key == end_key:
        print("RETURN Finished route, return 1")
        return 1
    if start_key.islower():
        print("First visit to lowercase, continue...")
        blacklisted_nodes = handle_blacklist(blacklisted_nodes, start_key)

    for end_point in nodes[start_key]:
        current_course.append(start_key)
        courses += find_all_course_combos(end_point, end_key, nodes, blacklisted_nodes, current_course)

    return courses


def main():
    courses = 0
    nodes = get_nodes(input_data)
    print(f"nodes: {nodes}")

    for node, val in nodes.items():
        print(f"node: {node}")
        print(f"val: {val}")
    courses += find_all_course_combos("start", "end", nodes, [], [])
    print(f"Final courses: {courses}")


if __name__ == '__main__':
    main()
