from flask import Flask, render_template, request, url_for, redirect, send_file
from forms import PersonalDetails
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'LOLU'


#Takes us to home page
@app.route('/', methods=['GET', 'POST'])
def index():
    form = PersonalDetails()
    return render_template('home.html', title='CV maker', form=form)

#Takes us to create page
@app.route('/create1.html', methods=['GET', 'POST'])
def create():
    form = PersonalDetails()
    return render_template('create1.html', title='create cv', form=form)


#
@app.route('/submitted', methods=['GET', 'POST'])
def create_cv():
    from fpdf import FPDF
    from flask import Flask, request
    from forms import PersonalDetails
    form = PersonalDetails()

    # Form data to create cv 
    name = request.form['name']
    last_name = request.form['last_name']
    street = request.form['street']
    suburb = request.form['suburb']
    city = request.form['city']
    province = request.form['province']
    #email_address = request.form['email_address']
    

    # CODE
    class PDF(FPDF):
        def header(self):
            # Logo
            # self.image('logo_pb.png', 10, 8, 33)
            # Arial bold 15
            self.set_font('Times', '', 12)
            # Move to the right
            self.cell(70)
            # Title
            self.cell(30, 10, f'Curriculum Vitae of {name}', border=False, ln=1)
            # Line break
            self.ln(10)

        def heading(self, heading_title):
            self.set_font('Times', '', 15)
            self.set_text_color(0, 0, 255)
            self.cell(10)
            self.cell(0, 0, heading_title)
            self.ln(10)

        def text(self, ans):
            self.set_font('Times', '', 12)
            self.set_text_color(0, 0, 0)
            self.cell(10)
            self.cell(0, 0, ans)
            self.ln(10)

        def footer(self):
            # Position at 1.5 cm from bottom
            self.set_y(-15)
            # Arial italic 8
            self.set_font('Times', 'I', 10)
            # Text color in gray
            self.set_text_color(128)
            # Page number
            self.cell(0, 10, f'page{self.page_no()}', align='C')
    # Create FPDF object
    pdf = PDF('P', 'mm', 'Letter')
    # Add page
    pdf.add_page()
    # set font
    pdf.set_font('Times', '', 12)
    # set page break
    pdf.set_auto_page_break(auto=True, margin=15)

    # CV Page
    pdf.heading('Personal details')
    pdf.text(f'First Names: {name}')
    pdf.text(f'Last Names: {last_name}')
    pdf.text(f'Residential Area: {street}, {suburb}, {city}, {province}')
    #pdf.text(f'Email Address: {email_address}')
    # pdf.text(f'Cell Numbers: {cell_num}')
    # pdf.text(f'Drivers License: {drivers_license}')
    #
    # pdf.heading('Links')
    # pdf.text(f'Personal Projects')
    # pdf.text(f'')
    # pdf.text(f'')
    # pdf.text(f'')

    # pdf.cell(40, 10, f"First Name: {name}", ln=True)
    # pdf.cell(40, 10, f" Hi {name}", ln=True)
    # pdf.cell(40, 10, f"You are {age} years old", ln=True)
    # pdf.cell(40, 10, "Im here to do your home work", ln=True)
    ap = pdf.output("tmp/my_cv.pdf")




    #render_template('home.html', title='CV maker', a=a)

    return render_template('thankyou.html', title='Create Cv', form=form, a=ap)

#download cv 
@app.route('/cvdownload', methods=['GET', 'POST'])
def download_v():

    cv_pdf = ('./tmp/my_cv.pdf')
    return send_file(cv_pdf, as_attachment=True, cache_timeout=0.0)

# @app.route('/base')
# def base():
#     form = UserDetails()
#     return render_template('base.html')

# @app.route('/return-files/')
# def return_files_tut():
# 	try:
# 		return send_file('/C:/Users/mudau/PycharmProjects/resbui/env', attachment_filename='test2.pdf')
# 	except Exception as e:
# 		return str(e)

if __name__ == '__main__':
    app.debug = True
    app.run()