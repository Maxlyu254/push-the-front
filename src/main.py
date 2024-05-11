import sys
from batch import *

if __name__ == "__main__":
  if len(sys.argv) == 2:
    draw_cards_from_json(os.path.join("./json_in", sys.argv[1]))
  elif len(sys.argv) == 3: 
    assert sys.argv[2] == "d"
    draw_tts_deck_from_json(os.path.join("./json_in", sys.argv[1]))
  