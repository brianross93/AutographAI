from flask import Blueprint

import os

import openai
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

main = Blueprint('main', __name__)

# Create your routes here.
#Create the post route for the user to enter in a prompt/thesis they want to write an essay for.
# We also need to enter a user id to save the prompt/thesis in the database.

#This is a route that will take in information from the user and save it in the database.

# Create a route for the show_essay.html page to show the user the generated essay from the database model.

@app.route('/show_essay', methods=['GET', 'POST'])
def show_essay():
    if request.method == 'POST':
        user_id = request.form['user_id']
        essay = UserEssay.query.filter_by(user_id=user_id).first()
        # getting an error saving essay to the database
        # A way to fix this would be to add the essay to the database after the user has submitted the essay.
        essay = UserEssay(user_id=user_id, essay=essay)
        return render_template('show_essay.html', essay=essay)
    else:
        return render_template('show_essay.html')



