from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.utils import platform
from qrreader import QRReader

class AppLayout(FloatLayout):
    qr_reader = ObjectProperty()
        
class ButtonsLayout(RelativeLayout):
    normal = StringProperty()
    down = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.normal = 'icons/flash-off.png'
        if platform == 'android':
            self.down   = 'icons/flash.png'
        else:
            self.down   = 'icons/flash-off.png'
  
    def on_size(self, layout, size):
        if Window.width < Window.height:
            self.pos = (0 , 0)
            self.size_hint = (1 , 0.2)
            self.ids.torch.pos_hint  = {'center_x':.5,'center_y':.5}
            self.ids.torch.size_hint = (.2, None)
        else:
            self.pos = (Window.width * 0.8, 0)
            self.size_hint = (0.2 , 1)
            self.ids.torch.pos_hint  = {'center_x':.5,'center_y':.5}
            self.ids.torch.size_hint = (None, .2)

    def enable_torch(self, state):
        if platform == 'android':
            if state == 'down':
                torch = 'on'
            else:
                torch = 'off'
            self.parent.qr_reader.torch(torch)

Builder.load_string("""
<AppLayout>:
    qr_reader: self.ids.preview
    QRReader:
        letterbox_color: 'steelblue'
        aspect_ratio: '16:9'
        id:preview
    ButtonsLayout:
        id:buttons

<ButtonsLayout>:
    ToggleButton:
        id:torch
        on_press: root.enable_torch(self.state)
        height: self.width
        width: self.height
        background_normal: root.normal
        background_down:   root.down

""")

            
