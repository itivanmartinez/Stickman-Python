import tkinter as Tk
import time
class Windows:
    def __init__(self, Tk):
        self.windows=Tk.Tk()
        self.windows.title("Stick Man")
        self.windows.resizable(0,0)
        self.canvas=Tk.Canvas(self.windows,width=700,height=800,bd=0)
        self.canvas.pack()
        
class stickman:
    def __init__(self,windows):
        self.run_right=[
            Tk.PhotoImage(file="stick1.gif"),
            Tk.PhotoImage(file="stick2.gif")
            ]
        self.windows=windows
        self.image=self.windows.canvas.create_image(350,600,image=self.run_right[1])
        self.speedx=0
        self.speedy=0
        self.coordinates=self.windows.canvas.coords(self.image)
        self.jumping=False
    def update(self):
        self.coordinates=self.windows.canvas.coords(self.image)
    def mov_left(self,evt):
        self.key=evt.keysym
        self.speedx=-5
   
    def mov_right(self,evt):
        self.update()
        self.speedx=0
        self.key=evt.keysym
        self.speedx=5

    def stop(self,evt):
        self.speedx=0

    def moving(self,blocks):
        self.speedy+=.5
        self.update()
        if self.coordinates[0]<20 and self.key=='Left':
            self.speedx=0
        if self.coordinates[0]>680 and self.key=='Right':
            self.speedx=0 
        self.windows.canvas.move(self.image,self.speedx,self.speedy)
        self.update()
        left,right=self.coordinates[0],self.coordinates[0]
        top,bottom=self.coordinates[1],self.coordinates[1]+30
        for block in blocks:
            if self.speedy>0:
                hits=self.windows.canvas.find_overlapping(left,top,right,bottom)
                if block.id in hits:
                    self.jumping=False
                    self.speedy=0
                    print(left)
                    self.windows.canvas.coords(self.image,left,block.y1-15)
                         
    def jump(self,evt):
        if self.jumping==False:
            self.jumping=True
            self.speedy=-10            
             
class Blocks:
    def __init__(self,windows,x1,y1,x2,y2):
        self.windows=windows
        self.id=self.windows.canvas.create_rectangle(x1,y1,x2,y2,fill="green")
        self.top=y1
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2

win=Windows(Tk)
floor=Blocks(win,0,750,700,800)
man=stickman(win)
platforms=[]
platforms.append(floor)
floor=Blocks(win,60,700,160,710)
platforms.append(floor)
floor=Blocks(win,180,650,280,660)
platforms.append(floor)
floor=Blocks(win,390,590,450,600) 
platforms.append(floor)
floor=Blocks(win,460,500,550,510)
platforms.append(floor)
floor=Blocks(win,460,440,550,450)
platforms.append(floor)
floor=Blocks(win,260,330,360,340)
platforms.append(floor)
floor=Blocks(win,10,280,110,290)
platforms.append(floor)
win.canvas.bind_all("<KeyPress-Left>",man.mov_left)
win.canvas.bind_all("<KeyPress-Right>",man.mov_right)
win.canvas.bind_all("<KeyRelease-Right>",man.stop)
win.canvas.bind_all("<KeyRelease-Left>",man.stop)
win.canvas.bind_all("<KeyPress-space>",man.jump)
go_on=True

def main_loop():
    while go_on:
        time.sleep(0.01)
        man.moving(platforms)
        win.canvas.update()
        
main_loop()
        
       
