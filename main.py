from flask import Flask, render_template
import requests
from datetime import datetime
from post import Post

app = Flask(__name__)

year = datetime.now().year

response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
results = response.json()
post_objects = []
for post in results:
    post_objects.append(Post(post['id'], post['title'], post['subtitle'], post['body']))

@app.route('/')
def home():
    return render_template("index.html", data=post_objects, year=year)

@app.route('/post/<int:blog_id>')
def get_blog(blog_id):
    chosen_post = ''
    for post in post_objects:
        if post.id == blog_id:
            chosen_post = post
    return render_template('post.html', post=chosen_post, year=year)

if __name__ == "__main__":
    app.run(debug=True)
