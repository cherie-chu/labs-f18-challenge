from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<query>', methods=['GET'])
def catch_pokemon(query):
	profile = requests.get('https://pokeapi.co/api/v2/pokemon/' + query).json()
	pokemon = profile['name']
	num = str(profile['id'])
	if query.isdigit():
		return render_template('pokemon.html', pokemon=pokemon, id=query)
	else:
		return render_template('pokemon2.html', pokemon=query, id=num)

if __name__ == '__main__':
    app.run()