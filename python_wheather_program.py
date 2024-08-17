import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {'q': location,   'appid': api_key, 'units': 'metric'}
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        if data.get('cod') != 200:
            return f"Error: {data.get('message', 'Unknown error occurred')}"
        
        main = data['main']
        weather = data['weather'][0]
        city = data['name']
        temp = main['temp']
        humidity = main['humidity']
        description = weather['description']
        
        return (f"City: {city}\n"
                f"Temperature: {temp}°C\n"
                f"Humidity: {humidity}%\n"
                f"Description: {description.capitalize()}")
    
    except requests.RequestException as e:
        return f"An error occurred: {e}"

def main():
    api_key = 'e498bb3fe062565a40bacc0e7c1a47c5'  
    while True:
        location = input("Enter a city or ZIP code (or type 'exit' to quit): ").strip()
        if location.lower() == 'exit':
            print("Exiting the program.")
            break
        if location:
            print(get_weather(api_key, location))
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
