def create_cv():
    from fpdf import FPDF
    from flask import Flask, request
    from forms import PersonalDetails
    form = PersonalDetails()

    # Form data to create cv
##PERSONAL_DETAILS
    # name = request.form['name']
    last_name = request.form['last_name']
    street = request.form['street']
    suburb = request.form['suburb']
    city = request.form['city']
    province = request.form['province']
    DOB = request.form['DOB']
    email_address = request.form['email_address']
    cell_num = request.form['cell_num']
    #When making checkboxes use exception
##Computer skills
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
##Interpersonal skills
    try:
        Teamwork = request.form['-Teamwork']
    except:
        Teamwork = ''
    try:
        V_t = request.form['Verbal & written communication']
    except:
         V_t = ''
    try:
        Dependability = request.form['Dependability']
    except:
        Dependability  = ''
    try:
        Responsibility = request.form['Responsibility']
    except:
        Responsibility = ''
    try:
        Empathy = request.form['Empathy']
    except:
        Empathy = ''
    try:
        negotiator = request.form['negotiator']
    except:
        negotiator = ''

##About me 
    learning1 = request.form['learning1']
    learning2 = request.form['learning2']
    learning3 = request.form['learning3']


##Education 
    #high school
    HS_name = request.form['school_name']
    Start_HS = request.form['start_HS_year']
    finish_HS = request.form['finish_HS_year']

    #Uni/college 
    start_college_year = request.form['start_college_year']
    finish_college_year = request.form['finish_college_year']
    college_name = request.form['college_name']
    qualification = request.form['qualification']

##Skills you are interested in 

        

##Online Certificates
    #Certificate 1
    cert_name = request.form['cert_name']
    site = request.form['site']
    cert_date = request.form['cert_name']
    cert_id = request.form['cert_id']

##Other Skills 
    other_skill1 =  request.form['other_skill1']
    other_skill2 =  request.form['other_skill2']
    other_skill3 =  request.form['other_skill3']
    other_skill4 =  request.form['other_skill4']
##Work experience 

##References 

##Volunteering
    

## CODE
    class PDF(FPDF):
        def header(self):
            # Logo
            # self.image('logo_pb.png', 10, 8, 33)
            # Arial bold 15
            self.set_font('Helvetica', 'B', 13)
            # Move to the right
            self.cell(66)
            # Title
            if self.page_no() == 1:
                self.cell(30, 20, f'{last_name} {last_name}', border=False, ln=1)
            else:
                self.cell(30,20," ")
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
##Personal details
    pdf.heading('Personal details')
    pdf.lines(21, 44, 190, 44)
    pdf.text(f'Contact number:                 {cell_num}')
    pdf.text(f'Email address:                    {email_address}')
    pdf.paragraph(f"""Date of Birth:                      {DOB}
Residential Area:               {street}, {suburb}, {city}, {province}""")
##About me 
    pdf.heading('About me')
    pdf.lines(21,92,190,92)
    pdf.paragraph(f"""I am an honest and hard-working individual who believes in quality work, continuous learning and sharing 
information. I am interested in learning {learning1}, {learning2} and {learning3}. My life goal is to contribute to {contribute1} and {contribute2} 
innovation in Africa. I currently code using {html}, {css}, {python} and {java}""")
##Education
    pdf.heading('Education')
    #pdf.lines(21,124,190,124)
    pdf.paragraph(f"""{Start_HS} - {finish_HS}                                                                                     National Senior Certificate
                                                                                                              School: {HS_name}""")
    pdf.paragraph(f"""{start_college_year} - {finish_college_year}                                                                           {qualification}
                                                                                                              School: {college_name}""")
##Certificates
    pdf.heading('Online Certificates')
    pdf.paragraph(f"""   {cert_name}  
    Completed: {cert_date}
    ID:   {cert_id}  """)
##Skills
    pdf.heading(f"""Skills""")
    #pdf.lines(21,170,190,170)

##Interpersonal skills
    pdf.paragraph(f"""Interperonal Skills                                                                       - {Teamwork}
                                                                                                                - {V_t}
                                                                                                                - {Dependability}
                                                                                                                - {Responsibility}
                                                                                                                - {Empathy}
                                                                                                                - {negotiator}""")
##Computer skills
    pdf.paragraph(f"""Computer Skills                                                                           - {javascript}
                                                                                                                - {html} 
                                                                                                                - {css}
                                                                                                                - {python} 
                                                                                                                - {java}
                                                                                                                - {sql}""")
##Other skills
    pdf.paragraph(f"""Other Skills                                                                              - {other_skill1}
                                                                                                                - {other_skill2} 
                                                                                                                - {other_skill3}
                                                                                                                - {other_skill4} 
                                                                                                                        """)
##Work experience 
    pdf.heading('Work Experience')
    #pdf.lines(21,124,190,124)
    pdf.paragraph(f"""2019-2018                                                                                 - Tutor
                                                                                                                - {html} 
                                                                                                                - {css}
                                                                                                                - {python} 
                                                                                                                - {java}
                                                                                                                - {sql}""")
    pdf.paragraph(f"""2019-2018                                                                                 - Tutor
                                                                                                                - {html} 
                                                                                                                - {css}
                                                                                                                - {python} 
                                                                                                                - {java}
                                                                                                                - {sql}""")
##Volunteering
    pdf.heading('Volunteering')
    #pdf.lines(21,124,190,124)
    pdf.paragraph(f"""2019-2018                                                                   - Student Volunteer
                                                                                                        """)
##References
    pdf.heading('References')
    pdf.paragraph(f"""Contact:                                  hgkgfkjtykj
                                                                gjhgfjfgjhj
                                                                ghjhfjfjrf
                                                                """)






      
   


    ap = pdf.output("tmp/my_cv.pdf")




    #render_template('home.html', title='CV maker', a=a)

    return render_template('thankyou.html', title='Create Cv', form=form, a=ap)