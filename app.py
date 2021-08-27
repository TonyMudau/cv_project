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
    #PERSONAL_DETAILS
    name = request.form['name']
    last_name = request.form['last_name']
    street = request.form['street']
    suburb = request.form['suburb']
    city = request.form['city']
    province = request.form['province']
    DOB = request.form['DOB']
    email_address = request.form['email_address']
    cell_num = request.form['cell_num']
    #When making checkboxes use exception
    try:
        html = request.form['html']
    except:
        html = ''
    try:
        css = request.form['css']
    except:
         css = ''
    try:
        python = request.form['python']
    except:
        python = ''
    try:
        java = request.form['Java']
    except:
        java = ''
    try:
        javascript = request.form['javascript']
    except:
        javascript = ''
    try:
        sql = request.form['SQL']
    except:
        sql = ''
    

    # CODE
    class PDF(FPDF):
        def header(self):
            # Logo
            # self.image('logo_pb.png', 10, 8, 33)
            # Arial bold 15
            self.set_font('Helvetica', 'B', 13)
            # Move to the right
            self.cell(66)
            # Title
            self.cell(30, 20, f'{name} {last_name}', border=False, ln=1)
            # Line break
            self.ln(10)
        
        #For creating a headding
        def heading(self, heading_title):
            self.set_font('Helvetica', '', 12 )
            #start, h, legnth, h
            self.set_text_color(0,0,255)
            self.cell(10)
            self.cell(0, 0, heading_title)
            self.ln(10)

        def lines(self, i,s,l,e):
            self.line(i, s, l, e)



        def text(self, ans):
            self.set_font('Helvetica', '', 10)
            self.set_text_color(0, 0, 0)
            self.cell(10)
            self.multi_cell(0, 0, ans)
            self.ln(10)

        def paragraph(self, para):
            self.set_font('Helvetica', '', 10)
            self.set_text_color(0, 0, 0)
            self.cell(10)
            self.multi_cell(0, 4, para)
            self.ln(10)


        def footer(self):
            # Position at 1.5 cm from bottom
            self.set_y(-15)
            # Arial italic 8
            self.set_font('Helvetica', 'I', 10)
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
    pdf.lines(21, 44, 190, 44)
    pdf.text(f'Contact number:                 {cell_num}')
    pdf.text(f'Email address:                    {email_address}')
    pdf.paragraph(f"""Date of Birth:                      {DOB}
Residential Area:               {street}, {suburb}, {city}, {province}""")
    pdf.heading('About me')
    pdf.lines(21,80,190,80)
    pdf.paragraph(f"""I am an honest and hard-working individual who believes in quality work, continuous learning and sharing information.
I am interested in learning data science, big-data, mechine learning, user experience and digital marketing. 
My life goal is to contribute to education and financial innovation in Africa. I currently code using {html} {css} {python} {java}""")
    pdf.heading('Education')
    



      
   


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