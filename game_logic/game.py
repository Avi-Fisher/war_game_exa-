def create_player(*name: str) -> dict:

    try:
        name = name[0]
    except:
        name = "Ai"

    hand = []
    won_pile = []

    player = {"name":name,"hand":hand,"won_pile":won_pile}
    return player






