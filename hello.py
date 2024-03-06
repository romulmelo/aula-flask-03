from flask import Flask, request, render_template
from datetime import datetime
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def index():
     return render_template('index.html', current_time=datetime.utcnow())


@app.route('/user/<name>/<id>/<institution>')
def user(name, id, institution):
    return render_template('user.html', name=name, id=id, institution=institution)

@app.route('/contextorequisicao/<name>')
def context(name):
		user_agent = request.headers.get('User-Agent')
		remote_ip = request.remote_addr
		host = request.host
		return render_template('context.html', name=name, user_agent=user_agent, remote_ip=remote_ip, host=host)