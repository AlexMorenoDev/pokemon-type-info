from variables import pokemon_types_table
from copy import deepcopy


def convert_dict_keys_to_list(pkm_types_table):
    return list(pkm_types_table.keys())


def remove_duplicates_from_list(target_list):
    return list(dict.fromkeys(target_list))


def get_atk_s_w(pkm_type_list, pkm_type):
    strengths = []
    weaknesses = []
    unaffected = []

    i = 0
    for value in pokemon_types_table[pkm_type]:
        if value == 2:
            strengths.append(pkm_type_list[i])
        elif value == 0.5:
            weaknesses.append(pkm_type_list[i])
        elif value == 0:
            unaffected.append(pkm_type_list[i])
        
        i += 1

    return strengths, weaknesses, unaffected


def get_def_s_w(pkm_type_list, pkm_type):
    strengths = []
    weaknesses = []
    unaffected = []

    index = pkm_type_list.index(pkm_type)
    for key, value in pokemon_types_table.items():
        if value[index] == 2:
            weaknesses.append(key)
        elif value[index] == 0.5:
            strengths.append(key)
        elif value[index] == 0:
            unaffected.append(key)

    return strengths, weaknesses, unaffected


def fill_dict(current_dict, target, strengths, weaknesses, unaffected):
    current_dict[target] = []
    current_dict[target].append(strengths)
    current_dict[target].append(weaknesses)
    current_dict[target].append(unaffected)


def show_atk_info(atk_results):
    print("####### ATAQUE #######")
    for key, value in atk_results.items():
        print("Tipo '{}':".format(key))
        print("\t\t- Muy eficaz contra: {}".format(value[0]))
        print("\t\t- Poco eficaz contra: {}".format(value[1]))
        print("\t\t- No afecta a: {}".format(value[2]))
    print("######################")


def show_def_info(def_results):
    print("####### DEFENSA #######")
    pkm_types = convert_dict_keys_to_list(def_results)
    if len(pkm_types) == 1:
        target_type = pkm_types[0]
        print("Tipo '{}':".format(target_type))
        print("\t\t- Le afecta poco: {}".format(def_results[target_type][0]))
        print("\t\t- Le afecta mucho: {}".format(def_results[target_type][1]))
        print("\t\t- Inmune a: {}".format(def_results[target_type][2]))
    else:
        types_to_remove = []

        i, j = 0, 1
        while i < 2:
            for strength in def_results[pkm_types[i]][0]:
                if (strength in def_results[pkm_types[j]][1]) or (strength in def_results[pkm_types[j]][2]):
                    types_to_remove.append(strength)

            for weakness in def_results[pkm_types[i]][1]:
                if (weakness in def_results[pkm_types[j]][0]) or (weakness in def_results[pkm_types[j]][2]):
                    types_to_remove.append(weakness)

            i += 1
            j -= 1

        types_to_remove = remove_duplicates_from_list(types_to_remove)
        updated_def_results = deepcopy(def_results)

        print(def_results)
        print(types_to_remove)
        
        updated_def_results = {key: [[pkm_type for pkm_type in type_info if pkm_type not in types_to_remove] for type_info in value] for key, value in def_results.items()}
        
        print("Tipo '{}' y '{}':".format(pkm_types[0], pkm_types[1]))
        print("\t\t- Le afecta poco: {}".format(remove_duplicates_from_list(updated_def_results[pkm_types[0]][0] + updated_def_results[pkm_types[1]][0])))
        print("\t\t- Le afecta mucho: {}".format(remove_duplicates_from_list(updated_def_results[pkm_types[0]][1] + updated_def_results[pkm_types[1]][1])))
        print("\t\t- Inmune contra: {}".format(remove_duplicates_from_list(def_results[pkm_types[0]][2] + def_results[pkm_types[1]][2])))

    print("######################")


def main():
    pkm_type_list = convert_dict_keys_to_list(pokemon_types_table)
    pkm_types_set = set(pkm_type_list)

    i = 1
    targets = []
    finish = False
    while not finish:
        target = None
        while target not in pkm_types_set:
            print("Introduce el tipo {} del pokemon:".format(i))
            target = input()

        targets.append(target)

        i += 1
        if i > 2:
            finish = True
        else:
            answer = (input("¿El pokemon tiene doble tipo? (S/N)")).lower()
            if answer == 'n':
                finish = True
    
    atk_results = {}
    def_results = {}
    for target in targets:
        atk_strengths, atk_weaknesses, atk_unaffected = get_atk_s_w(pkm_type_list, target)
        fill_dict(atk_results, target, atk_strengths, atk_weaknesses, atk_unaffected)

        def_strengths, def_weaknesses, def_unaffected = get_def_s_w(pkm_type_list, target)
        fill_dict(def_results, target, def_strengths, def_weaknesses, def_unaffected)
    
    show_atk_info(atk_results)
    show_def_info(def_results)


if __name__ == "__main__":
    main()