# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from ezgraphics import GraphicsWindow

class Rect():
    
    def __init__(self,width = 5, height = 3, marker = '-',fill=True,
                 xPos=30,yPos=30):
        self._width = width;   self._height = height
        self._marker = marker
        self._fill = fill
        self._xPos = xPos;  self._yPos = yPos
        
    def __str__(self):
        msg = 'Hi, I am a rectangle. My instance variables are:\n'
        for k in self.__dict__.items():
            msg = msg + k[0] + ' = ' + str(k[1]) + '\n'
        return msg


    def draw(self):
        # print top row
        print(self._marker * self._width)
        
        # print middle rows
        fillMarker = self._marker if self._fill else ' '
        for i in range(self._height-2):
            print(self._marker,fillMarker * (self._width-2),self._marker,sep='')
        
        # print bottom row
        print(self._marker * self._width)
        
    def scale(self,widthScale=2,heightScale=2):
        self._width = round(widthScale*self._width)
        self._height = round(heightScale*self._height)
        # Warning: Python 3 uses Bankers rounding, rounding .5s to 
        #  nearest even #

    def move(self,xPos,yPos):
        self._xPos = xPos;   self._yPos = yPos


    def getArea(self):
        return(self._width * self._height)
        
    def graph(self,canvas,win,erase=False):
        color = 'white' if erase else 'black'
        canvas.setOutline(color) 
        try:
#            win = GraphicsWindow(300,300)
#            canvas = win.canvas()
            canvas.drawRect(self._xPos,self._yPos,
                            self._width,self._height)
            
        except:
            print('Some kind of error occurred. Calling win.wait()')
            win.wait()
        finally:
            pass
#            win.wait()


def graphObjects(objList):
    try:
        win = GraphicsWindow(800,800)
        canvas = win.canvas()
        for obj in objList:
            obj.graph(canvas,win)
    finally:
        win.wait()

def bunchORects(num, width_range=(20,30),
                height_range = (10,100)):
    import random
    rectList = [0] * num
    markers = '*o-.<>#@!`~#$%()&18xc'
    for i in range(num):
        x = random.randint(0,250)
        y = random.randint(0,250)
        w = random.randint(*width_range)#20,30)
        #h = 1.618*w
        h = random.randint(*height_range)#10,100)
        fill = random.choice((True,False))
        marker = random.choice(markers)
        rectList[i] = Rect(w,h,marker,fill,x,y)
    return rectList

def goHome(objList, erase=True, scale_fac = .9,
           iterations = 20):
    # rects shrink back to origin if scale_fac < 1
    try:
        win = GraphicsWindow(800,800)
        canvas = win.canvas()
        for i in range(iterations):
            for obj in objList:
                obj.graph(canvas,win)
            win.pause(500) 
            for obj in objList:
                obj.graph(canvas,win,erase)  # erase them
                obj.move(scale_fac*obj._xPos,scale_fac*obj._yPos)
                #obj.scale(.9,.9)
    finally:
        win.wait()

def storeObjList(objList,fName):
    # use objects' dictionaries to write instance vars to a file
 #   numObjs = len(objList)
    outFile = open(fName,'w')
    print(' ,',end='',file=outFile)
    instVarList = list(objList[0].__dict__.keys())
    for key in instVarList:
        print(key+',',end='',file=outFile)
    print(file=outFile)
    for ind,obj in enumerate(objList):
        tmpDict = obj.__dict__
        print(str(ind) + ', ',end='',file=outFile)
        for key in instVarList:
            print(str(tmpDict[key])+',',end='',file=outFile)
        print(file=outFile)    
    
    
    outFile.close()
    

"""
# good stuff:
rl = bunchORects(12)
for item in rl:
    print(item)
    
for item in rl:
    item.draw()

rl3 = [Rect(k,k) for k in range(3,250,3)]
graphObjects(rl3)

rects = [Rect(k,k,'.',1,k,k) for k in range(3,350,20)]
graphObjects(rects)

xRad = [i*math
pi/180 for i in range(720)]
yLoc = [math.sin(i) for i in xRad]
rectList = [Rect(33,33,'.',1,100*xRad[i],200+200*yLoc[i]) for i in range(720)]
graphObjects(rectList)

rs = bunchORects(100);goHome(rs)
    
"""