def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

## exemple d'utilisation de fixture 
def get_user():
    # Imaginons qu'ici on appelle une API dédiée à l'authentification
    return {
        "id": 1,
        "nom": "Dupont",
        "email": "dupont@example.com"
    }