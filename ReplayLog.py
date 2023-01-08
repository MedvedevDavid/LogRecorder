import matplotlib.pyplot as plt
import search_number_in_text_contant as miner


def mine_data(input_string, data_to_be_mined):
    converter_obj = miner.TextNumberSearcher(input_string)
    converter_obj.set_text_to_be_find(data_to_be_mined)
    converter_obj.generate_sum_and_array()
    return converter_obj


mined_data_dict = {}
file_to_read = open("logs/putty.log", "r")
string_needs_to_be_mined_from = file_to_read.read().split("\n")
strings_to_be_mined_list = ["Ro", "Po", "Ri", "Pi", "M1", "M2", "M3","M4"]

for strings_to_be_mined in strings_to_be_mined_list:
    mined_data_dict[strings_to_be_mined] = mine_data(string_needs_to_be_mined_from, strings_to_be_mined)

file_to_read.close()
fig, ax = plt.subplots()
for key in mined_data_dict:
    ax.plot(mined_data_dict[key].get_element_list(), label=key)

ax.legend()
plt.show()
