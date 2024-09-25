import customtkinter

def lab(tab):
	button_frame = customtkinter.CTkFrame(master=tab)
 
	button_frame.pack( padx=20, pady=20, fill=customtkinter.X,side=customtkinter.TOP)
	return button_frame