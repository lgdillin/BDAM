#!/usr/bin/env python3

import cairo
import json
import math
import matplotlib.colors

colorConverter = matplotlib.colors.ColorConverter()

oceanColor = colorConverter.to_rgba("#FFFFFF", 1.0)

outlineFillColor = colorConverter.to_rgba("#989898", 0.3)
outlineStrokeColor = colorConverter.to_rgba("#0E94EC", 1.0)

nodeFillColor = colorConverter.to_rgba("#E7746F", 0.3)
nodeStrokeColor = colorConverter.to_rgba("#E7746F", 1.0)

outFile = "world.pdf"

width = 1920
height = 1080

nodePositions = [
    (50.102, 14.3916),
    (41.3897, 2.11273),
    (-41.2902, 174.768),
    (35.1566, 136.925),
    (-36.8538, 174.766),
    (19.3951, -99.2332),
    (-2.15, -79.96),
    (48.7835, 9.17517),
    (29.68, -82.27),
    (37.4557, -122.178),
    (39.98, -83.03),
    (48.8473, 2.35749),
    (46.59, 6.56),
    (49.015, 8.405),
    (32.877, -117.237),
    (33.7772, -84.3976),
    (55.7014, 12.5612),
    (-19.9333, -43.95),
    (33.95, -117.39),
    (42.71, -73.2),
    (44.04, -123.06),
    (22.3, 114.166),
    (36.1659, -86.8313),
    (29.5372, 106.602),
    (38.0232, -1.17473),
    (35.7, 139.767),
    (33.9815, -118.46),
    (38.7373, -9.30324),
    (47.3794, 8.54513),
    (40.4363, -3.69413),
    (47.4744, 19.0622),
    (42.7993, -1.63544),
    (46.5203, 6.5656),
    (59.93, 10.75),
    (40.6401, -8.65628),
    (48.1179, -1.60753),
    (47.6531, -122.313),
    (51.1, 16.93),
    (37.9966, 23.7399),
    (48.5237, 7.73833),
    (38, 23.73),
    (51.3622, 9.55996),
    (53.8341, 10.7043),
    (40.42, -3.72),
    (42.1692, -8.68458),
    (49.2637, -123.237),
    (40.4274, -86.9167),
    (60.19, 24.93),
    (51.498, -0.176655),
    (28.0587, -82.4152),
    (41.5615, -8.39722),
    (56.25, -3.03),
    (-20.905, 55.5),
    (39.0386, -94.5794),
    (53.4187, -7.90557),
    (37.9684, 23.7669),
    (52.211, 20.981),
    (35.17, 25),
    (41.8556, 12.6243),
    (50.2901, 18.6773),
    (14.1426, 100.604),
    (36.83, -2.40454),
    (52.2207, 21.0104),
    (50.6833, 4.61667),
    (53.5686, 10.0386),
    (32.9861, -96.75),
    (37.6118, 126.999),
    (37.2055, -80.4124),
    (31.1992, 121.43),
    (39.6182, 20.8386),
    (42.3907, -71.1478),
    (40, 116.327),
    (40.8, -96.6667),
    (48.9408, 2.30674),
    (39.6798, -104.963),
    (39.5398, -119.814),
    (59.52, 17.38),
    (50.8625, 4.68599),
    (42.37, -71.03),
    (35.92, -79.04),
    (49.45, 7.78),
    (1.37, 103.8),
    (42.35, -71.1),
    (43.0757, -89.3867),
    (39.19, -96.59),
    (-34.6039, -58.3679),
    (32.0479, 34.761),
    (34.0711, -118.442),
    (33.7895, -84.3255),
    (42.8189, -75.5357),
    (54.2047, 16.1972),
    (34.4403, 132.415),
    (-37.9096, 145.133),
    (35.42, 139.42),
    (43.4726, -80.5422),
    (-45.8656, 170.514),
    (39.9887, 116.307),
    (41.5022, -81.6079),
    (42.6544, -71.3266),
    (-37.7892, 175.318),
    (30.2636, 120.121)
]

def rectProjection(lat, lon):
    return width * (lon + 180.0)/360.0, height * (1.0 - (lat + 90.0)/180.0)

def drawPolygon(ctx, poly):
    for coords in poly:
        lastCoord = coords[0]
        (xU, yU) = rectProjection(lastCoord[1], lastCoord[0])
        ctx.move_to(xU, yU)
        for coord in coords[1:]:
            (xV, yV) = rectProjection(coord[1], coord[0])

            ctx.line_to(xV, yV)

            lastCoord = coord
        ctx.set_source_rgba(outlineFillColor[0], outlineFillColor[1], outlineFillColor[2], outlineFillColor[3])
        ctx.fill_preserve()

        ctx.set_source_rgba(outlineStrokeColor[0], outlineStrokeColor[1], outlineStrokeColor[2], outlineStrokeColor[3])
        ctx.stroke()

if __name__ == "__main__":
    #surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    surface = cairo.PDFSurface(outFile, width, height)
    ctx = cairo.Context(surface)

    ctx.set_line_width(0.5)

    ctx.set_source_rgba(oceanColor[0], oceanColor[1], oceanColor[2], oceanColor[3])
    ctx.rectangle(0, 0, width, height)
    ctx.fill()

    countryFile = "countries.geojson"
    countryGeoJSON = json.load(open(countryFile))
    for feature in countryGeoJSON["features"]:
        type = feature["geometry"]["type"]
        if type == "Polygon":
            drawPolygon(ctx, feature["geometry"]["coordinates"])

        if type == "MultiPolygon":
            for polygon in feature["geometry"]["coordinates"]:
                drawPolygon(ctx, polygon)

    for pos in nodePositions:
        (xU, yU) = rectProjection(pos[0], pos[1])
        ctx.arc(xU, yU, 3.0, 0.0, 2.0 * math.pi)
        ctx.set_source_rgba(nodeFillColor[0], nodeFillColor[1], nodeFillColor[2], nodeFillColor[3])
        ctx.fill_preserve()
        ctx.set_source_rgba(nodeStrokeColor[0], nodeStrokeColor[1], nodeStrokeColor[2], nodeStrokeColor[3])
        ctx.stroke()

    #surface.write_to_png("world.png")
