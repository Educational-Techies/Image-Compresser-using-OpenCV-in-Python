import cv2 as cv
import glob
import os

path = os.getcwd() + '\AISC\CHALLENGE OF THE WEEK\week 17-21 may\\assets'
os.chdir(path)
images = glob.glob('*.jpg')
folder = 'resized images'
if not os.path.exists(folder):
    os.makedirs(folder)


for image in images:
    img=cv.imread(image,1)
    
    resized=cv.resize(img,(int(img.shape[1]/8),int(img.shape[0]/8)))
       
    cv.imshow('Checking...Images',resized)
    
    cv.waitKey(2500)
    cv.destroyAllWindows()
    
    
    cv.imwrite(folder + '/' + 'resized_'+image, resized)

path = os.getcwd()
os.chdir(path)