import time
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window

Window.size = (275, 500)

imag = ['images/a.JPG', 'images/b.JPG', 'images/c.JPG', 'images/d.JPG', 'images/e.JPG', 'images/f.JPG', 'images/g.JPG',
        'images/h.JPG']
answer = ['2134', '4231', '4231', '2314', '1423', '1324', '3214', '4123']

class MyManager(ScreenManager):
    pass

class HomeScreen(Screen):
    pass

class PlayingScreen(Screen):
    value = NumericProperty(1)
    ans = StringProperty(answer[0])
    index = NumericProperty(0)
    image = StringProperty(imag[0])
    idx = NumericProperty(0)

    def eraseone(self):
        self.ids.one.disabled = True

    def erasetwo(self):
        self.ids.two.disabled = True

    def erasethree(self):
        self.ids.three.disabled = True

    def erasefour(self):
        self.ids.four.disabled = True

    # CLEARING THE BOXES, ACTIVATING THE BUTTONS AND SETTING BACK THEIR TEXT

    def clear(self):
        self.ids.input_one.text = ""
        self.ids.input_two.text = ""
        self.ids.input_three.text = ""
        self.ids.input_four.text = ""
        self.ids.one.disabled = False
        self.ids.two.disabled = False
        self.ids.three.disabled = False
        self.ids.four.disabled = False


    # INPUT WHEN A BUTTON IS PRESSED

    def but_val(self, num):
        i = self.ids.input_one.text
        j = self.ids.input_two.text
        k = self.ids.input_three.text
        l = self.ids.input_four.text

        if i == "":
            self.ids.input_one.text = f"{num}"
        elif (i == f"{1}" or i == f"{2}" or i == f"{3}" or i == f"{4}") and (
                j == "" or j == "" or j == "" or j == "") and (k == "" or k == "" or k == "" or k == "") and (
                l == "" or l == "" or l == "" or l == ""):
            self.ids.input_two.text = f"{num}"
        elif (i == f"{1}" or i == f"{2}" or i == f"{3}" or i == f"{4}") and (
                j == f"{1}" or j == f"{2}" or j == f"{3}" or j == f"{4}") and (
                k == "" or k == "" or k == "" or k == "") and (l == "" or l == "" or l == "" or l == ""):
            self.ids.input_three.text = f"{num}"
        elif(i == f"{1}" or i == f"{2}" or i == f"{3}" or i == f"{4}") and (
                j == f"{1}" or j == f"{2}" or j == f"{3}" or j == f"{4}") and (
                k == "1" or k == "2" or k == "3" or k == "4") and (l == "" or l == "" or l == "" or l == ""):
            self.ids.input_four.text = f"{num}"

        if self.ids.input_one.text != "" and self.ids.input_two.text != "" and self.ids.input_three.text != "" and self.ids.input_four.text != "":
            correct = f'{self.ids.input_one.text}{self.ids.input_two.text}{self.ids.input_three.text}{self.ids.input_four.text}'
            if answer[self.idx] == correct:
                Clock.schedule_once(lambda dt: self.npop(), 1.1)
            else:
                Clock.schedule_once(lambda dt: self.apop(), 1.1)
        

    def nexting(self):
        self.value += 1
        self.idx += 1
        self.index += 1
        self.image = imag[self.index]
        self.clear()
                
    @ staticmethod
    def tpop():
        tbox = GridLayout(size_hint=(1, 1), cols=2)
        tbtn1 = Button(text="", background_color="cyan")
        tbtn2 = Button(text="", background_color="cyan")
        tbtn3 = Button(text="", background_color="cyan")
        tbtn4 = Button(text="", background_color="cyan")
        tbtn5 = Button(text="", background_color="cyan")
        tbtn6 = Button(text="", background_color="cyan")
        tbox.add_widget(tbtn1)
        tbox.add_widget(tbtn2)
        tbox.add_widget(tbtn3)
        tbox.add_widget(tbtn4)
        tbox.add_widget(tbtn5)
        tbox.add_widget(tbtn6)
        tpopup = Popup(title='THEMES', title_align='center', content=tbox, auto_dismiss=True, background_color="cyan", size_hint=(0.7, 0.9), pos_hint={"center_x": .5})
        tpopup.open()
    @ staticmethod
    def bpop():
        bbox = BoxLayout(orientation='vertical', padding=5)
        bbtn1 = Button(text="+3 Hints  $1.99", background_color="cyan", font_size=10)
        bbtn2 = Button(text="+10 Hints  $3.99", background_color="cyan", font_size=10)
        bbtn3 = Button(text="+20 hints  $5.99", background_color="cyan", font_size=10)
        bbtn4 = Button(text="+40 hints  $9.99", background_color="cyan", font_size=10)
        bbtn5 = Button(text="+60 hints  $15.99", background_color="cyan", font_size=10)
        bbtn6 = Button(text="OTHERS", background_color="cyan", font_size=10)
        bbox.add_widget(bbtn1)
        bbox.add_widget(bbtn2)
        bbox.add_widget(bbtn3)
        bbox.add_widget(bbtn4)
        bbox.add_widget(bbtn5)
        bbox.add_widget(bbtn6)
        bpopup = Popup(title='SHOP', title_align='center', content=bbox, auto_dismiss=True, background_color="cyan", size_hint=(0.8, 0.8), pos_hint={"center_x": .5})
        bbtn6.bind(on_press=lambda x: PlayingScreen().tpop())
        bpopup.open()

    def npop(self):
        nbox = BoxLayout(orientation='vertical')
        nbtn1 = Button(text="NEXT", size_hint=(.3, 0), font_name="Caveat", font_size='20')
        nimg = Image(source=imag[self.index], size_hint=(.65, .8))
        nbox.add_widget(nimg)
        nbox.add_widget(nbtn1)
        npopup = Popup(title='', title_align='center', content=nbox, auto_dismiss=False, background='imags/correct.JPG')
        nbtn1.bind(on_release=npopup.dismiss)
        nbtn1.bind(on_press=lambda _: self.nexting())

        npopup.open()

    def apop(self):
        abox = AnchorLayout()
        abtn1 = Button(text="TRY AGAIN", size_hint=(.5, .1), font_name="Caveat", font_size='20')
        abox.add_widget(abtn1)
        apopup = Popup(title='', title_align='center', content=abox, auto_dismiss=False, background='imags/wrong.JPG')
        abtn1.bind(on_release=apopup.dismiss)
        abtn1.bind(on_press=lambda _: self.clear())
        apopup.open()

    def image_popup(self, image_index):
        image_box = BoxLayout()
        my_image = Image(source = str(image_index))
        image_box.add_widget(my_image)
        image_popup_box = Popup(title='LEVEL', title_align='center', content=image_box, size_hint=(0.9, 0.7), auto_dismiss=True)
        image_popup_box.open()

    def level_popup(self):
        i = 1
        my_box = GridLayout(rows = 50, cols = 2, size_hint=(1, None), height=400) 
        while i < len(imag)+1:
            l_button = Button(text=str(i), disabled=True)
            if int(l_button.text) < self.value+1:
                l_button.disabled = False
            my_box.add_widget(l_button)
            l_button.bind(on_press=lambda _, num=i: self.image_popup(imag[num-1]))
            i += 1
        scroll_view = ScrollView()
        scroll_view.add_widget(my_box)
        levo_popup = Popup(title='LEVELS', title_align='center', content = scroll_view, size_hint=(0.7, 0.9), auto_dismiss=True)
        levo_popup.open()

    def opening_level_popup(self):
        self.level_popup()

LabelBase.register(name='Tiltprism', fn_regular='fonts/TiltPrism-Regular-VariableFont_XROT,YROT.ttf')
LabelBase.register(name='Caveat', fn_regular='fonts/Caveat-VariableFont_wght.ttf')
LabelBase.register(name='Dyna', fn_regular='fonts/DynaPuff-VariableFont_wdth,wght.ttf')

class Jumbled(MDApp):
    def build(self):
        Builder.load_file("./Jumbled.kv")

        sm = MyManager()
        sm.add_widget(HomeScreen(name='home_screen'))
        sm.add_widget(PlayingScreen(name='playing_screen'))
        return sm
    
    def home_to_playing(self):
        self.root.current = 'playing_screen'

    def playing_to_home(self):
        self.root.current = 'home_screen'

if __name__ := "__main__":
    Jumbled().run()


