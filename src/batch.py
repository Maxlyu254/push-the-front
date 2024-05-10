import json
import os
import codecs
from card import draw_unit_card

IN_PATH = "../json_in/"
OUT_PATH = "../img_out/"

NAME="Name"
TYPE="Type"
COST="Cost"
ATK="Atk"
DEF="Def"
SUIT="Suit"
DESC="Desc"

UNIT="单位"
COMMAND="指令"

def draw_cards_from_json(path):
  """
  Draw a set of cards from a json file. The path to the json file is specified in path, 
  and the resulting images is saved to the directory "root/img_out/<name_of_json>"
  """
  file_name = os.path.basename(path).split('/')[-1].rsplit('.', 1)[0]
  out_dir_path = os.path.join(OUT_PATH, file_name)
  if not os.path.isdir(out_dir_path):
    os.makedirs(os.path.join(OUT_PATH, file_name), exist_ok=True)
  
  card_count = 0
  with codecs.open(path, encoding="utf-8") as file:
    data = json.load(file)
    for id, card in enumerate(data): 
      # card = data[id]
      assert TYPE in card
      type = card[TYPE]

      if type == UNIT:
        # if the card is a unit
        assert NAME in card
        assert COST in card
        assert ATK in card
        assert DEF in card
        img = draw_unit_card(
          card[NAME], 
          (card[COST], card[ATK], card[DEF]), 
          card[SUIT] if SUIT in card else " ", 
          card[DESC] if DESC in card else ""
        )
        img.save(os.path.join(OUT_PATH, file_name + "/", card[NAME] + ".png"), "PNG")
        card_count += 1

      else:
        # if the card is unkown type
        print("card type unkown, batch process aborted.")
        return card_count
    
    # all cards processed successfully
    print(f"All cards processed successfully, saved {card_count} cards to directory {os.path.join(OUT_PATH, file_name)}")
    return card_count
