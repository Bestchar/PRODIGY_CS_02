from PIL import Image # type: ignore
import os  # Pour manipuler les chemins de fichiers

def chiffrer_image(image_path, clef):
    # Ouvrir l'image
    image = Image.open(image_path)
    pixels = image.load()
    
    largeur, hauteur = image.size
    
    # Boucle pour chiffrer chaque pixel
    for x in range(largeur):
        for y in range(hauteur):
            r, g, b = pixels[x, y]
            r = (r + clef) % 256
            g = (g + clef) % 256
            b = (b + clef) % 256
            pixels[x, y] = (r, g, b)
    
    # Générer le chemin complet pour sauvegarder l'image chiffrée
    image_directory = os.path.dirname(image_path)
    image_chiffree_path = os.path.join(image_directory, "image_chiffree.png")
    
    image.save(image_chiffree_path)
    print(f"Image chiffrée enregistrée sous {image_chiffree_path}.")

def dechifrer_image(image_path, clef):
    # Ouvrir l'image chiffrée
    image = Image.open(image_path)
    pixels = image.load()
    
    largeur, hauteur = image.size
    
    # Boucle pour déchiffrer chaque pixel
    for x in range(largeur):
        for y in range(hauteur):
            r, g, b = pixels[x, y]
            r = (r - clef) % 256
            g = (g - clef) % 256
            b = (b - clef) % 256
            pixels[x, y] = (r, g, b)
    
    # Générer le chemin complet pour sauvegarder l'image déchiffrée
    image_directory = os.path.dirname(image_path)
    image_dechiffree_path = os.path.join(image_directory, "image_dechiffree.png")
    
    image.save(image_dechiffree_path)
    print(f"Image déchiffrée enregistrée sous {image_dechiffree_path}.")

# Utilisation du chemin de l'image source
image_path = "/home/mystik/Images/prodyg/RR.jpeg"  # Remplacer par le chemin de ton image
clef = 10  # La clé pour chiffrer et déchiffrer

# Chiffrer l'image
chiffrer_image(image_path, clef)

# Déchiffrer l'image chiffrée
dechifrer_image("/home/mystik/Images/prodyg/image_chiffree.png", clef)
