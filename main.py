
import cv2 
import glob
import os

path = os.getcwd() + r'\CHALLENGE OF THE WEEK\OpenCV Image Compresor\assets' 
os.chdir(path)  
images = glob.glob('*.jpg')
folder = 'resized images'
if not os.path.exists(folder):
    os.makedirs(folder)


for image in images:
    img=cv2.imread(image,1)
    
    re=cv2.resize(img,(int(img.shape[1]/8),int(img.shape[0]/8)))
    
    cv2.imshow('Checking...',re)
    
 
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    
    cv2.imwrite(folder + '/' + 'resized_'+image, re)
         

path = os.getcwd()
os.chdir(path)
