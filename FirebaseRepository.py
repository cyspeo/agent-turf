import firebase_admin
from firebase_admin import credentials, firestore

class FirebaseRepository:
    def __init__(self, credentials_path: str):
        # Initialiser l'application Firebase avec les informations d'identification
        cred = credentials.Certificate(credentials_path)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def write_data(self, collection: str, document: str, data: dict):
        """
        Écrit des données dans une collection et un document spécifiques.
        :param collection: Nom de la collection
        :param document: Nom du document
        :param data: Données à écrire (dict)
        """
        doc_ref = self.db.collection(collection).document(document)
        doc_ref.set(data)
        print(f"Données écrites dans {collection}/{document}: {data}")