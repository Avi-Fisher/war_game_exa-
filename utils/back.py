import all_name_card


def create_card(rank:str,suite:str) -> dict:

    suite_option = all_name_card.suite_name()
    rank_option = all_name_card.rank_name()

    if rank not in rank_option or suite not in suite_option:
        print("Error this velue cant use")
        return None


    dict_card = {"rank":rank, "suite":suite, "value":0}
    dict_values = {"J":11,"Q":12,"K":13,"A":14}
    try:
        num = int(rank)
        dict_card["value"] = num
    except:
        num = dict_values[rank]
        dict_card["value"] = num

    return dict_card

def compare_cards(p1_card:dict, p2_card:dict) -> str:

    if p1_card["value"] > p2_card["value"]:
        return "p1"
    elif p1_card["value"] < p2_card["value"]:
        return "p2"
    elif p1_card["value"] == p2_card["value"]:
        return "war"
    else:
        return "Error"

def create_deck() -> list[dict]:
    full_back = []

    for i in range(13):
        for i2 in range(4):
            card = {}
            card["rank"] = all_name_card.rank_name()[i]
            card["suite"] = all_name_card.suite_name()[i2]
            card["value"] = all_name_card.value()[i]

            full_back.append(card)

    return full_back











# def shuffle(deck:list[dict]) -> list[dict]:

































