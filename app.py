from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
def index():
    list = {
        '/anggota': 'Anggota Kelompok',
        '/foto': 'Foto',
        '/css': 'CSS',
    }
    return render_template('index.html', list=list)

@application.route('/anggota')
def anggota():
    listAnggota = [
        'Aryo',
        'Willy',
        'Randinesia',
        'Fulo',
    ]
    return render_template('listanggota.html', listAnggota=listAnggota)

@application.route('/foto')
def foto():
    return render_template('foto.html')

@application.route('/css')
def css():
    return render_template('css.html')

if __name__ == '__main__':
    application.run(debug=True)