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



def format_input(string, rules):
    result = {}
    for key in rules:

        result[]




def main():
    occurences = format_input(test_input_string, smart_rules)

if __name__ == '__main__':
    main()
