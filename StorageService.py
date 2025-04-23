from FirebaseRepository import FirebaseRepository

# Chemin vers le fichier JSON des informations d'identification Firebase
CREDENTIALS_PATH = "path/to/your/firebase_credentials.json"

# Initialiser le service Firebase
firebase_repository = FirebaseRepository(CREDENTIALS_PATH)

# Écrire des données dans Firebase
data = {
    "name": "Agent Turf",
    "description": "Service de gestion des courses",
    "date": "2025-04-23"
}
firebase_repository.write_data("courses", "course_001", data)