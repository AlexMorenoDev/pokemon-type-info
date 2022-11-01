from variables import pokemon_types, pokemon_types_table

def get_atk_s_w(pkm_type):
    strengths = []
    weaknesses = []
    unaffected = []

    i = 0
    for value in pokemon_types_table[pkm_type]:
        if value == 2:
            strengths.append(pokemon_types[i])
        elif value == 0.5:
            weaknesses.append(pokemon_types[i])
        elif value == 0:
            unaffected.append(pokemon_types[i])
        
        i += 1

    return strengths, weaknesses, unaffected

def get_def_s_w(pkm_type):
    strengths = []
    weaknesses = []
    unaffected = []

    index = pokemon_types.index(pkm_type)
    for key, value in pokemon_types_table.items():
        if value[index] == 2:
            weaknesses.append(key)
        elif value[index] == 0.5:
            strengths.append(key)
        elif value[index] == 0:
            unaffected.append(key)

    return strengths, weaknesses, unaffected

def main():
    target = None
    pokemon_types_set = set(pokemon_types)
    print(pokemon_types)
    while target not in pokemon_types_set:
        print('Introduce el tipo de pokemon que quieres consultar:')
        target = input()


    atk_strengths, atk_weaknesses, atk_unaffected = get_atk_s_w(target)
    def_strengths, def_weaknesses, def_unaffected = get_def_s_w(target)
    print("Tipo '{}':".format(target))
    print("\t- Ataque:")
    print("\t\t- Muy eficaz contra: {}".format(atk_strengths))
    print("\t\t- Poco eficaz contra: {}".format(atk_weaknesses))
    print("\t\t- No afecta a: {}".format(atk_unaffected))
    print("\t- Defensa:")
    print("\t\t- Le afecta poco: {}".format(def_strengths))
    print("\t\t- Le afecta mucho: {}".format(def_weaknesses))
    print("\t\t- Inmune contra: {}".format(def_unaffected))

if __name__ == "__main__":
    main()