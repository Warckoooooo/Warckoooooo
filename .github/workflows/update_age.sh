#!/bin/bash

# Ton anniversaire (format: MMDDYY)
BIRTHDATE="09022002"

# Recupère la date d'aujourd'hui
TODAY=$(date +%Y%m%d)

# Calcule le nombre de jour depuis ton anniversaire
DAYS=$(($(($(date -d"$TODAY" +%s) - $(date -d"$BIRTHDATE" +%s))) / 86400))

# Replace l'âge dans le fichier README
sed -i "s/I'm Ryan/I'm Ryan - ${DAYS} days old/1" README.md
