from py3markdown.TableWriter import TableWriter
from py3markdown.Writer import Writer

output_file = "example.md"
file = open(output_file, "w+")

# Setup
w = Writer()

# Headers
for i in range(1, 7):
    w.add_header(f"Alien Invasion! (Header level: {i})", i)

# Image
w.add_image("rocket.jpg", "two astronauts on the surface of Mars")
w.add_double_line_break()

# Paragraph
example_paragraph = (
    """“The chances against anything manlike on Mars are a million to one,” he said."""
)

example_paragraph_two = """
Hundreds of observers saw the flame that night and the night after about midnight, and again the night after; 
and so for ten nights, a flame each night. Why the shots ceased after the tenth no one on earth has attempted to explain.
It may be the gases of the firing caused the Martians inconvenience. Dense clouds of smoke or dust, 
visible through a powerful telescope on earth as little grey, fluctuating patches, spread through the clearness 
of the planet’s atmosphere and obscured its more familiar features.
"""

w.add_paragraph(example_paragraph)
w.add_paragraph(example_paragraph_two, 0, "italic")

# Fonts
w.add_text("Italic Text", "italic")
w.add_double_line_break()
w.add_text("Bold Text", "bold")
w.add_double_line_break()
w.add_colored_text("Red Text", "red")
w.add_double_line_break()
w.add_font_changes("Ancient Text", "Papyrus", "2em")
w.add_double_line_break()

# Lists
example_names_list = ["Sara", "Jacob", "Kevin", "Darlene"]
w.add_list(example_names_list, False, 0, "bold")
w.add_double_line_break()

# Superscript / Subscript
w.add_text("E=MC")
w.add_superscript("2")
w.add_double_line_break()
w.add_text("Plants need CO")
w.add_subscript("2")
w.add_double_line_break()

# Code
w.add_double_line_break()
w.add_code_block("This is an example of a code block")
w.add_double_line_break()

# Table
table = TableWriter(["Name", "Job", "Country", "Student Number"])
table.add_row(["Sara", "Student", "France", "33701"])
table.add_row(["Jacob", "IT Admin", "England", "55721"])
table.add_row(["Darlene", "Cartographer", "Kenya", "67789"])
w.add_table(table)

# Save the file
file.write(w.get_stream())
file.close()
