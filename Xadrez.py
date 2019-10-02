from tkinter import *
import time

#Sub-programas
class Tabuleiro(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.linha = [[], [], [], [], [], [], [], [],[]]
        self.sel1_x = None
        self.sel1_y = None
        self.sel2_x = None
        self.sel2_y = None
        self.cor1 = None
        self.cor2 = None
        self.Montar_Tabuleiro()



    def seleciona(self,x,y,cor):
        self.linha[x][y].config(bg="#52c0ff")
        if self.sel1_x == None:
            self.sel1_x = x
            self.sel1_y = y
            self.cor1 = cor
        else:
            self.sel2_x = x
            self.sel2_y = y
            self.cor2 = cor

        if self.sel1_x != None and self.sel2_x !=None:
            self.troca(self.sel1_x,self.sel1_y,self.sel2_x,self.sel2_y,self.cor1,self.cor2)
            self.sel1_x = None
            self.sel1_y = None
            self.sel2_x = None
            self.sel2_y = None
            self.cor1 = None
            self.cor2 = None


    def troca(self,x1,y1,x2,y2,cor1,cor2):
        print(x1,y1,x2,y2)
        temp = self.linha[x1][y1]
        self.linha[x1][y1] = self.linha[x2][y2]
        self.linha[x2][y2] = temp
        self.linha[x1][y1].grid(row=x1, column=y1)
        self.linha[x1][y1].config(command=lambda: self.seleciona(x1, y1, cor1), bg=cor1)
        self.linha[x2][y2].grid(row=x2, column=y2)
        self.linha[x2][y2].config(command=lambda: self.seleciona(x2, y2, cor2), bg=cor2)



    def Montar_Tabuleiro(self):
        self.casa = Frame(self)
        self.casa.grid(row=1)
        cor1 = "#ffffff"
        cor2 = "#c3c3c3",

        ''''Adiciona as peças pretas e brancas ao tabuleiro'''

        for y in range(8):
            for x in range(8):
                if y%2 ==1:
                    if x%2 == 0:
                        self.linha[y].append(Button())
                        img = PhotoImage(file="pecas/Preto.png")
                        self.linha[y][x].config(bg=cor2,image=img)
                        self.linha[y][x].img = img
                        self.linha[y][x].grid(row=y, column=x)

                    else:
                        self.linha[y].append(Button())
                        img = PhotoImage(file="pecas/Branco.png")
                        self.linha[y][x].config(bg=cor1,image=img)
                        self.linha[y][x].img = img
                        self.linha[y][x].grid(row=y, column=x)
                else:
                    if x % 2 == 0:
                        self.linha[y].append(Button())
                        img = PhotoImage(file="pecas/Branco.png")
                        self.linha[y][x].config(bg=cor1,image=img)
                        self.linha[y][x].img = img
                        self.linha[y][x].grid(row=y, column=x)
                    else:
                        self.linha[y].append(Button())
                        img = PhotoImage(file="pecas/Preto.png")
                        self.linha[y][x].config(bg=cor2,image=img)
                        self.linha[y][x].img = img
                        self.linha[y][x].grid(row=y, column=x)


        x = 0
        self.linha[8].append(Label())
        self.linha[8][0].grid(row=0, column=9)









        self.linha[2][0].config( command=lambda: self.seleciona(2, 0, cor1))
        self.linha[2][1].config( command=lambda: self.seleciona(2, 1, cor2))
        self.linha[2][2].config( command=lambda: self.seleciona(2, 2, cor1))
        self.linha[2][3].config( command=lambda: self.seleciona(2, 3, cor2))
        self.linha[2][4].config( command=lambda: self.seleciona(2, 4, cor1))
        self.linha[2][5].config( command=lambda: self.seleciona(2, 5, cor2))
        self.linha[2][6].config( command=lambda: self.seleciona(2, 6, cor1))
        self.linha[2][7].config( command=lambda: self.seleciona(2, 7, cor2))

        self.linha[3][0].config( command=lambda: self.seleciona(3, 0, cor2))
        self.linha[3][1].config( command=lambda: self.seleciona(3, 1, cor1))
        self.linha[3][2].config( command=lambda: self.seleciona(3, 2, cor2))
        self.linha[3][3].config( command=lambda: self.seleciona(3, 3, cor1))
        self.linha[3][4].config( command=lambda: self.seleciona(3, 4, cor2))
        self.linha[3][5].config( command=lambda: self.seleciona(3, 5, cor1))
        self.linha[3][6].config( command=lambda: self.seleciona(3, 6, cor2))
        self.linha[3][7].config( command=lambda: self.seleciona(3, 7, cor1))

        self.linha[4][0].config( command=lambda: self.seleciona(4, 0, cor1))
        self.linha[4][1].config( command=lambda: self.seleciona(4, 1, cor2))
        self.linha[4][2].config( command=lambda: self.seleciona(4, 2, cor1))
        self.linha[4][3].config( command=lambda: self.seleciona(4, 3, cor2))
        self.linha[4][4].config( command=lambda: self.seleciona(4, 4, cor1))
        self.linha[4][5].config( command=lambda: self.seleciona(4, 5, cor2))
        self.linha[4][6].config( command=lambda: self.seleciona(4, 6, cor1))
        self.linha[4][7].config( command=lambda: self.seleciona(4, 7, cor2))

        self.linha[5][0].config( command=lambda: self.seleciona(5, 0, cor2))
        self.linha[5][1].config( command=lambda: self.seleciona(5, 1, cor1))
        self.linha[5][2].config( command=lambda: self.seleciona(5, 2, cor2))
        self.linha[5][3].config( command=lambda: self.seleciona(5, 3, cor1))
        self.linha[5][4].config( command=lambda: self.seleciona(5, 4, cor2))
        self.linha[5][5].config( command=lambda: self.seleciona(5, 5, cor1))
        self.linha[5][6].config( command=lambda: self.seleciona(5, 6, cor2))
        self.linha[5][7].config( command=lambda: self.seleciona(5, 7, cor1))

        '''Inicio das Pretas'''



        img1 = PhotoImage(file="pecas/TorreP_B.png") #Torre Preta
        self.linha[0][0].config(bg=cor1,image=img1, command=lambda: self.seleciona(0,0,cor1))
        self.linha[0][0].img1 = img1


        img2 = PhotoImage(file="pecas/CavaloP_B.png") # Cavalo Preta
        self.linha[0][1].config(bg=cor2,image=img2, command=lambda: self.seleciona(0,1,cor2))
        self.linha[0][1].img2 = img2

        img3 = PhotoImage(file="pecas/BispoP_B.png") # Bispo Preta
        self.linha[0][2].config(bg=cor1,image=img3,command=lambda: self.seleciona(0,2,cor1))
        self.linha[0][2].img3 = img3

        img4 = PhotoImage(file="pecas/ReiP_B.png") # Rei Preta
        self.linha[0][3].config(bg=cor2,image=img4,command=lambda: self.seleciona(0,3,cor2))
        self.linha[0][3].img4 = img4

        img5 = PhotoImage(file="pecas/RainhaP_B.png") # Rainha Preta
        self.linha[0][4].config(bg=cor1,image=img5,command=lambda: self.seleciona(0,4,cor1))
        self.linha[0][4].img5 = img5

        img6 = PhotoImage(file="pecas/BispoP_B.png") # Bispo Preta
        self.linha[0][5].config(bg=cor2,image=img6,command=lambda: self.seleciona(0,5,cor2))
        self.linha[0][5].img6 = img6

        img7 = PhotoImage(file="pecas/CavaloP_B.png") # Cavalo Preta
        self.linha[0][6].config(bg=cor1,image=img7,command=lambda: self.seleciona(0,6,cor1))
        self.linha[0][6].img7 = img7

        img8 = PhotoImage(file="pecas/TorreP_B.png") # Torre Preta
        self.linha[0][7].config(bg=cor2,image=img8,command=lambda: self.seleciona(0,7,cor2))
        self.linha[0][7].img8 = img8

        img8 = PhotoImage(file="pecas/PeaoP_B.png") # Peão Preta
        self.linha[1][0].config(bg=cor2,image=img8,command=lambda: self.seleciona(1,0,cor2))
        self.linha[1][0].img8 = img8

        img8 = PhotoImage(file="pecas/PeaoP_B.png") # Peão Preta
        self.linha[1][1].config(bg=cor1,image=img8,command=lambda: self.seleciona(1,1,cor1))
        self.linha[1][1].img8 = img8

        img = PhotoImage(file="pecas/PeaoP_B.png") # Peão Preta
        self.linha[1][2].config(bg=cor2,image=img,command=lambda: self.seleciona(1,2,cor2))
        self.linha[1][2].img = img

        img = PhotoImage(file="pecas/PeaoP_B.png") # Peão Preta
        self.linha[1][3].config(bg=cor1,image=img,command=lambda: self.seleciona(1,3,cor1))
        self.linha[1][3].img = img

        img = PhotoImage(file="pecas/PeaoP_B.png") # Peão Preta
        self.linha[1][4].config(bg=cor2,image=img,command=lambda: self.seleciona(1,4,cor2))
        self.linha[1][4].img = img

        img = PhotoImage(file="pecas/PeaoP_B.png") # Peão Preta
        self.linha[1][5].config(bg=cor1,image=img,command=lambda: self.seleciona(1,5,cor1))
        self.linha[1][5].img = img

        img = PhotoImage(file="pecas/PeaoP_B.png") # Peão Preta
        self.linha[1][6].config(bg=cor2,image=img,command=lambda: self.seleciona(1,6,cor2))
        self.linha[1][6].img = img

        img = PhotoImage(file="pecas/PeaoP_B.png") # Peão Preta
        self.linha[1][7].config(bg=cor1,image=img,command=lambda: self.seleciona(1,7,cor1))
        self.linha[1][7].img = img

        '''Inicio das Brancas'''

        img = PhotoImage(file="pecas/TorreB_B.png")  # Torre Branca
        self.linha[7][0].config(bg=cor2,image=img,command=lambda: self.seleciona(7, 0, cor2))
        self.linha[7][0].img = img

        img = PhotoImage(file="pecas/CavaloB_B.png") # Cavalo Branca
        self.linha[7][1].config(bg=cor1,image=img,command=lambda: self.seleciona(7, 1, cor1))
        self.linha[7][1].img = img

        img = PhotoImage(file="pecas/BispoB_B.png") # Bispo Branca
        self.linha[7][2].config(bg=cor2,image=img,command=lambda: self.seleciona(7, 2, cor2))
        self.linha[7][2].img11 = img

        img = PhotoImage(file="pecas/ReiB_B.png") # Rei Branca
        self.linha[7][3].config(bg=cor1,image=img,command=lambda: self.seleciona(7, 3, cor1))
        self.linha[7][3].img12 = img

        img = PhotoImage(file="pecas/RainhaB_B.png") # Rainha Branca
        self.linha[7][4].config(bg=cor2,image=img,command=lambda: self.seleciona(7, 4, cor2))
        self.linha[7][4].img = img

        img = PhotoImage(file="pecas/BispoB_B.png") # Bispo Branca
        self.linha[7][5].config(bg=cor1,image=img,command=lambda: self.seleciona(7, 5, cor1))
        self.linha[7][5].img14 = img

        img = PhotoImage(file="pecas/CavaloB_B.png") # Cavalo Branca
        self.linha[7][6].config(bg=cor2,image=img,command=lambda: self.seleciona(7, 6, cor2))
        self.linha[7][6].img15 = img

        img = PhotoImage(file="pecas/TorreB_B.png") # Torre Branca
        self.linha[7][7].config(bg=cor1,image=img,command=lambda: self.seleciona(7, 7, cor1))
        self.linha[7][7].img16 = img

        img = PhotoImage(file="pecas/PeaoB_B.png") # Peão Branca
        self.linha[6][0].config(bg=cor1,image=img,command=lambda: self.seleciona(6, 0, cor1))
        self.linha[6][0].img17 = img

        img = PhotoImage(file="pecas/PeaoB_B.png") # Peão Branca
        self.linha[6][1].config(bg=cor2,image=img,command=lambda: self.seleciona(6, 1, cor2))
        self.linha[6][1].img = img

        img = PhotoImage(file="pecas/PeaoB_B.png") # Peão Branca
        self.linha[6][2].config(bg=cor1,image=img,command=lambda: self.seleciona(6, 2, cor1))
        self.linha[6][2].img = img

        img = PhotoImage(file="pecas/PeaoB_B.png") # Peão Branca
        self.linha[6][3].config(bg=cor2,image=img,command=lambda: self.seleciona(6, 3, cor2))
        self.linha[6][3].img = img

        img = PhotoImage(file="pecas/PeaoB_B.png") # Peão Branca
        self.linha[6][4].config(bg=cor1,image=img,command=lambda: self.seleciona(6, 4, cor1))
        self.linha[6][4].img = img

        img = PhotoImage(file="pecas/PeaoB_B.png") # Peão Branca
        self.linha[6][5].config(bg=cor2,image=img,command=lambda: self.seleciona(6, 5, cor2))
        self.linha[6][5].img = img

        img = PhotoImage(file="pecas/PeaoB_B.png") # Peão Branca
        self.linha[6][6].config(bg=cor1,image=img,command=lambda: self.seleciona(6, 6, cor1,))
        self.linha[6][6].img = img

        img = PhotoImage(file="pecas/PeaoB_B.png") # Peão Branca
        self.linha[6][7].config(bg=cor2,image=img,command=lambda: self.seleciona(6, 7, cor2))
        self.linha[6][7].img = img




'''

def reset():
    Tabuleiro = [['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
                 ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
                 ['◽', '◾', '◽', '◾', '◽', '◾', '◽', '◾'],
                 ['◾', '◽', '◾', '◽', '◾', '◽', '◾', '◽'],
                 ['◽', '◾', '◽', '◾', '◽', '◾', '◽', '◾'],
                 ['◾', '◽', '◾', '◽', '◾', '◽', '◾', '◽'],
                 ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
                 ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']]

def preencher(tab,x,y):
    if (x + y) % 2 == 0:
        tab[x][y] = '◽'
    else:
        tab[x][y] = '◾'
    return None


def imprima():
    for y in range(len(Tabuleiro)):
        for x in range(len(Tabuleiro[y])):
            print(Tabuleiro[y][x], end=" ")
            if x == 7:
                print()

def p1(tab):
    A = input("Entre player 1(branco):").split()
    print(A)
    if A[0] == 'salvar':
        imprima()
        salvar(tab,1.2)
        A = input("Entre player 1(branco):").split()
    if A[0] == 'carregar':
        carregar()
        imprima()
        A = input("Entre player 1(branco):").split()
    if A[0] == 'restart':
        reset()
        imprima()
        A = input("Entre player 1(branco):").split()

    x,y,a,b = int(A[0])-1,int(A[1])-1,int(A[2])-1,int(A[3])-1

    if tab[x][y] == '♟' and ((y == b and a == x + 1) or (y == b and x == 1 and a == x + 2)) or (((a == x+1 and b == y+1) or (a == x+1 and b == y-1)) and tab[a][b] != '◾' and tab[a][b] != '◽'):
        temp = tab[a][b]
        tab[a][b] = tab[x][y]
        preencher(tab,x,y)
        return None

    elif tab[x][y] == '♜' and (y == b or x == a):
        preencher(tab,x,y)
        return None

    else:
        return print("⛔ Movimento inválido ⛔")

def p2(tab):
    A = input("Entre player 1(branco):").split()
    x,y,a,b = int(A[0])-1,int(A[1])-1,int(A[2])-1,int(A[3])-1
    temp = tab[a][b]
    tab[a][b] = tab[x][y]
    if tab[a+1][b] =='◾' or tab[a][b+1] == '◾':
        tab[x][y] ='◾'
    else:
        tab[x][y] = temp
    return None

def salvar(tabuleiro,pl):
    import struct
    forma = struct.Struct('i')
    player = struct.Struct('d')
    try:
        with open("xadrez.bin", "wb") as arq:
          for x in range(len(tabuleiro)):
            for y in range(len(tabuleiro[x])):
                     print(".", end='')
                     if tabuleiro[x][y] == '◽':
                           arq.write(forma.pack(0))
                     elif tabuleiro[x][y] == '◾':
                           arq.write(forma.pack(1))
                     elif tabuleiro[x][y] == '♟':
                           arq.write(forma.pack(2))
                     elif tabuleiro[x][y] == '♙':
                           arq.write(forma.pack(3))
                     elif tabuleiro[x][y] == '♜':
                           arq.write(forma.pack(4))
                     elif tabuleiro[x][y] == '♖':
                           arq.write(forma.pack(5))
                     elif tabuleiro[x][y] == '♞':
                           arq.write(forma.pack(6))
                     elif tabuleiro[x][y] == '♘':
                           arq.write(forma.pack(7))
                     elif tabuleiro[x][y] == '♝':
                           arq.write(forma.pack(8))
                     elif tabuleiro[x][y] == '♗':
                           arq.write(forma.pack(9))
                     elif tabuleiro[x][y] == '♛':
                           arq.write(forma.pack(10))
                     elif tabuleiro[x][y] == '♕':
                           arq.write(forma.pack(11))
                     elif tabuleiro[x][y] == '♚':
                           arq.write(forma.pack(12))
                     elif tabuleiro[x][y] == '♔':
                           arq.write(forma.pack(13))
          arq.write(player.pack(pl))

        print("!Salvo com sucesso!")
    except IOError:
        print("Erro 404!")

def carregar():
    import struct
    forma = struct.Struct('i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i d')
    a = 0
    load=''
    with open("xadrez.bin","rb") as arq:
          arq.seek(0)
          load = forma.unpack(arq.read(forma.size))
          a += 4
          print(load)

'''

#Principal
if __name__ == '__main__':
    tabuleiro = Tk()
    tabuleiro.title("Xadrez")
    tabuleiro.resizable(0,0)
    app = Tabuleiro(tabuleiro).grid()
    tabuleiro.mainloop()
