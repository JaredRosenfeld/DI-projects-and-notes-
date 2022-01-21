import sqlite3
import feedparser
from app import app, db
import requests
from flask import redirect, render_template

from app.Forms import NewsForm
from app.models import News, Users, Pets


# db.drop_all()
# db.create_all()


def get_news():
    url = 'https://news.google.com/rss?x=1571747254.2933&hl=en-US&gl=US&ceid=US:en'
    f = feedparser.parse(url)
    f.keys()
    entries = f.entries
    for en in entries:
        for k , v in en.items():
           if k == 'title':
                title1 = str(v)
           elif k == 'summary':
               description1 = str(v)

           elif k == 'source':
               source1 = str(v)
        get_titles_from_db = [tit.title for tit in News.query.all()]
        if title1 not in get_titles_from_db:
            news_item = News(title = title1 ,description = description1, source = source1)
            db.session.add(news_item)
    db.session.commit()

@app.route('/')
def view_news():
    news = News.query.all()
    get_news()
    return render_template('base.html', news=news)

@app.route('/addnews', methods=['GET', 'POST'])
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        source = form.source.data
        news_item = News(title=title, description=description, source=source)
        # db.create_all()
        db.session.add(news_item)
        db.session.commit()
        return redirect('/')
    return render_template('add_news.html', form=form)

@app.route('/pets')
def pets():
    users = Users.query.all()
    pets = Pets.query.all()
    return render_template('pets.html',users = users, pets = pets )

    # data = data.json()
    # news = data['title']
    # news = news.replace("'","")
    # connection = sqlite3.connect('news.db')
    # cursor = connection.cursor()
    # query = f"INSERT INTO news (news) VALUES ('{news}');"
    # query_result = cursor.execute(query)
    # connection.commit()
    # connection.close()
    # print(news)
#
#