import subprocess
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(padx=20, pady=20)
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self, text="Run Script", command=self.run_script)
        self.hi_there.pack(side="top")

    def run_script(self):
        try:
            output = subprocess.check_output(["python", "C:/Users/esadk/OneDrive/Desktop/Programming/Coderminds/main.py"])
            output_text = output.decode("utf-8")
        except subprocess.CalledProcessError as e:
            output_text = f"Error running script: {e}"
        
        self.output_label = tk.Label(self, text=output_text)
        self.output_label.pack(side="top", padx=10, pady=10)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
