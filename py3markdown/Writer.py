from py3markdown.TableWriter import TableWriter


class Writer:
    def __init__(self, stream=""):
        self.stream = stream
        self.text_styles = ["normal", "italic", "bold"]

    def get_stream(self):
        return self.stream

    def get_stylized_text(self, text, text_style):
        string = ""
        # text needs to be stripped of white space to make the new formatting take effect ("_ text" -> "_text")
        text_stripped = text.strip()
        if text_style != self.text_styles[0]:
            if text_style == self.text_styles[1]:
                string += "_" + text_stripped + "_"
            elif text_style == self.text_styles[2]:
                string += "__" + text_stripped + "__"
            else:
                raise ValueError(
                    "text style is not available, possible values are: "
                    + ", ".join(self.text_styles)
                )
        else:
            string = text
        return string

    def transform_special_characters(self, text):
        string = text
        string = string.replace("*", "\*")
        string = string.replace("`", "\`")
        string = string.replace("_", "\_")
        string = string.replace("{", "\{")
        string = string.replace("}", "\}")
        string = string.replace("[", "\[")
        string = string.replace("]", "\]")
        string = string.replace("(", "\(")
        string = string.replace(")", "\)")
        string = string.replace("#", "\#")
        string = string.replace("+", "\+")
        string = string.replace("-", "\-")
        string = string.replace("!", "\!")
        string = string.replace("&", "&amp;")
        string = string.replace("<", "&lt;")
        return string

    def add_colored_text(self, text, text_color):
        string = ""
        text_stripped = text.strip()
        text_color = text_color.lower()
        string += f'<span style="color:{text_color}">{text_stripped}</span>'
        string += " "
        self.stream += string

    def add_font_changes(self, text, text_font, text_size):
        # <span style="font-family:Papyrus; font-size:4em;">LOVE!</span>
        string = ""
        text_stripped = text.strip()
        if text_font == "" and text_size == "":
            string += " "
        elif text_font == "":
            string += f'<span style="font-size:{text_size}">{text_stripped}</span>'
        elif text_size == "":
            string += f'<span style="font-family:{text_font}">{text_stripped}</span>'
        else:
            string += f'<span style="font-family:{text_font};font-size:{text_size}">{text_stripped}</span>'
        string += " "
        self.stream += string

    def add_superscript(self, text):
        # E=MC<sup>2</sup>
        string = ""
        text_stripped = text.strip()
        string += f"<sup>{text_stripped}</sup>"
        string += " "
        self.stream += string

    def add_subscript(self, text):
        # Plants need CO<sub>2</sub>
        string = ""
        text_stripped = text.strip()
        string += f"<sub>{text_stripped}</sub>"
        string += " "
        self.stream += string

    def add_space(self):
        self.stream += " "

    def add_simple_line_break(self):
        self.stream += "  \n"

    def add_double_line_break(self):
        self.stream += "\n \n"

    def add_tabulation(self, tab_num):
        self.stream += ">" * tab_num

    def add_horizontal_rule(self):
        self.add_double_line_break()
        self.stream += "-----"
        self.add_double_line_break()

    def add_header(self, text, level=1):
        if level < 1 or level > 6:
            raise ValueError("header level must be included in [1,6]")

        self.stream += "#" * level + " "
        self.stream += text + "\n"

    def add_paragraph(self, text, tabulation=0, text_style="normal"):
        if tabulation < 0:
            raise ValueError("tabulation number must be positive")

        self.stream += ">" * tabulation
        self.stream += self.get_stylized_text(
            self.transform_special_characters(text), text_style
        )
        self.add_double_line_break()

    def add_text(self, text, text_style="normal"):
        self.stream += self.get_stylized_text(
            self.transform_special_characters(text), text_style
        )

    def add_list(self, text, num_style_list=False, tabulation=0, text_style="normal"):
        if type(text) is not list:
            raise ValueError("request a list of string")

        if tabulation < 0:
            raise ValueError("tabulation number must be positive")

        for i in range(0, len(text)):
            if num_style_list is False:
                self.stream += ">" * tabulation
                self.stream += "+ "
                self.stream += self.get_stylized_text(text[i], text_style)
                self.add_simple_line_break()
            else:
                self.stream += ">" * tabulation
                self.stream += str(i + 1) + ". "
                self.stream += self.get_stylized_text(text[i], text_style)
                self.add_simple_line_break()

    def add_code_block(self, code_text):
        code_lines = code_text.split("\n")
        self.add_simple_line_break()
        for line in code_lines:
            self.stream += "\t"
            self.stream += line
            self.add_simple_line_break()

    def add_code_word(self, code_word):
        self.stream += "`"
        self.stream += code_word
        self.stream += "`"

    def add_link(self, link_url, link_text, link_title=""):
        self.stream += "[" + link_text + "]"
        self.stream += "(" + link_url
        if link_title != "":
            self.stream += ' "' + link_title + '"' + ")"
        else:
            self.stream += ")"

    def add_image(self, image_url, image_title="", alt_text="Alt. text"):
        self.stream += "![" + alt_text + "]"
        self.stream += "(" + image_url + ' "' + image_title + '")'

    def add_image_with_link(
        self, image_url, link_url, image_title="", alt_text="Alt. text"
    ):
        self.stream += "[![" + alt_text + "]"
        self.stream += "(" + image_url + ' "' + image_title + '")]'
        self.stream += "(" + link_url + ")"

    def add_table(self, table):
        if not isinstance(table, TableWriter):
            raise ValueError("request a 'TableWriter' object")
        self.stream += table.get_table()
