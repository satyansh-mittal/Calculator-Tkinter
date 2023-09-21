from tkinter import * 

first_number = second_number = operator = None 
previous_color = 'white'

# button functions 

    # get numbers
def get_number(number):
    current = result_label['text']
    # Check if the current text contains a decimal point
    if number == '.' and '.' in current:
        return
    new = current + str(number)
    result_label.config(text=new)
 
    # clear button funtion   
def clear():
    global previous_color
    result_label.config(text='', fg=previous_color)
    previous_color = 'white'
    
    # getting operator input 
def get_operator(op):
    global first_number, operator
    
    first_number = float(result_label['text'])
    operator = op
    result_label.config(text='')
    
    # get the output 
def get_result():
    global first_number,second_number, operator
    
    second_number = float(result_label['text'])
    
    if (operator == '+'):
        result_label.config(text=str(first_number + second_number))
    elif(operator == '-'):
        result_label.config(text=str(first_number - second_number))
    elif(operator == '-'):
        result_label.config(text=str(first_number - second_number))
    elif(operator == '*'): 
        result_label.config(text=str(first_number * second_number))
    elif(operator == '/'):
        if(second_number == 0):
            result_label.config(text='Error!', fg='red')
            previous_color = 'red'
        else:
            result_label.config(text=str(round(first_number / second_number,4)))
            
    
root = Tk()
root.title("Calculator")
root.geometry('280x445')
root.resizable(0,0)
root.configure(background="black")

# RESULT SECTION
result_label = Label(root, text='', bg="black", fg="white")
result_label.grid(row=0, column=0, pady=(50,25), columnspan=4, sticky='e')
result_label.config(font=('verdana',30,"bold"))

        # BUTTONS
# Row 1
btn7 = Button(root,text='7', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_number(7))
btn7.grid(row=1, column=0)
btn7.config(font=('verdana',14))

btn8 = Button(root,text='8', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_number(8))
btn8.grid(row=1, column=1)
btn8.config(font=('verdana',14))

btn9 = Button(root,text='9', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_number(9))
btn9.grid(row=1, column=2)
btn9.config(font=('verdana',14))

btn_div = Button(root,text='/', bg='pink', fg='black', width=5, height=2, command=lambda :get_operator('/'))
btn_div.grid(row=1, column=3)
btn_div.config(font=('verdana',14))

# Row 2
btn4 = Button(root,text='4', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_number(4))
btn4.grid(row=2, column=0)
btn4.config(font=('verdana',14))

btn5 = Button(root,text='5', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_number(5))
btn5.grid(row=2, column=1)
btn5.config(font=('verdana',14))

btn6 = Button(root,text='6', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_number(6))
btn6.grid(row=2, column=2)
btn6.config(font=('verdana',14))

btn_mul = Button(root,text='x', bg='pink', fg='black', width=5, height=2, command=lambda :get_operator('*'))
btn_mul.grid(row=2, column=3)
btn_mul.config(font=('verdana',14))

# Row 3
btn1 = Button(root,text='1', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_number(1))
btn1.grid(row=3, column=0)
btn1.config(font=('verdana',14))

btn2 = Button(root,text='2', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_number(2))
btn2.grid(row=3, column=1)
btn2.config(font=('verdana',14))

btn3 = Button(root,text='3', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_number(3))
btn3.grid(row=3, column=2)
btn3.config(font=('verdana',14))

btn_sub = Button(root,text='-', bg='pink', fg='black', width=5, height=2, command=lambda :get_operator('-'))
btn_sub.grid(row=3, column=3)
btn_sub.config(font=('verdana',14))

# Row 4
btn_clr = Button(root,text='C', bg='#00a65a', fg='white', width=5, height=2, command=lambda :clear())
btn_clr.grid(row=4, column=0)
btn_clr.config(font=('verdana',14))

btn0 = Button(root,text='0', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_number(0))
btn0.grid(row=4, column=1)
btn0.config(font=('verdana',14))

btn_point = Button(root, text='.', bg='pink', fg='black', width=5, height=2, command=lambda: get_number('.'))
btn_point.grid(row=4, column=2)
btn_point.config(font=('verdana', 14))

btn_add = Button(root,text='+', bg='pink', fg='black', width=5, height=2, command=lambda :get_operator('+'))
btn_add.grid(row=4, column=3)
btn_add.config(font=('verdana',14))

# Row 5 - Entire row
btn_equal = Button(root,text='=', bg='yellow', fg='black', width=5, height=2, command=lambda :get_result())
btn_equal.grid(row=5, column=0, columnspan=4, sticky='nsew')
btn_equal.config(font=('verdana',14))

root.mainloop()