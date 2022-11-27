input_string = "PFVKOBSHPSPOOOCOOHBP"

rules = {"FV": "C",
         "CP": "K",
         "FS": "K",
         "VF": "N",
         "HN": "F",
         "FF": "N",
         "SS": "K",
         "VS": "V",
         "BV": "F",
         "HC": "K",
         "BP": "F",
         "OV": "N",
         "BF": "V",
         "VH": "V",
         "PF": "N",
         "FC": "S",
         "CS": "B",
         "FK": "N",
         "VK": "H",
         "FN": "P",
         "SH": "V",
         "CV": "K",
         "HP": "K",
         "HO": "C",
         "NO": "V",
         "CK": "C",
         "VB": "S",
         "OC": "N",
         "NS": "C",
         "NF": "H",
         "SF": "N",
         "NK": "S",
         "NP": "P",
         "OO": "S",
         "NH": "C",
         "BC": "H",
         "KS": "H",
         "PV": "O",
         "KO": "K",
         "OK": "H",
         "OH": "H",
         "BH": "F",
         "NB": "B",
         "FH": "N",
         "HV": "F",
         "BN": "S",
         "ON": "V",
         "CB": "V",
         "CF": "H",
         "FB": "S",
         "KF": "S",
         "PS": "P",
         "OB": "C",
         "NN": "K",
         "KV": "C",
         "BK": "H",
         "SN": "S",
         "NC": "H",
         "PK": "B",
         "PC": "H",
         "KN": "S",
         "VO": "V",
         "FO": "K",
         "CH": "B",
         "PH": "N",
         "SO": "C",
         "KH": "S",
         "HB": "V",
         "HH": "B",
         "BB": "H",
         "SC": "V",
         "HS": "K",
         "SP": "V",
         "KB": "N",
         "VN": "H",
         "HK": "H",
         "KP": "K",
         "OP": "F",
         "CO": "B",
         "VP": "H",
         "OS": "N",
         "OF": "H",
         "KK": "N",
         "CC": "K",
         "BS": "C",
         "VV": "O",
         "CN": "H",
         "PB": "P",
         "BO": "N",
         "SB": "H",
         "FP": "F",
         "SK": "F",
         "PO": "S",
         "KC": "H",
         "VC": "H",
         "NV": "N",
         "HF": "B",
         "PN": "F",
         "SV": "K",
         "PP": "K"
         }


_smart_rules = {"FV": "C",
               "CP": "K",
               "FS": "K",
               "VF": "N",
               "HN": "F",
               "FF": "N",
               "SS": "K",
               "VS": "V",
               "BV": "F",
               "HC": "K",
               "BP": "F",
               "OV": "N",
               "BF": "V",
               "VH": "V",
               "PF": "N",
               "FC": "S",
               "CS": "B",
               "FK": "N",
               "VK": "H",
               "FN": "P",
               "SH": "V",
               "CV": "K",
               "HP": "K",
               "HO": "C",
               "NO": "V",
               "CK": "C",
               "VB": "S",
               "OC": "N",
               "NS": "C",
               "NF": "H",
               "SF": "N",
               "NK": "S",
               "NP": "P",
               "OO": "S",
               "NH": "C",
               "BC": "H",
               "KS": "H",
               "PV": "O",
               "KO": "K",
               "OK": "H",
               "OH": "H",
               "BH": "F",
               "NB": "B",
               "FH": "N",
               "HV": "F",
               "BN": "S",
               "ON": "V",
               "CB": "V",
               "CF": "H",
               "FB": "S",
               "KF": "S",
               "PS": "P",
               "OB": "C",
               "NN": "K",
               "KV": "C",
               "BK": "H",
               "SN": "S",
               "NC": "H",
               "PK": "B",
               "PC": "H",
               "KN": "S",
               "VO": "V",
               "FO": "K",
               "CH": "B",
               "PH": "N",
               "SO": "C",
               "KH": "S",
               "HB": "V",
               "HH": "B",
               "BB": "H",
               "SC": "V",
               "HS": "K",
               "SP": "V",
               "KB": "N",
               "VN": "H",
               "HK": "H",
               "KP": "K",
               "OP": "F",
               "CO": "B",
               "VP": "H",
               "OS": "N",
               "OF": "H",
               "KK": "N",
               "CC": "K",
               "BS": "C",
               "VV": "O",
               "CN": "H",
               "PB": "P",
               "BO": "N",
               "SB": "H",
               "FP": "F",
               "SK": "F",
               "PO": "S",
               "KC": "H",
               "VC": "H",
               "NV": "N",
               "HF": "B",
               "PN": "F",
               "SV": "K",
               "PP": "K"
               }


test_input_string = "NNCB"

smart_rules = {"CH": "B",
               "HH": "N",
               "CB": "H",
               "NH": "C",
               "HB": "C",
               "HC": "B",
               "HN": "C",
               "NN": "C",
               "BH": "H",
               "NC": "B",
               "NB": "B",
               "BN": "B",
               "BB": "N",
               "BC": "B",
               "CC": "N",
               "CN": "C"}


def get_queue(string):
    queue = []
    for i in range(0, len(string)):
        #print(f"data_string[i]: {string[i]}")
        if i > 0:
            queue.append(string[i-1] + string[i])
    return queue

def get_unique_queue(string):
    queue = []
    unique_queue = {}
    for i in range(0, len(string)):
        if i > 0:
            queue.append(string[i-1] + string[i])

    for el in queue:
        if el in unique_queue:
            unique_queue[el] += 1
        else:
            unique_queue[el] = 1

    return unique_queue

def get_smart_unique_queue(rules):
    unique_queue = {}
    for key in rules:
        unique_queue[key] = 0

    return unique_queue

def apply_rules(queue, rules):
    result = []
    last_segment = ""
    for s in queue:
        last_segment = s
        for rule in rules:
            for key, val in rule.items():
                if s == key:
                    string_list = list(s[0] + val) # Skipping last since it's part of next segment...
                    result.extend(string_list)
    # since skipping last segment every loop but stopping 1 from last last segment must be readded before return
    result.extend(last_segment[1])
    return result


def apply_rules_smarter(queue, rules_dict):
    result = []
    last_segment = queue[-1]

    for s in queue:
        #print(f"s: {s}")

        string_list = list(s[0] + rules_dict[s]) # Skipping last since it's part of next segment...
        result.extend(string_list)

    # since skipping last segment every loop but stopping 1 from last last segment must be readded before return
    result.extend(last_segment[1])
    #print("3")

    return result


def print_totals(unique_queue, last_char):
    totals = {}
    totals[last_char] = 1
    for key, val in unique_queue.items():
        if key[0] in totals:
            totals[key[0]] += val
        else:
            totals[key[0]] = val

    #print(f"totals: {totals}")

    #print(f"max(*[v for k, v in totals.items()]): {max(*[v for k, v in totals.items()])}")
    #print(f"min(*[v for k, v in totals.items()]): {min(*[v for k, v in totals.items()])}")

    total = max(*[v for k, v in totals.items()]) - min(*[v for k, v in totals.items()])
    print(f"total: {total}")


def apply_rules_even_smarter(unique_queue, rules_dict):
    #print(f"unique_queue: {unique_queue}")
    #print(f"rules_dict: {rules_dict}")



    unique_result = {}

    for key in unique_queue:
        if unique_queue[key] == 0:
            continue

        val = unique_queue[key]

        #if (key[0] + rules_dict[key]) in unique_queue:
        #    val_1 = unique_queue[key[0] + rules_dict[key]]
        #if (rules_dict[key] + key[1]) in unique_queue:
        #    val_2 = unique_queue[rules_dict[key] + key[1]]

        #print(f"{val}:{key} evolves to {val}:{key[0] + rules_dict[key]} and {val}:{rules_dict[key] + key[1]}")

        if (key[0] + rules_dict[key]) in unique_result:
            unique_result[key[0] + rules_dict[key]] += val
        else:
            unique_result[key[0] + rules_dict[key]] = val

        if (rules_dict[key] + key[1]) in unique_result:
            unique_result[rules_dict[key] + key[1]] += val
        else:
            unique_result[rules_dict[key] + key[1]] = val

    return unique_result


def get_unique_chars(string):
    #print(f"string: {string}")

    unique = set()
    for char in string:
        if char != " ":
            #print(f"Adding char: {char}")
            unique.add(char)

    return unique


def calculate_total(string, unique_chars):
    unique_values = {}
    for char in unique_chars:
        for element in string:
            if element == char:
                if char in unique_values:
                    unique_values[char] += 1
                else:
                    unique_values[char] = 1
    #print(f"unique_values: {unique_values}")
    return unique_values





def main():
    working_string = test_input_string

    unique_queue = get_smart_unique_queue(rules)
    # Initiate:
    unique_queue["PF"] += 1
    unique_queue["FV"] += 1
    unique_queue["VK"] += 1
    unique_queue["KO"] += 1
    unique_queue["OB"] += 1
    unique_queue["BS"] += 1
    unique_queue["SH"] += 1
    unique_queue["HP"] += 1
    unique_queue["PS"] += 1
    unique_queue["SP"] += 1
    unique_queue["PO"] += 1
    unique_queue["OO"] += 1
    unique_queue["OO"] += 1
    unique_queue["OC"] += 1
    unique_queue["CO"] += 1
    unique_queue["OO"] += 1
    unique_queue["OH"] += 1
    unique_queue["HB"] += 1
    unique_queue["BP"] += 1
    last_char = "P"
    for i in range(1, 10000):
        #print("")
        #print(f"Step: {i}")
        #print(f"input: {unique_queue}")

        #queue = get_queue(working_string)
        #print(f"queue: {queue}")

        #print(f"unique_queue: {unique_queue}")

        # working_string = apply_rules(queue, rules)
        #working_string = apply_rules_smarter(queue, smart_rules)

        unique_queue = apply_rules_even_smarter(unique_queue, rules)
        #print(f"output: {unique_queue}")
        #print("NC CN NB BC CH HB")
        #print("NB:2 BC:2 CC:1 CN:1 BB:2 CB:2 BH:1 HC:1")


        #print(f"result: {working_string}")



    #unique_chars = get_unique_chars(working_string)
    #print(f"unique_chars: {unique_chars}")
    #
    #totals = calculate_total(working_string, unique_chars)
    #
    #print(f"max(*[v for k, v in totals.items()]): {max(*[v for k, v in totals.items()])}")
    #print(f"min(*[v for k, v in totals.items()]): {min(*[v for k, v in totals.items()])}")
    #
    #
    #total = max(*[v for k, v in totals.items()]) - min(*[v for k, v in totals.items()])
    #print(f"total: {total}")

    print_totals(unique_queue, last_char)

if __name__ == '__main__':
    main()
