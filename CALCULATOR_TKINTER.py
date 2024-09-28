from tkinter import *
from tkinter import ttk

inputs = [] #inputs
oper = [["+", "-", "*"], ["/", "%", "^"]] #operations
oper1 = ["+", "-", "*", "/", "%", "^"]
ip = "" #input display string
l = "" #for appending into inputs list
op = 0 #for storing the output of the previous computation

def inp( k ): #add input values to the inputs list, ip string and display the input
    global ip
    global l
    global inputs
    ip += str(k)
    ttk.Label( opfrm, text = ip, 
              width = 12, relief = "sunken" , 
              anchor = "e", style="WB.TLabel" ).grid( row = 0, column = 0, columnspan = 3 )
    if( k in oper1 ):
        l += k
    else:
        l += str(k)

def assign(): #assigns inpṇuts to the inputs list
    global inputs
    global l
    global ip
    if( ip == "" ): #for using the answer of the previous computation to be the first input, 
                    #if the first input given in the next computation is an operation
        ip += str(op )
        inputs.append(op)
    if( l in oper1 ):
        inputs.append(l)
    else:
        if( l == "" ):
            pass
        else:
            try:
                inputs.append(int(l))
            except:
                inputs.append(float(l))
    l=""
    
        
def output(): #calculation of output
    global op
    try:
        if( inputs[1] == "+" ):
            op = inputs[0] + inputs[2]
        elif( inputs[1] == "-" ):
            op = inputs[0] - inputs[2]
        elif( inputs[1] == "*" ):
            op = inputs[0] * inputs[2]
        elif( inputs[1] == "/" ):
            op = inputs[0] / inputs[2]
        elif( inputs[1] == "%" ):
            op = inputs[0] % inputs[2]
        elif( inputs[1] == "^" ):
            op = 1
            for i in range( 1, inputs[2] + 1, 1 ): 
                op = op * inputs[0]
        ttk.Label( opfrm, text = op, 
                width = 12, relief = "sunken" ,
                anchor = "e", style="WB.TLabel" ).grid( row = 0, column = 0, columnspan = 3 ) #display the output
    except:
        ttk.Label( opfrm, text = "Error", 
                width = 12, relief = "sunken" ,
                anchor = "e", style="WB.TLabel" ).grid( row = 0, column = 0, columnspan = 3 )

def clr1(): #clear the inputs string and inputs list
    global inputs
    inputs = []
    global ip
    global l
    ip = ""
    l=""

def clr2(): #clears inputs string, inputs list and output label
    global inputs
    inputs = []
    global ip
    global l
    ip = ""
    l=""
    ttk.Label( opfrm, text = ip, 
              width = 12, relief = "sunken" , 
              anchor = "e", style="WB.TLabel" ).grid( row = 0, column = 0, columnspan = 3 )
    
def clr3(): #clear the last input from inputs string, inputs list and output label
    global inputs
    global ip
    global l
    if( l != "" ):
        pass
    else:
        inputs = inputs[:-1]
    ip = ip[:-1]
    l = l[:-1]
    ttk.Label( opfrm, text = ip, 
              width = 12, relief = "sunken" , 
              anchor = "e", style="WB.TLabel" ).grid( row = 0, column = 0, columnspan = 3 )

root = Tk()
root.title( "Calculator" )
root.attributes( "-alpha", 0.9 )
root.iconbitmap(r"C:\Users\Administrator\OneDrive\Desktop\calculator\CalculatorImage.ico")
frm = ttk.Frame( root, width = 50, 
                height = 50 ).grid(row = 0 , column = 0) #frame for input
opfrm = ttk.Frame( root, width = 50, 
                  height = 10, ).grid( row = 0, column = 0) #frame for output
style = ttk.Style()
style.configure("WB.TLabel", foreground = "Black", background = "RoyalBlue", font = ("Helvetica", 20) )
style.configure("WB.TButton", foreground = "Black", background = "RoyalBlue", font = ("Helvetica", 10) )

for i in range( 1, 10, 3 ): #number inputs
    for j in range ( 0, 3, 1 ):
        ttk.Button( frm, text = i+j, width = 8,  
                   command = lambda i = i, j = j: inp( i+j ), 
                   style="WB.TButton" ).grid( row = i, column = j )
ttk.Button( frm, text = 0, width = 8, 
           command = lambda: inp( 0 ), style="WB.TButton" ).grid( row = 10, column = 1 )
ttk.Button( frm, text = ".", width = 8, 
           command = lambda: inp( "." ), style="WB.TButton" ).grid( row = 10, column = 0 )
ttk.Button( frm, text = "ANS", width = 8, 
           command = lambda: [inp(op)], style="WB.TButton" ).grid( row = 10, column = 2 )

for i in range( 0, len(oper), 1 ): #operation inputs
    for j in range ( 0, 3, 1 ):
        ttk.Button( frm, text = oper[i][j], width = 8, 
                   command = lambda i = i, j = j: [assign(), inp( oper[i][j] ), assign()], 
                   style="WB.TButton" ).grid( row = i+12, column = j)
        
ttk.Button( frm, text = "=", width = 8, style="WB.TButton", 
           command = lambda: [assign(), output(), clr1()] ).grid( row = 20, column = 2 ) #calculate the result
ttk.Button( frm, text = "C", width = 8, style="WB.TButton", 
           command = lambda: clr2() ).grid( row = 20, column = 0 ) #clear output label
ttk.Button( frm, text = "X", width = 8, style="WB.TButton", 
           command = lambda: clr3() ).grid( row = 20, column = 1 ) #clear one input

root.mainloop()            