# pip install fpdf2

from fpdf import FPDF


class Shirtificate(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 44)
        self.cell(0, 60, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")


def main():
    name = input("Name: ").strip()
    make_shirtificate(name, "shirtificate.pdf")


def make_shirtificate(name, filename):
    pdf = Shirtificate(orientation="P", format="A4")
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()

    # Shirt image, centered horizontally (A4 is 210mm wide)
    image_width = 190
    pdf.image("shirtificate.png", x=(pdf.w - image_width) / 2, y=70, w=image_width)

    # Name in white on the shirt's chest
    pdf.set_font("helvetica", "B", 26)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(130)
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    pdf.output(filename)


if __name__ == "__main__":
    main()