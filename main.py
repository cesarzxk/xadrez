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
        self.ids = {

        }
        self.montar_tabuleiro()
        

    def seleciona(self,x,y, cor):
        self.linha[x][y].config(bg="#52c0ff")

        print

        if (self.sel1_x  == x and  self.sel1_y  == y):
            self.sel1_x = None
            self.sel1_y = None
            return self.reset_table_colors()


        if self.sel1_x == None:
            # try:
                if(self.linha[x][y]._id == None): 
                    return None
                
                
                self.moves_rules(x, y)
                self.sel1_x = x
                self.sel1_y = y
                self.cor1 = cor
            # except:
            #     return self.reset_table_colors()
        
        elif(self.linha[x][y]._isChangeable):
                self.sel2_x = x
                self.sel2_y = y
                self.cor2 = cor

        else:
            self.linha[x][y].config(bg="#FF5271")
       
        if self.sel1_x != None and self.sel2_x !=None:
            self.troca(self.sel1_x,self.sel1_y,self.sel2_x,self.sel2_y,self.cor1,self.cor2)
            self.sel1_x = None
            self.sel1_y = None
            self.sel2_x = None
            self.sel2_y = None
            self.cor1 = None
            self.cor2 = None


    def moves_rules(self, x:int, y:int):
        color = '#75F94D'
        selfObj = self.linha[x][y]

        def verify_has_object(extObj):
            try:
                print(selfObj._variant == extObj._variant)
                if(selfObj._variant == extObj._variant):
                    return {'has': True, 'enemy': False}
                else:
                     return {'has': True, 'enemy': True}
            except:
                 return {'has': False, 'enemy': False}
            
        def change_path_color(x, y):
            result = verify_has_object(self.linha[x][y])
            if(result['has'] and not result['enemy']): 
                return False
            
            self.linha[x][y].config(bg = color)
            self.linha[x][y]._isChangeable = True

            if(result['has']): return False

            return True
           
        if(selfObj._id == 'peao'):
            if(selfObj._isInitial):
                if(selfObj._variant == 'branco'):
                    if not change_path_color(x-1, y): return None
                    change_path_color(x-2, y)
                else:
                    if not change_path_color(x+1, y): return None
                    print(change_path_color(x+2, y))
            else:
                if(selfObj._variant == 'branco'):
                   change_path_color(x-1, y)
                else:
                   change_path_color(x+1, y)

        if(selfObj._id == 'bispo'):
            ignore_after_here = [False, False, False, False]
            print(ignore_after_here)

            for y2 in range (8):
                if(x+y2 <= 7 and y+y2 <= 7 ): 
                    change_path_color(x+y2, y+y2)

                if(x-y2 >= 0 and y-y2 >= 0  ): 
                    change_path_color(x-y2, y-y2)
                      
                if(x+y2 <= 7 and y-y2 >= 0  ):
                    change_path_color(x+y2, y-y2)
                        
                if(x-y2 >= 0 and y+y2 <= 7 ):  
                     change_path_color(x-y2, y+y2)

       
        if(selfObj._id == 'torre'):
            for i in range(8):
                change_path_color(x, i)   
                change_path_color(i, y)  
        

        if(selfObj._id == 'rainha'):
            for i in range(8):
                change_path_color(x, i)   
                change_path_color(i, y)

                if(x+i <= 7 and y+i <= 7 ): 
                    change_path_color(x+i, y+i)

                if(x-i >= 0 and y-i >= 0  ): 
                    change_path_color(x-i, y-i)
                        
                if(x+i <= 7 and y-i >= 0  ):
                    change_path_color(x+i, y-i)
                        
                if(x-i >= 0 and y+i <= 7 ):  
                        change_path_color(x-i, y+i)

        if(selfObj._id == 'rei'):
                
            if(x+1 <= 7 and y+1 <= 7 ): 
                change_path_color(x+1, y)
                change_path_color(x+1, y+1)

            if(x-1 >= 0 and y-1 >= 0  ): 
                change_path_color(x-1, y)
                change_path_color(x-1, y-1)
                    
            if(x+1 <= 7 and y-1 >= 0  ):
                change_path_color(x, y-1)
                change_path_color(x+1, y-1)
                    
            if(x-1 >= 0 and y+1 <= 7 ):  
                change_path_color(x, y+1)  
                change_path_color(x-1, y+1)

           
        if(selfObj._id == 'cavalo'):
            if(x+1 <= 7 and y+2 <= 7 ): 
                change_path_color(x+1, y+2)

            if(x+2 <= 7 and y+1 <= 7 ): 
                change_path_color(x+2, y+1)

            if(x-1 >= 0 and y-2 >= 0  ): 
                change_path_color(x-1, y-2)

            if(x-2 >= 0 and y-1 >= 0  ): 
                change_path_color(x-2, y-1)
                    
            if(x+1 <= 7 and y-2 >= 0  ):
               change_path_color(x+1, y-2)

            if(x+2 <= 7 and y-1 >= 0  ):
               change_path_color(x+2, y-1)
                    
            if(x-1 >= 0 and y+2 <= 7 ):  
                change_path_color(x-1, y+2)

            if(x-2 >= 0 and y+1 <= 7 ):  
                change_path_color(x-2, y+1)
    
    

    def troca(self,x1,y1,x2,y2,cor1,cor2):
        print(f"Trocando peças: ({x1}, {y1}) <-> ({x2}, {y2})")

        p1, p2 = self.linha[x1][y1], self.linha[x2][y2]

        if getattr(p1, "_id", None) == "peao":
            p1._isInitial = False

        try:
            if(p1._variant != p2._variant):
                p2.config(image= self.emptyImages['branco'], command=lambda:None)
                p2._isInitial = None
                p2._id = None
        except:
            print('Error ao remover')

        self.linha[x1][y1], self.linha[x2][y2] = p2, p1

        for (x, y, cor) in [(x1, y1, cor1), (x2, y2, cor2)]:
            btn = self.linha[x][y]
            btn.grid(row=x, column=y)
            btn.config(
                command=lambda xi=x, yi=y, ci=cor: self.seleciona(xi, yi, ci),
                bg=cor
            )
        
        self.reset_table_colors()

    def reset_table_colors(self):
        cor1, cor2 = "#ffffff", "#c3c3c3"

        for y in range(8):
            for x in range(8):
                cor = cor1 if (x + y) % 2 == 0 else cor2
                self.linha[x][y].config(bg=cor)
                self.linha[x][y]._isChangeable = False

    def montar_tabuleiro(self):
        self.casa = Frame(self)
        self.casa.grid(row=1)

        cor1, cor2 = "#ffffff", "#c3c3c3"

        pecas = {
            "torre_preto": "pecas/TorreP_B.png",
            "cavalo_preto": "pecas/CavaloP_B.png",
            "bispo_preto": "pecas/BispoP_B.png",
            "rei_preto": "pecas/ReiP_B.png",
            "rainha_preto": "pecas/RainhaP_B.png",
            "peao_preto": "pecas/PeaoP_B.png",

            "torre_branco": "pecas/TorreB_B.png",
            "cavalo_branco": "pecas/CavaloB_B.png",
            "bispo_branco": "pecas/BispoB_B.png",
            "rei_branco": "pecas/ReiB_B.png",
            "rainha_branco": "pecas/RainhaB_B.png",
            "peao_branco": "pecas/PeaoB_B.png",
        }

        self.images = {k: PhotoImage(file=v) for k, v in pecas.items()}
        self.emptyImages = {'branco':PhotoImage(file="pecas/Branco.png"), 'preto':PhotoImage(file="pecas/Preto.png")}
    
        for y in range(8):
            self.linha.append([])
            for x in range(8):
                peca = [cor1, self.emptyImages.get('branco')] if (x + y) % 2 == 0 else [cor2, self.emptyImages.get('preto')]
                btn = Button(self.casa, bg=peca[0])
                btn.grid(row=y, column=x)
                btn.config(image=peca[1], command=lambda yy=y, xx=x, cc=peca[0]: self.seleciona(yy, xx, cc))
                btn._isChangeable = False
                self.linha[y].append(btn)

    
        layout_inicial = {
            0: ["torre_preto", "cavalo_preto", "bispo_preto", "rei_preto", "rainha_preto", "bispo_preto", "cavalo_preto", "torre_preto"],
            1: ["peao_preto"] * 8,
            6: ["peao_branco"] * 8,
            7: ["torre_branco", "cavalo_branco", "bispo_branco", "rei_branco", "rainha_branco", "bispo_branco", "cavalo_branco", "torre_branco"],
        }

        for y, row in layout_inicial.items():
            for x, peca in enumerate(row):
                cor = cor1 if (x + y) % 2 == 0 else cor2
                self.linha[y][x].config(image=self.images[peca], bg=cor,
                                        command=lambda yy=y, xx=x, cc=cor: self.seleciona(yy, xx, cc) )
                tipo, variant = peca.split("_")

                self.linha[y][x]._id = tipo
                self.linha[y][x]._variant = variant

                if(self.linha[y][x]._id == 'peao'):
                    self.linha[y][x]._isInitial = True
            
                self.linha[y][x].image_ref = self.images[peca]  



#Principal
if __name__ == '__main__':
    tabuleiro = Tk()
    tabuleiro.title("Xadrez")
    tabuleiro.resizable(0,0)
    app = Tabuleiro(tabuleiro).grid()
    tabuleiro.mainloop()
