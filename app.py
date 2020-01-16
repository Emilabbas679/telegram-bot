from flask import Flask, render_template
import telegram
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bot = telegram.Bot(token='800787116:AAHQRDJp7paFRY9YuVeyje9mm511AiiampQ')
updates = bot.get_updates()
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root@localhost/last_jobs"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Jobs(db.Model):
    __tablename__ = 'avirdigital_jobustan_jobs'
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String, unique=True,)
    status = db.Column(db.Integer)
    qualifications = db.Column(db.Text)
    title = db.Column(db.String)
    aboutjob = db.Column(db.Text)


@app.route('/')
def index():
    chats = updates
    # for chat in chats:
    #     try:
    jobs = Jobs.query.filter_by(status=4).limit(4).all()
    for job in jobs:
        post = u'Title: {!s}' \
               u'\nSlug: http://jobustan.com/job/{!s}' \
               u'\nAbout Job: {!s}'.format(job.title,job.slug, job.aboutjob)
        bot.send_message(chat_id='-1001153991044', text=post, parse_mode=telegram.ParseMode.MARKDOWN)


    # bot.send_message(chat_id='-1001153991044', text=post)
    #     except:
    #         print('something went wrong')
    return render_template('index.html', chats=chats)


if __name__ == 'main':
    app.run(Debug=True)
