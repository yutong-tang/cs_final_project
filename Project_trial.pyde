import os
import random

HEIGHT = 900
WIDTH = 900
rols=30
cols=30
grid_w = WIDTH/rols
grid_h = HEIGHT/cols
object_number=3#the numbers of total objects we have in the list


intro = loadImage(os.getcwd()+ '\\images\\'+'intro.png')
instructions =  loadImage(os.getcwd()+ '\\images\\'+'Instructions.png')
start_button = loadImage(os.getcwd()+ '\\images\\'+'startbutton.png')
instructions_page = loadImage(os.getcwd() + '\\images\\'+ 'instructions_page.png')
back_button = loadImage(os.getcwd() + '\\images\\'+ 'back_button.png')

object_images=[1,2,3]
#for i in range (object_number):
    #object_images.append(i)
    

class Game: 
    def __init__(self,bg):
        self.start_game = False 
        self.instructions =False
        #self. gamebg = image (intro, 0, 0, 900, 900)
        
        #maybe put the background pictures into a dictionaries like level 1,2,3
        self.bg = loadImage(os.getcwd()+'\\images\\'+bg+'.jpg')
        self.object_lists=[]
        self.game_detected = False
        self.selected_item= "none"
        
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
            image(self.bg,0,0,WIDTH,HEIGHT-100)
            #displa promt object 
            prompt.display()
            for a in self.object_lists:
                a.display()
    
    def generate_objects(self):
        image_list=[]
        while len(image_list)<3:#3 objects for, use while loop to avoid repetition
            rol=random.randint(10,20)
            col=random.randint(0,29)#need to calculate the background
            img=random.choice(object_images)
            if img not in image_list:
                object=Object(rol,col,img)
                self.object_lists.append(object)
                image_list.append(img)
            
    def select_prompt_object(self):
        self.selected_item=random.choice(self.object_lists)
        return self.selected_item
        
    def detect_object(self,x_axis,y_axis):
        if self.selected_item.x <= x_axis <= self.selected_item.x + grid_w and self.selected_item.y <= y_axis <= self.selected_item.y + grid_h:
                self.game_detected = True
                # need to figure out what we do next after detecing the object
                print("Hooray! Object detected!")
                #return
        self.game_detected = False
        
           

class Object:

    def __init__(self,rol,col,img,r=30):
        self.r=r
        self.rol=rol
        self.col=col
        self.img=loadImage(os.getcwd()+'\\images\\'+str(img)+'.png')
        self.x=self.col*grid_w
        self.y=self.rol*grid_h
        
    
    def display(self):    
        #stroke(255, 140, 210)
        #fill(255, 140, 210)
        #ellipse(self.x+grid_w/2,self.y+grid_h/2,self.r,self.r)
        image(self.img,self.x,self.y,grid_w,grid_h)

class Prompt:
    def __init__(self,selected_object):
        self.prompt=game.selected_item
        self.picture=game.selected_item.img
    
    def display(self):
        noStroke()
        fill(255,255,255)
        rect(0,HEIGHT-100,WIDTH,HEIGHT)
        image(self.picture,100,HEIGHT-90,grid_w,grid_h)
        
        
    

        
        
        
        
    
      
game = Game("palms")
game.generate_objects()
selected_object=game.select_prompt_object()
prompt=Prompt(selected_object)


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
        x_axis,y_axis = mouseClicked()
        game.detect_object(x_axis,y_axis)
        
    
    
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
        return x_axis,y_axis
