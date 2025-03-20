from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Active CORS pour permettre les requêtes depuis un frontend

# Liste des calendriers avec leurs URLs (informations sensibles supprimées)
CALENDARS = [
    {
        "name": "Personne1",
        "url": "https://exemple.index-education.net/pronote/ical/mesinformations.ics?icalsecurise=TOKEN_SECURISE_1",
        "className": "person1"
    },
    {
        "name": "Personne2",
        "url": "https://exemple.index-education.net/pronote/ical/mesinformations.ics?icalsecurise=TOKEN_SECURISE_2",
        "className": "person2"
    },
    {
        "name": "Personne3",
        "url": "https://exemple.index-education.net/pronote/ical/mesinformations.ics?icalsecurise=TOKEN_SECURISE_3",
        "className": "person3"
    },
    {
        "name": "Personne4",
        "url": "https://exemple.index-education.net/pronote/ical/mesinformations.ics?icalsecurise=TOKEN_SECURISE_4",
        "className": "person4"
    }
]

@app.route('/api/calendars', methods=['GET'])
def get_calendars():
    """Récupère les calendriers depuis leurs URLs et les renvoie sous forme JSON."""
    all_calendars = []
    for calendar in CALENDARS:
        try:
            response = requests.get(calendar['url'], timeout=5)  # Timeout pour éviter que ça bloque trop longtemps
            if response.status_code == 200:
                all_calendars.append({
                    'data': response.text,
                    'name': calendar['name'],
                    'className': calendar['className']
                })
            else:
                print(f"Erreur {response.status_code} pour {calendar['name']}")
        except requests.RequestException as e:
            print(f"Erreur de connexion pour {calendar['name']}: {str(e)}")
    
    return jsonify(all_calendars)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)  # Port générique
