from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font(family = 'Times', size = 12)
f = open("test.txt", "r")
for x in f:
    pdf.cell(200,10, txt = x, ln = 1, align = "L")

pdf.output("test.pdf")


