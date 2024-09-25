import customtkinter
from data.data import ciphers_names_lab_1
from data.data import ciphers_names_lab_2
from lab.lab import lab
from helpers.helpers import getMethodButtons
from data.data import menu_case_lab_1
from data.data import menu_case_lab_2

input_value = ''

def interface():
  
    
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    root = customtkinter.CTk()
    root.geometry("500x750")
    label_frame = customtkinter.CTkFrame(master=root)
    tab_menu = customtkinter.CTkTabview(master=root)
    tab_1 = tab_menu.add('Lab-1')
    tab_2 = tab_menu.add('Lab-2')
    

    label_frame.pack(padx=20, pady=20, fill=customtkinter.X,side=customtkinter.TOP)
    label = customtkinter.CTkLabel(master=label_frame,text="NNcryption",font=("",32))
    label.pack(padx=20, pady=20)
    tab_menu.pack( padx=20, pady=20, fill=customtkinter.X,side=customtkinter.TOP)
    
    lab_1= lab(tab_1)
    lab_2= lab(tab_2)
    getMethodButtons(ciphers_names_lab_1,lab_1,menu_case_lab_1)
    getMethodButtons(ciphers_names_lab_2,lab_2,menu_case_lab_2)
    

    

    
   
    


    
    root.mainloop()


