import os
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

DATA_FOLDER = "data"
YEARS = range(2007, 2026)


def construire_graphe():
    G = nx.DiGraph()
    for year in YEARS:
        file = f"{DATA_FOLDER}/{year}.csv"
        if not os.path.exists(file):
            continue
        df = pd.read_csv(file)
        G.add_node(year, type="annee")
        for _, row in df.iterrows():
            gp = row["grand_prix"]
            team = row["team"]
            engine = row["engine"]
            pilot = row["pilot"]
            pilot_year = f"{pilot}_{year}"
            gp_node = f"{gp}_{year}"

            G.add_node(engine, type="motoriste")
            G.add_node(team, type="ecurie")
            G.add_node(pilot_year, type="pilote")
            G.add_node(gp_node, type="grand_prix")
            G.add_edge(year, gp_node, weight=1)
            G.add_edge(year, engine, weight=1)
            G.add_edge(engine, team, weight=1)
            G.add_edge(year, team, weight=1)
            G.add_edge(team, pilot_year, weight=1)
            G.add_edge(year, pilot_year, weight=1)
    return G


def info_graphe(G):
    print("Noeuds :", G.number_of_nodes())
    print("Arêtes :", G.number_of_edges())
    deg = dict(G.degree())
    print("Degré moyen :", sum(deg.values()) / len(deg))


def statistiques(G):
    pilotes = {}
    gps = {}
    moteurs = {}
    for year in YEARS:
        if year not in G:
            continue
        p = set()
        g = set()
        m = set()
        for n in G.successors(year):
            t = G.nodes[n]["type"]
            if t == "pilote":
                p.add(n)
            if t == "grand_prix":
                g.add(n)
            if t == "motoriste":
                m.add(n)
        pilotes[year] = len(p)
        gps[year] = len(g)
        moteurs[year] = len(m)
    print()

    print("Année + pilotes :", max(pilotes, key=pilotes.get))
    print("Année - pilotes :", min(pilotes, key=pilotes.get))

    print("Année + GP :", max(gps, key=gps.get))
    print("Année - GP :", min(gps, key=gps.get))

    print("Année + motoristes :", max(moteurs, key=moteurs.get))
    print("Année - motoristes :", min(moteurs, key=moteurs.get))


def bfs(G, start):
    print("BFS :", list(nx.bfs_tree(G, start)))


def dfs(G, start):
    print("DFS :", list(nx.dfs_tree(G, start)))


def dijkstra_chemin(G, source, cible):
    try:
        chemin = nx.dijkstra_path(G, source, cible, weight="weight")
        distance = nx.dijkstra_path_length(G, source, cible, weight="weight")
        print("Plus court chemin :")
        print(" -> ".join(chemin))
        print("Distance :", distance)
    except nx.NetworkXNoPath:
        print("Aucun chemin entre", source, "et", cible)


def afficher_graphe(G):
    plt.figure(figsize=(20,20))
    pos = nx.spring_layout(G, k=0.8)
    couleurs = []
    tailles = []
    for n, d in G.nodes(data=True):
        t = d["type"]
        if t == "annee":
            couleurs.append("blue")
            tailles.append(1200)
        elif t == "motoriste":
            couleurs.append("orange")
            tailles.append(900)
        elif t == "ecurie":
            couleurs.append("red")
            tailles.append(700)
        elif t == "grand_prix":
            couleurs.append("purple")
            tailles.append(500)
        else:
            couleurs.append("green")
            tailles.append(300)
    nx.draw(
        G,
        pos,
        node_size=tailles,
        node_color=couleurs,
        with_labels=True,
        font_size=7,
        font_weight="bold"
    )
    plt.title("Graphe Formule 1 2020-2025")
    plt.show()


def main():
    G = construire_graphe()
    info_graphe(G)
    statistiques(G)
    dijkstra_chemin(G, "Charles Leclerc_2022", "Ferrari")
    dijkstra_chemin(G, "Max Verstappen_2021", "Honda")
    dijkstra_chemin(G, "Lando Norris_2023", "Mercedes")
    dijkstra_chemin(G, "Pierre Gasly_2024", "Red Bull")
    if 2023 in G:
        bfs(G, 2023)
        dfs(G, 2023)
    afficher_graphe(G)


if __name__ == "__main__":
    main()