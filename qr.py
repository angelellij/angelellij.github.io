#Python code to create your own words for codenames game.

import qrcode
import math
from PIL import Image, ImageDraw, ImageFont, ImageOps

def move_rotate_and_paste(img, text_img, r:int, px:int, py:int):
    text_img = text_img.rotate(r, expand=1)
    sx, sy = text_img.size
    img.paste(text_img, (px, py, px + sx, py + sy), text_img)
    return img

def create_qr(word):
    qr = qrcode.QRCode(version=1,box_size = 20, border=10 )
    qr.add_data(word)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white').convert("RGBA")

    if word == 'https://angelellij.github.io/': return img

    frame = Image.open('Frame.png')
    img.paste(frame, (0,0), frame)

    width = 500
    height = 100
    font = ImageFont.truetype("CaveatBrush-Regular.ttf", 96)

    text_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw2 = ImageDraw.Draw(text_img)
    draw2.text((0, 0), text=word, font=font, fill='black')

    img = move_rotate_and_paste(img, text_img, 0, 220, 660)
    img = move_rotate_and_paste(img, text_img, 180, 120, 60)
    img = move_rotate_and_paste(img, text_img, 90, 660, 120)
    img = move_rotate_and_paste(img, text_img, 270, 60, 220)
    return img

words = [
    'https://angelellij.github.io/',
    'Shirt', 
    'Chocolate', 
    'Grass', 
    'Boat', 
    'Armour', 
    'Dinosaur', 
    'Sub',
    'Door',
    'Car',
    'Lake',
    'Mage',
    'Baby',
    'Germany',
    'Hidden',
    'Game',
    'Apple',
    'Carrot',
    'Guitar',
    'Pool',
    'Toilet',
    'Fantasy',
    'Hole',
    'Trench',
    'Knife',
    'Parachute',
    'Astronaut',
    'River',
    'Mouth',
    'Race',
    'Independence',
    'Small',
    'Adventurer',
    'Spy',
    'Cross',
    'Cow',
    'Field',
    'Speaker',
    'Stadium',
    'Party',
    'Obelisc',
    'Swiss',
    'Peru',
    'Bolivia',
    'Australia',
    'Tortoise',
    'Lion',
    'Kangaroo',
    'Refugee',
    'Shark',
    'Fish',
    'Bear',
    'Dog',
    'Car',
    'Chicken',
    'Money',
    'Gold',
    'Document',
    'Academy',
    'Argentina',
    'China',
    'Russia',
    'Horse',
    'Sheep',
    'Bee',
    'Insect',
    'Bird',
    'Oak',
    'Rose',
    'Jazmine',
    'Violet',
    'Tomato',
    'Beef',
    'Peer',
    'Peach',
    'Wheat',
    'Bread',
    'Taco',
    'Circle',
    'Cross',
    'Line',
    'Triangle',
    'Professor',
    'Program',
    'Psychologist',
    'Medic',
    'Music',
    'President',
    'Bike',
    'Train',
    'Bus',
    'Administrator',
    'Skate',
    'Wheel',
    'Cofee',
    'Colombia',
    'Africa',
    'Heat',
    'Cold',
    'Snow',
    'Sun',
    'Moon',
    'Triumph',
    'Mercury',
    'Ice',
    'Coke',
    'Rum',
    'Beer',
    'Smoke',
    'Leaf',
    'Wood',
    'Stone',
    'Screen',
    'Control',
    'Remote',
    'Analisis',
    'Science',
    'Microscope',
    'Math',
    'Language',
    'Sombrero',
    'Chair'
    ]

row = 4
col = 3
page_n = row*col
qr_in_page = page_n
pages = math.ceil( len(words) / (page_n) )
count_page = 0
count_row = 0
count_col = 0
py_margin = 120
px_margin = 120
py_space = 850
px_space = 850
page_size_y = 3620
page_size_x = 2780

print('words',len(words) )
print('words per page', len(words)/page_n)

while count_page < len(words)/12:
    if count_page == pages-1:
        qr_in_page = len(words) - (pages-1) * page_n - 1
        row = math.ceil(qr_in_page/col)
    page_img = Image.new('RGBA', (page_size_x, page_size_y), (255, 255, 255, 255))

    while count_row < row:
        if count_page == pages-1 and count_row == row-1:
            col = math.floor(qr_in_page / row)-1

        while count_col < col:
            # print(count_row, count_col, count_page, count_col + count_row*col + count_page*(page_n) )
            word = words[count_col + count_row*col + count_page*(page_n)]
            img = create_qr(word)
            px = px_margin + px_space*count_col
            py = py_margin + py_space*count_row
            sx, sy = img.size
            page_img.paste(img, (px, py, px + sx, py + sy))

            count_col += 1
        count_row += 1
        count_col = 0
    count_page += 1
    count_row = 0

    page_img.save(f'Pages/Page{count_page}.png')

