from flask import Flask, render_template, request, send_file, redirect, url_for, Response, redirect

from fight import * 
from createMob import *
from personnage import *
from compteurEnnemisTues import *


app = Flask(__name__)


import sys
import os



@app.route('/', methods=['GET', 'POST'])

def home():
    if request.form:
        pseudo = request.form["pseudo"]
        compteurkills = 0

        liste_monstre_vaincus = []
       
        MonPerso = personnage("pseudo", 20,6,3)

        while  MonPerso[1] > 0:
            Ennemi = createMob()
            fight(MonPerso, Ennemi)

            if MonPerso[1] > 0:
                compteurkills=compteurEnnemisTue(compteurkills)
                liste_monstre_vaincus.append(Ennemi[0])


        return render_template("home.html", pseudo=pseudo, compteurkill=compteurkills, liste_monstre_vaincus=liste_monstre_vaincus)
    return render_template ("home.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8001) 
 