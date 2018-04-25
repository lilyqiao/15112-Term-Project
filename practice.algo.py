
import module_manager  # from course website
module_manager.review()
from tkinter import *
import quandl
import pandas as pd
import matplotlib.pyplot as plt
quandl.ApiConfig.api_key = "mGtMJWKAbxyxUy5fTm5f"  # my APIkey from Quandl acc.



def actualThing():

    ##########################################################
    # getting (end of day stock) data from Quandl: APPL
    ##########################################################

    # paginate=True bc Quandl limits tables API to 10,000 rows per call
    APPL_data = quandl.get_table('WIKI/PRICES', ticker = ['AAPL'],
                            qopts={'columns': ['ticker', 'date', 'adj_close']},
                            date={'gte': '2016-12-31', 'lte': '2017-12-31'},
                            paginate=True)  # code from medium.com

    APPL_new = APPL_data.set_index('date')  # create new data frame.'data' as index
    # APPLdata will be the table I'm using for APPL stock data
    APPLdata = APPL_new.pivot(columns='ticker')  # format adj_close by ticker

    ##########################################################
    # adding Moving Average columns. input step size
    ##########################################################
    length = len(APPLdata.index)  # how many 'rows (w stock p)'

    def MA(n):
        APPL_MA = [0] * (n - 1)
        for i in range(n - 1, length):
            sum = 0
            for j in range(i - (n - 1), i + 1):
                sum += APPLdata.iloc[j][0]
            APPL_MA.append(sum / n)
        ColIndex = ("MA" + str(n))
        APPLdata[ColIndex] = APPL_MA

    MA(5)  # adding column 'MA5' to table APPLdata
    MA(20)  # adding column 'MA20' to table APPLdata

    # debugging purposes:
    print(APPLdata.head(30))  # prints out first 10 rows of entire table




    ########################################################
    # plotting
    ########################################################

    stock = []  # for APPL
    for j in range(length):
        stock += [APPLdata.iloc[j][0]]

    plt.plot(range(length), stock, color="grey")
    plt.plot(range(length), APPLdata["MA5"], color="red")
    plt.plot(range(length), APPLdata["MA20"], color="green")
    plt.ylim(110, 200)
    # ax.set(xlabel="dates", ylabel="$$$")
    plt.legend()
    plt.show() #line pops up


####################################
# user interface
####################################

def init(data):
    data.mode = "startScreen"
    data.image = PhotoImage(file="stock.png")
    data.yes = (277, 260)
    data.no = (277,310)
    data.YesOrNo = data.yes

def mousePressed(event, data):
    # use event.x and event.y
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
        data.root.destroy()  # ummmm
        actualThing()

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

####################################
# use the run function as-is
####################################

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




