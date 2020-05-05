from fpdf import FPDF
import os
from PIL import Image
Image.MAX_IMAGE_PIXELS=None #for super large image, avoid decompression bomb error


pdf = FPDF()
path =r"D:\zzzzz\xxx\\"
dirs = os.listdir( path )
#letter is 216mm x 279mm
paperwidth=210
paperheigth=297
margin=5
phm=paperheigth-2*margin

for item in dirs:
    wi =paperwidth-(2*margin)  # 5+211+5=216
    if os.path.isfile(path+item):
            
            im = Image.open(path+item)
            
            #choose image size to fill page: 
            #always keep the image ratio
            #maximize with or heigth
            ratio=im.height/im.width
            hi = int(wi*ratio)
            if hi>phm:
                hi=phm
                wi=int(hi/ratio)
            
            print("Processing:",item,hi,wi)
            legend=item.replace('resized15percent.jpg','')
            legend=legend.replace("_"," ")
            legend=legend.replace("-"," ")
            pdf.add_page()
            pdf.image(path+item,x=5, y=5,w=wi,h=hi)
            # Text format
            pdf.set_font('Arial', '', 12)
            pdf.set_text_color(0, 0, 0)
            pdf.set_y(265)
            pdf.write(10,legend)

pdf.output(r"D:\hhhhhh.pdf", "F")
