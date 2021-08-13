from fpdf import FPDF
from flask import Flask, request
from forms import UserDetails

#This page will be used to test python code that will be used as logic
#Inside the app.py classes.

























# #Form
# name = request.form['name']
#
# #CODE
# class PDF(FPDF):
#     def header(self):
#         # Logo
#         #self.image('logo_pb.png', 10, 8, 33)
#         # Arial bold 15
#         self.set_font('Times', '', 12)
#         # Move to the right
#         self.cell(70)
#         # Title
#         self.cell(30, 10, f'Curriculum Vitae of {name}', border=False, ln=1)
#         # Line break
#         self.ln(10)
#
#     def heading(self, heading_title):
#         self.set_font('Times', '', 15)
#         self.set_text_color(0,0,255)
#         self.cell(10)
#         self.cell(0, 0, heading_title)
#         self.ln(10)
#
#     def text(self, ans):
#         self.set_font('Times', '', 12)
#         self.set_text_color(0, 0, 0)
#         self.cell(10)
#         self.cell(0, 0, ans)
#         self.ln(10)
#
#
#     def footer(self):
#         # Position at 1.5 cm from bottom
#         self.set_y(-15)
#         # Arial italic 8
#         self.set_font('Times', 'I', 10)
#         # Text color in gray
#         self.set_text_color(128)
#         # Page number
#         self.cell(0, 10, f'page{self.page_no()}', align='C')
#
#
# #Create FPDF object
# pdf = PDF('P', 'mm', 'Letter')
#
# #Add page
# pdf.add_page()
#
# #set font
# pdf.set_font('Times', '', 12)
#
#
# #set page break
# pdf.set_auto_page_break(auto=True, margin=15)
#
# #Form
#
# # last_name = input('what are last name')
# # nationality = input('Nationality')
# # street = input('Street number and name')
# # suburb = input('Suburb')
# # city = input('City')
# # province = input('province')
# # email_address = input('email_address')
# # cell_num = input('cell_num ')
# # drivers_license = input('drivers_license')
# # project_link = input('project_link')
# #
# # high_school_name = input('high_school_name')
# # qualification = input('qualification ')
# # work_experience = input('work_experience')
# # skills = input('skills')
# # extra_activities = input('extra_activities')
# # references = input('references')
# # age = input('what is your age?')
#
# #Page
#
# pdf.heading('Personal details')
# pdf.text(f'First Names: {name}')
# # pdf.text(f'Last Names: {last_name}')
# # pdf.text(f'Nationality: {nationality}')
# # pdf.text(f'Residential Area: {street}, {suburb}, {city}, {province}')
# # pdf.text(f'Email Address: {email_address}')
# # pdf.text(f'Cell Numbers: {cell_num}')
# # pdf.text(f'Drivers License: {drivers_license}')
# #
# # pdf.heading('Links')
# # pdf.text(f'Personal Projects')
# # pdf.text(f'')
# # pdf.text(f'')
# # pdf.text(f'')
#
# # pdf.cell(40, 10, f"First Name: {name}", ln=True)
# # pdf.cell(40, 10, f" Hi {name}", ln=True)
# # pdf.cell(40, 10, f"You are {age} years old", ln=True)
# # pdf.cell(40, 10, "Im here to do your home work", ln=True)
#
#
#
# pdf.output('test1.pdf')