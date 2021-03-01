from tkinter import *
from sys import platform
from tkinter import filedialog
import os
import pytube

class Downloader(Tk):
    def __init__(self):
        super().__init__()
        self.title("Tube Downloader")
        self.geometry("600x330")
        self.resizable(False, False)

        icon = PhotoImage(file="icon.png")
        self.iconphoto(True, icon)

        if platform == "darwin":
            self.def_font_size = 22
        elif platform == "win32":
            self.def_font_size = 17

        self.link_str = StringVar()
        self.path_str = StringVar()
        if platform == "darwin":
            self.title_str = StringVar()

        self.init_widgets()
        
        self.mainloop()


    def init_widgets(self):
        self.title = Label(self, text="Tube Downloader", bg="red", height=2, fg="#fff", font=("Helvetica", 35, "bold"))
        self.title.place(height=100, width=600, x=0, y=0)

        self.link_lbl = Label(self, text="Enter video url: ", font=("Helvetica", self.def_font_size, "bold"))
        self.link_lbl.place(width=200, x=0, y=120)

        self.link = Entry(self, width=50, textvariable=self.link_str, font=("Helvetica", self.def_font_size, "bold"))
        self.link.place(width=400, x=190, y=118)

        if platform == "darwin":
            self.title_lbl = Label(self, text="Enter Title: ", font=("Helvetica", self.def_font_size, "bold"))
            self.title_lbl.place(width=235, x=11, y=170)

            self.title = Entry(self, width=50, textvariable=self.title_str, font=("Helvetica", self.def_font_size, "bold"))
            self.title.place(width=400, x=190, y=170)

        self.download_btn = Button(self, text="Download", font=("Helvetica", self.def_font_size, "bold"), command=self.ask_download)
        self.download_btn.place(width=200, height=50, x=200, y=220)

        self.error_lbl = Label(self, text="", font=("Helvetica", self.def_font_size, "bold"))
        self.error_lbl.pack(side=BOTTOM, pady=15)

        self.init_menu()


    def init_menu(self):
        self.menu = Menu(self)

        self.help1 = Menu(self.menu, tearoff=False)
        self.help1.add_command(label="About...", command=self.show_about)

        self.menu.add_cascade(label="Help", menu=self.help1)
        self.config(menu=self.menu)


    def show_about(self):
        about_win = Tk()
        about_win.title("About Me")
        about_win.resizable(False, False)
        if platform == "win32":
            about_win.attributes('-toolwindow', True) # Windows Only
        about_win.geometry("200x200")

        about_win.mainloop()


    def ask_download(self):
        if self.link_str.get() != "":
            self.download_path = filedialog.askdirectory()

            if not self.download_path:
                print("No dld path")
                return

            try:
                yt = pytube.YouTube(self.link_str.get())
            except:
                self.error_lbl.config(text=f"Invalid URL '{self.link_str.get()}'")
                print(self.path_str.get())
                print("Invalid URL")
                return
            try:
                d_video = yt.streams.filter(res="720p")[0]
            except:
                d_video = yt.streams.first()

            if platform == "darwin":
                if self.title_str.get() != "":
                    error = self.dld_video(d_video)
                    if error == "error": return
                else:
                    self.error_lbl.config(text=f"Please enter a title")
                    print("No title") 
                    return
            else:
                error = self.dld_video(d_video)

            if platform == "darwin":
                self.error_lbl.config(text=f"Video '{self.title_str.get()}' downloaded successfully!")
            else:
                self.error_lbl.config(text = "Video downloaded sucessfully!")


    def dld_video(self, d_video):
        try:
            if os.path.exists(f"{self.download_path}/{d_video.title}.mp4"):
                self.error_lbl.config(text="File already exixts")
                return

            d_video.download(self.download_path)

            if platform == "darwin" or platform == "linux":
                path = f"{self.download_path}/{d_video.title}.mp4"
                print(path)
                os.rename(path, f"{self.download_path}/{self.title_str.get()}.mp4")

        except OSError as e:
            self.error_lbl.config(text="Error in downloading the video")
            print("OS Error")
            return "error"


if __name__ == "__main__":
    app = Downloader()