import requests

response = requests.get('https://the-trivia-api.com/v2/questions')
question = response.json()[0]

print(question['category'])
print(question['question'])
print(question['correctAnswer'])