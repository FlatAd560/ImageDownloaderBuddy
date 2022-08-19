from asyncore import loop
from google_images_download import google_images_download
from cProfile import label
from timeit import repeat
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from pygame import TEXTINPUT
from bing_image_downloader import downloader
class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.greeting = Label(
            text="type what you want, after, check out the  >data source< or >downloads< folder from where you saved the app!",
            font_size = 16,
            color = '#808000'
            )
        self.window.add_widget(self.greeting)
        self.user = TextInput(
            multiline=False,
            padding_y = (20, 20),
            size_hint = (1, 0.5)
            )
        self.window.add_widget(self.user)
        self.Button = Button(
            text="enter",
            size_hint = (1, 0.5),
            bold = True,
            background_color = '#808000',
            background_normal = "#fb4570"
            )
        
        self.Button.bind(on_press=self.callback)
        self.window.add_widget(self.Button)
        return self.window
    
    def callback(self, instance):
        response = google_images_download.googleimagesdownload()
        arguments = {"keywords": self.user.text, "print_urls":False, "adult_filter_on" : True }
        paths = response.download(arguments)
        print(paths)
        downloader.download(self.user.text,output_dir='dataset',adult_filter_off=False, force_replace=False)



if __name__ == "__main__":
    SayHello().run()
