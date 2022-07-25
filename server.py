import datetime
from flask import Flask, render_template
import random
import requests

app = Flask(__name__)

current_year = datetime.datetime.now().year

@app.route('/')
def home():
    random_number = random.randint(1,10)
    return render_template('index.html', num=random_number, year=current_year) ##kwargs


@app.route('/guess/<name>')
def guess(name):
    response = requests.get(f'https://api.genderize.io?name={name}')
    gender_result = response.json()
    response = requests.get(f'https://api.agify.io?name={name}')
    age_result = response.json()
    return render_template('guess.html', year=current_year, name=name, gender=gender_result['gender'], age=age_result['age']) ##kwargs

@app.route('/blog/<num>')
def get_blog(num):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', number=num, year=current_year, posts=all_posts) ##kwargs

if __name__ == '__main__':
    app.run(debug=True)