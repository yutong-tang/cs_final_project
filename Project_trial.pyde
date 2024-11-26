import os
import random

HEIGHT = 900
WIDTH = 900
rols=30
cols=30
grid_w = WIDTH/rols
grid_h = HEIGHT/cols


intro = loadImage(os.getcwd()+ '\\images\\'+'intro.png')
instructions =  loadImage(os.getcwd()+ '\\images\\'+'Instructions.png')
start_button = loadImage(os.getcwd()+ '\\images\\'+'startbutton.png')
instructions_page = loadImage(os.getcwd() + '\\images\\'+ 'instructions_page.png')
back_button = loadImage(os.getcwd() + '\\images\\'+ 'back_button.png')

class Game: 
    def __init__(self,bg):
        self.start_game = False 
        self.instructions =False
        #self. gamebg = image (intro, 0, 0, 900, 900)
        
        #maybe put the background pictures into a dictionaries like level 1,2,3
        self.bg = loadImage(os.getcwd()+'\\images\\'+bg+'.jpg')
        self.object_lists=[]
        self.object_rols=[]
        self.object_cols=[]
        self.game_detected = False
        
    def intro_display(self):
       #image (intro, 0, 0, 900, 900)
       if self.start_game == False and self.instructions== False: 
         image (instructions, WIDTH//4, HEIGHT//2, 462, 77)
         image (start_button, WIDTH//4, HEIGHT//2 +100, 462, 77)
         if mouseX in range (WIDTH//4, WIDTH//4 +462) and mouseY in range(HEIGHT//2, HEIGHT//2 + 77):
            strokeWeight(15)
            stroke(0, 0, 0)
            rect(WIDTH//4, HEIGHT//2, 462, 77)
            image (instructions, WIDTH//4, HEIGHT//2, 462, 77)
           
         if mouseX in range (WIDTH//4, WIDTH//4 +462) and mouseY in range(HEIGHT//2 +100, HEIGHT//2 + 177):
            strokeWeight(15)
            stroke(0, 0, 0)
            rect(WIDTH//4, HEIGHT//2 +100, 462, 77)
            image (start_button, WIDTH//4, HEIGHT//2 +100 , 462, 77)
            
       if self.instructions ==True and self.start_game == False: 
           image (back_button,  WIDTH//3 ,  5*HEIGHT//6 +20, 278, 63)
           if mouseX in range (WIDTH//3, WIDTH//3 +278) and mouseY in range(5* HEIGHT//6 +20, 5* HEIGHT//6 + 63):
              strokeWeight(15)
              stroke(0, 0, 0)
              rect(WIDTH//3 ,  5*HEIGHT//6 +20, 278, 63)
              image (back_button, WIDTH//3 ,  5*HEIGHT//6 +20, 278, 63)
    
    def display(self):
        if self.start_game:
            image(self.bg,0,0,WIDTH,HEIGHT)
            for a in self.object_lists:
                a.display()
    
    def generate_objects(self):
        for i in range(10):#10 objects for now
            rol=random.randint(20,29)
            col=random.randint(0,29)
            object=Object(rol,col)
            self.object_lists.append(object)
            self.object_rols.append(object.x)
            self.object_cols.append(object.y)
        
           

class Object:

    def __init__(self,rol,col,r=30):
        self.r=r
        self.rol=rol
        self.col=col
        self.img="img"
        self.x=self.col*grid_w
        self.y=self.rol*grid_h
        
    
    def display(self):    
        stroke(255, 140, 210)
        fill(255, 140, 210)
        ellipse(self.x+grid_w/2,self.y+grid_h/2,self.r,self.r)
    
    def detect_object(self):
        for y in object_rols:
            if y_axis in range(y,y+30):
                for x in object_cols:
                    if x_axis in range(x,x+30):
                        game.detected==True
                        print("horray!")
            
        
        
        
        
    
      
game = Game("palms")
game.generate_objects()


def setup(): 
    size(900, 900)
    image(intro, 0, 0, 900, 900)

    
def draw():
    if game. start_game == False and game.instructions == False: 
       image (intro, 0, 0, 900, 900)
       game.intro_display()
    if game.instructions == True and game.start_game == False: 
       image (instructions_page, 0, 0, WIDTH, HEIGHT)
       game.intro_display()
    if game.start_game and not game.instructions:
        game.display()
    
    
def mouseClicked():
    if mouseX in range (WIDTH//4, WIDTH//4 +462) and mouseY in range(HEIGHT//2, HEIGHT//2 + 77):
        game.instructions = True
    if mouseX in range (WIDTH//4, WIDTH//4 +462) and mouseY in range(HEIGHT//2 +100, HEIGHT//2 + 177):
        game.start_game = True
        game.instructions = False
    if game.instructions: 
        if mouseX in range (WIDTH//3, WIDTH//3 +278) and mouseY in range(5* HEIGHT//6 +20, 5* HEIGHT//6 + 63):
            game. instructions = False
    if game.start_game:
        x_axis = mouseX 
        y_axis = mouseY
