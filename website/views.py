from fileinput import filename
from flask import Blueprint, render_template
import ast

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    # out = open(r'ping.py', 'r').read()
    # exec(out)

    with open("convert.txt", "r") as data:
        dictionary = ast.literal_eval(data.read())
        # print(dictionary)

    return render_template('home.html', dictionary=dictionary)
