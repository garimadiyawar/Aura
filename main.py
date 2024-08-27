import requests
from speech_engine import speak, greet_user, take_user_input
from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
from functions.os_ops import open_calculator, open_camera, open_chrome, open_cmd, open_notion
from pprint import pprint

if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()
        
        if 'open notion' in query:
            open_notion()

        elif 'open chrome' in query:
            open_chrome()

        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()

        elif 'open camera' in query:
            open_camera()

        elif 'open calculator' in query:
            open_calculator()

        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen mam.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, mam?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen mam.")
            print(results)

        elif 'youtube' in query:
            speak('What do you want to play on Youtube, mam?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak('What do you want to search on Google, mam?')
            query = take_user_input().lower()
            search_on_google(query)

        elif "send whatsapp message" in query:
            speak('On what number should I send the message, mam? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message mam?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message, mam.")

        elif "send an email" in query:
            speak("On what email address do I send, mam? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject, mam?")
            subject = take_user_input().capitalize()
            speak("What is the message, mam?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email, mam.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs, mam.")

        elif 'joke' in query:
            speak(f"Hope you like this one, mam")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen, mam.")
            pprint(joke)

        elif "advice" in query:
            speak(f"Here's an advice for you, mam")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen mam.")
            pprint(advice)

        elif "trending movies" in query:
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen mam.")
            print(*get_trending_movies(), sep='\n')

        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines, mam")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen mam.")
            print(*get_latest_news(), sep='\n')

        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen mam.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
        