from flask import Flask, render_template, request, url_for, redirect, send_file
from forms import PersonalDetails
form = PersonalDetails()


name = request.form['name']

print(name)


