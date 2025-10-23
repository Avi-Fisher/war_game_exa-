from utils import back

def create_player(*name: str) -> dict:

    try:
        name = name[0]
    except:
        name = "Ai"

    hand = []
    won_pile = []

    player = {"name":name,"hand":hand,"won_pile":won_pile}
    return player

def init_game() -> dict:
    game_dict = {}
    user_name = input("Enter your name")

    player1 = create_player(user_name)
    player2 = create_player()

    new_deck = back.create_deck()
    s_deck = back.shuffle(new_deck)
    game_dict["deck"] = s_deck

    player1["hand"] = s_deck[:27]
    game_dict["player_1"] = player1

    player2["hand"] = s_deck[27:]
    game_dict["player_2"] = player2

    return game_dict

def play_round(player_1: dict, player_2: dict)-> None:

    # global player_1
    # global player_2
    #

    cards_play1 = player_1["hand"].pop[0]
    cards_play2 = player_2["hand"].pop[0]

    win = back.compare_cards(cards_play1[0],cards_play2[0])

    if win == "p1":
        player_1["won_pile"] += cards_play1,cards_play2
    if win == "p2":
        player_2["Won_pile"] += cards_play1,cards_play2






















