import random
import sys
from tkinter import *

cards = ['AS', 'AC', 'AH', 'AD', 'KS', 'KC', 'KH', 'KD', 'QS', 'QC', 'QH', 'QD', 'JS', 'JC', 'JH', 'JD', 'TS', 'TC',
         'TH', 'TD', 'NS', 'NC',
         'NH', 'ND', 'ES', 'EC', 'EH', 'ED', 'SS', 'SC', 'SH', 'SD']

p = ""
card_symbol = ["S", "C", "H", "D"]

i = 0
k = 0


class fry:
    def __init__(self, iid):
        self.iid = iid
        self.dds = None
        self.dd = None
        self.ddd = None

    def f2(self):
        self.dd = random.sample(cards, 4)
        for c in range(4):
            cards.remove(self.dd[c])

    def f3(self):
        print(self.dd)

    def f4(self):
        self.dds = random.sample(cards, 4)
        for c in range(4):
            cards.remove(self.dds[c])
        for v in range(4):
            self.dd.append(self.dds[v])

    def f5(self):
        global i
        for q in range(8):
            if self.dd[q][0] == 'A':
                i = i + 1
        for O in range(8):
            if self.dd[O][0] == 'K':
                i = i + 1
        for n in range(8):
            if self.dd[n][0] == 'Q':
                i = i + 1
        for m in range(8):
            if self.dd[m][0] == 'J':
                i = i + 1

        if i == 0:
            sys.exit('reshuffle')


user_1 = fry(1)
user_2 = fry(2)
user_3 = fry(3)
user_4 = fry(4)

# points
AS = AC = AH = AD = 14
KS = KC = KH = KD = 13
QS = QC = QH = QD = 12
JS = JC = JH = JD = 11
TS = TC = TH = TD = 10
NS = NC = NH = ND = 9
ES = EC = EH = ED = 8
SS = SC = SH = SD = 7


def ss():
    global p
    p = 'S'
    print('Thurumbu:' + p)
    gg()


def cc():
    global p
    p = 'C'
    print('Thurumbu:' + p)
    gg()


def hh():
    global p
    p = 'H'
    print('Thurumbu:' + p)
    gg()


def dd():
    global p
    p = 'D'
    print('Thurumbu:' + p)
    gg()


# high points for thurumbu
def thurumbu():
    user_1.f2()
    user_1.f3()
    user_2.f2()
    user_3.f2()
    user_4.f2()

    global AS, AC, AH, AD, KS, KC, KH, KD, QS, QC, QH, QD, JS, JC, JH, JD, TS, TC, TH, TD, NS, NC, NH, ND, ES, EC, EH, ED, SS, SC, SH, SD, p
    buttons = Button(text='S', command=ss, font=('Ink Free', 25))
    buttonc = Button(text='C', command=cc, font=('Ink Free', 25))
    buttonh = Button(text='H', command=hh, font=('Ink Free', 25))
    buttond = Button(text='D', command=dd, font=('Ink Free', 25))

    buttons.place(x=100, y=225)
    buttonc.place(x=150, y=225)
    buttonh.place(x=200, y=225)
    buttond.place(x=255, y=225)

    user_1.f4()
    user_2.f4()
    user_3.f4()
    user_4.f4()

    user_1.f5()
    user_2.f5()
    user_3.f5()
    user_4.f5()


def gg():
    global AS, AC, AH, AD, KS, KC, KH, KD, QS, QC, QH, QD, JS, JC, JH, JD, TS, TC, TH, TD, NS, NC, NH, ND, ES, EC, EH, ED, SS, SC, SH, SD, p
    if p == 'S':
        AS = 30
        KS = 29
        QS = 28
        JS = 27
        TS = 26
        NS = 25
        ES = 24
        SS = 23
        aaa()

    elif p == 'C':
        AC = 30
        KC = 29
        QC = 28
        JC = 27
        TC = 26
        NC = 25
        EC = 24
        SC = 23
        aaa()
    elif p == 'H':
        AH = 30
        KH = 29
        QH = 28
        JH = 27
        TH = 26
        NH = 25
        EH = 24
        SH = 23
        aaa()

    elif p == 'D':
        AD = 30
        KD = 29
        QD = 28
        JD = 27
        TD = 26
        ND = 25
        ED = 24
        SD = 23
        aaa()


u = [0, 0, 0, 0]
decks = []
car = ['AS', 'AC', 'AH', 'AD', 'KS', 'KC', 'KH', 'KD', 'QS', 'QC', 'QH', 'QD', 'JS', 'JC', 'JH', 'JD', 'TS', 'TC', 'TH',
       'TD', 'NS', 'NC',
       'NH', 'ND', 'ES', 'EC', 'EH', 'ED', 'SS', 'SC', 'SH', 'SD']
deck = []
l = 0


class pry(fry):
    def __init__(self):
        self.ssss = None
        self.sss = None
        self.ss = None

    def f1(self):
        global u, decks, car, deck, h, AS, AC, AH, AD, KS, KC, KH, KD, QS, QC, QH, QD, JS, JC, JH, JD, TS, TC, TH, TD, NS, NC, NH, ND, ES, EC, EH, ED, SS, SC, SH, SD, l, K
        labeldd = Label(text=self.dd)
        labeldd.place(x=200, y=400)

        etc = Label(text='USER_' + str(self.iid) + ' ENTER THE CARD:')
        etc.place(x=0, y=400)

        entry = Entry(window, font=('Ink Free', 25))
        entry.place(x=0, y=300)

        def jj():
            self.ddd = entry.get()
            kk()

        buttone = Button(text='Enter', command=jj)
        buttone.place(x=0, y=360)

        def kk():
            global u, decks, car, deck, h, AS, AC, AH, AD, KS, KC, KH, KD, QS, QC, QH, QD, JS, JC, JH, JD, TS, TC, TH, TD, NS, NC, NH, ND, ES, EC, EH, ED, SS, SC, SH, SD, l, k
            if len(decks) != 0:
                if self.ddd[1] == decks[0][1]:
                    pass
                else:
                    for w in range(8):
                        if decks[0][1] == self.dd[w][1]:
                            u.insert(4, 0)
            if len(decks) == 0:
                if self.ddd[1] == 'S':
                    AS = AS + 8
                    KS = KS + 8
                    QS = QS + 8
                    JS = JS + 8
                    TS = TS + 8
                    NS = NS + 8
                    ES = ES + 8
                    SS = SS + 8
                elif self.ddd[1] == 'C':
                    AC = AC + 8
                    KC = KC + 8
                    QC = QC + 8
                    JC = JC + 8
                    TC = TC + 8
                    NC = NC + 8
                    EC = EC + 8
                    SC = SC + 8
                elif self.ddd[1] == 'H':
                    AH = AH + 8
                    KH = KH + 8
                    QH = QH + 8
                    JH = JH + 8
                    TH = TH + 8
                    NH = NH + 8
                    EH = EH + 8
                    SH = SH + 8
                elif self.ddd[1] == 'D':
                    AD = AD + 8
                    KD = KD + 8
                    QD = QD + 8
                    JD = JD + 8
                    TD = TD + 8
                    ND = ND + 8
                    ED = ED + 8
                    SD = SD + 8
                else:
                    pass

            card = [AS, AC, AH, AD, KS, KC, KH, KD, QS, QC, QH, QD, JS, JC, JH, JD, TS, TC, TH, TD, NS, NC, NH, ND, ES,
                    EC,
                    EH, ED,
                    SS, SC, SH,
                    SD]

            def bb():
                labeld = Label(text=decks)
                labeld.place(x=200, y=0)

            for i in range(32):
                if self.ddd == car[i]:
                    decks.append(car[i])
                    deck.append(card[i])
                    bb()

            k += 1

            self.ss = set(self.dd)
            self.sss = set(decks)
            self.ssss = list(self.ss.intersection(self.sss))
            self.dd.remove(self.ssss[0])
            self.dd.insert(7, 'xx')

            if len(u) > 4:
                sys.exit("you cheated")
            if len(deck) < 4:
                if l == 0:
                    aaa()
                elif l == 1:
                    bbb()
                elif l == 2:
                    ccc()
                else:
                    ddd()

            if len(deck) == 4:
                k = 0
                if decks[0][1] == 'S':
                    AS = AS - 8
                    KS = KS - 8
                    QS = QS - 8
                    JS = JS - 8
                    TS = TS - 8
                    NS = NS - 8
                    ES = ES - 8
                    SS = SS - 8
                elif decks[0][1] == 'C':
                    AC = AC - 8
                    KC = KC - 8
                    QC = QC - 8
                    JC = JC - 8
                    TC = TC - 8
                    NC = NC - 8
                    EC = EC - 8
                    SC = SC - 8
                elif decks[0][1] == 'H':
                    AH = AH - 8
                    KH = KH - 8
                    QH = QH - 8
                    JH = JH - 8
                    TH = TH - 8
                    NH = NH - 8
                    EH = EH - 8
                    SH = SH - 8
                elif decks[0][1] == 'D':
                    AD = AD - 8
                    KD = KD - 8
                    QD = QD - 8
                    JD = JD - 8
                    TD = TD - 8
                    ND = ND - 8
                    ED = ED - 8
                    SD = SD - 8
                else:
                    pass

                y = max(deck)
                print('MAX = ' + str(y))
                for j in range(4):
                    if y == deck[j]:
                        if l == 0:
                            l = j
                            print('user_' + str(j + 1) + ' won')
                            u.insert(j + 1, u[j] + 1)
                            u.pop(j)
                            print(u)
                        elif l == 1:
                            if j == 3:
                                l = 0
                                print('user_' + str(1) + ' won')
                                u.insert(1, u[0] + 1)
                                u.pop(0)
                                print(u)
                            else:
                                l = j + 1
                                print('user_' + str(j + 2) + ' won')
                                u.insert(j + 2, u[j + 1] + 1)
                                u.pop(j + 1)
                                print(u)
                        elif l == 2:
                            if j < 2:
                                l = j + 2
                                print('user_' + str(j + 3) + ' won')
                                u.insert(j + 3, u[j + 2] + 1)
                                u.pop(j + 2)
                                print(u)
                            else:
                                l = j - 2
                                print('user_' + str(j - 1) + ' won')
                                u.insert(j - 1, u[j - 2] + 1)
                                u.pop(j - 2)
                                print(u)
                        else:
                            if j == 0:
                                l = j + 3
                                print('user_' + str(j + 4) + ' won')
                                u.insert(j + 4, u[j + 3] + 1)
                                u.pop(j + 3)
                                print(u)
                            else:
                                l = j - 1
                                print('user_' + str(j) + ' won')
                                u.insert(j, u[j - 1] + 1)
                                u.pop(j - 1)
                                print(u)

                        if sum(u) < 8:
                            if l == 0:
                                decks.clear()
                                deck.clear()
                                aaa()
                            elif l == 1:
                                decks.clear()
                                deck.clear()
                                bbb()
                            elif l == 2:
                                decks.clear()
                                deck.clear()
                                ccc()
                            elif l == 3:
                                decks.clear()
                                deck.clear()
                                ddd()

                        else:
                            w = max(u)
                            for t in range(4):
                                if w == u[t]:
                                    print('user_' + str(t + 1) + ' is the winner')


def aaa():
    global k
    if k == 0:
        pry.f1(user_1)
    elif k == 1:
        pry.f1(user_2)
    elif k == 2:
        pry.f1(user_3)
    else:
        pry.f1(user_4)
        k = 0


def bbb():
    global k
    if k == 0:
        pry.f1(user_2)
    elif k == 1:
        pry.f1(user_3)
    elif k == 2:
        pry.f1(user_4)
    else:
        pry.f1(user_1)
        k = 0


def ccc():
    global k
    if k == 0:
        pry.f1(user_3)
    elif k == 1:
        pry.f1(user_4)
    elif k == 2:
        pry.f1(user_1)
    else:
        pry.f1(user_2)
        k = 0


def ddd():
    global k
    if k == 0:
        pry.f1(user_4)
    elif k == 1:
        pry.f1(user_1)
    elif k == 2:
        pry.f1(user_2)
    else:
        pry.f1(user_3)
        k = 0


window = Tk()

window.geometry('420x420')
window.title('omi')
window.config(background='#34d8eb')

photo = PhotoImage(file='C:\\Users\\User\\Downloads\\pngimg.com - cards_PNG8488.png')

label = Label(window,
              text='Welcome to omi',
              font=('comic sans', 20, 'bold',),
              fg='#7258bf',
              bg='#da9cdb',
              compound='bottom',
              padx=0,
              pady=0,
              image=photo)
label.pack()

buttont = Button(text='Start', command=thurumbu, activebackground='#7258bf')
buttont.place(x=0, y=0)

window.mainloop()
