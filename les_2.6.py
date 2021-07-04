n = int(input("Сколько всего\n"))
all_data = []
with_data = {}
for i in range(n):
    this_dict = {}
    quan_of_char = int(input("Сколько характеристик?\n"))
    for cycle in range(quan_of_char):
        start_v = input("Название характеристики\n")
        end_v = input("Параметр характеристики\n")
        this_dict[start_v] = end_v

        if start_v not in with_data.keys():
            with_data[start_v] = [end_v]
        else:
            with_data[start_v].append(end_v)

    all_data.append(tuple([i + 1, this_dict]))

#print(all_data)
for key, value in with_data.items():
    with_data[key] = list(set(value))
print("Информация - ", with_data)


