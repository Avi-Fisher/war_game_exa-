def create_card(rank:str,suite:str) -> dict:

    suite_option = ["H","C","D","S"]
    rank_option = ["2","3", "4","5","6","7","8","9","10","J","Q","K","A"]

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
















# def create_deck() -> list[dict]:
#
# def shuffle(deck:list[dict]) -> list[dict]:

































