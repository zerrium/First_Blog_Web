from flask import Flask, render_template, request
application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/about')
def about():
    return render_template('about.html')

@application.route('/prime_odd', methods=['POST', 'GET'])
def prime_odd():
    if request.method == 'POST':
        input = 0
        scroll = int(request.form['scroll']) + 20
        #Menggunakan exception handling python untuk menangani input dari user yang bukan angka
        try:
            input = int(request.form['input']) #Typecast dari string dari input text box ke integer
        except ValueError:
            error = "Only number inputs are allowed!" #Ketika user menginput bukan angka
            return render_template('prime_odd.html', error=error, scroll=scroll)
        else:
            output = [] #variabel list
            output.append(input)

            #Cek prima
            if input > 1:
                for i in range(2, input):
                    if input%i == 0:
                        output.append('No')
                        break
                else:
                    output.append('Yes')
            else:
                output.append('No')

            # Cek ganjil/genap (menggunakan ternary operator)
            output.append('No' if input % 2 == 0 else 'Yes')

            return render_template('prime_odd.html', output=output, scroll=scroll)

    return render_template('prime_odd.html')

@application.route('/2d_shapes')
def twod_shapes():
    return render_template('2d_shapes.html')

@application.route('/3d_shapes')
def threed_shapes():
    return render_template('3d_shapes.html')

if __name__ == '__main__':
    application.run(debug=True)