import pygal

def drawmap(keyword, countries):
    for country in countries:
        countries[country] = countries[country] * 100

    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'Positive Sentimental value towards: ' + keyword
    worldmap_chart.add('+Percentage', countries)
    return worldmap_chart

# Get lat/long from address --> convert to country
