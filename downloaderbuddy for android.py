from cgitb import text
from email.mime import image
import kivy
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.image import Image
from bing_image_downloader import downloader

class downloaderbuddy(MDApp):
    def flip(self):
        print("Downloading")
    
    def download(self, args):
        if bool(downloaderbuddy) == True:
            downloader.download(self.input.text, limit=200 ,adult_filter_off=False, force_replace=False, timeout=60)
            self.label.text = "please check your gallery for your images and don't close the app"
    
    def build(self):
        screen = MDScreen()

        self.toolbar = MDToolbar(title = "Downloader Buddy")
        self.toolbar.pos_hint = {"top": 1}
        screen.add_widget(self.toolbar)
        self.toolbar.right_action_items = [
            ["download", lambda x:self.flip()]]
        screen.add_widget(Image(
            source= 'thelogo.ico' ,
            pos_hint = {"center_x": 0.5, "center_y": 0.8},
            size_hint_max_x = "100",
            size_hint_max_y = "100"
            ))
        self.input = MDTextField(
            text = "type name of the thing you're looking for",
            halign="center",
            size_hint = (0.8, 1),
            pos_hint = {"center_x": 0.5, "center_y": 0.5},
            font_size = 22
            )
        screen.add_widget(self.input)

        self.label = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y": 0.4},
            theme_text_color = "Secondary"
        )
        self.credit = MDLabel(
            text= '''images are from Microsoft's Bing, Please check your gallery after pressing download bottom''',
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y": 0.3},
            theme_text_color = "Primary",
            font_style = "H5"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.credit)
        screen.add_widget(MDFillRoundFlatButton(
            text="DOWNLOAD",
            font_size = 17,
            pos_hint = {"center_x": 0.5, "center_y": 0.15},
            on_press = self.download
        ))
        return screen




if __name__ == "__main__":
    downloaderbuddy().run()