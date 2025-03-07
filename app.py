import streamlit as st
import pickle
import pandas as pd

pipe = pickle.load(open('model.pkl', 'rb'))

teams = [
    'India',
    'England',
    'New Zealand',
    'Australia',
    'Sri Lanka',
    'South Africa',
    'Bangladesh',
    'Pakistan',
    'Afghanistan',
    'Netherlands'
]

cities = [
    'Dhaka', 
    'Chandigarh', 
    'Colombo', 
    'Johannesburg', 
    'London',
    'Centurion', 
    'Potchefstroom', 
    'Southampton', 
    'Bloemfontein',
    'Cardiff', 
    'Lahore', 
    'Kandy', 
    'Hambantota', 
    'Chattogram',
    'Harare',
    'Bulawayo', 
    'Karachi', 
    'Rawalpindi', 
    'Benoni', 
    'Hamilton',
    'Auckland', 
    'Chennai', 
    'Visakhapatnam', 
    'Mumbai', 
    'Kimberley',
    'Indore', 
    'Raipur', 
    'Hyderabad', 
    'Thiruvananthapuram', 
    'Kolkata',
    'Guwahati', 
    'Sydney', 
    'Adelaide', 
    'Delhi', 
    'Ranchi', 
    'Lucknow',
    'Cairns', 
    'Rotterdam', 
    'Manchester', 
    'Chester-le-Street',
    'Amstelveen', 
    'Mount Maunganui', 
    'Doha', 
    'Cape Town', 
    'Paarl',
    'Birmingham', 
    'Pune', 
    'Wellington', 
    'Christchurch', 
    'Dunedin',
    'Canberra', 
    'Unknown', 
    'Bengaluru', 
    'Rajkot', 
    'Leeds',
    'Nottingham', 
    'Taunton', 
    'Bristol', 
    'Dubai', 
    'Abu Dhabi',
    'Sharjah', 
    'Port Elizabeth', 
    'Nagpur', 
    'Napier', 
    'Durban',
    'Melbourne', 
    'Nelson', 
    'Hobart', 
    'Brisbane', 
    'Dharamsala',
    'Kanpur', 
    'East London', 
    'Dublin', 
    'Cuttack', 
    'Perth',
    'Dharmasala', 
    'Chittagong', 
    'Mirpur', 
    'St Kitts', 
    'Guyana',
    'Ahmedabad', 
    'Fatullah', 
    'Bangalore', 
    'Jaipur', 
    'Trinidad',
    'Jamaica', 
    'Kochi', 
    'Vadodara', 
    'Gwalior', 
    'Darwin', 
    'Faisalabad',
    'Belfast', 
    'St Lucia', 
    'Grenada', 
    'Barbados', 
    'Antigua', 
    'Margao',
    'Kuala Lumpur', 
    'Jamshedpur', 
    'Faridabad', 
    'Bogra', 
    'Queenstown',
    'Canterbury', 
    'Dambulla', 
    'Peshawar', 
    'Multan', 
    'Gqeberha'
]

st.title('ODI World Cup 2023 Win Probability')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select Bowling Team', sorted(teams))

venue = st.selectbox('Select Venue', sorted(cities))

score = st.number_input('1st Innings Score')

col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs = st.number_input('Overs Done')
with col5:
    wickets = st.number_input('Wickets Out')

if st.button('Predict Probability'):
    runs_left = score - current_score
    balls_left = 300 - (overs*6)
    wickets_left = 10 - wickets
    crr = current_score / overs
    rrr = (runs_left*6) / balls_left

    input_df = pd.DataFrame(
        {'batting_team' : [batting_team], 'bowling_team': [bowling_team], 'city': [venue],
        'runs_left': [runs_left], 'balls_left': [balls_left], 'wickets_left': [wickets_left],
        'total_runs_x': [score], 'crr': [crr], 'rrr': [rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    gain = result[0][1]

    st.header(batting_team + "- " + str(round(gain*100)) + "%")
    st.header(bowling_team + "- " + str(round(loss*100)) + "%")