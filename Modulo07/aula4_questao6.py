import os, csv
import pandas as pd

#Impressão das 5 primeiras linhas do arquivo:
'''
with open ('spotify-2023.csv', 'r', encoding='latin-1') as p:
    pri_lin = p.readlines()
    print (pri_lin[:5])
'''

#Tratamento dos dados:
with open ('spotify-2023.csv', 'r') as original, \
    open ('nova_tab_spotify.csv', 'w') as modificada:
    aux = pd.read_csv(original)
    modificada = aux.drop(labels=['released_month','released_day','in_spotify_playlists','in_spotify_charts','in_apple_playlists','in_apple_charts','in_deezer_playlists','in_deezer_charts','in_shazam_charts','bpm','key','mode','danceability_%','valence_%','energy_%','acousticness_%','instrumentalness_%','liveness_%','speechiness_%'],axis=1)

i, j = 0, 0
ano = 2012
maior = 0
coluna = []

modificada['released_year'] = modificada['released_year'].astype('Int64')
modificada['streams'] = modificada['streams'].astype('Int64')

coluna = modificada['released_year']

for j in range (len(coluna)):
    if coluna[j] == ano:
        maior = modificada['streams'].max() & (modificada['released_year'] == ano)
        print ('variavel ano: ', ano)
        print ('coluna ano: ', coluna[j])
        print ('max: ', maior)

#ano = modificada[(modificada['released_year'] > 2022)]

#maior = modificada['streams'].max()

#print(modificada.track_name.describe())

#print (ano)
print (maior)



'''Love Grows (Where My Rosemary Goes),Edison Lighthouse,1,1970,1,1,2877,0,BPM110KeyAModeMajorDanceability53Valence75Energy69Acousticness7Instrumentalness0Liveness17Speechiness3,16,0,54,0,0,110,A,Major,53,75,69,7,0,17,3'''