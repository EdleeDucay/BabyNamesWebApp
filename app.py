from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from actions import *
from process_files import *
import sys

app = Flask(__name__,
    static_url_path='',
    static_folder='static')

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
else:
    app.debug = False

topTen_dict, names_dict = load_file()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
            action = request.form.get('action', '')         
            nameInput = request.form.get('search')
            nameInputwc = request.form.get('search-wc')
            genderInput = request.form.get('gender')
            yearInput = request.form.get('year')

            if action:
                switcher = {
                        '1': print_top_ten,
                        '2': names_search,
                        '3': get_unique_names,
                        '4': longest_names,
                        '5': wildcard_search
                }

                func = switcher.get(action)
                if action == '1':
                    if yearInput == '' or genderInput == '':
                        return render_template('index.html', emptyError='*Please enter required fields')
                    data = func(topTen_dict, genderInput, int(yearInput))                 
                    return render_template('index.html', topTen=data, topTenYear=yearInput, action=1)
                elif action == '2':
                    if nameInput == '':
                        return render_template('index.html', emptyError='*Please enter required fields')
                    data = func(names_dict, nameInput.capitalize())
                    return render_template('index.html', nameData=data, action=2, nameInput=nameInput.capitalize())
                elif action == '3':
                    if yearInput == '' or not yearInput.isdigit() or int(yearInput) not in range(1980, 2018):
                        return render_template('index.html', emptyError='*Please enter required fields')
                    boysData, girlsData = func(names_dict, int(yearInput))
                    return render_template('index.html', boysData=boysData, girlsData=girlsData, action=3)
                elif action == '4':
                    data = func(names_dict)
                    return render_template('index.html', longestData=data, action=4)
                elif action == '5':
                    if nameInputwc == '':
                        return render_template('index.html', emptyError='*Please enter required fields')
                    data = func(names_dict, nameInputwc.capitalize())
                    return render_template('index.html', wildcardData=data, action=5)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=os.environ.get("PORT", 8080))
    