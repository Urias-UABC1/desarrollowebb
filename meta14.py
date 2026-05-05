from flask import Flask, render_template
import pandas as pd
import numpy as np
 
app = Flask(__name__)
 
@app.route("/")
def inicio():
    nombres = ["Ana", "Luis", "Carlos", "Sofía"]
    calificaciones = np.array([85, 90, 78, 92])
 
    df = pd.DataFrame({
        "nombre": nombres,
        "calificacion": calificaciones
    })
 
    promedio = np.mean(calificaciones)
    maximo = np.max(calificaciones)
 
    datos = df.to_dict(orient="records")
 
    return render_template("meta14.html", datos=datos, promedio=promedio, maximo=maximo)
 
if __name__ == "__main__":
    app.run(debug=True)
 
