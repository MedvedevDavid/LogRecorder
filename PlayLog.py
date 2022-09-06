import matplotlib.pyplot as plt
import search_number_in_text_contant as miner



def mine_data(file_to_read, list_of_texts):
    input_string = file_to_read.read().split("\n")
    return_list = []
    for text_to_be_searched in list_of_texts:
        return_list.append (miner.TextNumberSearcher(input_string))
        return_list[-1].set_text_to_be_find(text_to_be_searched)
        return_list[-1].generate_sum_and_array()
        


    return return_list



data_to_be_mined = ["sig1", "sig2", "sig3"]
file_to_read = open("logs/log.txt", "r")

list_of_mined_data = mine_data(file_to_read,data_to_be_mined)


file_to_read.close()
fig, ax = plt.subplots()


for index, data in enumerate(data_to_be_mined):
    ax.plot(list_of_mined_data[index].get_element_list(), label=data)


ax.legend()
plt.show()
