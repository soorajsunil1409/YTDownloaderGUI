from tkinter import *

class Downloader(Tk):
    def __init__(self):
        super().__init__()
        self.title("Video Downloader")
        self.geometry("600x600")

        self.mainloop()

if __name__ == "__main__":
    app = Downloader()