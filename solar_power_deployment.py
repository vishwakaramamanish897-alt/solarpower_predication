import streamlit as st
import pandas as pd
import joblib

st.title('Solar Power Generation Prediction System')
st.write("Enter weather and environmental data to predict solar power generation")

# Load model safely
try:
    model = joblib.load('solar_power_genrator_model.pkl')
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Inputs
day_of_year = st.number_input('Day of Year')
year = st.number_input('Year')
month = st.number_input('Month')
day = st.number_input('Day')

first_hour = st.number_input('First Hour of Period')
is_daylight = st.selectbox('Is Daylight', [0,1])

distance_solar_noon = st.number_input('Distance to Solar Noon')

avg_temp = st.number_input('Average Temperature (Day)')
avg_wind_dir = st.number_input('Average Wind Direction (Day)')
avg_wind_speed_day = st.number_input('Average Wind Speed (Day)')

sky_cover = st.number_input('Sky Cover')
visibility = st.number_input('Visibility')

humidity = st.number_input('Relative Humidity')

avg_wind_speed_period = st.number_input('Average Wind Speed (Period)')
barometric_pressure = st.number_input('Average Barometric Pressure (Period)')


# DataFrame
df = pd.DataFrame({
    "Day of Year":[day_of_year],
    "Year":[year],
    "Month":[month],
    "Day":[day],
    "First Hour of Period":[first_hour],
    "Is Daylight":[is_daylight],
    "Distance to Solar Noon":[distance_solar_noon],
    "Average Temperature (Day)":[avg_temp],
    "Average Wind Direction (Day)":[avg_wind_dir],
    "Average Wind Speed (Day)":[avg_wind_speed_day],
    "Sky Cover":[sky_cover],
    "Visibility":[visibility],
    "Relative Humidity":[humidity],
    "Average Wind Speed (Period)":[avg_wind_speed_period],
    "Average Barometric Pressure (Period)":[barometric_pressure]
})

# Prediction
if st.button('Predict Solar Power'):
    try:
        prediction = model.predict(df)
        st.success(f"Predicted Solar Power Generated: {prediction[0]:.2f}")
    except Exception as e:
        st.error(f"Prediction error: {e}")
