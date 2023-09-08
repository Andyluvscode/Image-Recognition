from tkinter import *

from PIL import Image, ImageFilter

from PIL import ImageTk

def calcDistance(tuple1,tuple2):

  x1 = tuple1[0]

  y1 = tuple1[1]

  z1 = tuple1[2]

  x2 = tuple2[0]

  y2 = tuple2[1]

  z2 = tuple2[2]

  d = ((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

  return d
#print(calcDistance((1,2,3),(6,7,8)))

#opens the image
im1 = Image.open('image_A.jpeg','r')
print('Image A is an ocean')
width, height = im1.size
pixel_values = list(im1.getdata())
im1.close()
print()
lengthA= len(pixel_values) 
#print(pixel_values[:100])

#display image A
root = Tk()  
canvas = Canvas(root, width = 300, height = 300)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("image_A.jpeg"))  
canvas.create_image(20, 20, anchor=NW, image=img)
root.after(5000,lambda:root.destroy())

root.mainloop()
#opens the image
im1 = Image.open('image_B.jpeg','r')
print('Image B is an forest')
width, height = im1.size
pixel_values2 = list(im1.getdata())
im1.close()
print()
lengthB= len(pixel_values) 
#print(pixel_values[:100])

#display image B
root = Tk()  
canvas = Canvas(root, width = 300, height = 300)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("image_B.jpeg"))  
canvas.create_image(20, 20, anchor=NW, image=img)
root.after(5000,lambda:root.destroy())

root.mainloop()

ans= input('Would you like to pick mystery.jpeg or mystery2.jpeg?')
if ans== 'mystery.jpeg':
  imc = Image.open('mystery.jpeg','r')
  print('Image C is an ocean')
  width, height = imc.size
  pixel_values3 = list(imc.getdata())
  imc.close()
  print()
  lengthC= len(pixel_values)
else:
  imc = Image.open('mystery2.jpeg','r')
  print('Image C is an forest')
  width, height = imc.size
  pixel_values3 = list(imc.getdata())
  imc.close()
  print()
  lengthC= len(pixel_values)

#making all the images the same size
pics = [pixel_values, pixel_values2, pixel_values3]
lengths = [lengthA, lengthB, lengthC]
minimum = min(lengths)
#print(minimum)

#same length
holder = []
for i in range(len(pics)):
  if len(holder) < minimum:
    holder = []
    for j in range(len(pics[i])):
      holder.append(pics[i][j])
    pics[i] = holder

for i in range(len(pics)):
  print(len(pics[i]))

#calculating the disctance 
AC = []
BC = []
for i in range(len(pics[2])):
  dA = calcDistance(pics[2][i],pics[0][i])
  AC.append(dA)
  dB = calcDistance(pics[2][i],pics[1][i])
  BC.append(dB)

#Determines if the distance between Image A and the mystery image is the shortest or the longest for each pixel
AC_shortest = []
for i in range(len(AC)):
  if AC[i] < BC[i]:
    AC_shortest.append(1)
  else:
    AC_shortest.append(0)
# calculate the ratio of AC
result = sum(AC_shortest)/len(AC_shortest)

#print(result)
result=int(result*100)
if result >= 50:
  print("Mystery Image is a forest because its pixels are" , str(result) , '%' , 'similar to Image B')
else:
  print("Mystery Image is a ocean because its pixels are" ,str(result) ,'%' , 'similar to Image A')