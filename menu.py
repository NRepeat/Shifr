import customtkinter
from data.data import ciphers_names
from data.data import menu_case
from helpers.helpers import choose_method


input_value = ''

def interface():
  
    
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    root = customtkinter.CTk()
    root.geometry("500x750")
    root.grid_columnconfigure((0, 1), weight=1)
    # root.grid_rowconfigure(0, weight=1)
    button_frame = customtkinter.CTkFrame(master=root)
    
    label_frame = customtkinter.CTkFrame(master=root)
 
    label_frame.pack(padx=20, pady=20, fill=customtkinter.X,side=customtkinter.TOP)
    label = customtkinter.CTkLabel(master=label_frame,text="NNcryption",font=("",32))
    label.pack(padx=20, pady=20)
    button_frame.pack( padx=20, pady=20, fill=customtkinter.X,side=customtkinter.TOP)
    def button_callback(value):
        entry_key = ''
        entry_shift = 0
        input_value = value
        text_input = customtkinter.CTkToplevel()
        text_input.geometry("500x450")

        entry_frame = customtkinter.CTkFrame(master=text_input)
        entry_frame.pack(padx=20, pady=20, fill=customtkinter.BOTH, expand=True)  

        
        result_widget_frame = customtkinter.CTkFrame(master=text_input, height=200)
        result_widget_frame.pack(padx=20, pady=20, fill=customtkinter.BOTH, expand=True) 
        result_widget = None
        cipher = menu_case[input_value] 
        encrypt_button = customtkinter.CTkButton(master=entry_frame, text='Encrypt', command=lambda isEncrypt =True  : submit_callback(isEncrypt), height=38)
        decrypt_button = customtkinter.CTkButton(master=entry_frame, text='Decrypt', command=lambda isEncrypt =False : submit_callback(isEncrypt), height=38)
      
       
        if(input_value==5):{
           decrypt_button.destroy() 
        }
        def submit_callback(isEncrypt):
            nonlocal result_widget
            method = choose_method(isEncrypt)  
            print(method)
            print(input_value)
            input_text = entry_text.get()
            if input_value == 0:  
                entry_shift_value = int(entry_shift.get())  
                result = method(cipher, input_text, entry_shift_value,entry_key)
            elif input_value in (2, 3, 6):  
                entry_key_value = entry_key.get()  
                print(entry_key_value)
                result = method(cipher, input_text, entry_shift,entry_key_value)
            else:
                result = method(cipher, input_text, 0,'') 
            if result_widget is not None:
                    result_widget.destroy()
                
            result_widget = customtkinter.CTkTextbox(master=result_widget_frame, height=100, font=("", 24))  
            result_widget.configure("center")
            result_widget.insert("0.0", result + '\n')  
            result_widget.tag_add("center", "1.0", "end")  
            result_widget.pack(padx=10, pady=10, fill=customtkinter.BOTH, expand=True)  
            result_widget.configure(state='disabled')

        
        entry_text = customtkinter.CTkEntry(master=entry_frame, placeholder_text="Text to encrypt", height=50)
        entry_text.pack(padx=10, pady=10, fill=customtkinter.X) 

        
        if input_value == 0:
            entry_shift = customtkinter.CTkEntry(master=entry_frame, placeholder_text="Enter shift (for Caesar cipher):", height=50)
            entry_shift.pack(padx=10, pady=10, fill=customtkinter.X) 
        elif input_value in (2, 3, 6):
            entry_key = customtkinter.CTkEntry(master=entry_frame, placeholder_text="Enter key: ", height=50)
            entry_key.pack(padx=10, pady=10, fill=customtkinter.X) 
        else:
            entry_shift = None  
            entry_key = None

        encrypt_button.pack(pady=10)  
        decrypt_button.pack(pady=10) 
        result_widget_frame.pack_propagate(False) 
        text_input.focus()
    
    for i,name in enumerate(ciphers_names):
        button = customtkinter.CTkButton(master=button_frame, text=name, command=lambda name=i: button_callback(name),height=38)
        button.pack( padx=20, pady=20, fill=customtkinter.X,side=customtkinter.TOP)
    

    
   
    


    
    root.mainloop()


