import tkinter as tk
from tkinter import ttk
from Controller import ProteinSystem
from UseCases import RnaManager, DnaManager


class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.frame_switch(MainPage)

    def frame_switch(self, frame):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class MainPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Welcome to the Protein Synthesis Master!") \
            .pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Get the matching DNA pair of a DNA sequence",
                  command=lambda: master.frame_switch(DNAtoDNA)).pack()
        tk.Button(self, text="Convert DNA sequence to its matching mRNA"
                             " sequence",
                  command=lambda: master.frame_switch(DNAtoRNA)).pack()
        tk.Button(self, text="Convert RNA sequence to its "
                             "matching DNA sequence",
                  command=lambda: master.frame_switch(RNAtoDNA)).pack()
        tk.Button(self, text="Find the polypeptide chain for a DNA sequence",
                  command=lambda: master.frame_switch(DNAtoProtein)).pack()


class DNAtoDNA(tk.Frame):
    def __init__(self, master):
        dm = DnaManager()
        rm = RnaManager()
        ps = ProteinSystem(dm, rm)
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Input DNA sequence").pack(side="top", anchor="nw")
        entry = tk.Entry(self, width=15)
        entry.pack()
        label = ttk.Label(self, text="")
        label.pack()
        convert = tk.Button(self, text="Convert",
                            command=lambda:
                            label.config(text=ps.dna_pairing(entry.get())))
        convert.pack()
        tk.Button(self, text="Return to start page",
                  command=lambda: master.frame_switch(MainPage)).pack()


class DNAtoRNA(tk.Frame):
    def __init__(self, master):
        dm = DnaManager()
        rm = RnaManager()
        ps = ProteinSystem(dm, rm)
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Input DNA sequence").pack(side="top", anchor="nw")
        entry = tk.Entry(self, width=15)
        entry.pack()
        label = ttk.Label(self, text="")
        label.pack()
        convert = tk.Button(self, text="Convert",
                            command=lambda:
                            label.config(text=ps.get_mrna(entry.get())))
        convert.pack()
        tk.Button(self, text="Return to start page",
                  command=lambda: master.frame_switch(MainPage)).pack()


class RNAtoDNA(tk.Frame):
    def __init__(self, master):
        dm = DnaManager()
        rm = RnaManager()
        ps = ProteinSystem(dm, rm)
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Input RNA sequence").pack(side="top", anchor="nw")
        entry = tk.Entry(self, width=15)
        entry.pack()
        label = ttk.Label(self, text="")
        label.pack()
        convert = tk.Button(self, text="Convert",
                            command=lambda:
                            label.config(text=ps.get_dna(entry.get())))
        convert.pack()
        tk.Button(self, text="Return to start page",
                  command=lambda: master.frame_switch(MainPage)).pack()


class DNAtoProtein(tk.Frame):
    def __init__(self, master):
        dm = DnaManager()
        rm = RnaManager()
        ps = ProteinSystem(dm, rm)
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Input DNA sequence").pack(side="top", anchor="nw")
        entry = tk.Entry(self, width=15)
        entry.pack()
        label = ttk.Label(self, text="")
        label.pack()
        convert = tk.Button(self, text="Convert",
                            command=lambda:
                            label.config(text=ps.get_protein(entry.get())))
        convert.pack()
        tk.Button(self, text="Return to start page",
                  command=lambda: master.frame_switch(MainPage)).pack()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
