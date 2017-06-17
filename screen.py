from papirus import PapirusText, PapirusTextPos

sans_font="/usr/share/fonts/truetype/freefont/FreeSans.ttf"
bold_sans_font="/usr/share/fonts/truetype/freefont/FreeSansBold.ttf"

class Screen:
  def __init__(self, rotation=0):
    self.text = PapirusTextPos(False, rotation=rotation)
    self.text.AddText("", x=0, y=5, size=36, Id="title", font_path=sans_font)
    self.text.AddText("", x=7, y=55, size=16, Id="body", font_path=sans_font)
    self.text.AddText("", x=7, y=75, size=16, Id="footer", font_path=sans_font)

  def update_header(self, text):
    self.text.UpdateText("title", text, font_path=sans_font)

  def update_body(self, text):
    self.text.UpdateText("body", text, font_path=bold_sans_font)

  def update_footer(self, text):
    self.text.UpdateText("footer", text, font_path=bold_sans_font)

  def write(self):
    self.text.WriteAll()
