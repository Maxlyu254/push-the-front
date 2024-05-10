import sys
from batch import *

if __name__ == "__main__":
  assert len(sys.argv) == 2
  draw_cards_from_json(sys.argv[1])
  