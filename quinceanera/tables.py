routes = {
    'Amsterdam': {'Berlin': 657, 'Brussels': 210, 'Luxembourg': 391, 'Vienna': 1145},
    'Andorra': {'Bern': 1044, 'Madrid': 619, 'Paris': 864, 'Rome': 1385},
    'Berlin': {'Amsterdam': 657,'Bern': 956, 'Brussels': 868, 'Luxembourg': 763, 'Rome': 1503, 'Vienna': 681, 'Warsaw': 574},
    'Bern': {'Andorra': 1044, 'Berlin': 957, 'Luxembourg': 447, 'Paris': 564, 'Rome': 851, 'Vienna': 944, 'Warsaw': 1444},
    'Brussels': {'Amsterdam': 210, 'Berlin': 868, 'Luxembourg': 224, 'Paris': 312},
    'Lisbon': {'Madrid': 633},
    'Luxembourg': {'Amsterdam': 391, 'Berlin': 763, 'Bern': 447, 'Brussels': 763, 'Paris': 373, 'Vienna': 939},
    'Madrid': {'Andorra': 619, 'Lisbon': 633, 'Paris': 1275},
    'Paris': {'Andorra': 864, 'Bern': 564, 'Brussels': 312, 'Luxembourg': 373, 'Madrid': 1275},
    'Rome': {'Andorra': 1385, 'Bern': 851, 'Vienna': 1122},
    'Vienna': {'Amsterdam': 1145, 'Berlin': 681, 'Bern': 944, 'Luxembourg': 939, 'Rome': 1122, 'Warsaw': 727},
    'Warsaw': {'Berlin': 574, 'Bern': 1444, 'Vienna': 727}              
}
# Tabla de distancias lineales a Bucarest
lineal_distance = {
    'Amsterdam': {'Amsterdam': 0, 'Andorra': 1125, 'Berlin': 578, 'Bern': 630, 'Brussels': 173, 'Lisbon': 1865, 'Luxembourg': 319, 'Madrid': 1481, 'Paris': 430, 'Rome': 1296, 'Vienna': 937, 'Warsaw': 1096},
    'Andorra': {'Amsterdam': 1125, 'Andorra': 0, 'Berlin': 1424, 'Bern': 680, 'Brussels': 952, 'Lisbon': 994, 'Luxembourg': 865, 'Madrid': 494, 'Paris': 709, 'Rome': 908, 'Vienna': 1321, 'Warsaw': 1816},
    'Berlin': {'Amsterdam': 578, 'Andorra': 1424, 'Berlin': 0, 'Bern': 753, 'Brussels': 652, 'Lisbon': 2316, 'Luxembourg': 604, 'Madrid': 1871, 'Paris': 880, 'Rome': 1181, 'Vienna': 522, 'Warsaw': 517},
    'Bern': {'Amsterdam': 630, 'Andorra': 680, 'Berlin': 753, 'Bern': 0, 'Brussels': 489, 'Lisbon': 1627, 'Luxembourg': 375, 'Madrid': 1152, 'Paris': 435, 'Rome': 689, 'Vienna': 684, 'Warsaw': 1138},
    'Brussels': {'Amsterdam': 173, 'Andorra': 952, 'Berlin': 652, 'Bern': 489, 'Brussels': 0, 'Lisbon': 1713, 'Luxembourg': 118, 'Madrid': 1317, 'Paris': 264, 'Rome': 1173, 'Vienna': 915, 'Warsaw': 1160},
    'Lisbon': {'Amsterdam': 1865, 'Andorra': 994, 'Berlin': 2316, 'Bern': 1627, 'Brussels': 1713, 'Lisbon': 0, 'Luxembourg': 1707, 'Madrid': 502, 'Paris': 1453, 'Rome': 1863, 'Vienna': 2299, 'Warsaw': 2759},
    'Luxembourg': {'Amsterdam': 319, 'Andorra': 865, 'Berlin': 604, 'Bern': 310, 'Brussels': 186, 'Lisbon': 1711, 'Luxembourg': 0, 'Madrid': 1279, 'Paris': 286, 'Rome': 988, 'Vienna': 764, 'Warsaw': 1080},
    'Madrid': {'Amsterdam': 1481, 'Andorra': 494, 'Berlin': 1869, 'Bern': 1152, 'Brussels': 1316, 'Lisbon': 502, 'Luxembourg': 1279, 'Madrid': 0, 'Paris': 1052, 'Rome': 1364, 'Vienna': 1809, 'Warsaw': 2289},
    'Paris': {'Amsterdam': 430, 'Andorra': 709, 'Berlin': 880, 'Bern': 434, 'Brussels': 263, 'Lisbon': 1452, 'Luxembourg': 286, 'Madrid': 1052, 'Paris': 0, 'Rome': 1105, 'Vienna': 1033, 'Warsaw': 1366},
    'Rome': {'Amsterdam': 1296, 'Andorra': 908, 'Berlin': 522, 'Bern': 684, 'Brussels': 1173, 'Lisbon': 1863, 'Luxembourg': 988, 'Madrid': 1364, 'Paris': 1105, 'Rome': 0, 'Vienna': 761, 'Warsaw': 1310},
    'Vienna': {'Amsterdam': 937, 'Andorra': 1321, 'Berlin': 880, 'Bern': 434, 'Brussels': 915, 'Lisbon': 2299, 'Luxembourg': 764, 'Madrid': 1809, 'Paris': 1033, 'Rome': 761, 'Vienna': 0, 'Warsaw': 553},
    'Warsaw': {'Amsterdam': 1096, 'Andorra': 1816, 'Berlin': 517, 'Bern': 1138, 'Brussels': 1160, 'Lisbon': 2759, 'Luxembourg': 1080, 'Madrid': 2289, 'Paris': 1366, 'Rome': 1310, 'Vienna': 553, 'Warsaw': 0}
}

# Tabla A*
a_star = {
    'Amsterdam': {'Amsterdam': 0, 'Andorra': 0, 'Berlin': 0, 'Bern': 0, 'Brussels': 0, 'Lisbon': 0, 'Luxembourg': 0, 'Madrid': 0, 'Paris': 0, 'Rome': 0, 'Vienna': 0, 'Warsaw': 0},

    'Andorra': {'Amsterdam': 0, 'Andorra': 0, 'Berlin': 0, 'Bern': 0, 'Brussels': 0, 'Lisbon': 0, 'Luxembourg': 0, 'Madrid': 0, 'Paris': 0, 'Rome': 0, 'Vienna': 0, 'Warsaw': 0},

    'Berlin': {'Amsterdam': 0, 'Andorra': 0, 'Berlin': 0, 'Bern': 0, 'Brussels': 0, 'Lisbon': 0, 'Luxembourg': 0, 'Madrid': 0, 'Paris': 0, 'Rome': 0, 'Vienna': 0, 'Warsaw': 0},

    'Bern': {'Amsterdam': 0, 'Andorra': 0, 'Berlin': 0, 'Bern': 0, 'Brussels': 0, 'Lisbon': 0, 'Luxembourg': 0, 'Madrid': 0, 'Paris': 0, 'Rome': 0, 'Vienna': 0, 'Warsaw': 0},

    'Brussels': {'Amsterdam': 0, 'Andorra': 0, 'Berlin': 0, 'Bern': 0, 'Brussels': 0, 'Lisbon': 0, 'Luxembourg': 0, 'Madrid': 0, 'Paris': 0, 'Rome': 0, 'Vienna': 0, 'Warsaw': 0},

    'Lisbon': {'Amsterdam': 0, 'Andorra': 0, 'Berlin': 0, 'Bern': 0, 'Brussels': 0, 'Lisbon': 0, 'Luxembourg': 0, 'Madrid': 0, 'Paris': 0, 'Rome': 0, 'Vienna': 0, 'Warsaw': 0},

    'Luxembourg': {'Amsterdam': 0, 'Andorra': 0, 'Berlin': 0, 'Bern': 0, 'Brussels': 0, 'Lisbon': 0, 'Luxembourg': 0, 'Madrid': 0, 'Paris': 0, 'Rome': 0, 'Vienna': 0, 'Warsaw': 0},

    'Madrid': {'Amsterdam': 0, 'Andorra': 0, 'Berlin': 0, 'Bern': 0, 'Brussels': 0, 'Lisbon': 0, 'Luxembourg': 0, 'Madrid': 0, 'Paris': 0, 'Rome': 0, 'Vienna': 0, 'Warsaw': 0},

    'Paris': {'Amsterdam': 0, 'Andorra': 0, 'Berlin': 0, 'Bern': 0, 'Brussels': 0, 'Lisbon': 0, 'Luxembourg': 0, 'Madrid': 0, 'Paris': 0, 'Rome': 0, 'Vienna': 0, 'Warsaw': 0},

    'Rome': {'Amsterdam': 0, 'Andorra': 0, 'Berlin': 0, 'Bern': 0, 'Brussels': 0, 'Lisbon': 0, 'Luxembourg': 0, 'Madrid': 0, 'Paris': 0, 'Rome': 0, 'Vienna': 0, 'Warsaw': 0},

    'Vienna': {'Amsterdam': 0, 'Andorra': 0, 'Berlin': 0, 'Bern': 0, 'Brussels': 0, 'Lisbon': 0, 'Luxembourg': 0, 'Madrid': 0, 'Paris': 0, 'Rome': 0, 'Vienna': 0, 'Warsaw': 0},

    'Warsaw': {'Amsterdam': 0, 'Andorra': 0, 'Berlin': 0, 'Bern': 0, 'Brussels': 0, 'Lisbon': 0, 'Luxembourg': 0, 'Madrid': 0, 'Paris': 0, 'Rome': 0, 'Vienna': 0, 'Warsaw': 0}
}