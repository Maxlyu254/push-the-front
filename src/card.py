from PIL import Image, ImageFont, ImageDraw

UNIT = 36
DIE_DICT = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}

ARIAL_PATH = "./fonts/ARIAL.TTF"
TIMES_PATH = "./fonts/TIMES.TTF"
CONSOLA_PATH = "./fonts/CONSOLA.TTF"
ARIALB_PATH = "./fonts/ARIALBD.TTF"
SIMHEI_PATH = "./fonts/simhei.ttf"
SEGOEUI_PATH = "./fonts/SEGOEUI.TTF"
SYMBOL_PATH = "./fonts/SYMBOL.TTF"
DENGB_PATH = "./fonts/DENGB.TTF"

ARIALB1 = ImageFont.truetype(ARIALB_PATH, size=UNIT)
ARIALB2 = ImageFont.truetype(ARIALB_PATH, size=2*UNIT)
ARIALB3 = ImageFont.truetype(ARIALB_PATH, size=3*UNIT)
ARIAL5 = ImageFont.truetype(ARIAL_PATH, size=5*UNIT)
CONSOLA5 = ImageFont.truetype(CONSOLA_PATH, size=5*UNIT)
TIMES5 = ImageFont.truetype(CONSOLA_PATH, size=5*UNIT)
SIMHEI5 = ImageFont.truetype(SIMHEI_PATH, size=5*UNIT)
SEGOEUI5 = ImageFont.truetype(SEGOEUI_PATH, size=5*UNIT)
SYMBOL5 = ImageFont.truetype(SYMBOL_PATH, size=5*UNIT)
DENGB5 = ImageFont.truetype(DENGB_PATH, size=5*UNIT)

def draw_unit_card(name, stats, desc):
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
  draw_centered_text(draw, (0.5*UNIT, 0.5*UNIT, 5*UNIT, 5*UNIT), text="1", font=ARIALB3)
  draw_centered_die(draw, (0.5*UNIT, 25*UNIT, 5*UNIT, 29.5*UNIT), die_num=6, font=DENGB5)

  img.show()


def draw_centered_text(draw, xy, text, font, fill='white'):
  b_width = xy[2] - xy[0]
  b_height = xy[3] - xy[1]
  x_offset = b_width // 2
  y_offset = b_height // 2
  bbox = draw.textbbox((xy[0] + x_offset, xy[1] + y_offset), text, anchor="mm", font=font)
  draw.text((xy[0] + x_offset, xy[1] + y_offset), text, anchor="mm", font=font, align="center", fill=fill)



def draw_centered_die(draw, xy, die_num, font, fill='white'):
  if die_num < 0 or die_num > 999:
    raise RuntimeError("die number not applicable")
  if 1 <= die_num <= 6:
    draw_centered_text(draw, xy, text=DIE_DICT[die_num], font=font, fill=fill)
  else:
    bbox = draw.textbbox((xy[0], xy[1]), "⚂", font=font)
    outline_width = int((bbox[2] - bbox[0]) / 6)
    draw.rectangle(bbox, outline=fill, width=outline_width)
    num_str = str(die_num)
    num_size = int((bbox[3] - bbox[1]) / len(num_str))
    num_font = ImageFont.truetype(ARIALB_PATH, size=num_size)
    draw_centered_text(draw, bbox, text=num_str, font=num_font, fill=fill)
    



if __name__ == "__main__":
  draw_unit_card("东西", ["1", "1", "1"], "描述")