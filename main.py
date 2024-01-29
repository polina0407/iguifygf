from PIL import Image, ImageFilter

class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = list()

    def open (self):
        try:
            self.original = Image.open(self.filename)
        except:
            print( 'Файл не знайдений!')
        self.original.show()

    def do_flip1(self):
        rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self. changed.append(rotated)
        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0]+ str(len(self.changed))+'.jpg'
        rotated.save (new_filename)

    def do_flip2(self):
        rotated2 = self.original.transpose(Image.FLIP_TOP_BOTTOM)
        self.changed.append(rotated2)
        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0]+ str(len(self.changed))+'.jpg'
        rotated2.save(new_filename)

    def do_cropped(self):
        box = (250, 100, 600, 400)
        cropped = self.original.crop(box)
        self.changed.append (cropped)
        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0] + str(len(self.changed)) + '.jpg'
        cropped.save(new_filename)

    def do_bw(self):
        bw = self.original.convert("L")
        self.changed. append(bw)
        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0] + str(len(self.changed)) + '.jpg'
        bw.save (new_filename)

    def do_red(self):
        red, green, blue = self.original.split()
        zeroed_band = red.point(lambda _: 0)
        red_merge = Image.merge("RGB", (red, zeroed_band, zeroed_band))
        self.changed.append(red_merge)
        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0] + str(len(self.changed)) + '.jpg'
        red_merge. save(new_filename)

    def do_blue(self):
        red, green, blue = self.original.split()
        zeroed_band = red. point(lambda _: 0)
        blue_merge = Image.merge("RGB", (zeroed_band, zeroed_band, blue))
        self. changed. append (blue_merge)
        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0] + str(len(self.changed)) + '.jpg'
        blue_merge.save (new_filename)

    def do_smooth(self):
        smooth = self.original.filter(ImageFilter.SMOOTH)
        self.changed.append(smooth)
        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0] + str(len(self.changed)) + '.jpg'
        smooth.save (new_filename)

MyImage = ImageEditor ('c735fe8b93614667c187c4e049c82a39.jpg')
MyImage.open()
MyImage.do_flip1()
MyImage.do_flip2()
MyImage.do_cropped()
MyImage.do_bw()
MyImage.do_red()
MyImage.do_blue ()
MyImage.do_smooth()
for im in MyImage.changed:
    im.show()
