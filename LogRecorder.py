import matplotlib.pyplot as plt
import search_number_in_text_contant as miner



def mine_controller_data(file_to_read):
    input_string = file_to_read.read().split("\n")
    converter_obj_Pic_in = miner.TextNumberSearcher(input_string)
    converter_obj_Pic_in.set_text_to_be_find("Pi")
    converter_obj_Pic_in.generate_sum_and_array()

    converter_obj_Rol_in = miner.TextNumberSearcher(input_string)
    converter_obj_Rol_in.set_text_to_be_find("Ri")
    converter_obj_Rol_in.generate_sum_and_array()

    converter_obj_Pic_out = miner.TextNumberSearcher(input_string)
    converter_obj_Pic_out.set_text_to_be_find("Po")
    converter_obj_Pic_out.generate_sum_and_array()

    converter_obj_Rol_out = miner.TextNumberSearcher(input_string)
    converter_obj_Rol_out.set_text_to_be_find("Ro")
    converter_obj_Rol_out.generate_sum_and_array()
    return input_string,converter_obj_Pic_in,converter_obj_Rol_in,converter_obj_Pic_out,converter_obj_Rol_out


def mine_motor_data(input_string):
    converter_obj_motor_1 = miner.TextNumberSearcher(input_string)
    converter_obj_motor_1.set_text_to_be_find("M1")
    converter_obj_motor_1.generate_sum_and_array()

    converter_obj_motor_2 = miner.TextNumberSearcher(input_string)
    converter_obj_motor_2.set_text_to_be_find("M2")
    converter_obj_motor_2.generate_sum_and_array()

    converter_obj_motor_3 = miner.TextNumberSearcher(input_string)
    converter_obj_motor_3.set_text_to_be_find("M3")
    converter_obj_motor_3.generate_sum_and_array()

    converter_obj_motor_4 = miner.TextNumberSearcher(input_string)
    converter_obj_motor_4.set_text_to_be_find("M4")
    converter_obj_motor_4.generate_sum_and_array()
    return converter_obj_motor_1,converter_obj_motor_2,converter_obj_motor_3,converter_obj_motor_4


file_to_read = open("logs/putty.log", "r")

input_string, converter_obj_Pic_in, converter_obj_Rol_in, converter_obj_Pic_out, converter_obj_Rol_out = mine_controller_data(file_to_read)
converter_obj_motor_1, converter_obj_motor_2, converter_obj_motor_3, converter_obj_motor_4 = mine_motor_data(input_string)

file_to_read.close()
fig, ax = plt.subplots()

ax.plot(converter_obj_Pic_in.get_element_list(), linestyle = "-", color = "black", label="Pic in")
ax.plot(converter_obj_Rol_in.get_element_list(), linestyle = "--", color = "blue", label="Roll in")
ax.plot(converter_obj_Pic_out.get_element_list(), linestyle = "-.", color = "green", label="Pic out")
ax.plot(converter_obj_Rol_out.get_element_list(), linestyle = ":", color = "red", label="Roll out")
ax.plot(converter_obj_motor_1.get_element_list(), linestyle = "-.", color = "darkmagenta", label="Motor 1")
ax.plot(converter_obj_motor_2.get_element_list(), linestyle = ":", color = "fuchsia", label="Motor 2")
ax.plot(converter_obj_motor_3.get_element_list(), linestyle = ":", color = "gray", label="Motor 3")
ax.plot(converter_obj_motor_4.get_element_list(), linestyle = ":", color = "darkgreen", label="Motor 4")

ax.legend()
plt.show()
