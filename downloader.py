from tkinter import *
import pytube

class Downloader(Tk):
    def __init__(self):
        super().__init__()
        self.title("Video Downloader")
        self.geometry("600x400")
        self.geometry("600x600")

        self.link_str = StringVar()
        self.path_str = StringVar()

        self.init_widgets()
        
        self.mainloop()

    def init_widgets(self):
        title = Label(self, text="Video Downloader", bg="red", height=2, fg="#fff", font=("Helvetica", 35, "bold"))
        title.place(height=100, width=600, x=0, y=0)

        link_lbl = Label(self, text="Enter video link: ", font=("Helvetica", 22, "bold"))
        link_lbl.place(width=200, x=0, y=120)

        link = Entry(text="Enter Link", width=50, textvariable=self.link_str, font=("Helvetica", 22, "bold"))
        link.place(width=400, x=190, y=118)

        path_lbl = Label(self, text="Enter Download Path: ", font=("Helvetica", 22, "bold"))
        path_lbl.place(width=235, x=10, y=170)

        path = Entry(text="Enter Link", width=50, textvariable=self.path_str, font=("Helvetica", 22, "bold"))
        path.place(width=345, x=245, y=168)

class MainLogic:
    def __init__(self):
        gui = Downloader



if __name__ == "__main__":
    app = Downloader()