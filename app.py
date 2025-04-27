from flask import Flask, render_template, request

app = Flask(__name__)

# Liste pour stocker les commentaires
comments = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Récupérer les informations envoyées par le formulaire
            username = request.form["username"]
            comment = request.form["comment"]
            
            # Vérifier si les champs sont vides
            if not username or not comment:
                raise ValueError("Les champs ne peuvent pas être vides.")
            
            # Ajouter le commentaire à la liste
            comments.append({"username": username, "comment": comment})
        
        except Exception as e:
            # Afficher l'erreur dans le terminal et rediriger l'utilisateur
            print(f"Erreur lors de la soumission du formulaire: {e}")
            return render_template("index.html", comments=comments, error=str(e))

    # Afficher la page avec les commentaires
    return render_template("index.html", comments=comments)

if __name__ == "__main__":
    app.run(debug=True)








