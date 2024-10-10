import pandas as pd
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv('international_matches.csv', encoding='utf-8')

df.drop(['home_team_goalkeeper_score'], axis=1, inplace=True)
df.drop(['away_team_goalkeeper_score'], axis=1, inplace=True)
df.drop(['home_team_mean_defense_score'], axis=1, inplace=True)
df.drop(['home_team_mean_offense_score'], axis=1, inplace=True)
df.drop(['home_team_mean_midfield_score'], axis=1, inplace=True)
df.drop(['away_team_mean_defense_score'], axis=1, inplace=True)
df.drop(['away_team_mean_offense_score'], axis=1, inplace=True)
df.drop(['away_team_mean_midfield_score'], axis=1, inplace=True)
df.drop(['country'], axis = 1, inplace=True)
df.drop(['city'], axis = 1, inplace=True)
df = df.drop(df[df['tournament'] == 'Friendly'].index)
df.drop(['neutral_location'], axis=1, inplace=True)

idx= df.isnull().index
# df.drop(idx)
df.dropna(inplace=True)


label_encoder = LabelEncoder()

df['home_team_numeric'] = label_encoder.fit_transform(df['home_team'])
df['away_team_numeric'] = label_encoder.fit_transform(df['away_team'])
df['home_team_continent_numeric'] = label_encoder.fit_transform(df['home_team_continent'])
df['away_team_continent_numeric'] = label_encoder.fit_transform(df['away_team_continent'])
df['tournament_numeric'] = label_encoder.fit_transform(df['tournament'])
df = df.replace({'shoot_out': {'Yes': True, 'No': False}})

in_50 = [
    "Argentina", "France", "Spain", "England", "Brazil", "Belgium", 
    "Netherlands", "Portugal", "Colombia", "Italy", "Uruguay", 
    "Croatia", "Germany", "Morocco", "Switzerland", "Japan", 
    "Mexico", "USA", "IR Iran", "Denmark", "Senegal", 
    "Austria", "Korea Republic", "Ukraine", "Australia", "Turkey", 
    "Ecuador", "Sweden", "Wales", "Poland", "Egypt", "Hungary", 
    "Côte d'Ivoire", "Russia", "Serbia", "Tunisia", "Panama", 
    "Canada", "Nigeria", "Venezuela", "Algeria", "Slovakia", 
    "Peru", "Qatar", "Romania", "Czech Republic", "Norway", 
    "Greece", "Chile", "Costa Rica"
]

fifa_team_pre = []
fifa_team_numeric = []
for i in in_50:
    fifa_team_pre.extend(df[df['home_team']==i]['home_team_numeric'])


for value in fifa_team_pre:
    if value not in fifa_team_numeric:
        fifa_team_numeric.append(value)

fifa_conti_numeric = []

for j in fifa_team_numeric:
    fifa_conti_numeric.append(list(df[df['home_team_numeric']==j]['home_team_continent_numeric'])[0])

fifa_point = [
    1889,1851,1836,1817,1772,1768,1759,1752,1738,1726,1701,1699,1692,1676,1641,
    1639,1635,1632,1622,1621,1620,1580,1572,1548,1544,1538,1535,1528,1526,1525,
    1515,1511,1509,1508,1505,1504,1502,1502,1498,1488,1486,1485,1483,1481,1481,
    1473,1472,1469,1467,1466
]

team_info = pd.DataFrame({'team' : in_50, 'rank' : range(1,51), 'point' : fifa_point, 'numeric' : fifa_team_numeric,
                        'continent_numeric' :fifa_conti_numeric })
team_info.head()
