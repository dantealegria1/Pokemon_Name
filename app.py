from flask import Flask, render_template
from name_generator import nombre
from stats import estadisticas, Tipo, moveset, abilies
from fotito import pokefeo
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", nombre=nombre(), ataque=estadisticas()[0], defensa=estadisticas()[1], hp=estadisticas()[2], sp_atk=estadisticas()[3], sp_def=estadisticas()[4], speed=estadisticas()[5], tipo1=Tipo(), move1=moveset()[0], move2=moveset()[1], move3=moveset()[2], move4=moveset()[3], ability=abilies(), foto=pokefeo())

if __name__ == "__main__":
    app.run(debug=True)
