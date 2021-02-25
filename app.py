from flask import Flask, render_template, request
from math import pi

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
        scroll = int(request.form['scroll']) + 20
        # Menggunakan exception handling python untuk menangani input dari user yang bukan angka
        try:
            input1 = int(request.form['input'])  # Typecast dari string dari input text box ke integer
        except ValueError:
            error = "Only number inputs are allowed!"  # Ketika user menginput bukan angka
            return render_template('prime_odd.html', error=error, scroll=scroll)
        else:
            output = [input1]  # variabel list

            # Cek prima
            if input1 > 1:
                for i in range(2, input1):
                    if input1 % i == 0:
                        output.append('No')
                        break
                else:
                    output.append('Yes')
            else:
                output.append('No')

            # Cek ganjil/genap (menggunakan ternary operator)
            output.append('No' if input1 % 2 == 0 else 'Yes')

            return render_template('prime_odd.html', output=output, scroll=scroll)

    return render_template('prime_odd.html')


@application.route('/2d_shapes', methods=['POST', 'GET'])
def twod_shapes():
    input2 = 0
    if request.method == 'POST':
        shape = request.form['shape']
        scroll = int(request.form['scroll']) + 20
        # Menggunakan exception handling python untuk menangani input dari user yang bukan angka
        try:
            input1 = int(request.form['input1'])  # Typecast dari string dari input text box ke integer
            if shape == "rectangle" or shape == "triangle":
                input2 = int(request.form['input2'])
        except ValueError:
            error = "Only number inputs are allowed!"  # Ketika user menginput bukan angka
            return render_template('2d_shapes.html', error=error, scroll=scroll)
        else:
            output = [shape, input1, input2]  # variabel list

            if shape == "circle":
                output.append(pi * input1 ** 2)  # Luas lingkaran
                output.append(2 * pi * input1)  # Keliling lingkaran
            elif shape == "square":
                output.append(input1 ** 2)  # Luas pesergi
                output.append(4 * input1)  # Keliling pesergi
            elif shape == "rectangle":
                output.append(input1 * input2)  # Luas segi panjang
                output.append(2 * (input1 + input2))  # Keliling segi panjang
            elif shape == "triangle":
                output.append(0.5 * input1 * input2)  # Luas segitiga
                output.append("Not available")  # Keliling segitiga, tidak bisa karena inputnya belum tersedia
            else:
                error = "Please select a shape!"  # Ketika user tidak memilih shape
                return render_template('2d_shapes.html', error=error, scroll=scroll)

            return render_template('2d_shapes.html', output=output, scroll=scroll)

    return render_template('2d_shapes.html')


@application.route('/3d_shapes', methods=['POST', 'GET'])
def threed_shapes():
    input2 = 0
    input3 = 0
    if request.method == 'POST':
        shape = request.form['shape']
        scroll = int(request.form['scroll']) + 20
        # Menggunakan exception handling python untuk menangani input dari user yang bukan angka
        try:
            input1 = int(request.form['input1'])  # Typecast dari string dari input text box ke integer
            if shape == "cone" or shape == "cube" or shape == "cylinder":
                input2 = int(request.form['input2'])
            if shape == "cube":
                input3 = int(request.form['input3'])
        except ValueError:
            error = "Only number inputs are allowed!"  # Ketika user menginput bukan angka
            return render_template('3d_shapes.html', error=error, scroll=scroll)
        else:
            output = [shape, input1, input2, input3]  # variabel list

            if shape == "cylinder":
                output.append(pi * input1 ** 2 * input2)  # Volume tabung
                output.append(2 * pi * input1 * input2 + 2 * pi * input1 ** 2)  # Luas permukaan tabung
            elif shape == "cone":
                output.append(1/3 * pi * input1 ** 2 * input2)  # Volume kerucut
                output.append(pi * input1 * (input1 + (input2**2 + input1**2)**0.5))  # Luas permukaan kerucut
            elif shape == "cube":
                output.append(input1 * input2 * input3)  # Volume balok/kubus
                output.append(2 * (input1 + input2) + 2 * (input1 + input3) + 2 * (input2 + input3))  # Luas permukaan balok/kubus
            elif shape == "sphere":
                output.append(4/3 * pi * input1 ** 3)  # Volume bola
                output.append(4 * pi * input1 ** 2)  # Luas permukaan bola
            else:
                error = "Please select a shape!"  # Ketika user tidak memilih shape
                return render_template('3d_shapes.html', error=error, scroll=scroll)

            return render_template('3d_shapes.html', output=output, scroll=scroll)

    return render_template('3d_shapes.html')


if __name__ == '__main__':
    application.run(debug=True)
