import json
import os
import codecs
from PIL import Image
from card import draw_unit_card, draw_command_card, draw_tactic_card, ULEN

IN_PATH = "./json_in/"
OUT_PATH = "./img_out/"

NAME="name"
TYPE="type"
COST="cost"
ATK="atk"
DEF="def"
SUIT="suit"
DESC="desc"

UNIT_TYPES = {"单位", "unit"}
COMMAND_TYPES = {"指令", "command"}
TACTIC_TYPES = {"战术", "tactic"}

DECK_ROW_NUM = 7
DECK_COL_NUM = 10
DECK_SIZE = 69

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
      card_count += 1

      # set all card ids to lower case
      card = { str.lower(key) : card[key] for key in card.keys() }
      img = draw_card_from_dict(card)

      if img == None: 
        # if the card type is unidentified
        print(f"Card {card_count} type unkown, batch process aborted.")
        return card_count

      else: 
        img.save(os.path.join(OUT_PATH, file_name + "/", card[NAME] + ".png"), "PNG")
    
    # all cards processed successfully
    print(f"All cards processed successfully, saved {card_count} cards to directory {os.path.join(OUT_PATH, file_name)}")
    return card_count


def draw_tts_deck_from_json(path):
  """
  Draw an image that can be exported into tts as a custom deck. The deck will contain 
  all cards defined in the designated json file. 
  """
  file_name = os.path.basename(path).split('/')[-1].rsplit('.', 1)[0]
  out_dir_path = os.path.join(OUT_PATH, file_name)
  if not os.path.isdir(out_dir_path):
    os.makedirs(os.path.join(OUT_PATH, file_name), exist_ok=True)
  
  # Make an array to story all deck images. The image should contain 7 * 10 sections. Each section contains
  # one card, and the last section is the hidden face.
  deck_imgs: list[Image.Image] = []

  # create each card image
  card_count = 0
  with codecs.open(path, encoding="utf-8") as file:
    data = json.load(file)
    for id, card in enumerate(data): 
      card_count += 1

      # set all card ids to lower case
      card = { str.lower(key) : card[key] for key in card.keys() }

      # create a new deck image if the current deck images are not enough to hold all cards
      if card_count > len(deck_imgs) * DECK_SIZE:
        deck_imgs.append(Image.new(mode="RGB", size=(20*ULEN*DECK_COL_NUM, 30*ULEN*DECK_ROW_NUM), color="white"))
      
      img = draw_card_from_dict(card)

      if img == None: 
        # if the card type is unidentified
        print(f"Card {card_count} type unkown, batch process aborted.")
        return card_count

      else: 
        deck_imgs[id // DECK_SIZE].paste(img, ((id % DECK_COL_NUM) * 20 * ULEN, (id // DECK_COL_NUM) * 30 * ULEN))

    # all cards processed successfully
    for i, img in enumerate(deck_imgs):
      img.save(os.path.join(OUT_PATH, file_name + "/", f"{file_name}({i}).png"), "PNG")
    print(f"All cards processed successfully, saved {card_count} cards to directory {os.path.join(OUT_PATH, file_name)}, in {i + 1} deck images.")
    return card_count


def draw_card_from_dict(card):

  assert TYPE in card
  card_type = card[TYPE]

  if card_type in UNIT_TYPES: 
    # if the card is a unit
    assert NAME in card
    assert COST in card
    assert ATK in card
    assert DEF in card
    img = draw_unit_card(
      card[NAME], 
      (int(card[COST]), int(card[ATK]), int(card[DEF])), 
      card[SUIT] if SUIT in card else " ", 
      card[DESC] if DESC in card else ""
    )
    return img

  elif card_type in COMMAND_TYPES:
    # if the card is a command
    assert NAME in card
    assert COST in card
    img = draw_command_card(
      card[NAME], 
      (int(card[COST]), ), 
      card[SUIT] if SUIT in card else " ", 
      card[DESC] if DESC in card else ""
    )
    return img

  elif card_type in TACTIC_TYPES:
      # if the card is a tactic
      assert NAME in card
      assert COST in card
      img = draw_tactic_card(
        card[NAME], 
        (int(card[COST]), ), 
        card[SUIT] if SUIT in card else " ", 
        card[DESC] if DESC in card else ""
      )
      return img

  else:
    # card type unidentified
    return None