from asyncore import loop
from google_images_download import google_images_download
from cProfile import label
from timeit import repeat
from bing_image_downloader import downloader
from tkinter import *

def submit():
    dibs = entry.get()
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords": dibs, "print_urls":True, "adult_filter_on" : True }
    paths = response.download(arguments)
    print(paths)
    downloader.download(dibs,output_dir='dataset',adult_filter_off=False, force_replace=False)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)
window = Tk()
window.title("Main Window")
submit = Button(window, text="Download", command=submit)
delete = Button(window, text="Delete", command=delete)
backspace = Button(window, text="Backspace", command=backspace)
submit.pack(side = RIGHT)
delete.pack(side = RIGHT)
backspace.pack(side = RIGHT)
entry = Entry()
entry.config(font=('Ink Free', 50))
entry.config(bg='#00ff00')
entry.config(width=10)
entry.pack()
window.mainloop()

    