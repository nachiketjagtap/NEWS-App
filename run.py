import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image
class NewsApp:
    def __init__(self):
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=0b5f016413dd45cdb800cb781669752c').json()

        self.load_gui()

        self.load_news_item(5)




    def load_gui(self):
        self.root=Tk()
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.configure(background='black')


    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
    def load_news_item(self,index):

        self.clear()

        img_url = self.data['articles'][index]['urlToImage']
        raw_data = urlopen(img_url).read()
        im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
        photo = ImageTk.PhotoImage(im)

        label=Label(self.root,image=photo)
        label.pack()




        heading = Label(self.root,text=self.data['articles'][index]['title'],bg='black',fg='white',wraplength=350,justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',15))

        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white', wraplength=350,
                        justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))

        frame = Frame(self.root,bg='black')
        frame.pack(expand=True,fill=BOTH)

        prev = Button(frame,text='Prev',width=16,height=3)
        prev.pack(side=LEFT)

        more = Button(frame, text='Read More', width=16, height=3)
        more.pack(side=LEFT)

        next = Button(frame, text='Next', width=16, height=3)
        next.pack(side=LEFT)




        self.root.mainloop()




obj = NewsApp()