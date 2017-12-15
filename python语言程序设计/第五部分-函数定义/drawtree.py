from turtle import Turtle,mainloop

def tree(plist,l,a,f):
    """ plist is list of pens
    l is length of branch
    a is half of the angle between 2 branches
    f is factor by which branch is shortened from level to level.
    """
    if l>5:
        lst = []
        for p in plist:
            p.forward(l)#沿着当前的方向画画
            q = p.clone()#Create and return a clone of the turtle with same position,heading
            p.left(a)
            q.right(a)
            lst.append(p)#将元素增加到列表最后
            lst.append(q)
        tree(lst,l*f,a,f)
        
def main():
    p = Turtle()
    p.color("green")
    p.pensize(5)
    #p.setundobuffer(None)
    p.hideturtle()
    #Make the turtle invisible.It's a good idea to do this while you're in the middle of doing some
    #complex drawing,because hiding the turtle speeds up the drawing observably.
    p.speed(10)
    # p.getscreen().tracer(30,0)
    #return the TurtleScreen object the turtle is drawing on. TurtleScreen methods can then be called
    #for that object.
    p.left(90)#Turn turtle left by angle units.direction调整画笔
    p.penup() #Pull the pen up-no drawing when moving.
    p.goto(0,-200)#Move turtle to an absolute position.
    #if the pen is down,draw line.Do not change the turtle's orientation.
    p.pendown()#Pull the pen down -drawing when moving.这三条语句是一个组合相当于先把
    #画笔移动到指定位置，再把笔放下开始画，否则turtle一移动就好自动把线画出来、
    t = tree([p],110,65,0.6375)
    
main()
