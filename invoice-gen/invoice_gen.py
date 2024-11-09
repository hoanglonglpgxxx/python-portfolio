#Read data from xlsx, then turn into PDF
import pandas as pd
import glob
import os
from fpdf import FPDF

filepaths = glob.glob('invoices/*.xlsx')

#Auto tạo folder pdf nếu chưa có
if not os.path.exists('pdf'):
    os.makedirs('pdf')

for filepath in filepaths:
    filename, date= filepath.split('\\')[1].split('-')

    pdf = FPDF(orientation='p', format='a4', unit='mm')
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=16)
    pdf.cell(50, 16, 'Invoice nr.' + filename, align='L', ln=1, border=0)

    pdf.cell(50, 16, 'Date' + date.split('.xlsx')[0], align='L', ln=1, border=0)

    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    columns = list(df)
    columns = [item.replace('_', ' ').title() for item in columns]
    for index, col in enumerate(columns):
        pdf.set_font(family='Times', style='B', size=10)
        pdf.cell(50 if index in [1, 3] else 30, 10, col, border=1, ln=(index == 4))

    for index, row in df.iterrows():
        pdf.set_font(family='Times', style='B', size=10)
        pdf.cell(30, 10, str(row['product_id']), border=1)
        pdf.cell(50, 10, str(row['product_name']), border=1)
        pdf.cell(30, 10, str(row['amount_purchased']), border=1)
        pdf.cell(50, 10, str(row['price_per_unit']), border=1)
        pdf.cell(30, 10, str(row['total_price']), border=1, ln=1)

    pdf.set_font(family='Times', style='B', size=10)
    pdf.cell(30, 10, 'Total', border=1)
    pdf.cell(50, 10, '', border=1)
    pdf.cell(30, 10, '', border=1)
    pdf.cell(50, 10,'', border=1)
    pdf.cell(30, 10, str(df['total_price'].sum()), border=1, ln=1)

    pdf.set_font(family='Times', style='B', size=10)
    pdf.cell(30, 10, f'The total price is {df["total_price"].sum()}', ln=1)

    pdf.set_font(family='Times', style='B', size=20)
    pdf.cell(30,20, 'TESTTTTTTTTTTTTTTTTTTT')
    # pdf.image(':shark', w=10)

    pdf.output(f"pdf/{filename}-output.pdf")

