from fpdf import FPDF

#Create FPDF object
pdf = FPDF('P', 'mm', 'Letter')

#Add page
pdf.add_page()

#set font
pdf.set_font('Arial', '', 16)

name = input('what is your name')

pdf.cell(40, 10, name)

pdf.out