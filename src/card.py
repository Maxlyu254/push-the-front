from PIL import Image, ImageFont, ImageDraw

UNIT = 36
DIE_DICT = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}
SUIT_DICT = {"spade": "♠", "heart": "♥", "diamond": "♦", "club": "♣", "spade0": "♤", "heart0": "♡", "diamond0": "♢", "empty_club": "♧"}

ARIAL_PATH = "../fonts/ARIAL.TTF"
TIMES_PATH = "../fonts/TIMES.TTF"
CONSOLA_PATH = "../fonts/CONSOLA.TTF"
ARIALB_PATH = "../fonts/ARIALBD.TTF"
SIMHEI_PATH = "../fonts/simhei.ttf"
SEGOEUI_PATH = "../fonts/SEGOEUI.TTF"
SEGUISYM_PATH = "../fonts/SEGUISYM.TTF"
SYMBOL_PATH = "../fonts/SYMBOL.TTF"
DENGB_PATH = "../fonts/DENGB.TTF"

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

def draw_unit_card(name, stats, suit, desc):
  img = Image.new(mode="RGB", size=(20*UNIT, 30*UNIT), color="white")
  draw = ImageDraw.Draw(img)

  # card background color
  draw.rounded_rectangle((UNIT, UNIT, 19*UNIT, 28*UNIT), fill="#FBE3D6", radius=UNIT)

  # card description panel
  draw.rectangle((UNIT, 18*UNIT, 19*UNIT, 27*UNIT), fill="#C9B6AB")

  # name banner
  draw.arc((-20*UNIT, -11*UNIT, 40*UNIT, 29.2*UNIT), start=75, end=105, width=3*UNIT, fill="#E4E4E4")
  draw.rectangle((0, 25.6*UNIT, 2.75*UNIT, 28.6*UNIT), fill="#E4E4E4")
  draw.rectangle((17.25*UNIT, 25.6*UNIT, 20*UNIT, 28.6*UNIT), fill="#E4E4E4")

  # cost icon
  draw.rounded_rectangle((0.5*UNIT, 0.5*UNIT, 5*UNIT, 5*UNIT), fill="#FCE53A", radius=UNIT)

  # atk icon
  draw.rounded_rectangle((0.5*UNIT, 25*UNIT, 5*UNIT, 29.5*UNIT), fill="#E97132", radius=UNIT)

  # def icon
  draw.rounded_rectangle((15*UNIT, 25*UNIT, 19.5*UNIT, 29.5*UNIT), fill="#156082", radius=UNIT)

  # draw stats
  draw_centered_text(draw, (0.5*UNIT, 0.5*UNIT, 5*UNIT, 5*UNIT), text=str(stats[0]), font=ARIALB3)
  draw_centered_die(draw, (0.5*UNIT, 25*UNIT, 5*UNIT, 29.5*UNIT), die_num=stats[1], font_size=5*UNIT)
  draw_centered_die(draw, (15*UNIT, 25*UNIT, 19.5*UNIT, 29.5*UNIT), die_num=stats[2], font_size=5*UNIT)

  # draw card name
  draw_centered_text(draw, (0, 26.7*UNIT, 20*UNIT, 29*UNIT), text=name, font=DENGB1_8, fill="black")

  # draw card icon
  card_icon = SUIT_DICT[suit] if suit in SUIT_DICT else suit
  draw_centered_text(draw, (5*UNIT, 5*UNIT, 15*UNIT, 15*UNIT), text=card_icon, font=SEGUISYM10, fill="black")

  # draw card description
  draw_centered_multiline_text(draw, (1.5*UNIT, 18.5*UNIT, 18.5*UNIT, 25*UNIT), text=desc, font=DENGB1_2, fill="black")

  img.show()
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
  draw.text((xy[0] + x_offset, xy[1] + y_offset), multilined_text, anchor="mm", font=font, align="center", fill=fill)


def draw_centered_die(draw, xy, die_num, font_size, fill='white'):
  die_font = ImageFont.truetype(SEGUISYM_PATH, size=font_size)
  assert 0 <= die_num < 1000
  if 1 <= die_num <= 6:
    die_xy = [xy[0], xy[1] - font_size * 0.05, xy[2], xy[3] - font_size * 0.05]
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
  img = draw_unit_card("一个长名字", [1, 1, 100], "spade", "这是一个非常长的描述，该描述的目的是为了测试文本分行是否在正常工作。同时，为了保证我们能在同一个文本里写下粗体和非粗体的文本，我们会要用pillow写一个脚本，或者尝试换一个图像库完成这件事。")
  img.save("../img_out/test.jpg", "JPEG")