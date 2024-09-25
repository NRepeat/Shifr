import customtkinter
from ciphers.magic_square import create_magic_square_3x3
from ciphers.magic_square import create_magic_square_4x4

def perform_cipher(method,text,shift,key,slug,square):
    print('key',key)
    print('shift',shift)
    if slug == 'magic_square' and square:
        return method['cipher'](text,square)
    if shift == 0 and key=='':
        return method['cipher'](text)
    if key !=0 or key !='' or key !=None:
        return method['cipher'](text,key)
   
   
    else:
        return method['cipher'](text, shift)
def perform_decipher(method, text, shift,key,slug,square):
    
    if slug == 'magic_square':
        return method['cipher'](text,square)
    if shift == 0 and key=='':
        return method['decipher'](text)
    if key !=0 or key !=None:
        return method['decipher'](text,key)
    
    else:
        return method['decipher'](text, shift)  
def choose_method(input_value):
    while True:
        method = input_value
        if method == True:
            return perform_cipher
        elif method == False:
            return perform_decipher
def button_callback(value,cipher):
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
        
        encrypt_button = customtkinter.CTkButton(master=entry_frame, text='Encrypt', command=lambda isEncrypt =True  : submit_callback(isEncrypt), height=38)
        decrypt_button = customtkinter.CTkButton(master=entry_frame, text='Decrypt', command=lambda isEncrypt =False : submit_callback(isEncrypt), height=38)
      
       
        if(input_value==5):{
           decrypt_button.destroy() 
        }
        def submit_callback(isEncrypt):
            nonlocal result_widget
            method = choose_method(isEncrypt)  
            input_text = entry_text.get()

            if input_value == 0 and cipher['slug'] == 'caesar':  
                entry_shift_value = int(entry_shift.get())  
                result = method(cipher, input_text, entry_shift_value,entry_key,'',0)
            elif cipher['slug'] == 'magic_square':
                print(is3Square.get())
                print(cipher['slug'])
                if is3Square.get() == 1:
                    square = create_magic_square_3x3()
                else:
                    square = create_magic_square_4x4()
                result = method(cipher, input_text, entry_shift,entry_key,'magic_square',square)
            elif input_value in (2, 3, 6):  
                entry_key_value = entry_key.get()  
                print('asdassd',entry_key_value)
                result = method(cipher, input_text, entry_shift,entry_key_value,'',0)     
            else:
                result = method(cipher, input_text, 0,'', 0,'') 
                
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

        print(input_value)
        if input_value == 0 and cipher['slug'] == 'caesar':
            entry_shift = customtkinter.CTkEntry(master=entry_frame, placeholder_text="Enter shift (for Caesar cipher):", height=50)
            entry_shift.pack(padx=10, pady=10, fill=customtkinter.X) 
        elif input_value in (2, 3, 7):
            entry_key = customtkinter.CTkEntry(master=entry_frame, placeholder_text="Enter key: ", height=50)
            entry_key.pack(padx=10, pady=10, fill=customtkinter.X) 
        elif cipher['slug'] == 'magic_square':
             is3Square = customtkinter.CTkCheckBox(master=entry_frame, text='3x3')
             is4Square = customtkinter.CTkCheckBox(master=entry_frame, text='4x4')
             
             is3Square.pack()
             is4Square.pack()
        else:
            entry_shift = None  
            entry_key = None

        encrypt_button.pack(pady=10)  
        decrypt_button.pack(pady=10) 
        result_widget_frame.pack_propagate(False) 
        text_input.focus()
        
def getMethodButtons(ciphers_names,frame,menu_case):
        
        for i,name in enumerate(ciphers_names):
            button = customtkinter.CTkButton(master=frame, text=name, command=lambda name=i: button_callback(name,menu_case[name] ),height=38)
            button.pack(padx=20, pady=20, fill=customtkinter.X,side=customtkinter.TOP)