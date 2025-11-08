days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
forecast = [
    [12, 5, "rainy"],        # day 1
    [14, 7, "cloudy"],       # day 2
    [17, 9, "sunny"],        # day 3
    [15, 8, "partly cloudy"],# day 4
    [11, 3, "snow"],         # day 5
    [13, 6, "windy"],        # day 6
    [16, 10, "sunny"]        # day 7
]

for i in range(7):
    high, low, weather = forecast[i]
    print(f"{days[i]}: High {high}°C, Low {low}°C, Weather: {weather}")