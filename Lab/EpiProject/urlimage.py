import matplotlib.pyplot as plt
import numpy as np
from scipy import misc
from PIL import Image, ImageChops, ImageFilter, ImageDraw
import urllib.request
import requests
from io import BytesIO

class URLImage():
    """
        Image object represents a single image with the ability to get information and show it
        
        For information on images see:
        https://pillow.readthedocs.io/en/latest/handbook/tutorial.html

        url    #url to access image
        scale  #scale for image sizing 0.5 means reduce to 50%
        mode   #mode defines the the way to treat the image data where None uses data as load
               # if mode doesn't match the loaded image mode a transformation needs to be performed
        rot    #rotation of image
        ref    #refence url to related information for this image (site or metadata)
        img    #loaded image data
        tImg   #transformed image data
    """
   # myIMG = urlimage.URLImage() or 
   # myIMG = urlimage.URLImage('http://mysite/img1.jpg')  
   # myIMG = urlimage.URLImage('http://mysite/img1.jpg',0.5,None,90) or 
   # myIMG = urlimage.URLImage('http://mysite/img1.jpg', rotation = 90) or 
    def __init__(self, img_url=None, scale=1, mode=None, rotation = None, reference = None):
        self.url = img_url
        self.scale = scale
        self.mode = mode
        self.rot = rotation
        self.ref = reference
        self.img = None
        self.tImg = None

    #myIMG.loadImage()
    def loadImage(self, url = None, scale = None, mode = None):
        '''
            Load this image objects url from internet or fail
            Args:
                 url: new url
               scale: new scale
                mode: new mode
            Returns:
             True if load is successful, False otherwise

        '''
        if url != None: #change url
            self.url = url
        if scale != None: #change scale
            self.scale = url
        if mode != None: #change mode
            self.mode = mode
            self.img = None
            self.tImg = None

         # try to load image from url    
        if self.url == None:
            print("no url to load")
            return False
        else:
            hdrs = {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'}
            req = urllib.request.Request(self.url, headers = hdrs)
            try:
                response = requests.get(self.url)
                self.img = Image.open(BytesIO(response.content))
            except urllib.error.HTTPError as e:
                print('Image load of '+ self.url,'with error code '+ e.code)
                print(e.read())
                return False
            
        # adjust image if needed
        if  self.scale != 1:
            newsize = (int(self.img.width*scale),int(self.img.height*scale))
            self.tImg = self.img.resize( newsize, Image.BICUBIC)
        else:
            self.tImg = self.img
        if self.rot != None:
            self.tImg = self.tImg.rotate(self.rot)

        return True
    
    def show(self):
        self.tImg.show()
        
################# getters ##################
    def getURL(self):
        return self.url
    
    def getScale(self):
        return self.scale

    def getRotation(self):
        return self.rot

    def getMode(self):
        return self.mode

    def getImage(self):
        return self.img
        
################# setters ##################
    def setURL(self, url = None, autoLoad = False):
        changed = (self.url != url) # capture that there is a different url
        self.url = url
        if autoLoad:
            pass #todo add code to reload ?? call loadImage ??
    
    def setScale(self, scale = None):
        self.scale = scale
        #todo add code to retransform the loaded image

    def setRotation(self, rotation = None):
        self.rot = rotation
        #todo add code to retransform the loaded image

    def setMode(self, mode = None):
        self.mode = None
        #todo add code to retransform the loaded image

