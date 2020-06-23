import tkinter
import random


def load_images(card_images):
    suits = ["club", "spade", "diamond", "heart"]
    face_cards = ["jack", "queen", "king"]
    for suit in suits:
        for card_value in range(1, 11):
            name = "cards/{}_{}.png".format(card_value, suit)
            image = tkinter.PhotoImage(file=name)
            card_images.append((suit, image))
    for card in face_cards:
        for suit in suits:
            name = "cards/{}_{}.png".format(card, suit)
            image = tkinter.PhotoImage(file=name)
            card_images.append((suit, image))


def load_player1_cards():
    try:
        global player1_cards
        global player2_available_cards
        global n
        player1_available_cards.append(player1_cards[0])
        next_card = player1_cards.pop(0)
        tkinter.Label(card_frame, image=next_card[1]).grid(row=0, column=0, sticky="w")
        print(player1_cards)
        if n > 0:
            card = previous_card(player2_available_cards)
            if next_card[0] == card[0]:
                player1_available_cards.append(card)
                print("The card is appended for player1")
            n += 1
        turn.set("Player2 Turn")
    except IndexError:
        result_text.set("Player1 Wins!")


def load_player2_cards():
    try:
        global player1_available_cards
        global player2_cards
        global n
        player2_available_cards.append(player2_cards[0])
        next_card = player2_cards.pop(0)
        tkinter.Label(card_frame, image=next_card[1]).grid(row=0, column=2, sticky="e")
        print(player2_cards)
        if n > 0:
            card = previous_card(player1_available_cards)
            if next_card[0] == card[0]:
                player2_available_cards.append(card)
            print("The card is appended for player2")
        n += 1
        turn.set("Player1 Turn")
    except IndexError:
        result_text.set("Player2 Wins!")


def previous_card(card_list):
    return card_list[len(card_list)-1]


def new_frame():
    global card_frame
    card_frame = tkinter.Frame(game_frame, relief="sunken", background="green", borderwidth=1)
    card_frame.grid(row=1, column=1, sticky="ew", columnspan=3)


def new_game():
    global player1_cards
    global player2_available_cards
    global n
    global player1_available_cards
    global player2_cards
    global card_frame
    global deck
    global result_text
    player1_cards.clear()
    player2_available_cards.clear()
    n = 0
    player1_available_cards.clear()
    player2_cards.clear()
    card_frame.destroy()
    new_frame()
    player1_cards = list(deck[0:len(deck)//2])
    player2_cards = list(deck[len(deck)//2:])
    turn.set("Player1 Turn")
    result_text.set("")


main_window = tkinter.Tk()
main_window.geometry("300x300")
main_window.title("Cards_game")
main_window.configure(background="green", borderwidth=1, relief="sunken")
main_window["padx"] = 8
main_window.rowconfigure(0, weight=100)
main_window.rowconfigure(1, weight=100)
main_window.rowconfigure(2, weight=1000)
result_text = tkinter.StringVar()
result = tkinter.Label(main_window, textvariable=result_text, background="green", fg="white")
result.grid(row=0, column=0)
game_frame = tkinter.Frame(main_window, background="green")
game_frame.grid(row=1, column=0, sticky="ew")
game_frame.columnconfigure(0, weight=300)
game_frame.columnconfigure(2, weight=0)
turn = tkinter.StringVar()
turn_text = tkinter.Label(game_frame, textvariable=turn, background="green", fg="black")
turn_text.grid(row=1, column=0, sticky="ew")
turn.set("player1 turn")
card_frame = tkinter.Frame(game_frame, background="green", borderwidth=1)
card_frame.grid(row=1, column=1, sticky="ew", columnspan=3)
button_frame = tkinter.Frame(main_window, background="green")
button_frame.grid(row=2, column=0, sticky="ew")
button_frame.columnconfigure(0, weight=700)
button_frame.columnconfigure(1, weight=0)
player1_button = tkinter.Button(button_frame, text="Player1", command=load_player1_cards)
player1_button.grid(row=0, column=0, sticky="e")
player2_button = tkinter.Button(button_frame, text="Player2", command=load_player2_cards)
player2_button.grid(row=0, column=1, sticky="ew")
new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game)
new_game_button.grid(row=0, column=2)
cards = []
load_images(cards)
deck = list(cards)
random.shuffle(deck)
player1_cards = list(deck[0:len(deck)//2])
player2_cards = list(deck[len(deck)//2:])
player1_available_cards = []
player2_available_cards = []
n = 0
main_window.mainloop()
