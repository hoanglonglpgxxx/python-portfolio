#Turn CSV to PDF
from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='p', format='a4', unit='mm')
pdf.set_auto_page_break(auto=False)
df = pd.read_csv('topics.csv')

page_height = pdf.h

def set_footer(pdf_param, title):
    pdf_param.set_y(-15)  # Set the position 15 mm from the bottom

    pdf_param.set_font(family='Times', style='I', size=8)
    pdf_param.set_text_color(180, 180, 180)
    pdf_param.cell(w=0, h=16, txt=title, align='L', ln=1, border=0)

for index, row in df.iterrows():
    for page in range(row['Pages']):
        if page == 0:
            pdf.add_page()
            pdf.set_text_color(100, 100, 100)
            pdf.set_font(family='Times', style='B', size=16)
            pdf.cell(w=0, h=16, txt=row['Topic'], align='L', ln=1, border=0)
            set_footer(pdf, row['Topic'])
        else:
            pdf.add_page()
            set_footer(pdf, row['Topic'])


pdf.output('output.pdf')

