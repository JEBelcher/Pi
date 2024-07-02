import tkinter as tk
import subprocess
import os,sys
class App:

    def __init__(self, master):
        self.master = master
        self.label = tk.Label(master, text="", width=10)
        self.label.pack()
        self.update_temp()


    def update_temp(self):
        # use global variable
        global my_text
        temp = self.get_cpu_temp()
        root.title(" "+temp+ " c")
        my_text = temp + " c"
        self.label.config(text=my_text)
        self.master.after(5000, self.update_temp)                

    def get_cpu_temp(self):
        temp = subprocess.check_output(['vcgencmd', 'measure_temp']).decode('utf-8')
        return temp.replace("temp=","").replace("'C\n","")

root = tk.Tk()
program_directory=sys.path[0]
root.iconphoto(True, tk.PhotoImage(file=os.path.join(program_directory, "thermometer.png")))
root.geometry("100x30+0+0")
root.wm_attributes("-topmost", 1)
root.resizable(False,False)
app = App(root)
root.iconify()
root.mainloop()