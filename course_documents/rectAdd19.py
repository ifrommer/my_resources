# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:28:38 2018

@author: ifrommer
2019 version replacing EZgraphics with turtle
"""
import turtle
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
        
    def getDimensions(self):
        return self._width, self._height        
        
       
    def scale(self,widthScale,heightScale):       
        self._width = self._width * widthScale
        self._height = self._height * heightScale
        
    
    def __add__(self,otherRectObj):
        # otherRectObj is an object variable for another rect
        newWidth = self._width + otherRectObj._width        
        newHeight = self._height + otherRectObj._height
        
        sumRectObj = Rect(newWidth, newHeight)
        return sumRectObj
        
        
    def __gt__(self,otherRectObj):
        # based on area
        selfArea = self.getArea()
        otherArea = otherRectObj.getArea()
        if selfArea > otherArea:
            return True
        else:            
            return False
        
    """   
    def drawT(self):
        for i in range(2):
            turtle.forward(self._width)
            turtle.right(90)
            turtle.forward(self._height)
            turtle.right(90)
        turtle.exitonclick()
    """    
    """
    def __add__(self,otherRectObj):
        newWidth = self._width + otherRectObj._width
        newHeight = self._height + otherRectObj._height
        sumRectObj = Rect(newWidth,newHeight)
        return sumRectObj
    """

    def draw(self):
        # print top row
        print(self._marker * self._width)
        
        # print middle rows
        fillMarker = self._marker if self._fill else ' '
        for i in range(self._height-2):
            print(self._marker,fillMarker * (self._width-2),
                  self._marker,sep='')
        
        # print bottom row
        print(self._marker * self._width)

    """    
    def scale(self,widthScale=2,heightScale=2):
        self._width = round(widthScale*self._width)
        self._height = round(heightScale*self._height)
        # Warning: Python 3 uses Bankers rounding, rounding .5s to 
        #  nearest even #
    """    

    def move(self,xPos,yPos):
        self._xPos = xPos;   self._yPos = yPos

    
    def getArea(self):
        return(self._width * self._height)
            
    def graphT(self,exitOnClick=True):
        
        def graphTsub(exitOnClick=True):
            turtle.penup()
            turtle.goto(self._xPos,self._yPos)
            turtle.pendown()
            turtle.forward(self._width)
            turtle.right(90)
            turtle.forward(self._height)
            turtle.right(90)
            turtle.forward(self._width)
            turtle.right(90)
            turtle.forward(self._height)
            turtle.right(90)
            if exitOnClick: turtle.exitonclick()
        """
        try:
            print('trying')
            graphTsub(exitOnClick)
            print('did it')
        except:
            print('hiccup')
            graphTsub(exitOnClick)
         """   

# Make a list of Rect objects
# @num - number of Rect objects to make
def bunchORects(num):
    rectList = [0] * num
    markers = '*o-.<>#@!`~#$%()&18xc'
    for i in range(num):
        x = random.randint(0,250)
        y = random.randint(0,250)
        w = random.randint(20,30)
        h = random.randint(10,100)
        fill = random.choice((True,False))
        marker = random.choice(markers)
        rectList[i] = Rect(w,h,marker,fill,x,y)
        rectList[i].graphT(False)  # draw it with turtle
    return rectList    

bunchORects(10)
turtle.exitonclick()  # click exits the turtle window
