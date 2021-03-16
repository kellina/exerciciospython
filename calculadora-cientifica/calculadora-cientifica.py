# Exercício 05: Crie uma CALCULADORA CIENTÍFICA:
# Crie utilizando a parte gráfica e a base da calculadora feita em sala.
# Deve possuir, além das operações aritméticas básicas (adição, # subtração, divisão e multiplicação),
# a possibilidade de calcular raiz quadrada, potenciação de números, funções trigonométricas (seno, cosseno, tangente).

import tkinter as tk
from tkinter.constants import BOTH, END, GROOVE, LEFT, RIGHT, TRUE
import tkinter.messagebox
import math
from tkinter.font import Font

root = tk.Tk()
root.geometry('650x400+300+300')
root.title('Calculadora Científica')

switch = None

# Quando clicar nos botões
def bt1_click():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '1')

def bt2_click():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '2')

def bt3_click():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '3')

def bt4_click():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '4')

def bt5_click():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '5')

def bt6_click():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '6')

def bt7_click():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '7')

def bt8_click():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '8')

def bt9_click():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '9')

def bt0_click():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '0')

def evento_chave(*args):
    if disp.get() == '0':
        disp.delete(0, END)

def btsoma_click():
    pos = len(disp.get())
    disp.insert(pos, '+')

def btsubt_click():
    pos = len(disp.get())
    disp.insert(pos, '-')

def btmult_click():
    pos = len(disp.get())
    disp.insert(pos, '*')

def btdiv_click():
    pos = len(disp.get())
    disp.insert(pos, '/')

def btc_click(*args):
    disp.delete(0, END)
    disp.insert(0, '0')

def seno_click():
    try:
        resp = float(disp.get())
        if switch is True:
            resp = math.sin(math.radians(resp))
        else:
            resp = math.sin(resp)
        disp.delete(0, END)
        disp.insert(0, str(resp))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Verifique seus valores e operadores")

def coseno_click():
    try:
        resp = float(disp.get())
        if switch is True:
            resp = math.cos(math.radians(resp))
        else:
            resp = math.cos(resp)
        disp.delete(0, END)
        disp.insert(0, str(resp))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Verifique seus valores e operadores")

def tan_click():
    try:
        resp = float(disp.get())
        if switch is True:
            resp = math.tan(math.radians(resp))
        else:
            resp = math.tan(resp)
        disp.delete(0, END)
        disp.insert(0, str(resp))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Verifique seus valores e operadores")

def arcseno_click():
    try:
        resp = float(disp.get())
        if switch is True:
            resp = math.degrees(math.asin(resp))
        else:
            resp = math.asin(resp)
        disp.delete(0, END)
        disp.insert(0, str(resp))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Verifique seus valores e operadores")

def arccoseno_click():
    try:
        resp = float(disp.get())
        if switch is True:
            resp = math.degrees(math.acos(resp))
        else:
            resp = math.acos(resp)
        disp.delete(0, END)
        disp.insert(0, str(resp))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Verifique seus valores e operadores")

def arctan_click():
    try:
        resp = float(disp.get())
        if switch is True:
            resp = math.degrees(math.atan(resp))
        else:
            resp = math.atan(resp)
        disp.delete(0, END)
        disp.insert(0, str(resp))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Verifique seus valores e operadores")

def potencia_click():
    pos = len(disp.get())
    disp.insert(pos, '**')

def arredonda_click():
    try:
        resp = float(disp.get())
        resp = round(resp)
        disp.delete(0, END)
        disp.insert(0, str(resp))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Verifique seus valores e operadores")

def log10_click():
    try:
        resp = float(disp.get())
        resp = math.log10(resp)
        disp.delete(0, END)
        disp.insert(0, str(resp))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Verifique seus valores e operadores")


def fatorial_click():
    try:
        resp = float(disp.get())
        resp = math.factorial(resp)
        disp.delete(0, END)
        disp.insert(0, str(resp))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Verifique seus valores e operadores")


def raiz2_click():
    try:
        resp = float(disp.get())
        resp = math.sqrt(resp)
        disp.delete(0, END)
        disp.insert(0, str(resp))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Verifique seus valores e operadores")


def ponto_click():
    pos = len(disp.get())
    disp.insert(pos, '.')


def pi_click():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.pi))


def expon_click():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.e))


def parent1_click():
    pos = len(disp.get())
    disp.insert(pos, '(')


def parent2_click():
    pos = len(disp.get())
    disp.insert(pos, ')')


def del_clicked():
    pos = len(disp.get())
    display = str(disp.get())
    if display == '':
        disp.insert(0, '0')
    elif display == ' ':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else:
        disp.delete(0, END)
        disp.insert(0, display[0:pos-1])


def conv_click():
    global switch
    if switch is None:
        switch = True
        bt_conv['text'] = "Deg"
    else:
        switch = None
        bt_conv['text'] = "Rad"


def log_click():
    try:
        resp = float(disp.get())
        resp = math.log(resp)
        disp.delete(0, END)
        disp.insert(0, str(resp))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Verifique seus valores e operadores")


def modulo_click():
    pos = len(disp.get())
    disp.insert(pos, '%')


def btigual_click(*args):
    try:
        resp = disp.get()
        resp = eval(resp)
        disp.delete(0, END)
        disp.insert(0, resp)

    except:
        tkinter.messagebox.showerror("Value Error", "Verifique seus valores e operadores")

# Label
data = tk.StringVar()
myFont = Font(family="Segoe", size=20)
disp = tk.Entry(root, font=myFont, fg="black", bg="#abbab1", bd=0, justify=RIGHT, insertbackground="#abbab1", cursor="arrow")
disp.focus_set()
disp.pack(expand=TRUE, fill=BOTH)


def gerarBotao(container, text, command):
    botao = tk.Button(container, text=text, font="Segoe 18", relief=GROOVE, bd=0, command=command, fg="white", bg="#333333", width=3)
    botao.pack(side=LEFT, expand=TRUE, fill=BOTH)
    return botao

# Botoẽs da linha 1
fr_linha1 = tk.Frame(root, bg="#f0f0f0")
fr_linha1.pack(expand=TRUE, fill=BOTH)

bt_pi = gerarBotao(container=fr_linha1, text='π', command=pi_click)
bt_fat = gerarBotao(container=fr_linha1, text='x!', command=fatorial_click)
bt_sen = gerarBotao(container=fr_linha1, text='sin', command=seno_click)
bt_cos = gerarBotao(container=fr_linha1, text='cos', command=coseno_click)
bt_tan = gerarBotao(container=fr_linha1, text='tan', command=tan_click)
bt_1 = gerarBotao(container=fr_linha1, text='1', command=bt1_click)
bt_2 = gerarBotao(container=fr_linha1, text='2', command=bt2_click)
bt_3 = gerarBotao(container=fr_linha1, text='3', command=bt3_click)
bt_soma = gerarBotao(container=fr_linha1, text='+', command=btsoma_click)

# Botoẽs da linha 2
fr_linha2 = tk.Frame(root)
fr_linha2.pack(expand=TRUE, fill=BOTH)

bt_e = gerarBotao(container=fr_linha2, text='e', command=expon_click)
bt_raiz = gerarBotao(container=fr_linha2, text='√x ', command=raiz2_click)
bt_sinh = gerarBotao(container=fr_linha2, text='sinh', command=arcseno_click)
bt_cosh = gerarBotao(container=fr_linha2, text='cosh ', command=arccoseno_click)
bt_tanh = gerarBotao(container=fr_linha2, text='tanh', command=arctan_click)
bt_4 = gerarBotao(container=fr_linha2, text='4', command=bt4_click)
bt_5 = gerarBotao(container=fr_linha2, text='5', command=bt5_click)
bt_6 = gerarBotao(container=fr_linha2, text='6', command=bt6_click)
bt_subt = gerarBotao(container=fr_linha2, text='-', command=btsubt_click)

# Botoões da linha 3
fr_linha3 = tk.Frame(root)
fr_linha3.pack(expand=TRUE, fill=BOTH)

bt_conv = gerarBotao(container=fr_linha3, text='Rad', command=conv_click)
bt_arrend = gerarBotao(container=fr_linha3, text='rnd', command=arredonda_click)
bt_ln = gerarBotao(container=fr_linha3, text='ln', command=log_click)
bt_log = gerarBotao(container=fr_linha3, text='log', command=log10_click)
bt_pot = gerarBotao(container=fr_linha3, text='x^y', command=potencia_click)
bt_7 = gerarBotao(container=fr_linha3, text='7', command=bt7_click)
bt_8 = gerarBotao(container=fr_linha3, text='8', command=bt8_click)
bt_9 = gerarBotao(container=fr_linha3, text='9', command=bt9_click)
bt_mult = gerarBotao(container=fr_linha3, text='x', command=btmult_click)

# Botões da linha 4
fr_linha4 = tk.Frame(root)
fr_linha4.pack(expand=TRUE, fill=BOTH)

bt_mod = gerarBotao(container=fr_linha4, text='%', command=modulo_click)
bt_pesq = gerarBotao(container=fr_linha4, text='(', command=parent1_click)
bt_pdir = gerarBotao(container=fr_linha4, text=')', command=parent2_click)
bt_ponto = gerarBotao(container=fr_linha4, text='.', command=ponto_click)
bt_c = gerarBotao(container=fr_linha4, text='C', command=btc_click)
bt_del = gerarBotao(container=fr_linha4, text='⌫', command=del_clicked)
bt_0 = gerarBotao(container=fr_linha4, text='0', command=bt0_click)
bt_igual = gerarBotao(container=fr_linha4, text='=', command=btigual_click)
bt_div = gerarBotao(container=fr_linha4, text='÷', command=btdiv_click)

root.mainloop()
