from hashlib import sha256

entree = input ("Quel est le nom du fichier a crypter/décrypter ? ")    #Récupère les fichiers a ouvrir
sortie = input ("Entrez le nom du fichier final ? ")
key = input("Entrez la clé de chiffrement : ")                          #Récupère la clé de cryptage

keys = sha256(key.encode('utf-8')).digest()                             #Encoder la clé selon le sha256

with open(entree,'rb') as f_entree:                                     #Ouvre le fichier entree en binaire
    with open(sortie,'wb') as f_sortie:                                 #Ouvre ou crée le fichier de sortie en binaire
        i = 0
        while f_entree.peek():                                          #Permet de passer sur chaque caractère du fichier
            c = ord(f_entree.read(1))                                   #Affecte a c chaque octet 1 à 1
            j = i % len(keys)
            b = bytes([c^keys[j]])                                      #Convertie les octets reçu selon le cryptage xor
            f_sortie.write(b)
            i = i + 1