from PIL import Image, ImageFont, ImageDraw

UNIT = 36
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

ARIALB1 = ImageFont.truetype(ARIALB_PATH, size=UNIT)
ARIALB2 = ImageFont.truetype(ARIALB_PATH, size=2*UNIT)
ARIALB3 = ImageFont.truetype(ARIALB_PATH, size=3*UNIT)
DENGB1 = ImageFont.truetype(DENGB_PATH, size=UNIT)
DENGB1_2 = ImageFont.truetype(DENGB_PATH, size=1.2*UNIT)
DENGB1_5 = ImageFont.truetype(DENGB_PATH, size=1.5*UNIT)
DENGB1_8 = ImageFont.truetype(DENGB_PATH, size=1.8*UNIT)
DENGB2 = ImageFont.truetype(DENGB_PATH, size=2*UNIT)
DENGB2_5 = ImageFont.truetype(DENGB_PATH, size=2.5*UNIT)
DENGB3 = ImageFont.truetype(DENGB_PATH, size=3*UNIT)
SEGUISYM10 = ImageFont.truetype(SEGUISYM_PATH, size=10*UNIT)

BKGDBOX = (UNIT, UNIT, 19*UNIT, 28*UNIT)
DESCBOX = (UNIT, 18*UNIT, 19*UNIT, 27*UNIT)
COSTBOX = (UNIT, UNIT, 5*UNIT, 5*UNIT)
ATKBOX = (UNIT, 23.8*UNIT, 5*UNIT, 27.8*UNIT)
DEFBOX = (15*UNIT, 23.8*UNIT, 19*UNIT, 27.8*UNIT)
NAMEBOX = (0, 26.7*UNIT, 20*UNIT, 29*UNIT)
ICONBOX = (5*UNIT, 5*UNIT, 15*UNIT, 15*UNIT)
DESCTEXTBOX = (1.5*UNIT, 18.5*UNIT, 18.5*UNIT, 25*UNIT)

def draw_unit_card(name, stats, suit, desc):
  img = Image.new(mode="RGB", size=(20*UNIT, 30*UNIT), color="white")
  draw = ImageDraw.Draw(img)

  # card background color
  draw.rounded_rectangle(BKGDBOX, fill="#FBE3D6", radius=0.5*UNIT)

  # card description panel
  draw.rectangle(DESCBOX, fill="#C9B6AB")

  # name banner
  draw.arc((-20*UNIT, -11*UNIT, 40*UNIT, 29.2*UNIT), start=75, end=105, width=3*UNIT, fill="#E4E4E4")
  draw.rectangle((0, 25.6*UNIT, 2.75*UNIT, 28.6*UNIT), fill="#E4E4E4")
  draw.rectangle((17.25*UNIT, 25.6*UNIT, 20*UNIT, 28.6*UNIT), fill="#E4E4E4")

  # cost icon
  draw.rounded_rectangle(COSTBOX, fill="#FCE53A", radius=0.5*UNIT)

  # atk icon
  draw.rounded_rectangle(ATKBOX, fill="#E97132", radius=0.5*UNIT)

  # def icon
  draw.rounded_rectangle(DEFBOX, fill="#156082", radius=0.5*UNIT)

  # draw stats
  draw_centered_text(draw, COSTBOX, text=str(stats[0]), font=ARIALB3)
  draw_centered_die(draw, ATKBOX, die_num=stats[1], font_size=5*UNIT)
  draw_centered_die(draw, DEFBOX, die_num=stats[2], font_size=5*UNIT)

  # draw card name
  draw_centered_text(draw, NAMEBOX, text=name, font=DENGB1_8, fill="black")

  # draw card icon
  card_icon = SUIT_DICT[suit] if suit in SUIT_DICT else suit
  draw_centered_text(draw, ICONBOX, text=card_icon, font=SEGUISYM10, fill="black")

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
  draw.text((xy[0] + x_offset, xy[1] + y_offset), multilined_text, anchor="mm", font=font, align="center", spacing=0.5*UNIT, fill=fill)


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
  img = draw_unit_card("一个长名字", [1, 1, 100], "spade", "文本分行正常工作，但是过于长的文本会遮挡住攻击和防御数字，所以还是不能太长")
  img.save("../img_out/test.jpg", "JPEG")