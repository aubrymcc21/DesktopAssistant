import speech_recognition as sr
import pyttsx3
import wikipediaapi

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia('en')

def speak(text):
    # Function to speak the given text
    engine.say(text)
    engine.runAndWait()

def get_weather(city):
    # Function to get weather updates (Replace with preferred weather API)
    # This is a placeholder function and needs a valid API key!
    return f"The weather in {city} is sunny."

def search_wikipedia(query):
    # Function to search for information on Wikipedia
    page = wiki_wiki.page(query)
    if page.exists():
        return page.summary[:500] + "..."
    else:
        return "Sorry, I couldn't find any relevant information."

def main():
    print("Listening...")
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio).lower()
        print("You said: " + command)

        if 'time' in command:
            # Get current time
            speak("The current time is 12:00 PM.")  # Replace with actual time retrieval function
        elif 'weather' in command:
            # Get weather update for a city
            city = command.split('weather in ')[1]
            weather_info = get_weather(city)
            speak(weather_info)
        elif 'search' in command:
            # Search Wikipedia for a query
            query = command.split('search ')[1]
            result = search_wikipedia(query)
            speak(result)
        elif 'exit' in command:
            speak("Goodbye!")
            return False
        else:
            speak("I'm sorry, I didn't understand that.")
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return True

if __name__ == "__main__":
    keep_running = True
    while keep_running:
        keep_running = main()
