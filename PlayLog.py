import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import search_number_in_text_contant as miner

LIST_LENGTH_TO_PLOT = 100
PLOT_CYCLETIME = 100

def mine_data(input_string, data_to_be_mined):
    converter_obj = miner.TextNumberSearcher(input_string)
    converter_obj.set_text_to_be_find(data_to_be_mined)
    converter_obj.generate_sum_and_array()
    return converter_obj
   

file_to_read = open("logs/putty.log", "r")
strings_to_be_mined_list = ["Ro", "Po", "Ri", "Pi", "M1", "M2", "M3","M4"]
plot_data_dict = {}
mined_data_dict = {}
fig, ax = plt.subplots()

def animate(i):

    mine_currectcycle_data()
    sort_mined_data_for_plot()
    plot_data()

def plot_data():
    ax.cla()
    for key in plot_data_dict:
        ax.plot(plot_data_dict[key], label=key)
        ax.legend()

def sort_mined_data_for_plot():
    for key in mined_data_dict:
        if key in plot_data_dict:
            plot_data_dict[key] = plot_data_dict[key] + mined_data_dict[key].get_element_list()
        else:
            plot_data_dict[key] = mined_data_dict[key].get_element_list()
        if len(plot_data_dict[key]) > LIST_LENGTH_TO_PLOT:
            del plot_data_dict[key][0:(len(plot_data_dict[key]) - LIST_LENGTH_TO_PLOT)]

def mine_currectcycle_data():
    string_needs_to_be_mined_from = file_to_read.read().split("\n")
    for strings_to_be_mined in strings_to_be_mined_list:
        mined_data_dict[strings_to_be_mined] = mine_data(string_needs_to_be_mined_from, strings_to_be_mined)

animation = FuncAnimation(fig, animate, interval = PLOT_CYCLETIME)

plt.tight_layout()
plt.show()
file_to_read.close()
