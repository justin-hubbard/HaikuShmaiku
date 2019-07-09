from PIL import Image, ImageDraw, ImageFont
import random
import datetime as dt

def get_lum(rgb):

    lum = (rgb[0]*0.299 + rgb[1]*0.587 + rgb[2]*0.114)

    return lum


def get_background():

    print(dt.datetime.now().hour)
    if dt.datetime.now().hour+16 > 3 & dt.datetime.now().hour+16 < 24:
        mix = (255,255,255)
    else:
        mix = (0,0,0)

    (r, g, b) = (random.randint(0,256), random.randint(0,256), random.randint(0,256))
    (r, g, b) = ((r+mix[0])/2,(g+mix[1])/2,(b+mix[2])/2)

    return (r,g,b)

def get_rect(rgb):
    
    if dt.datetime.now().hour+16 > 10 & dt.datetime.now().hour+16 < 24:
        lum = (int(get_lum(rgb))+255)/2
    else:
        lum = (int(get_lum(rgb))+255)/2
    return (lum, lum, lum)

def get_text_color(rgb):
    
    lum = int(get_lum(rgb))

    if lum > 100:
        return (0,0,0)
    else:
        return (255,255,255)

def generate_image(message, filename):

    # Image size
    (cW, cH) = (1024, 1024)

    font = ImageFont.truetype('AppleGaramond.ttf', size=70)

    # Find longest line, calculate dimensions
    lines = message.split("\n")
    long = max(lines, key=len)
    (w, h) = font.getsize(long)
    (offset_x, offset_y) = font.getoffset(long)
    hH = h*3
    ascent, descent = font.getmetrics()
    diff = descent - offset_y

    padding = 50

    # Top left corner
    (x,y) = ((cW-w)/2, (cH-hH)/2)

    # Generate colors
    bg = get_background()
    rect = get_rect(bg)
    lum = get_lum(bg)
    color = get_text_color(rect)

    #Create image and draw rectangle and text
    image = Image.new("RGB", (cW, cH), bg)
    draw = ImageDraw.Draw(image)
    draw.rectangle([(x-padding,y + offset_y - padding), ((x+w)+padding, (y+hH-descent)+padding-10)], fill=rect)
    draw.text((x,y), message, fill=color, font=font)

    # Save image to file
    print('uploads/{}'.format(filename))
    image.save('uploads/{}'.format(filename))
    #image.show()

    print("SHIT")


#generate_image("It's hard getting up\nWith no clock of consequence\nHello, afternoon")
