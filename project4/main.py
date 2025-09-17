import requests
import csv


def intro():
    print("\n" + "="*50)
    print("🤣  Welcome to the *Official Joke Machine* 🤣")
    print("="*50)
    print("Get ready to laugh with random jokes straight")
    print("from the Official Joke API. Let's have some fun!")
    print("="*50 + "\n")

def save_to_csv(type,joke,punchline,rating):
    with open("joke_log.csv",'a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow([type,joke,punchline,rating])

def read_csv():
    with open("joke_log.csv",'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def joke_type():
    url = "https://official-joke-api.appspot.com/types"
    response = requests.get(url)
    types = response.json()
    print("\n🎭 Available Joke Categories 🎭")
    for t in types:
        print("-",t)


def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    data = response.json()
    type = data['type']
    joke = data['setup']
    punchline = data['punchline']
    print(joke,punchline)
    rate_joke(type,joke,punchline)

def get_specific_joke(type):
    url = f"https://official-joke-api.appspot.com/jokes/{type}/random"
    response = requests.get(url)
    data = response.json()
    type = data[0]['type']
    joke = data[0]['setup']
    punchline = data[0]['punchline']
    print(joke,punchline)
    rate_joke(type,joke,punchline)
    print("✅ Saved to joke_log.csv")

def rate_joke(type,joke,punchline):
    rating = int(input("How would you rate this joke from 1-5"))
    save_to_csv(type,joke,punchline,rating)






def main():
    intro()
    joke_type()
    
    answer = input("Type the category name, 'random' for a random joke, or 'q' to quit: ").lower()

    while answer != 'q':
        if answer == 'random':
            get_random_joke()
            
        
        elif answer in ['general', 'programming', 'knock-knock', 'dad']:
            get_specific_joke(answer)

        elif answer == 's':
            read_csv()

        else:
            print('Try again')

        answer = input("\nType the category name, 'random' for a random joke, 's' to view your saved jokes or 'q' to quit: ").lower()

    print("Goodbye")


if __name__ == "__main__":
    main()