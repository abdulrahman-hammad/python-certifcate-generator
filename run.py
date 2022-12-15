from fileinput import filename
import os
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np  
import time

list_of_names = []


def delete_old_data():
   # this method deletes the old generated-certificates
   for i in os.listdir("generated-certificates/"):
      os.remove("generated-certificates/{}".format(i))


def read_names():
   file_name = 'name-data.txt'
   with open(file_name) as f:
      for line in f:
          list_of_names.append(line.strip())


def generate_certificates():


   #The name of the certficate template to be used
   blank_certficate_template_name = 'Certificate Final wo name-1.png'
   #The name of the font to be used, its size, and position
   font_name = 'Janna LT Regular.ttf'
   font_size = 80
   #Text position
   x = 104
   y = 780

   #RGB color code
   color_r = 255
   color_g = 255
   color_b = 255

   
   # Load image in OpenCV  
   image = cv2.imread(blank_certficate_template_name)  
      
   # Convert the image to RGB (OpenCV uses BGR)  
   cv2_im_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)  
      
   # Pass the image to PIL  
   pil_im = Image.fromarray(cv2_im_rgb)  
      
   draw = ImageDraw.Draw(pil_im)  
   font = ImageFont.truetype(font_name, 40)  
   for index, name in enumerate(list_of_names):
      image = cv2.imread(blank_certficate_template_name)  
      cv2_im_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)  
      pil_im = Image.fromarray(cv2_im_rgb)  
      draw = ImageDraw.Draw(pil_im)  
      font = ImageFont.truetype(font_name, font_size)  
      draw.text((x,y), name.strip(), font=font,fill=(color_r,color_g,color_b),align="Centeral") 
      draw.rectangle((120,120,120,120),fill=(8,41,108))
      cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
  
      image  = cv2.imwrite("generated-certificates/{}.png".format(name.strip()), cv2_im_processed)
      print("Processing {} / {}".format(index + 1,len(list_of_names)))



      
def main():
   start_time = time.time()
   delete_old_data()
   read_names()
   generate_certificates()
   print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
   main()

