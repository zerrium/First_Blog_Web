from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/about')
def about():
    return render_template('about.html')

@application.route('/prime_odd')
def prime_odd():
    return render_template('prime_odd.html')

@application.route('/2d_shapes')
def twod_shapes():
    return render_template('2d_shapes.html')

@application.route('/3d_shapes')
def threed_shapes():
    return render_template('3d_shapes.html')

if __name__ == '__main__':
    application.run(debug=True)