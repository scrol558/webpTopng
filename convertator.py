import os
from PIL import Image

class Convert:
    def __init__(self, image_webp, image_png) -> str:
        self.image_webp = image_webp
        self.image_png = image_png

    def main(self):
        file_name, _ = os.path.splitext(self.image_webp)
        self.image_png = file_name + ".png"

        im = Image.open(self.image_webp)
        im.save(self.image_png, format="png", lossless=True)