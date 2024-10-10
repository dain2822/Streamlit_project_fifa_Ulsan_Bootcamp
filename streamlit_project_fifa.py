import streamlit as st
import pandas as pd
# import KNneighbor_model
import rank_point_python
import joblib
import sklearn
from sklearn.neighbors import KNeighborsClassifier

st.title(':soccer:축구 승부 예측:soccer:')
team_info = rank_point_python.team_info
# st.write(team_info
# in_50 =  ['아르헨티나','프랑스','스페인','영국','브라질','벨기에','네덜란드','포르투갈','콜롬비아','이탈리아',
#         '우루과이','크로아티아','독일','모로코','스위스,','일본','멕시코','미국','이란','덴마크','세네갈',
#         '오스트리아','대한민국','우크라이나','호주','튀르키예','에콰도르','스웨덴','웨일스','폴란드','이집트','헝가리',
#         '크르디부아르','러시아','세르비아','튀니지','파나마','캐나다','나이지리아','베네수엘라','알제리','슬로바키아',
#         '페루','카타르','루마니아','체코','노르웨이','그리스','칠레','코스타리카']

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

# predict = KNneighbor_model

home_selectbox = st.selectbox('홈팀을 선택해주세요.', in_50)

# not_selected = in_50[home_selectbox]
in_50.remove(home_selectbox)

away_selectbox = st.selectbox('원정팀을 선택해주세요.', in_50)

button = st.button('예측하기')

if button:
    home = team_info[team_info['team'] == home_selectbox]
    away = team_info[team_info['team'] == away_selectbox]
    # st.write(list(home['rank']))
    # st.write(away)
    df = pd.DataFrame({'home_team_fifa_rank':[home['rank'].iloc[0]], 
                                'away_team_fifa_rank':[away['rank'].iloc[0]],
                                'home_team_total_fifa_points':[home['point'].iloc[0]], 
                                'away_team_total_fifa_points':[away['point'].iloc[0]],
                                'home_team_numeric':[home['numeric'].iloc[0]],
                                'away_team_numeric':[away['numeric'].iloc[0]],
                                'home_team_continent_numeric':[home['continent_numeric'].iloc[0]],
                                'away_team_continent_numeric':[away['continent_numeric'].iloc[0]]})
    model_from_joblib = joblib.load('KNneighbor_model.pkl')
    model_from_joblib.predict(df)
    st.write(home_selectbox,model_from_joblib.predict(df))

    # 국기 사진 출력
    ##st.image()
    # 전적 출력(홈 vs 원정)
    # st.subheader('<홈팀 vs 원정팀 전적>')
    # st.write('어쩌구저쩌구(전승무패)')

else:
    st.write('예측하기를 눌러주세요.')