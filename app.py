from flask import Flask, request, render_template
import recommendation

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('form.html')

@app.route('/player', methods=['GET', 'POST'])
def recommend_players():
    if request.method == 'POST':
        res = recommendation.results(request.form.get('title'))
        return render_template('/index.html', list = res)

if __name__ == '__main__':
    app.run(port=5000, debug = False)
