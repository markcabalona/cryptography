import tkinter as tk
import numpy as np
import decipher0 as dcp

def main():
    win = tk.Tk()
    win.title("Application of Matrices in Cryptography")
    win.geometry("400x250")


    menu = My_app(win).display_menu()

    
    

    win.mainloop()


class My_app():
    def __init__(self,win):
        self.mode = ""
        #main menu contents
        self.menu_frame = None
        self.win = win
        

        #get_dim frame
        self.dim_frame = None
        #get matrix key frame
        self.mkey_frame = None
        #message_frame
        self.message_frame = None
        #result frame
        self.result_frame = None
        #warning frame
        self.warning_frame = None

    def initialize_frames(self):
        self.menu_frame = tk.Frame(self.win)
        #get_dim frame
        self.dim_frame = tk.Frame(self.win)
        #get matrix key frame
        self.mkey_frame = tk.Frame(self.win)
        #message_frame
        self.message_frame = tk.Frame(self.win)
        #result frame
        self.result_frame = tk.Frame(self.win)
        #warning frame
        self.warning_frame = tk.Frame(self.win)

    
    def display_menu(self,*args):
        self.initialize_frames()

        self.mylabel = tk.Label(self.menu_frame, text= "Welcome!", padx = 10, pady = 20)
        self.encode_button = tk.Button(self.menu_frame, text = "Encode Message", padx = 20, pady = 10,command = lambda: self.ask_dimension(self.dim_frame,"encode"))
        self.decode_button = tk.Button(self.menu_frame, text = "Decode Message", padx = 20, pady = 10,command = lambda: self.ask_dimension(self.dim_frame,"decode"))
        self.quit_button = tk.Button(self.menu_frame, text = "Quit", padx = 20, pady = 10,command = self.win.destroy)
        try:
            self.clear_window(args[0])
            
        except:
            pass
        self.mylabel.grid(row = 0, column = 0)
        self.encode_button.grid(row = 1, column = 0)
        self.decode_button.grid(row = 2, column = 0)
        self.quit_button.grid(row = 3, column = 0)
        self.menu_frame.pack()

    def clear_window(self,frame):
        frame.destroy()

    def ask_dimension(self, frame:tk.Frame, btn:str):
        self.clear_window(self.menu_frame)#clear the previous frame(main menu)
        global mode
        mode = btn

        my_label = tk.Label(frame, text = "Select Matrix Key Dimension")
        my_label.grid(row = 0, column = 0, padx = 25, pady = 20)

        #dropdown menu
        global dim_var
        dim_var = tk.IntVar()
        dim_var.set(1)
        dim_mbutton = tk.OptionMenu(frame, dim_var, 1,2,3,4,5,6)#temporary lang muna haha
        dim_mbutton.grid(row = 1, column = 0, padx = 20, pady = 15, ipadx = 15)

        #next button
        next_button = tk.Button(frame, text = "Next", padx = 20, pady = 10, command = lambda: self.get_matrix_key(self.mkey_frame))
        next_button.grid(row = 2, column = 0, padx = 20, pady = 25, ipadx = 15)
        
        frame.pack()

    def get_matrix_key(self,frame):
        self.clear_window(self.dim_frame)

        my_label = tk.Label(frame, text = "Enter Matrix Key")
        my_label.grid(row = 0, column = 0, padx = 25, pady = 20)

        global mkey_box
        mkey_box = tk.Text(frame, width = dim_var.get()*2 -1, height = dim_var.get(), borderwidth = 5)
        mkey_box.grid(row = 1, column = 0, pady = 10)

        enter_mkey = tk.Button(frame, text = "Translate Message", padx = 10, pady = 10, command = lambda: self.validate_key(self.warning_frame))
        enter_mkey.grid(row = 2, column = 0, pady = 10)


        frame.pack()

    def validate_key(self,frame):
        global key
        key = list(map(int, mkey_box.get(1.0,tk.END).split()))
        key = np.array(key)

        warning = ""
        if np.size(key) != dim_var.get() * dim_var.get():
            warning += f"You chose {dim_var.get()} by {dim_var.get()} as your matrix key dimension.\nBut the matrix key you entered only has {np.size(key)} element/s\n"
            key = np.zeros((1,dim_var.get()*dim_var.get()))

        self.clear_window(self.mkey_frame)
        matrix_key = dcp.Key_matrix(dim_var.get(), key).validate_key()

        if not(np.array_equal(key.flatten(),matrix_key.flatten())):
            warning += f"Invalid Key.\n\n{matrix_key}\n\n this matrix will be used as key."
            warning_label = tk.Label(frame, text = warning)
            warning_label.grid(row = 0, column = 0, pady = 30)

            warning_button = tk.Button(frame, text = "Next", command = lambda: self.get_message(self.message_frame))
            warning_button.grid(row = 1, column = 0, pady = 10)
            frame.pack()

        else:
            frame.pack()
            self.get_message(self.message_frame)

        



    def get_message(self,frame):
        
        
        self.clear_window(self.warning_frame)

        my_label = tk.Label(frame, text = "Enter Message")
        my_label.grid(row = 0, column = 0, pady = 20)

        global message_box
        message_box = tk.Text(frame, width = 25, height = 2, borderwidth = 5)
        message_box.grid(row = 1, column = 0, pady = 10)

        

        enter_message = tk.Button(frame, text = "Translate Message", padx = 10, pady = 10, command = lambda: self.show_result(self.result_frame))
        enter_message.grid(row = 2, column = 0, pady = 10)

        frame.pack()
    
    def show_result(self,frame):

        #para to sa kung paano babasahin yung message
        #pag encode yung mode meaning alphabet yung ineexpect
        #pag decode naman, numbers yung laman ng message box(ilalagay sa list)
        if mode.lower() == "encode":
            message = message_box.get(1.0, tk.END)
            message = message.rstrip("\n")
            
        else:
            message = list(map(int, message_box.get(1.0,tk.END).split()))
            message = np.array(message)
            
        print(message)
        self.clear_window(self.message_frame)#clear the previous frame(main menu)


        matrix_key = dcp.Key_matrix(dim_var.get(), key)
        translator = dcp.Translator(matrix_key, message)
        
        #this decides which method to use(encode or decode)
        result = translator.encode() if mode.lower() == "encode" else translator.decode()

        my_label = tk.Label(frame, text = f"Success\n\n{result}")
        my_label.grid(row = 0, column = 0, pady = 20)

        enter_message = tk.Button(frame, text = "Go back to main menu", padx = 10, pady = 10, command = lambda:self.display_menu(self.result_frame))
        enter_message.grid(row = 2, column = 0, pady = 10)

        frame.pack()




    
        
        

        

if __name__ == "__main__":
    main()