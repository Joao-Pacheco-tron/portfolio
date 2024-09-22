'''
Projeto simples             Data Limite [SDL]

Descrição:
Montar uma janela com aba para um d6, 2d6 e um d20 
{
Código do d6 / 2d6, já pronto com o que foi encontrado na internet, agora deve pesquisar e montar como 
criar diferentes tela para aba de janela e como as dividir, ou mesmo só fazer uma lista longa com os 
outros tipos.
}
'''
import random
from tkinter import *


class DiceRollerD6(object):
    
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        self.label = Label(master, font=("times",150))
        button= Button(master, text="Rolar dados", command=self.roll)
        button.place(x=160,y=0)
        
    def roll(self):
        symbols = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
        self.label.config(text=f"{random.choice(symbols)}")
        self.label.pack()
        
class DiceRoller2D6(object):
    
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        self.label = Label(master, font=("times",150))
        button= Button(master, text="Rolar dados", command=self.roll)
        button.place(x=160,y=230)
        
    def roll(self):
        symbols = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
        self.label.config(text=f"{random.choice(symbols)}{random.choice(symbols)}")
        self.label.pack()

if __name__ == "__main__":
    root = Tk()
    root.title("Jogo de Dados")
    root.geometry("400x1200")
    DiceRollerD6(root)
    DiceRoller2D6(root)
    root.mainloop()