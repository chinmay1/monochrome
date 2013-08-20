from PIL import Image 
from Level import Level
import sys

asceescale = [
            " ",
            ".",
            ",",
	    "-",	
            "+",
            "/",
            "*",
            "D",
	    "O",
            "Q",
	    "P",
            "K",
	    "G",
            "B",
	    "8",
            "%",
            ]

ranging = [16,32,48,64,80,96,112,128,144,160,176,192,208,224,240,256]

def getReplacements(dictpath):
    text_file = open(dictpath, "r")
    txtfile = text_file.read()
    length = len(txtfile.rstrip().split('\n'))
    nlvl =[]
    for x in range(length,257,length):
        nlvl.append(x)
    return (txtfile,nlvl)

def to_ascee(path,destination):
    lvl = Level(ranging) 
    image_file = Image.open(path) # open colour image
    image_file = image_file.convert('L')
#   image_file = image_file.resize((384,216))
    new_image = """<html>
                   <body>
                   <pre  style="font-size:1px">\n
		"""
    for y in range(image_file.size[1]):
	for x in range(image_file.size[0]):
	    pixel = 255 - image_file.getpixel((x,y))
            new_image += asceescale[lvl.level(pixel)] 
        new_image += "\n"
    new_image += """
		</pre>
		</body>
		</html>"""
    text_file = open(destination, "w")
    text_file.write(new_image)
    text_file.close()

if(len(sys.argv)>2):
    getReplacements(sys.argv[3])

to_ascee(sys.argv[1],sys.argv[2])  



