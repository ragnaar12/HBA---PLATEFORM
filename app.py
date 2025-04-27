from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Liste pour stocker les commentaires
comments = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        comment = request.form['comment']
        comments.append({'username': username, 'comment': comment})
        return redirect('/')
    return render_template('index.html', comments=comments)

if __name__ == '__main__':



