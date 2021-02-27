from tkinter import *
from tkinter import filedialog
import pytube

class Downloader(Tk):
    def __init__(self):
        super().__init__()
        self.title("Video Downloader")
        self.geometry("600x330")

        self.link_str = StringVar()
        self.path_str = StringVar()
        self.title_str = StringVar()

        self.init_widgets()
        
        self.mainloop()

    def init_widgets(self):
        self.title = Label(self, text="Video Downloader", bg="red", height=2, fg="#fff", font=("Helvetica", 35, "bold"))
        self.title.place(height=100, width=600, x=0, y=0)

        self.link_lbl = Label(self, text="Enter video link: ", font=("Helvetica", 22, "bold"))
        self.link_lbl.place(width=200, x=0, y=120)

        self.link = Entry(self, width=50, textvariable=self.link_str, font=("Helvetica", 22, "bold"))
        self.link.place(width=400, x=190, y=118)

        self.title_lbl = Label(self, text="Enter Title: ", font=("Helvetica", 22, "bold"))
        self.title_lbl.place(width=235, x=11, y=170)

        self.title = Entry(self, width=50, textvariable=self.title_str, font=("Helvetica", 22, "bold"))
        self.title.place(width=400, x=190, y=170)

        self.download_btn = Button(self, text="Download", font=("Helvetica", 22, "bold"), command=self.ask_download)
        self.download_btn.place(width=200, height=50, x=200, y=220)

        self.error_lbl = Label(self, text="", font=("Helvetica", 22, "bold"))
        self.error_lbl.pack(side=BOTTOM, pady=15)


    def ask_download(self):
        if self.path_str != "":
            download_path = filedialog.askdirectory(title="Download")

            if not download_path:
                return

            try:
                yt = pytube.YouTube()
            except:
                self.error_lbl.config(text="Connection error")
                return

        mp4files = yt.filter('mp4')

        if self.title_str != "":
            yt.set_filename(self.title_str)
        
        



if __name__ == "__main__":
    app = Downloader()