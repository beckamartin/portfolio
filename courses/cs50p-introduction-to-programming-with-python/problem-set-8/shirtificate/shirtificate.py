# CS50 Shirtificate


from fpdf import FPDF


class PDF():
    def __init__(self, name):
        self.pdf = FPDF(orientation="P", unit="mm", format="A4")
        self.pdf.add_page()

        self.pdf.image("shirtificate.png", 15, 80, 180, 0)

        self.pdf.set_font('helvetica', "B", size=50)
        self.pdf.set_xy(10, 40)
        self.pdf.cell(0, 0, txt="CS50 Shirtificate", border=0, align="C")

        self.pdf.set_font('helvetica', size=25)
        self.pdf.set_text_color(255, 255, 255)
        self.pdf.set_xy(10, 130)
        self.pdf.cell(0, 0, txt=f"{name} took CS50", border=0, align="C")

    def save(self):
        self.pdf.output("shirtificate.pdf")


def main():
    name = input("Name: ")

    pdf = PDF(name)

    pdf.save()


if __name__ == "__main__":
    main()