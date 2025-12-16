import os

# Préfixes attribués par l’ARCEP aux opérateurs
OPERATEURS = {
    "Orange": ["0601","0602","0603","0604","0605","0607","0608","0609",
               "0761","0762","0763","0764","0765"],
    "SFR": ["0610","0611","0612","0613","0614","0615","0616","0617","0618","0619",
            "0771","0772","0773","0774","0775"],
    "Bouygues": ["0660","0661","0662","0663","0664","0665","0666","0667","0668","0669",
                 "0781","0782","0783","0784","0785"],
    "Free": ["0755","0756","0757","0758","0759",
             "0766","0767","0768","0769",
             "0786","0787","0788","0789"]
}

def normaliser_numero(numero: str) -> str:
    """Nettoie et normalise le format du numéro (supprime espaces, gère indicatif international)."""
    numero = numero.replace(" ", "").replace("-", "")
    if numero.startswith("0033"):
        numero = "0" + numero[4:]
    elif numero.startswith("+33"):
        numero = "0" + numero[3:]
    elif numero.startswith("33"):
        numero = "0" + numero[2:]
    return numero

def identifier_operateur(numero: str) -> str:
    """Retourne l'opérateur correspondant au numéro ou 'AutreOperateur'."""
    numero = normaliser_numero(numero)
    prefixe4 = numero[:4]
    for operateur, prefixes in OPERATEURS.items():
        if prefixe4 in prefixes:
            return operateur
    return "AutreOperateur"

def trier_numeros(numeros, dossier_sortie="resultats"):
    """Trie les numéros par opérateur, enregistre dans des fichiers et retourne les stats."""
    if not os.path.exists(dossier_sortie):
        os.makedirs(dossier_sortie)
    
    stats = {op: 0 for op in list(OPERATEURS.keys()) + ["AutreOperateur"]}
    fichiers = {op: open(os.path.join(dossier_sortie, f"{op}.txt"), "w", encoding="utf-8")
                for op in stats.keys()}
    
    for num in numeros:
        op = identifier_operateur(num)
        fichiers[op].write(num + "\n")
        stats[op] += 1
    
    for f in fichiers.values():
        f.close()
    
    return stats

def main():
    print("=== TRI DES NUMÉROS PAR OPÉRATEUR ===")
    choix = input("Voulez-vous fournir un fichier (f) ou entrer manuellement une liste (m) ? [f/m] : ").lower()
    
    numeros = []
    if choix == "f":
        chemin = input("Entrez le chemin du fichier .txt contenant les numéros : ").strip()
        try:
            with open(chemin, "r", encoding="utf-8") as f:
                numeros = [ligne.strip() for ligne in f if ligne.strip()]
        except FileNotFoundError:
            print("❌ Fichier introuvable.")
            return
    elif choix == "m":
        print("Entrez vos numéros séparés par des espaces ou des virgules :")
        saisie = input(">> ")
        numeros = [n.strip() for n in saisie.replace(",", " ").split() if n.strip()]
    else:
        print("❌ Choix invalide.")
        return
    
    stats = trier_numeros(numeros)
    print("✅ Tri terminé. Résultats enregistrés dans le dossier 'resultats'.")
    
    # Résumé statistique
    print("\n=== RÉSUMÉ STATISTIQUE ===")
    for op, count in stats.items():
        print(f"{op} : {count} numéro(s) trouvé(s)")

if __name__ == "__main__":
    main()
