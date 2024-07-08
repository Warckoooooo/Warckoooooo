#!/bin/bash

# Date de naissance (format: MMDDYYYY)
BIRTHDATE="09022002"

# Récupère la date d'aujourd'hui (format: MMDDYYYY)
TODAY=$(date +%m%d%Y)

# Calcule le nombre de jours depuis la date de naissance
DAYS=$(( ( $(date -d "$TODAY" +%s) - $(date -d "$BIRTHDATE" +%s) ) / 86400 ))

# Remplace l'âge dans le fichier README.md
sed -i "s/Hi 👋, I'm Ryan.*/Hi 👋, I'm Ryan - ${DAYS} days old/" README.md

