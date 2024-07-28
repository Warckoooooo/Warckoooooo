import datetime

# Ma date de naissance
birthdate = datetime.date(2002, 9, 2)

# Calculer le nombre de jours depuis la naissance
today = datetime.date.today()
days_old = (today - birthdate).days

# Lire le fichier README.md
readme_path = "README.md"
with open(readme_path, "r", encoding="utf-8") as file:
    readme_content = file.read()

# La ligne de base à rechercher
base_line = '<h1 align="center">Hi 👋, I\'m Ryan'
new_content = f'{base_line} ({days_old} days old)'

# Remplacer ou ajouter l'âge en jours
if base_line in readme_content:
    # Trouver la ligne et la remplacer
    updated_readme_content = readme_content.replace(base_line, new_content)
    
    # Écrire le contenu mis à jour dans README.md
    with open(readme_path, "w", encoding="utf-8") as file:
        file.write(updated_readme_content)
else:
    print("La ligne de base n'a pas été trouvée dans le fichier README.md.")
