from flask import Flask, request, render_template
import recommendation
import pandas as pd

app = Flask(__name__)

def get_data():
    data = pd.read_csv('datasets/half_players_21_clean.csv')
    return data

@app.route('/')
def homepage():
    data = get_data()
    long_names = data.long_name
    # long_names = ["Lionel Messi", "Cristiano Ronaldo dos Santos Aveiro", "Jan Oblak", "Robert Lewandowski", "Kevin De Bruyne"]

    return render_template('form.html', long_names=long_names)

@app.route('/player', methods=['GET', 'POST'])
def recommend_players():
    if request.method == 'POST':
        res = recommendation.results(request.form.get('title'))
        return render_template('/index.html', list = res)

if __name__ == '__main__':
    app.run(port=5000, debug = False)
