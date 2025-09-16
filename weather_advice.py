'''
This program designed to give you weather advice.
First you need to choose one of sunny/rainy/cold,
Then it will give you the advice.
'''

user_input = input("What's the weather like today? (Sunny/Rainy/Cold)")

if user_input.strip().lower() == 'sunny':
    weather_advice = "Wear a t-shirt and sunglasses."

elif user_input.strip().lower() == 'rainy':
    weather_advice = "Don't forget your umbrella and raincoat."

elif user_input.strip().lower() == 'cold':
    weather_advice = "Make sure tp wear a warm coat and a scarf."

else:
    weather_advice = "Make sure you write (sunny, rainy, or cold) not other things."

print(weather_advice)