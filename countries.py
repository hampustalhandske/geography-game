import requests as rq
from bs4 import BeautifulSoup as bs
from functions import *
from collections import deque

response = rq.get("https://en.wikipedia.org/wiki/List_of_countries_and_territories_by_number_of_land_borders")
soup = bs(response.content, "html.parser")

def get_boarders():
    table = soup.find("div", {"class": "mw-page-container"})
    table = table.find_all("table")[1]
    countries = []
    borders = {}
    trs = table.find_all("tr")[2:]
    for row in trs:
        country = row.find("a")
        if country and country.text not in countries:
            countries.append(country.text)
            neighbors = row.find_all("a")
            neighbors = [n.text for n in neighbors]
            nbr = len(neighbors)
            borders[country.text] = neighbors
    countries = [c for c in countries if c != ""]
    for country, neighbor in borders.items():
        borders[country] = [n for n in borders[country] if n != country and n in countries]
    borders = {key: value for key, value in borders.items() if key != ""}
    borders["France"] = [n for n in borders["France"] if n != "Brazil" and n != "Canada" and n != "Netherlands" and n != "Suriname"]
    return (borders, countries)

def relation():
    borders = get_boarders()[0]
    relation = set()
    for country, neighbors in borders.items():
        for n in neighbors:
            border = (country, n)
            relation.add(border)
    relation = {(a, b) for a, b in relation if (b, a) in relation}
    return relation

def is_reachable(c1, c2, R, visited=None):
    if visited is None:
        visited = set()

    if c1 == c2:
        return True
    visited.add(c1)

    neighbors = image_of(R, c1)

    for neighbor in neighbors:
        if neighbor not in visited:
            if is_reachable(neighbor, c2, R, visited):
                return True
    return False

def shortest_way(c1, c2, R):
    queue = deque([(c1, [c1])])
    visited = set()
    
    while queue:
        current, path = queue.popleft()

        if current == c2:
            return path
        
        visited.add(current)

        neighbors = image_of(R, current)

        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    
    return []


R = relation()
borders = get_boarders()[0]
countries = get_boarders()[1]

