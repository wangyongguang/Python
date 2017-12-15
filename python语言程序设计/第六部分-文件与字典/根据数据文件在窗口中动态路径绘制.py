import turtle
def main():
    turtle.title('数据驱动的动态路径绘制')
    turtle.setup(800,600,0,0)
    pen = turtle.Turtle()
    pen.color("red")
    pen.width(5)
    pen.shape("turtle")
    pen.speed(5)
    result =[]
    file = open("/Users/Milton/百度云同步盘/python/python语言程序设计/第六部分-文件与字典/data.txt","r")
    for line in file:
        result.append(list(map(float,line.split(','))))
    print(result)
    for i in range(len(result)):
        pen.color((result[i][3],result[i][4],result[i][5]))
        pen.forward(result[i][0])
        if result[i][1]:
            pen.rt(result[i][2])
        else:
            pen.lt(result[i][2])
    pen.goto(0,0)

if __name__=='__main__':
        main()
