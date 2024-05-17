from PIL import Image
import os
f1 = open("textures by positions\colturi_inter_ids.txt", "r")
s=f1.read()
if not s:
    quit()
s=s.split('\n')
colturi=eval(s[0])
inter=eval(s[1])

directory = 'textures by positions\\all'
png_files = [file for file in os.listdir(directory) if file.endswith('.png')]
files_to_delete = png_files[:20]
for file in files_to_delete:
    os.remove(os.path.join(directory, file))

f3=open("textures by positions\cntr.txt",'r')
cnt=f3.read()
cnt=int(cnt)

i=0
def generator_textura_colturi():
    global i
    #colt 0 textura
    image1 = Image.open(f'textures by positions\\1\\0.png')
    image2 = Image.open(f'textures by positions\\2\\{colturi[0][0]}.png')
    image3 = Image.open(f'textures by positions\\3\\{colturi[0][2]}.png')
    image4 = Image.open(f'textures by positions\\4\\0.png')
    image5 = Image.open(f'textures by positions\\5\\{colturi[0][1]}.png')
    image6 = Image.open(f'textures by positions\\6\\0.png')
    width, height = image1.size
    combined_image = Image.new('RGBA', (width, height))
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, 0), mask=image2)
    combined_image.paste(image3, (0, 0), mask=image3)
    combined_image.paste(image4, (0, 0), mask=image4)
    combined_image.paste(image5, (0, 0), mask=image5)
    combined_image.paste(image6, (0, 0), mask=image6)
    combined_image.save(f'textures by positions\\all\\{cnt}combined_image{i}.png')

    i+=1
    #colt 1 textura
    image1 = Image.open(f'textures by positions\\1\\0.png')
    image2 = Image.open(f'textures by positions\\2\\{colturi[1][0]}.png')
    image3 = Image.open(f'textures by positions\\3\\0.png')
    image4 = Image.open(f'textures by positions\\4\\0.png')
    image5 = Image.open(f'textures by positions\\5\\{colturi[1][1]}.png')
    image6 = Image.open(f'textures by positions\\6\\{colturi[1][2]}.png')
    width, height = image1.size
    combined_image = Image.new('RGBA', (width, height))
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, 0), mask=image2)
    combined_image.paste(image3, (0, 0), mask=image3)
    combined_image.paste(image4, (0, 0), mask=image4)
    combined_image.paste(image5, (0, 0), mask=image5)
    combined_image.paste(image6, (0, 0), mask=image6)
    combined_image.save(f'textures by positions\\all\\{cnt}combined_image{i}.png')

    i+=1
    #colt 2 textura
    image1 = Image.open(f'textures by positions\\1\\{colturi[2][2]}.png')
    image2 = Image.open(f'textures by positions\\2\\{colturi[2][0]}.png')
    image3 = Image.open(f'textures by positions\\3\\0.png')
    image4 = Image.open(f'textures by positions\\4\\0.png')
    image5 = Image.open(f'textures by positions\\5\\0.png')
    image6 = Image.open(f'textures by positions\\6\\{colturi[2][1]}.png')
    width, height = image1.size
    combined_image = Image.new('RGBA', (width, height))
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, 0), mask=image2)
    combined_image.paste(image3, (0, 0), mask=image3)
    combined_image.paste(image4, (0, 0), mask=image4)
    combined_image.paste(image5, (0, 0), mask=image5)
    combined_image.paste(image6, (0, 0), mask=image6)
    combined_image.save(f'textures by positions\\all\\{cnt}combined_image{i}.png')

    i+=1
    #colt 3 textura
    image1 = Image.open(f'textures by positions\\1\\{colturi[3][1]}.png')
    image2 = Image.open(f'textures by positions\\2\\{colturi[3][0]}.png')
    image3 = Image.open(f'textures by positions\\3\\{colturi[3][2]}.png')
    image4 = Image.open(f'textures by positions\\4\\0.png')
    image5 = Image.open(f'textures by positions\\5\\0.png')
    image6 = Image.open(f'textures by positions\\6\\0.png')
    width, height = image1.size
    combined_image = Image.new('RGBA', (width, height))
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, 0), mask=image2)
    combined_image.paste(image3, (0, 0), mask=image3)
    combined_image.paste(image4, (0, 0), mask=image4)
    combined_image.paste(image5, (0, 0), mask=image5)
    combined_image.paste(image6, (0, 0), mask=image6)
    combined_image.save(f'textures by positions\\all\\{cnt}combined_image{i}.png')

    i+=1
    #colt 4 textura
    image1 = Image.open(f'textures by positions\\1\\0.png')
    image2 = Image.open(f'textures by positions\\2\\0.png')
    image3 = Image.open(f'textures by positions\\3\\{colturi[4][2]}.png')
    image4 = Image.open(f'textures by positions\\4\\{colturi[4][0]}.png')
    image5 = Image.open(f'textures by positions\\5\\{colturi[4][1]}.png')
    image6 = Image.open(f'textures by positions\\6\\0.png')
    width, height = image1.size
    combined_image = Image.new('RGBA', (width, height))
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, 0), mask=image2)
    combined_image.paste(image3, (0, 0), mask=image3)
    combined_image.paste(image4, (0, 0), mask=image4)
    combined_image.paste(image5, (0, 0), mask=image5)
    combined_image.paste(image6, (0, 0), mask=image6)
    combined_image.save(f'textures by positions\\all\\{cnt}combined_image{i}.png')

    i+=1
    #colt 5 textura
    image1 = Image.open(f'textures by positions\\1\\0.png')
    image2 = Image.open(f'textures by positions\\2\\0.png')
    image3 = Image.open(f'textures by positions\\3\\0.png')
    image4 = Image.open(f'textures by positions\\4\\{colturi[5][0]}.png')
    image5 = Image.open(f'textures by positions\\5\\{colturi[5][1]}.png')
    image6 = Image.open(f'textures by positions\\6\\{colturi[5][2]}.png')
    width, height = image1.size
    combined_image = Image.new('RGBA', (width, height))
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, 0), mask=image2)
    combined_image.paste(image3, (0, 0), mask=image3)
    combined_image.paste(image4, (0, 0), mask=image4)
    combined_image.paste(image5, (0, 0), mask=image5)
    combined_image.paste(image6, (0, 0), mask=image6)
    combined_image.save(f'textures by positions\\all\\{cnt}combined_image{i}.png')

    i+=1
    #colt 6 textura
    image1 = Image.open(f'textures by positions\\1\\{colturi[6][2]}.png')
    image2 = Image.open(f'textures by positions\\2\\0.png')
    image3 = Image.open(f'textures by positions\\3\\0.png')
    image4 = Image.open(f'textures by positions\\4\\{colturi[6][0]}.png')
    image5 = Image.open(f'textures by positions\\5\\0.png')
    image6 = Image.open(f'textures by positions\\6\\{colturi[6][1]}.png')
    width, height = image1.size
    combined_image = Image.new('RGBA', (width, height))
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, 0), mask=image2)
    combined_image.paste(image3, (0, 0), mask=image3)
    combined_image.paste(image4, (0, 0), mask=image4)
    combined_image.paste(image5, (0, 0), mask=image5)
    combined_image.paste(image6, (0, 0), mask=image6)
    combined_image.save(f'textures by positions\\all\\{cnt}combined_image{i}.png')

    i+=1
    #colt 7 textura
    image1 = Image.open(f'textures by positions\\1\\{colturi[7][2]}.png')
    image2 = Image.open(f'textures by positions\\2\\0.png')
    image3 = Image.open(f'textures by positions\\3\\{colturi[7][1]}.png')
    image4 = Image.open(f'textures by positions\\4\\{colturi[7][0]}.png')
    image5 = Image.open(f'textures by positions\\5\\0.png')
    image6 = Image.open(f'textures by positions\\6\\0.png')
    width, height = image1.size
    combined_image = Image.new('RGBA', (width, height))
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, 0), mask=image2)
    combined_image.paste(image3, (0, 0), mask=image3)
    combined_image.paste(image4, (0, 0), mask=image4)
    combined_image.paste(image5, (0, 0), mask=image5)
    combined_image.paste(image6, (0, 0), mask=image6)
    combined_image.save(f'textures by positions\\all\\{cnt}combined_image{i}.png')

def generator_textura_inter():
    global i
    i+=1
    #inter 0 textura
    image1 = Image.open(f'textures by positions\\1\\0.png')
    image2 = Image.open(f'textures by positions\\2\\{inter[0][0]}.png')
    image3 = Image.open(f'textures by positions\\3\\0.png')
    image4 = Image.open(f'textures by positions\\4\\0.png')
    image5 = Image.open(f'textures by positions\\5\\{inter[0][1]}.png')
    image6 = Image.open(f'textures by positions\\6\\0.png')
    width, height = image1.size
    combined_image = Image.new('RGBA', (width, height))
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, 0), mask=image2)
    combined_image.paste(image3, (0, 0), mask=image3)
    combined_image.paste(image4, (0, 0), mask=image4)
    combined_image.paste(image5, (0, 0), mask=image5)
    combined_image.paste(image6, (0, 0), mask=image6)
    combined_image.save(f'textures by positions\\all\\{cnt}combined_image{i}.png')

    i+=1
    #inter 1 textura
    image1 = Image.open(f'textures by positions\\1\\0.png')
    image2 = Image.open(f'textures by positions\\2\\{inter[1][0]}.png')
    image3 = Image.open(f'textures by positions\\3\\0.png')
    image4 = Image.open(f'textures by positions\\4\\0.png')
    image5 = Image.open(f'textures by positions\\5\\0.png')
    image6 = Image.open(f'textures by positions\\6\\{inter[1][1]}.png')
    width, height = image1.size
    combined_image = Image.new('RGBA', (width, height))
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, 0), mask=image2)
    combined_image.paste(image3, (0, 0), mask=image3)
    combined_image.paste(image4, (0, 0), mask=image4)
    combined_image.paste(image5, (0, 0), mask=image5)
    combined_image.paste(image6, (0, 0), mask=image6)
    combined_image.save(f'textures by positions\\all\\{cnt}combined_image{i}.png')

    i+=1
    #inter 2 textura
    image1 = Image.open(f'textures by positions\\1\\{inter[2][1]}.png')
    image2 = Image.open(f'textures by positions\\2\\{inter[2][0]}.png')
    image3 = Image.open(f'textures by positions\\3\\0.png')
    image4 = Image.open(f'textures by positions\\4\\0.png')
    image5 = Image.open(f'textures by positions\\5\\0.png')
    image6 = Image.open(f'textures by positions\\6\\0.png')
    width, height = image1.size
    combined_image = Image.new('RGBA', (width, height))
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, 0), mask=image2)
    combined_image.paste(image3, (0, 0), mask=image3)
    combined_image.paste(image4, (0, 0), mask=image4)
    combined_image.paste(image5, (0, 0), mask=image5)
    combined_image.paste(image6, (0, 0), mask=image6)
    combined_image.save(f'textures by positions\\all\\{cnt}combined_image{i}.png')

    i+=1
    #inter 3 textura
    image1 = Image.open(f'textures by positions\\1\\0.png')
    image2 = Image.open(f'textures by positions\\2\\{inter[3][0]}.png')
    image3 = Image.open(f'textures by positions\\3\\{inter[3][1]}.png')
    image4 = Image.open(f'textures by positions\\4\\0.png')
    image5 = Image.open(f'textures by positions\\5\\0.png')
    image6 = Image.open(f'textures by positions\\6\\0.png')
    width, height = image1.size
    combined_image = Image.new('RGBA', (width, height))
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, 0), mask=image2)
    combined_image.paste(image3, (0, 0), mask=image3)
    combined_image.paste(image4, (0, 0), mask=image4)
    combined_image.paste(image5, (0, 0), mask=image5)
    combined_image.paste(image6, (0, 0), mask=image6)
    combined_image.save(f'textures by positions\\all\\{cnt}combined_image{i}.png')

    i+=1
    #inter 4 textura
    image1 = Image.open(f'textures by positions\\1\\0.png')
    image2 = Image.open(f'textures by positions\\2\\0.png')
    image3 = Image.open(f'textures by positions\\3\\0.png')
    image4 = Image.open(f'textures by positions\\4\\{inter[4][0]}.png')
    image5 = Image.open(f'textures by positions\\5\\{inter[4][1]}.png')
    image6 = Image.open(f'textures by positions\\6\\0.png')
    width, height = image1.size
    combined_image = Image.new('RGBA', (width, height))
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, 0), mask=image2)
    combined_image.paste(image3, (0, 0), mask=image3)
    combined_image.paste(image4, (0, 0), mask=image4)
    combined_image.paste(image5, (0, 0), mask=image5)
    combined_image.paste(image6, (0, 0), mask=image6)
    combined_image.save(f'textures by positions\\all\\{cnt}combined_image{i}.png')

    i+=1
    #inter 5 textura
    image1 = Image.open(f'textures by positions\\1\\0.png')
    image2 = Image.open(f'textures by positions\\2\\0.png')
    image3 = Image.open(f'textures by positions\\3\\0.png')
    image4 = Image.open(f'textures by positions\\4\\{inter[5][0]}.png')
    image5 = Image.open(f'textures by positions\\5\\0.png')
    image6 = Image.open(f'textures by positions\\6\\{inter[5][1]}.png')
    width, height = image1.size
    combined_image = Image.new('RGBA', (width, height))
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, 0), mask=image2)
    combined_image.paste(image3, (0, 0), mask=image3)
    combined_image.paste(image4, (0, 0), mask=image4)
    combined_image.paste(image5, (0, 0), mask=image5)
    combined_image.paste(image6, (0, 0), mask=image6)
    combined_image.save(f'textures by positions\\all\\{cnt}combined_image{i}.png')

    i+=1
    #inter 6 textura
    image1 = Image.open(f'textures by positions\\1\\{inter[6][1]}.png')
    image2 = Image.open(f'textures by positions\\2\\0.png')
    image3 = Image.open(f'textures by positions\\3\\0.png')
    image4 = Image.open(f'textures by positions\\4\\{inter[6][0]}.png')
    image5 = Image.open(f'textures by positions\\5\\0.png')
    image6 = Image.open(f'textures by positions\\6\\0.png')
    width, height = image1.size
    combined_image = Image.new('RGBA', (width, height))
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, 0), mask=image2)
    combined_image.paste(image3, (0, 0), mask=image3)
    combined_image.paste(image4, (0, 0), mask=image4)
    combined_image.paste(image5, (0, 0), mask=image5)
    combined_image.paste(image6, (0, 0), mask=image6)
    combined_image.save(f'textures by positions\\all\\{cnt}combined_image{i}.png')

    i+=1
    #inter 7 textura
    image1 = Image.open(f'textures by positions\\1\\0.png')
    image2 = Image.open(f'textures by positions\\2\\0.png')
    image3 = Image.open(f'textures by positions\\3\\{inter[7][1]}.png')
    image4 = Image.open(f'textures by positions\\4\\{inter[7][0]}.png')
    image5 = Image.open(f'textures by positions\\5\\0.png')
    image6 = Image.open(f'textures by positions\\6\\0.png')
    width, height = image1.size
    combined_image = Image.new('RGBA', (width, height))
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, 0), mask=image2)
    combined_image.paste(image3, (0, 0), mask=image3)
    combined_image.paste(image4, (0, 0), mask=image4)
    combined_image.paste(image5, (0, 0), mask=image5)
    combined_image.paste(image6, (0, 0), mask=image6)
    combined_image.save(f'textures by positions\\all\\{cnt}combined_image{i}.png')

    i+=1
    #inter 8 textura
    image1 = Image.open(f'textures by positions\\1\\0.png')
    image2 = Image.open(f'textures by positions\\2\\0.png')
    image3 = Image.open(f'textures by positions\\3\\{inter[8][1]}.png')
    image4 = Image.open(f'textures by positions\\4\\0.png')
    image5 = Image.open(f'textures by positions\\5\\{inter[8][0]}.png')
    image6 = Image.open(f'textures by positions\\6\\0.png')
    width, height = image1.size
    combined_image = Image.new('RGBA', (width, height))
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, 0), mask=image2)
    combined_image.paste(image3, (0, 0), mask=image3)
    combined_image.paste(image4, (0, 0), mask=image4)
    combined_image.paste(image5, (0, 0), mask=image5)
    combined_image.paste(image6, (0, 0), mask=image6)
    combined_image.save(f'textures by positions\\all\\{cnt}combined_image{i}.png')

    i+=1
    #inter 9 textura
    image1 = Image.open(f'textures by positions\\1\\0.png')
    image2 = Image.open(f'textures by positions\\2\\0.png')
    image3 = Image.open(f'textures by positions\\3\\0.png')
    image4 = Image.open(f'textures by positions\\4\\0.png')
    image5 = Image.open(f'textures by positions\\5\\{inter[9][0]}.png')
    image6 = Image.open(f'textures by positions\\6\\{inter[9][1]}.png')
    width, height = image1.size
    combined_image = Image.new('RGBA', (width, height))
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, 0), mask=image2)
    combined_image.paste(image3, (0, 0), mask=image3)
    combined_image.paste(image4, (0, 0), mask=image4)
    combined_image.paste(image5, (0, 0), mask=image5)
    combined_image.paste(image6, (0, 0), mask=image6)
    combined_image.save(f'textures by positions\\all\\{cnt}combined_image{i}.png')

    i+=1
    #inter 10 textura
    image1 = Image.open(f'textures by positions\\1\\{inter[10][0]}.png')
    image2 = Image.open(f'textures by positions\\2\\0.png')
    image3 = Image.open(f'textures by positions\\3\\0.png')
    image4 = Image.open(f'textures by positions\\4\\0.png')
    image5 = Image.open(f'textures by positions\\5\\0.png')
    image6 = Image.open(f'textures by positions\\6\\{inter[10][1]}.png')
    width, height = image1.size
    combined_image = Image.new('RGBA', (width, height))
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, 0), mask=image2)
    combined_image.paste(image3, (0, 0), mask=image3)
    combined_image.paste(image4, (0, 0), mask=image4)
    combined_image.paste(image5, (0, 0), mask=image5)
    combined_image.paste(image6, (0, 0), mask=image6)
    combined_image.save(f'textures by positions\\all\\{cnt}combined_image{i}.png')

    i+=1
    #inter 11 textura
    image1 = Image.open(f'textures by positions\\1\\{inter[11][0]}.png')
    image2 = Image.open(f'textures by positions\\2\\0.png')
    image3 = Image.open(f'textures by positions\\3\\{inter[11][1]}.png')
    image4 = Image.open(f'textures by positions\\4\\0.png')
    image5 = Image.open(f'textures by positions\\5\\0.png')
    image6 = Image.open(f'textures by positions\\6\\0.png')
    width, height = image1.size
    combined_image = Image.new('RGBA', (width, height))
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, 0), mask=image2)
    combined_image.paste(image3, (0, 0), mask=image3)
    combined_image.paste(image4, (0, 0), mask=image4)
    combined_image.paste(image5, (0, 0), mask=image5)
    combined_image.paste(image6, (0, 0), mask=image6)
    combined_image.save(f'textures by positions\\all\\{cnt}combined_image{i}.png')

generator_textura_colturi()
generator_textura_inter()
