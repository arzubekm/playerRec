import pandas as pd
import joblib
from sklearn.neighbors import NearestNeighbors

def get_data():
    data = pd.read_csv('players_21_clean.csv')
    return data

def load_model():
    return joblib.load('knnplayer.pkl')

def results(player):
    data = get_data()

    index = data[data['short_name']==player].index.tolist()[0]

    model = load_model()

    recommendations = NearestNeighbors(n_neighbors=6, algorithm='ball_tree').fit(model)
    player_indices = recommendations.kneighbors(model)[1]

    list = []

    # print('Here are 5 players similar to', player, ':' '\n')
    for i in player_indices[index][1:]:
            # print(data.iloc[i]['short_name'], '\n')
            list.append(data.iloc[i]['short_name'])
    return list
