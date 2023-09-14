import cv2
import matplotlib.pyplot as plt
import time
from flask import Flask, render_template,request
import random
class Snake:
    
    def create_board(self):
        
        for i in range(10):
            temp=[]
            for j in range(10):
                temp.append(list())
            self.board.append(temp)
                
        
    def __init__(self):
        self.c=5
        
        positions_ladder_Snake=[
                                [3, 9, 6, 8, 1 ],
                                [8, 9, 9, 6, 3],
                                [3, 8, 6, 9, 0],
                                [0, 7, 1, 5, 4],
                                [9, 4, 6, 3, 6],
                                [6, 4, 6, 6, 3],
                                [1, 3, 1, 8, 1],
                                [3, 3, 0, 4, 5],
                                [8, 2, 9, 0, 9],
                                [0, 2, 1, 0, 9],
                                [6, 1, 4, 6, 3],
                                [7, 0, 6, 2, 7],
                                [5, 0, 5, 2, 7],
                                [2, 0, 1, 2, 7]
                                ]
        self.board=[]
        self.position_x=50
        self.position_y=50+(100*9)
        self.x=0
        self.y=9
        self.level=0
        self.create_board()
        for i in positions_ladder_Snake:
            self.board[i[0]][i[1]].append(i[2])
            self.board[i[0]][i[1]].append(i[3])
            self.board[i[0]][i[1]].append(i[4])
       
            
        
        
    def chance_generator(self):
        val = random.randint(1, 6)
        return val
        
    def movement(self,val,lev):
        while(val>0):
            #print("ok",self.x," ",self.y)
            if(lev%2==0):
                self.position_x+=100;
                self.x+=1
                if(self.x==10):
                    self.x=9
                    self.y-=1
                    self.position_x=50+(100*9)
                    self.position_y-=100
                    lev+=1
            else:
                self.position_x-=100
                self.x-=5
                if(self.x==-1):
                    self.x=0
                    self.y-=1
                    self.position_x=50
                    self.position_y-=100
                    lev+=1
            val-=1
        self.level=lev
    def source_destination(self):
        #print(self.x," ",self.y," ",self.level)
        if(len(self.board[self.x][self.y])==0):
            return
        t_x=self.board[self.x][self.y][0]
        t_y=self.board[self.x][self.y][1]
        
        self.level=self.board[self.x][self.y][2]
        self.x=t_x
        self.y=t_y
        self.position_x=50+(100*(t_x))
        self.position_y=50+(100*(t_y))
        
    def display_Game(self):
        self.c+=1
        img = cv2.imread("./static/snake2.png")
        radius = 25
        color = (0, 255, 255)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        thickness = -1
        img = cv2.resize(img, (1000, 1000))
        a = cv2.circle(img, (self.position_x, self.position_y), radius, color, thickness)
        p = "./static/snake{}.png".format(self.c)
        cv2.imwrite(p, img)
        #plt.imshow(img)
        #plt.show()
        return p
       
        
        
        
    def brain(self):
        print("Game is Started ")
        self.display_Game()
        
        
            
    def chance(self):
        if(self.position_x==30 and self.position_y==30):
            print("You win")
            self.display_Game()
            return
        val=  self.chance_generator()
        self.movement(val,self.level)
        self.source_destination()
        x=self.display_Game()
        print("You Got :-",val)
        l=[x,val]
        return l
            
            


app = Flask(__name__)
# Define the global Snake instance outside the function
s = None

@app.route("/", methods=["GET"])
def brain():
    global s
    s = Snake()
    s.brain()
     # Access the global variable
    print("get")
    return render_template("index.html",scr1="./static/snake2.png"  ,scr2="./static/d1.png")

@app.route("/", methods=["POST"])
def brain2():
     # Access the global variable
    if request.method == "POST":
        print("post")
        res = s.chance()
        return render_template("index.html", scr1=res[0] ,scr2="./static/d{}.png".format(res[1]))
        
    



if __name__ == "__main__":
    
    app.run()

        

        
            
