##########################################################
# user interaction with different modes
##########################################################

import webScrape
from tkinter import *

import MovingAverages
import MonteCarlo
# import LinearRegression


def everything():  #core of the project is here
    # data.root.destroy()  # Mentor said the other tk pop up is fine
    APPLdata = webScrape.getData()

    # ~~~~~~ prediction section ~~~~~~
    MovingAverages.addMA(APPLdata)
    # MonteCarlo.predict(APPLdata, days)
    # LinearRegression.runRegression(APPLdata, days)


def letsBegin(days=30):  # days: prediction period, default=30
    def init(data):
        data.mode = "startScreen"
        data.image = PhotoImage(file="stock.png")
        data.yes = (277, 260)
        data.no = (277,310)
        data.YesOrNo = data.yes
    def mousePressed(event, data):
        pass
    def keyPressed(event, data):
        if data.mode == "startScreen":
            if data.YesOrNo == data.yes and event.keysym == "Down":
                data.YesOrNo = data.no
            elif data.YesOrNo == data.no and event.keysym == "Up":
                data.YesOrNo = data.yes

            if data.YesOrNo == data.yes and event.keysym == "Return":
                data.mode = "realScreen"
            elif data.YesOrNo == data.no and event.keysym == "Return":
                data.mode = "overScreen"
    def timerFired(data):
        if data.mode == "realScreen":
            everything()  # this is where the cole unfolds
    def redrawAll(canvas, data):
        if data.mode == "startScreen":
            canvas.create_image(0,0, anchor=NW,image=data.image)
            canvas.create_text(data.width/2, data.height/2,
                               text="Ready to make MONEY?",
                               font="Forte 30 bold", fill="white")
            canvas.create_text(300, 260, text="yes",
                               font="Arial 14 bold", fill="white")
            canvas.create_text(300, 310, text="no",
                               font="Arial 14 bold", fill="white")
            canvas.create_text(data.YesOrNo, text="$",
                               font="Arial 14 bold", fill="white")
        if data.mode == "overScreen":
            canvas.create_image(0,0, anchor=NW,image=data.image)
            canvas.create_text(data.width/2, data.height/2,
                               text="$ Alright then, \n have a great day! $",
                               font="Forte 38", fill="white")
    def run(width=300, height=300):
        def redrawAllWrapper(canvas, data):
            canvas.delete(ALL)
            canvas.create_rectangle(0, 0, data.width, data.height,
                                    fill='white', width=0)
            redrawAll(canvas, data)
            canvas.update()

        def mousePressedWrapper(event, canvas, data):
            mousePressed(event, data)
            redrawAllWrapper(canvas, data)

        def keyPressedWrapper(event, canvas, data):
            keyPressed(event, data)
            redrawAllWrapper(canvas, data)

        def timerFiredWrapper(canvas, data):
            timerFired(data)
            redrawAllWrapper(canvas, data)
            # pause, then call timerFired again
            canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
        # Set up data and call init
        class Struct(object): pass
        data = Struct()
        data.width = width
        data.height = height
        data.timerDelay = 100 # milliseconds
        data.root = Tk()
        init(data)
        # create the root and the canvas
        canvas = Canvas(data.root, width=data.width, height=data.height)
        canvas.pack()
        # set up events
        data.root.bind("<Button-1>", lambda event:
                                mousePressedWrapper(event, canvas, data))
        data.root.bind("<Key>", lambda event:
                                keyPressedWrapper(event, canvas, data))
        timerFiredWrapper(canvas, data)
        # and launch the app
        data.root.mainloop()  # blocks until window is closed
        print("bye!")
    run(600, 400)
