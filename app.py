from flask import Flask, render_template, request

app = Flask(__name__)

# Liste pour stocker les commentaires
comments = []

@app.route("/", methods=["GET", "POST"])
def index():
    # Si la méthode est POST, cela signifie que le formulaire a été soumis
    if request.method == "POST":
        username = request.form["username"]
        comment = request.form["comment"]
        
        # Ajouter le commentaire à la liste
        comments.append({"username": username, "comment": comment})
    
    # Afficher la page avec les commentaires
    return render_template("index.html", comments=comments)

if __name__ == "__main__":
    # Lancer l'application en mode debug
    app.run(debug=True)





