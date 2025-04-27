from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# Exemple de projets
projects = [
    {"title": "Plateforme IA", "description": "Projet d'intelligence artificielle avancée."},
    {"title": "Application Mobile", "description": "Développement d'une application pour étudiants."},
]

@app.route('/')
def home():
    # HTML + CSS intégrés dans la même chaîne
    html_content = '''
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Projets</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }
            .container {
                width: 80%;
                margin: 0 auto;
                padding: 20px;
                background-color: #fff;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                margin-top: 30px;
            }
            h1 {
                text-align: center;
            }
            .project {
                background-color: #f9f9f9;
                margin: 15px 0;
                padding: 15px;
                border-radius: 5px;
                box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
            }
            .add-btn {
                display: block;
                width: 200px;
                padding: 10px;
                margin: 20px auto;
                background-color: #4CAF50;
                color: white;
                text-align: center;
                border-radius: 5px;
                text-decoration: none;
            }
            .add-btn:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Liste des Projets</h1>
            {% for project in projects %}
            <div class="project">
                <h3>{{ project.title }}</h3>
                <p>{{ project.description }}</p>
            </div>
            {% else %}
            <p>Aucun projet disponible pour le moment.</p>
            {% endfor %}
            <a href="/add" class="add-btn">Ajouter un projet</a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content, projects=projects)

@app.route('/add', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        title = request.form['title']
        description = request.form['description']
        
        # Ajouter le projet à la liste
        projects.append({"title": title, "description": description})
        
        # Rediriger vers la page d'accueil après l'ajout
        return redirect('/')
    
    # Formulaire HTML pour ajouter un projet
    html_content_add = '''
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ajouter un Projet</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }
            .container {
                width: 80%;
                margin: 0 auto;
                padding: 20px;
                background-color: #fff;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                margin-top: 30px;
            }
            h1 {
                text-align: center;
            }
            form {
                display: flex;
                flex-direction: column;
            }
            input, textarea {
                margin: 10px 0;
                padding: 10px;
                font-size: 16px;
            }
            button {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border: none;
                font-size: 16px;
                cursor: pointer;
                border-radius: 5px;
            }
            button:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Ajouter un Nouveau Projet</h1>
            <form method="POST">
                <input type="text" name="title" placeholder="Titre du projet" required>
                <textarea name="description" placeholder="Description du projet" required></textarea>
                <button type="submit">Ajouter le Projet</button>
            </form>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content_add)

if __name__ == "__main__":
    app.run(debug=True)










