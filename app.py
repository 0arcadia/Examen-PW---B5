from flask import Flask, render_template, request

app = Flask(__name__)

# Usuarios predefinidos
usuarios = {
    "juan": "admin",
    "pepe": "user"
}
# Ruta para la página principal
@app.route('/')

def index():
    return render_template('index.html')

# Ruta para el Ejercicio 1
@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    tarros = int(request.form['tarros'])

    precio_tarro = 9000


    total_sin_descuento = tarros * precio_tarro

    if 18 <= edad <= 30:
        descuento = 0.15
    elif edad > 30:
        descuento = 0.25
    else:
        descuento = 0


    total_con_descuento = total_sin_descuento * (1 - descuento)


    total_sin_descuento = round(total_sin_descuento)
    total_con_descuento = round(total_con_descuento)


    return render_template('ejercicio1.html',
                           nombre=nombre,
                           total_sin_descuento=total_sin_descuento,
                           descuento=descuento * 100,
                           total_con_descuento=total_con_descuento)

# Ruta para el Ejercicio 2
@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/verificar', methods=['POST'])
def verificar():
    nombre = request.form['nombre']
    contrasena = request.form['contrasena']

    if nombre in usuarios and usuarios[nombre] == contrasena:
        if nombre == "juan":
            mensaje = f"Bienvenido administrador {nombre}"
        else:
            mensaje = f"Bienvenido usuario {nombre}"
    else:
        mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)