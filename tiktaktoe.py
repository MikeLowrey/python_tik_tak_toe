import random
from tkinter import *
import tkinter.messagebox

class Table():

    __game_config = {
        'round_switch': True,
        'active_player_color': "green"
    }

    def __init__(self, player1 = None, player2 = None):
        self.player1 = player1
        self.player2 = player2
        self.exists_ki_player = self.exists_ki_player()
        
        self.player = {
            1: {
                'name': "Spieler 2",
                'sign': "X",
                'moves': []
            },
            2: {
                'name': "Spieler 1",
                'sign': "O",
                'moves': []
            },
        }
        if not player1 == None:
            self.player[1]["name"] = player1.get_name()
        if not player2 == None:
            self.player[2]["name"] =  player2.get_name()
        self.win_statistic = WinStatistic()
        self.active_player = 0
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__turns = []

        self._t = tkinter
        self._tk = self._t.Tk()
        self.pane = Frame(self._tk)
        self.pane.pack(fill=BOTH, expand=True)

        self._tk.title("TTT :-)")
        self._tk.minsize(width=300, height=100)
        self.initBtns()
        self.highlights_active_player()
        self._tk.mainloop()

    def exists_ki_player(self):
        if self.player1.is_ki_on() or self.player2.is_ki_on():
            return True
        return False

    def initBtns(self):
        self.win_counter_1 = Button(self.pane, text=self.win_statistic.get_statistic()[0], font='Times 20 bold', bg='gray', fg='white', height=1, width=4, state=DISABLED)
        self.win_counter_1.grid(row=1, column=1, columnspan=8)

        self.win_counter_2 = Button(self.pane, text=self.win_statistic.get_statistic()[1], font='Times 20 bold', bg='gray', fg='white', height=1, width=4, state=DISABLED)
        self.win_counter_2.grid(row=2, column=1, columnspan=8)


        self.label1 = Label(self.pane, text=self.player[1]['name'][:6], font='Times 20 bold', bg='green', fg='black', height=1, width=8)
        self.label1.grid(row=1, column=0)

        self.label2 = Label(self.pane, text=self.player[2]['name'][:6], font='Times 20 bold', bg='white', fg='black', height=1, width=8)
        self.label2.grid(row=2, column=0)

        self.l = []
        self.button1 = Button(self.pane, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.btnClick(self.button1, 0))
        self.button1.grid(row=3, column=0)
        self.l.append(self.button1)

        self.button2 = Button(self.pane, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.btnClick(self.button2, 1))
        self.button2.grid(row=3, column=1)
        self.l.append(self.button2)

        self.button3 = Button(self.pane, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.btnClick(self.button3, 2))
        self.button3.grid(row=3, column=2)
        self.l.append(self.button3)

        self.button4 = Button(self.pane, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.btnClick(self.button4, 3))
        self.button4.grid(row=4, column=0)
        self.l.append(self.button4)

        self.button5 = Button(self.pane, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.btnClick(self.button5, 4))
        self.button5.grid(row=4, column=1)
        self.l.append(self.button5)

        self.button6 = Button(self.pane, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.btnClick(self.button6, 5))
        self.button6.grid(row=4, column=2)
        self.l.append(self.button6)

        self.button7 = Button(self.pane, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.btnClick(self.button7, 6))
        self.button7.grid(row=5, column=0)
        self.l.append(self.button7)

        self.button8 = Button(self.pane, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.btnClick(self.button8, 7))
        self.button8.grid(row=5, column=1)
        self.l.append(self.button8)

        self.button9 = Button(self.pane, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.btnClick(self.button9, 8))
        self.button9.grid(row=5, column=2)
        self.l.append(self.button9)

    def btnClick(self, button, cell):        
        if self.active_player == 0:            
            self.active_player = self.check_how_starts()

        if not self.make_turn(cell):
            return False

        button["text"] = self.player[self.active_player]["sign"]

        self.set_turn(cell)
        self.set_move(cell)

        if self.check_win():
            print("1. player hat gewonnen")
            self.win_statistic.countWin(self.active_player)
            self.win_counter_1["text"] = self.win_statistic.get_statistic()[0]
            self.win_counter_2["text"] = self.win_statistic.get_statistic()[1]

            n = self.player[self.active_player]["name"]
            self._t.messagebox.showinfo("Gewonnen", n + " hat gewonnen!")
            q = self._t.messagebox.askyesno("Nochmal spielen?")
            if q == False:
                quit()
            else:
                self.play_again()
                self.active_player = self.check_how_starts()                
                if self.if_ki():
                    self.make_computer_move()                    
                    self.switch_player()                    
                elif not self.exists_ki_player:                    
                    self.switch_player()
                return


        if self.is_full():
            q = self._t.messagebox.askyesno("Nochmal spielen?")
            if q == False:
                quit()
            else:
                self.play_again()
        
        self.switch_player()
        if self.if_ki():
            self.make_computer_move()
            self.switch_player()
            return
                
        self.switch_player()
        if not self.exists_ki_player:            
            self.switch_player()

    def make_computer_move(self):
        # AI
        # 1. check ob next turn wins
        # 2. check if opotunet win next turn and block field
        # 3 set corners
        # 4 set middle

        e = []
        i = 1
        state = self.state
        for s in state:
            if (s == 0):
                e.append(i)
            i = i + 1        
        cell = random.choice(e)        
        if not self.make_turn(cell-1):
            return False

        self.set_turn(cell-1)
        self.set_move(cell-1)        
        self.l[cell-1]["text"] = self.player[self.active_player]["sign"]

        if self.check_win():
            self.win_statistic.countWin(self.active_player)
            self.win_counter_1["text"] = self.win_statistic.get_statistic()[0]
            self.win_counter_2["text"] = self.win_statistic.get_statistic()[1]
            n = self.player[self.active_player]["name"]
            self._t.messagebox.showinfo("Gewonnen", n + " hat gewonnen!")
            q = self._t.messagebox.askyesno("Nochmal spielen?")
            if q == False:
                quit()
            else:                
                self.play_again()
                self.active_player = self.check_how_starts()                
                if self.if_ki():                    
                    self.make_computer_move()                    
                    return
                else:
                    self.switch_player()                    

        else:
            if self.is_full():
                q = self._t.messagebox.askyesno("Nochmal spielen?")
                if q == False:
                    quit()
                else:
                    self.play_again()



    def if_ki(self):
        if self.player[self.active_player]["name"] == 'KI':
            print("...ki")
            return True
        return False



    def switch_player(self):        
        if self.active_player == 1:
            self.active_player = 2
            self.label1["bg"] = "white"
            self.label2["bg"] = "green"
        elif self.active_player == 2:
            self.active_player = 1
            self.label1["bg"] = "green"
            self.label2["bg"] = "white"        

    def make_turn(self, cell):
        if self.is_valid_turn(cell):
            self.state[cell] = self.active_player            
            return True
        return False

    def is_valid_turn(self, cell):
        if self.state[cell] == 0:
            return True
        else:
            return False

    def play_again(self):        
        self.__turns = []        
        self.player[1]["moves"] = []
        self.player[2]["moves"] = []        
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.check_how_starts()
        self.player1.switch_round()
        self.active_player = 0
        self.initBtns()
        self.check_how_starts()

    def check_how_starts(self):
        return self.player1.get_last_round()

    def check_win(self):
        win_opportunities = [
            {1,2,3},
            {4,5,6},
            {7,8,9},
            {1,4,7},
            {2,5,8},
            {3,6,9},
            {1,5,9},
            {3,5,7}
        ]
        for list in win_opportunities:
            result = all(elem in self.player[self.active_player]["moves"] for elem in list)
            if (result):
                return True
        return False

    def is_full(self):
        for i in self.state:
            if i == 0:
                return False
        return True

    def highlights_active_player(self):
        pass

    def set_move(self, turn):
        self.player[self.active_player]["moves"].append(turn+1)

    def set_turn(self, turn):
        self.__turns.append(turn)

    def get_turns(self):
        return self.__turns

    def close_window(self):
        self._tk.destroy()


class WinStatistic():

    player1 = 0
    player2 = 0

    def __init__(self):
        #self.player1 = 0
        #self.player2 = 0
        pass

    def countWin(self, player):
        if player == 1 :
            self.player1 += 1
        if player == 2 :
            self.player2 += 1

    def get_statistic(self) :
        return (self.player1, self.player2)

class MyKi:
    #ki_on = False

    def __init__(self):
        self.ki_on = False

    def set_ki_status(self, status):        
        self.ki_on = status

    def is_ki_on(self):
        return self.ki_on


class Player(MyKi):

    __turns = []
    __last_round = 1    

    def __init__(self, name='', sign=''):
        MyKi.__init__(self)
        self.__sign = sign
        self.__player_is_ki = False
        if name == '':            
            name = 'KI'
            self.__player_is_ki = True
            MyKi.set_ki_status(self,True)            

        self.__name = name
        self.__moves = []

    def set_name(self, name):
        self.__name = str(name)

    def set_sign(self, sign):
        self.__sign = sign

    def switch_round(self):
        print("switched")
        if self.__last_round == 1:
            self.__last_round = 2
        else:
            self.__last_round = 1

    def set_move(self, move):
        if move in range(1, 9):
            self.__moves.append(move)
            self.__set_turn(move)

    def __set_turn(self, turn):
            self.__turns.append(turn)

    def is_player_ki(self):
        return self.__player_is_ki

    def get_name(self):
        return self.__name

    def get_sign(self):
        return self.__sign

    def get_moves(self):
        return self.__moves

    def get_last_round(self):
        return self.__last_round

    def get_turns(self):
        return self.__turns

# -----------------------------
player1 = Player("Frida Maria")
player2 = Player()

table = Table(player1,player2)
