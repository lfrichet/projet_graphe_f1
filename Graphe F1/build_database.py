import requests
import pandas as pd
import os
import time

YEARS = range(2023, 2026)

if not os.path.exists("data"):
    os.mkdir("data")

for year in YEARS:

    print("Téléchargement saison", year)

    url = f"https://api.jolpi.ca/ergast/f1/{year}/results.json?limit=2000"

    try:

        r = requests.get(url)

        if r.status_code != 200:
            print("Erreur API :", r.status_code)
            continue

        data = r.json()

    except Exception as e:

        print("Erreur pour la saison", year)
        print(e)

        print("Nouvelle tentative...")
        time.sleep(5)

        r = requests.get(url)
        data = r.json()

    races = data["MRData"]["RaceTable"]["Races"]

    rows = []

    for race in races:

        gp = race["raceName"]

        for result in race["Results"]:

            driver = result["Driver"]
            constructor = result["Constructor"]

            pilot = driver["givenName"] + " " + driver["familyName"]
            team = constructor["name"]

            rows.append({
                "year": year,
                "grand_prix": gp,
                "team": team,
                "engine": team,
                "pilot": pilot,
                "replacement": 0
            })

    df = pd.DataFrame(rows)

    df.to_csv(f"data/{year}.csv", index=False)

    print("Saison", year, "terminée")

    time.sleep(1)

print("Base de données terminée")