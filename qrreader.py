import webbrowser
from kivy.clock import mainthread
from kivy.metrics import dp
from kivy.graphics import Line, Color, Rectangle

from pyzbar import pyzbar
from pyzbar.pyzbar import ZBarSymbol
from PIL import Image

from gestures4kivy import CommonGestures
from camera4kivy import Preview


class QRReader(Preview, CommonGestures):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.annotations = []

    ####################################
    # Analyze a Frame - NOT on UI Thread
    ####################################
    
    def analyze_pixels_callback(self, pixels, size, pos, scale, mirror):
        # pixels : Kivy Texture pixels
        # size   : pixels size (w,h)
        # pos    : location of Texture in Preview Widget (letterbox)
        # scale  : scale from Analysis resolution to Preview resolution
        # mirror : true if Preview is mirrored
        pil_image = Image.frombytes(mode='RGBA', size=size, data= pixels)
        barcodes = pyzbar.decode(pil_image, symbols=[ZBarSymbol.QRCODE])
        found = []
        for barcode in barcodes:
            text = barcode.data.decode('utf-8')
            if 'https://' in text or 'http://' in text:
                x, y, w, h = barcode.rect
                # Map Zbar coordinates to Kivy coordinates
                y = max(size[1] -y -h, 0)
                # Map Analysis coordinates to Preview coordinates
                if mirror:
                    x = max(size[0] -x -w, 0)
                x = round(x * scale + pos[0])
                y = round(y * scale + pos[1])
                w = round(w * scale)
                h = round(h * scale)
                found.append({'x':x, 'y':y, 'w':w, 'h':h, 't':text})
        self.make_thread_safe(list(found)) ## A COPY of the list

    @mainthread
    def make_thread_safe(self, found):
        self.annotations = found

    ################################
    # Annotate Screen - on UI Thread
    ################################
        
    def canvas_instructions_callback(self, texture, size, pos):
        # Add the analysis annotations
        Color(1,0,0,1)
        for r in self.annotations:
            Line(rectangle=(r['x'], r['y'], r['w'], r['h']), width = dp(2))

    #################################
    # User Touch Event - on UI Thread
    #################################

    def cg_long_press(self, touch, x, y):
        self.open_browser(x, y)

    def cg_double_tap(self, touch, x, y):
        self.open_browser(x, y)

    def open_browser(self, x, y):
        for r in self.annotations:
            if x >= r['x'] and x <= r['x'] + r['w'] and\
               y >= r['y'] and y <= r['y'] + r['h']:
                webbrowser.open_new_tab(r['t'])
