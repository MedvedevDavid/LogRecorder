import matplotlib.pyplot as plt
import search_number_in_text_contant as miner


file_to_read = open("putty20220427171405.txt", "r")

input_string = file_to_read.read().split("\n")
converter_obj_Pic_in = miner.TextNumberSearcher(input_string)
converter_obj_Pic_in.set_text_to_be_find("PIC_in:")
converter_obj_Pic_in.generate_sum_and_array()

converter_obj_Rol_in = miner.TextNumberSearcher(input_string)
converter_obj_Rol_in.set_text_to_be_find("ROL_in:")
converter_obj_Rol_in.generate_sum_and_array()

converter_obj_Pic_out = miner.TextNumberSearcher(input_string)
converter_obj_Pic_out.set_text_to_be_find("PIC_out:")
converter_obj_Pic_out.generate_sum_and_array()

converter_obj_Rol_out = miner.TextNumberSearcher(input_string)
converter_obj_Rol_out.set_text_to_be_find("ROL_out:")
converter_obj_Rol_out.generate_sum_and_array()



converter_obj_Mtr_1 = miner.TextNumberSearcher(input_string)
converter_obj_Mtr_1.set_text_to_be_find("Mtr 1:")
converter_obj_Mtr_1.generate_sum_and_array()

converter_obj_Mtr_2 = miner.TextNumberSearcher(input_string)
converter_obj_Mtr_2.set_text_to_be_find("Mtr 2:")
converter_obj_Mtr_2.generate_sum_and_array()

converter_obj_Mtr_3 = miner.TextNumberSearcher(input_string)
converter_obj_Mtr_3.set_text_to_be_find("Mtr 3:")
converter_obj_Mtr_3.generate_sum_and_array()

converter_obj_Mtr_4 = miner.TextNumberSearcher(input_string)
converter_obj_Mtr_4.set_text_to_be_find("Mtr 4:")
converter_obj_Mtr_4.generate_sum_and_array()

fig, ax = plt.subplots()

ax.plot(converter_obj_Pic_in.get_element_list(), linestyle = "-", color = "black", label="Pic in")
ax.plot(converter_obj_Rol_in.get_element_list(), linestyle = "--", color = "blue", label="Roll in")
ax.plot(converter_obj_Pic_out.get_element_list(), linestyle = "-.", color = "green", label="Pic out")
ax.plot(converter_obj_Rol_out.get_element_list(), linestyle = ":", color = "red", label="Roll out")
ax.plot(converter_obj_Mtr_1.get_element_list(), linestyle = "-.", color = "darkmagenta", label="Motor 1")
ax.plot(converter_obj_Mtr_2.get_element_list(), linestyle = ":", color = "fuchsia", label="Motor 2")
ax.plot(converter_obj_Mtr_3.get_element_list(), linestyle = ":", color = "gray", label="Motor 3")
ax.plot(converter_obj_Mtr_4.get_element_list(), linestyle = ":", color = "darkgreen", label="Motor 4")

ax.legend()
plt.show()

file_to_read.close()