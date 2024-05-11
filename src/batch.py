import json
import os
import codecs
from card import draw_unit_card

IN_PATH = "../json_in/"
OUT_PATH = "../img_out/"



def draw_cards_from_json(path):
  """
  Draw a set of cards from a json file. The path to the json file is specified in path, 
  and the resulting images is saved to the directory "root/img_out/<name_of_json>"
  """
  file_name = os.path.basename(path).split('/')[-1].rsplit('.', 1)[0]
  out_dir_path = os.path.join(OUT_PATH, file_name)
  if not os.path.isdir(out_dir_path):
    os.mkdir(os.path.join(OUT_PATH, file_name))
  
  card_count = 0
  with codecs.open(path, encoding="utf-8") as file:
    data = json.load(file)
    for id in data: 
      card = data[id]
      assert "type" in card
      type = card["type"]

      if type == "unit":
        # if the card is a unit
        assert "name" in card
        assert "cost" in card
        assert "atk" in card
        assert "def" in card
        img = draw_unit_card(
          card["name"], 
          (card["cost"], card["atk"], card["def"]), 
          card["suit"] if "suit" in card else " ", 
          card["desc"] if "desc" in card else ""
        )
        img.save(os.path.join(OUT_PATH, file_name + "/", id + ".png"), "PNG")
        card_count += 1

      else:
        # if the card is unkown type
        print("card type unkown, batch process aborted.")
        return card_count
    
    # all cards processed successfully
    print(f"All cards processed successfully, saved {card_count} cards to directory {os.path.join(OUT_PATH, file_name)}")
    return card_count
