from PIL import Image, ImageFont, ImageDraw

ULEN = 36 # Unit length
DIE_DICT = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}
SUIT_DICT = {
  "黑桃": "♠", "红桃": "♥", "方片": "♦", "梅花": "♣", 
  "spade": "♠", "heart": "♥", "diamond": "♦", "club": "♣", 
  "spade0": "♤", "heart0": "♡", "diamond0": "♢", "club0": "♧"
}

ARIAL_PATH = "./fonts/ARIAL.TTF"
TIMES_PATH = "./fonts/TIMES.TTF"
CONSOLA_PATH = "./fonts/CONSOLA.TTF"
ARIALB_PATH = "./fonts/ARIALBD.TTF"
SIMHEI_PATH = "./fonts/simhei.ttf"
SEGOEUI_PATH = "./fonts/SEGOEUI.TTF"
SEGUISYM_PATH = "./fonts/SEGUISYM.TTF"
SYMBOL_PATH = "./fonts/SYMBOL.TTF"
DENGB_PATH = "./fonts/DENGB.TTF"

ARIALB1 = ImageFont.truetype(ARIALB_PATH, size=ULEN)
ARIALB2 = ImageFont.truetype(ARIALB_PATH, size=2*ULEN)
ARIALB3 = ImageFont.truetype(ARIALB_PATH, size=3*ULEN)
DENGB1 = ImageFont.truetype(DENGB_PATH, size=ULEN)
DENGB1_2 = ImageFont.truetype(DENGB_PATH, size=1.2*ULEN)
DENGB1_5 = ImageFont.truetype(DENGB_PATH, size=1.5*ULEN)
DENGB1_8 = ImageFont.truetype(DENGB_PATH, size=1.8*ULEN)
DENGB2 = ImageFont.truetype(DENGB_PATH, size=2*ULEN)
DENGB2_5 = ImageFont.truetype(DENGB_PATH, size=2.5*ULEN)
DENGB3 = ImageFont.truetype(DENGB_PATH, size=3*ULEN)
SEGUISYM3 = ImageFont.truetype(SEGUISYM_PATH, size=3*ULEN)
SEGUISYM10 = ImageFont.truetype(SEGUISYM_PATH, size=10*ULEN)

BKGDBOX = (ULEN, ULEN, 19*ULEN, 28*ULEN)
DESCBOX = (ULEN, 18*ULEN, 19*ULEN, 29*ULEN)
BANNERBOX = (ULEN, 16.7*ULEN, 19*ULEN, 19.7*ULEN)
COSTBOX = (ULEN, ULEN, 4*ULEN, 4*ULEN)
TOPLEFTSUITBOX = (ULEN, 4*ULEN, 4*ULEN, 6*ULEN)
ATKBOX = (ULEN, 16.7*ULEN, 5*ULEN, 20.7*ULEN)
DEFBOX = (15*ULEN, 16.7*ULEN, 19*ULEN, 20.7*ULEN)
NAMEBOX = BANNERBOX
ICONBOX = (5*ULEN, 4.5*ULEN, 15*ULEN, 14.5*ULEN)
DESCTEXTBOX = (1.5*ULEN, 20.5*ULEN, 18.5*ULEN, 28.5*ULEN)

BLACK_PALETTE = {"icon": "black", "banner": "black", "name": "white"}
RED_PALETTE = {"icon": "#cc0000", "banner": "#cc0000", "name": "white"}
BLUE_PALETTE = {"icon": "#002244", "banner": "#002244", "name": "white"}
GREEN_PALETTE = {"icon": "#001d3d", "banner": "#001d3d", "name": "white"}

BLACK_SUITS = {"spade0", "spade", "club0", "club", "黑桃", "梅花"}
RED_SUITS = {"heart0", "heart", "diamond0", "diamond", "红桃", "方片"}

def draw_unit_card(name, stats, suit, desc, palette=None):
  img = Image.new(mode="RGB", size=(20*ULEN, 30*ULEN), color="white")
  draw = ImageDraw.Draw(img, "RGBA")

  # decide which palette to use
  if palette == None and suit in BLACK_SUITS:
    palette = BLUE_PALETTE
  elif palette == None and suit in RED_SUITS:
    palette = RED_PALETTE
  else: 
    palette = BLACK_PALETTE

  # card description panel
  draw.rounded_rectangle(DESCBOX, fill=(0, 0, 0, 200), radius=0.5*ULEN)

  # name banner
  draw.rounded_rectangle(BANNERBOX, fill=palette["banner"], radius=0.5*ULEN)
  # draw_banner(draw, BANNERBOX, palette["banner"], "#666666")
  # draw.arc((-20*ULEN, -11*ULEN, 40*ULEN, 29.2*ULEN), start=75, end=105, width=3*ULEN, fill=palette["banner"])
  # draw.rectangle((0, 25.6*ULEN, 2.75*ULEN, 28.6*ULEN), fill=palette["banner"])
  # draw.rectangle((17.25*ULEN, 25.6*ULEN, 20*ULEN, 28.6*ULEN), fill=palette["banner"])

  # atk icon
  draw.rounded_rectangle(ATKBOX, fill="#E97132", radius=0.5*ULEN)

  # def icon
  draw.rounded_rectangle(DEFBOX, fill="#156082", radius=0.5*ULEN)

  # draw stats
  draw_centered_text(draw, COSTBOX, text=str(stats[0]), font=ARIALB3, fill=palette["icon"])
  draw_centered_die(draw, ATKBOX, die_num=stats[1], font_size=5*ULEN)
  draw_centered_die(draw, DEFBOX, die_num=stats[2], font_size=5*ULEN)

  # draw card name
  draw_centered_text(draw, NAMEBOX, text=name, font=DENGB1_8, fill=palette["name"])



  # draw card icon
  card_icon = SUIT_DICT[suit] if suit in SUIT_DICT else suit
  draw_centered_text(draw, ICONBOX, text=card_icon, font=SEGUISYM10, fill=palette["icon"])

  # draw topleft suit
  draw_centered_text(draw, TOPLEFTSUITBOX, text=card_icon, font=SEGUISYM3, fill=palette["icon"])

  # draw card description
  draw_centered_multiline_text(draw, DESCTEXTBOX, text=desc, font=DENGB1_2, fill="white")

  return img


def draw_command_card(name, stats, suit, desc, palette=None):
  img = Image.new(mode="RGB", size=(20*ULEN, 30*ULEN), color="white")
  draw = ImageDraw.Draw(img, "RGBA")

  # decide which palette to use
  if palette == None and suit in BLACK_SUITS:
    palette = BLUE_PALETTE
  elif palette == None and suit in RED_SUITS:
    palette = RED_PALETTE
  else: 
    palette = BLACK_PALETTE

  # card description panel
  draw.rounded_rectangle(DESCBOX, fill=(0, 0, 0, 200), radius=0.5*ULEN)

  # name banner
  draw.rounded_rectangle(BANNERBOX, fill=palette["banner"], radius=0.5*ULEN)
  draw.rectangle((BANNERBOX[0], (BANNERBOX[1] + BANNERBOX[3]) // 2, BANNERBOX[2], BANNERBOX[3]), fill=palette["banner"])

  # draw stats
  draw_centered_text(draw, COSTBOX, text=str(stats[0]), font=ARIALB3, fill=palette["icon"])

  # draw card name
  draw_centered_text(draw, NAMEBOX, text=name, font=DENGB1_8, fill=palette["name"])

  # draw card icon
  card_icon = SUIT_DICT[suit] if suit in SUIT_DICT else suit
  draw_centered_text(draw, ICONBOX, text=card_icon, font=SEGUISYM10, fill=palette["icon"])

  # draw topleft suit
  draw_centered_text(draw, TOPLEFTSUITBOX, text=card_icon, font=SEGUISYM3, fill=palette["icon"])

  # draw card description
  draw_centered_multiline_text(draw, DESCTEXTBOX, text=desc, font=DENGB1_2, fill="white")

  return img



def draw_centered_text(draw, xy, text, font, fill="white"):
  b_width = xy[2] - xy[0]
  b_height = xy[3] - xy[1]
  x_offset = b_width // 2
  y_offset = b_height // 2
  draw.text((xy[0] + x_offset, xy[1] + y_offset), text, anchor="mm", font=font, align="center", fill=fill)


def draw_centered_multiline_text(draw, xy, text, font, fill="white"):
  b_width = xy[2] - xy[0]
  b_height = xy[3] - xy[1]
  x_offset = b_width // 2
  y_offset = b_height // 2
  multilined_text = make_text_multiline(draw, text, font, b_width)
  draw.text((xy[0] + x_offset, xy[1] + y_offset), multilined_text, anchor="mm", font=font, align="center", spacing=0.5*ULEN, fill=fill)


def draw_centered_die(draw, xy, die_num, font_size, fill='white'):
  die_font = ImageFont.truetype(SEGUISYM_PATH, size=font_size)
  assert 0 <= die_num < 1000
  if 1 <= die_num <= 6:
    die_xy = [xy[0], xy[1] - font_size * 0.07, xy[2], xy[3] - font_size * 0.07]
    draw_centered_text(draw, die_xy, text=DIE_DICT[die_num], font=die_font, fill=fill)
  else:
    # First, draw a box that resembles the outline of a die
    die_width = font_size * 0.55
    width = xy[2] - xy[0]
    height = xy[3] - xy[1]
    x_offset = (width - die_width) / 2
    y_offset = (height - die_width) / 2
    die_box = (xy[0] + x_offset, xy[1] + y_offset, xy[0] + x_offset + die_width, xy[1] + y_offset + die_width)
    draw.rectangle(die_box, outline=fill, width=int(font_size * 0.06))
    # Then, draw a number that shows the number on the die if the number is not 0
    if die_num > 0:
      num_font = ImageFont.truetype(ARIALB_PATH, int(font_size * 0.4) / (len(str(die_num)) ** 0.5))
      draw_centered_text(draw, die_box, str(die_num), num_font)


def draw_banner(draw: ImageDraw.ImageDraw, xy, fill1, fill2):
  """
  Draw the shape of a banner. fill1 is the color of the front side of the banner, fill2 is the color of the back.

  :DEPRICATED: This does not look too different from the original, so I wouldn't use it.
  """
  draw.rectangle(get_relative_box(xy, (0, 0, 0.2, 0.875)), fill=fill1)
  draw.rectangle(get_relative_box(xy, (0.8, 0, 1, 0.875)), fill=fill1)
  draw.rectangle(get_relative_box(xy, (0.1, 0.125, 0.9, 1)), fill=fill1)
  draw.rectangle(get_relative_box(xy, (3/32, 28/32, 29/32, 31/32)), fill=fill1)
  draw.rectangle(get_relative_box(xy, (32/160, 1/32, 33/160, 4/32)), fill=fill2)
  draw.rectangle(get_relative_box(xy, (127/160, 1/32, 128/160, 4/32)), fill=fill2)
  draw.rectangle(get_relative_box(xy, (16/160, 1/16, 33/160, 2/16)), fill=fill2)
  draw.rectangle(get_relative_box(xy, (127/160, 1/16, 144/160, 2/16)), fill=fill2)

  draw.ellipse(get_relative_box(xy, (15/160, 15/16, 17/160, 1)), fill=fill1)
  draw.ellipse(get_relative_box(xy, (143/160, 15/16, 145/160, 1)), fill=fill1)
  draw.ellipse(get_relative_box(xy, (15/160, 1/16, 17/160, 2/16)), fill=fill2)
  draw.ellipse(get_relative_box(xy, (143/160, 1/16, 145/160, 2/16)), fill=fill2)
  draw.ellipse(get_relative_box(xy, (31/160, 0, 33/160, 1/16)), fill=fill1)
  draw.ellipse(get_relative_box(xy, (127/160, 0, 129/160, 1/16)), fill=fill1)


def get_relative_box(box, relative_xy):
  """
  Return a new box, positioned relative to the provided box, by the corresponding x and y percentage. 
  e.g. if box = (10, 10, 20, 20), and relative_xy = (0.2, 0.4, 0.6, 0.8), the returned box would be (12, 14, 16, 18)
  """
  w = box[2] - box[0]
  h = box[3] - box[1]
  return (box[0] + relative_xy[0] * w, box[1] + relative_xy[1] * h, box[0] + relative_xy[2] * w, box[1] + relative_xy[3] * h)


def make_text_multiline(draw, text, font, width):
  """
  make a text into multiline so that it does not exceed the given width limit.
  """
  lines = []
  end = 0
  while len(text) > 0:
    bbox = draw.textbbox((0, 0), text[0: end + 1], anchor="mm", font=font, align="center")
    line_width = bbox[2] - bbox[0]
    if line_width > width or end >= len(text):
      lines.append(text[0: end])
      text = text[end: len(text)]
      end = 0
    else: 
      end += 1
  return str.join("\n", lines)


if __name__ == "__main__":
  img = draw_unit_card("黑桃", [5, 5, 6], "spade", "黑桃象征的是军人")
  img.save("./img_out/test.png")
  img.show()
  img = draw_command_card("命令", [3], "club", "命令可以使单位行动")
  img.save("./img_out/test_command.png")
  img.show()