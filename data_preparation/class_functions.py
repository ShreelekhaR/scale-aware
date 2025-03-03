def istennis(tags):
    #tennis
    if 'leisure' in tags and tags['leisure']=='pitch':
        if 'sport' in tags and 'tennis' in tags['sport']:
            return True
    return False

def isskate(tags):
    #skateboard
    if 'leisure' in tags and tags['leisure']=='pitch':
        if 'sport' in tags and 'skateboard' in tags['sport']:
#             if 'surface' in tags and 'turf' in tags['surface']:
            return True
    return False

def isamfootball(tags):
    #american football
    if 'leisure' in tags and tags['leisure']=='pitch':
        if 'sport' in tags and 'american_football' in tags['sport']:
            return True
    return False

def isswimming(tags):
    #swimming pool
    if 'leisure' in tags and tags['leisure']=='swimming_pool':
        return True
    return False

def iscemetery(tags):
    #cemeterey
    if 'landuse' in tags and tags['landuse']=='cemetery':
        return True
    return False

def isgarage(tags):
    #multi-storey parking lot
    if 'amenity' in tags and tags['amenity']=='parking':
        if 'parking' in tags and tags['parking']=='multi-storey':
            return True
    return False

def isgolf(tags):
    #golf
    if 'leisure' in tags and tags['leisure']=='golf_course':
        return True
    return False

def isroundabout(tags):
    #roundabout
    if 'junction' in tags and tags['junction']=='roundabout':
        return True
    return False


def isparkinglot(tags):
    if 'parking' in tags and tags['parking']=='surface':
        return True
    if 'amenity' in tags and tags['amenity']=='parking':
        return True
    return False

def issupermarket(tags):
    #supermarket
    if 'shop' in tags and tags['shop']=='supermarket':
        return True
    elif 'amenity' in tags and tags['amenity']=='pharmacy':
        return True
    elif 'building' in tags and tags['building']=='retail':
        return True
    return False

def isschool(tags):
    #school
    if 'amenity' in tags and tags['amenity']=='school':
        return True
    return False


def ismarina(tags):
    #marina
    if 'leisure' in tags and tags['leisure']=='marina':
        return True
    return False

def isbaseball(tags):
    #baseball
    if 'leisure' in tags and tags['leisure']=='pitch':
        if 'sport' in tags and 'baseball' in tags['sport']:
            return True
    return False

def isfall(tags):
    #waterfall
    if 'waterway' in tags and tags['waterway']=='waterfall':
        return True
    return False

def ispond(tags):
    #pond
    if 'water' in tags and tags['water']=='pond':
        return True
    return False


def isairport(tags):
    #airportoutline
    if 'aeroway' in tags and tags['aeroway']=='aerodrome':
        return True
    elif 'aeroway' in tags and tags['aeroway']=='runway':
        if 'surface' in tags and tags['surface']=='paved':
            return True
    return False

def isbeach(tags):
    #beach
    if 'natural' in tags and tags['natural']=='beach':
        return True
    return False

def isbridge(tags):
    #bridge
    if 'bridge' in tags and tags['bridge']=='yes':
        return True
    elif 'man_made' in tags and tags['man_made']=='bridge':
        return True
    else:
        return False

def isreligious_building(tags):
    #building for religious 
    if 'amenity' in tags and tags['amenity'] == 'place_of_worship':
        return True
    elif 'building' in tags and tags['building'] in ['church', 'mosque', 'cathedral', 'synagogue', 'temple', 'chapel', 'shrine']:
        return True
    else:
        return False

def isresidential(tags):
    #building for accommodation
    if 'building' in tags:
        if tags['building'] in ['apartments', 'barracks', 'bungalow', 'cabin', 'detached', 'dormitory', 'farm', 'ger', 'hotel', 'house', 'houseboat', 'residential', 'semidetached_house', 'static_caravan', 'stilt_house', 'terrace', 'tree_house']:
            return True
        elif 'landuse' in tags and tags['landuse']=='residential':
            return True
    return False


def iswarehouse(tags):
    #warehouse
    if 'building' in tags and tags['building']=='warehouse':
        return True
    return False


def isoffice(tags):
    #office
    if 'building' in tags and tags['building']=='office':
        return True
    return False

def isfarmland(tags):
    #farmland
    if 'landuse' in tags and tags['landuse']=='farmland':
        return True
    return False


def isuniversity_building(tags):
    #university
    if 'building' in tags and tags['building']=='university':
        return True
    return False

def isforest(tags):
    #forest
    if 'landuse' in tags and tags['landuse']=='forest':
        return True
    elif 'natural' in tags and tags['natural']=='wood':
        return True
    else:
        return False

def islake(tags):
    #lake
    if 'water' in tags and tags['water']=='lake':
        return True
    return False


def isnaturereserve(tags):
    #nature reserve
    if 'leisure' in tags and tags['leisure']=='nature_reserve':
        return True
    return False

def ispark(tags):
    #park
    if 'leisure' in tags and tags['leisure']=='park':
        return True
    return False

def issand(tags):
    #sand
    if 'natural' in tags and tags['natural']=='sand':
        return True
    return False

    
def issoccer(tags):
    #soccer field
    if 'leisure' in tags and tags['leisure'] in ['pitch','sports_centre','stadium']:
        if 'sport' in tags and tags['sport']=='soccer':
            return True
    else:
        return False
    
def isequestrian(tags):
    #equestrian field
    if 'leisure' in tags and tags['leisure'] in ['pitch']:
        if 'sport' in tags and tags['sport']=='equestrian':
            return True
    else:
        return False
    
def isshooting(tags):
    #shooting
    if 'leisure' in tags and tags['leisure'] in ['pitch']:
        if 'sport' in tags and tags['sport']=='shooting':
            return True
    else:
        return False
    
def isicerink(tags):
    #icerink
    if 'leisure' in tags and tags['leisure'] in ['pitch','sports_centre','stadium']:
        if 'sport' in tags and tags['sport'] in ['ice_skating','ice_hockey']:
            return True
    else:
        return False
    

def iscommercialarea(tags):
    #commercial area
    if 'amenity' in tags and tags['amenity'] in ['bar','pub']:
        return True
    elif 'amenity' in tags and tags['amenity']==['restaurant','cafe','fast_food']:
        return True
    elif 'amenity' in tags and tags['amenity']=='bank':
        return True
    elif 'leisure' in tags and tags['leisure']=='fitness_center':
        return True
    return False
    
def isgarden(tags):
    #garden
    if 'leisure' in tags and tags['leisure']=='garden':
        return True
    return False

def isdam(tags):
    #dam
    if 'waterway' in tags and tags['waterway']=='dam':
        return True
    return False

def israilroad(tags):
    #railroad
    if 'railway' in tags and tags['railway'] in ['abandoned', 'construction', 'disused', 'funicular', 'light_rail', 'miniature', 'monorail', 'narrow_gauge', 'preserved', 'rail', 'subway', 'tram']:
        return True
    return False

def ishighway(tags):
    #highway 
    if 'highway' in tags:
        if tags['highway'] in ['motorway','trunk','primary','secondary','tertiary']:
            return True
    return False


def isriver(tags):
    #river
    if 'water' in tags and tags['water']=='river':
        return True
    elif 'waterway' in tags and tags['waterway']=='river':
        return True
    return False

def iswetland(tags):
    #wetland
    if 'natural' in tags and tags['natural']=='wetland':
        return True
    return False

filterfuncs = [
    istennis,
    isskate,
    isamfootball,
    isswimming,
    iscemetery,
    isgarage,
    isgolf,
    isroundabout,
    isparkinglot,
    issupermarket,
    isschool,
    ismarina,
    isbaseball,
    isfall,
    ispond,
    isairport,
    isbeach,
    isbridge,
    isreligious_building,
    isresidential,
    iswarehouse,
    isoffice,
    isfarmland,
    isuniversity_building,
    isforest,
    islake,
    isnaturereserve,
    ispark,
    issand,
    issoccer,
    isequestrian,
    isshooting,
    isicerink,
    iscommercialarea,
    isgarden,
    isdam,
    israilroad,
    ishighway,
    isriver,
    iswetland
]

output_files = [
    'classes/tennis.csv',
    'classes/skate.csv',
    'classes/amfootball.csv',
    'classes/swimming.csv',
    'classes/cemetery.csv',
    'classes/garage.csv',
    'classes/golf.csv',
    'classes/roundabout.csv',
    'classes/parkinglot.csv',
    'classes/supermarket.csv',
    'classes/school.csv',
    'classes/marina.csv',
    'classes/baseball.csv',
    'classes/fall.csv',
    'classes/pond.csv',
    'classes/airport.csv',
    'classes/beach.csv',
    'classes/bridge.csv',
    'classes/religious.csv',
    'classes/residential.csv',
    'classes/warehouse.csv',
    'classes/office.csv',
    'classes/farmland.csv',
    'classes/university.csv',
    'classes/forest.csv',
    'classes/lake.csv',
    'classes/naturereserve.csv',
    'classes/park.csv',
    'classes/sand.csv',
    'classes/soccer.csv',
    'classes/equestrian.csv',
    'classes/shooting.csv',
    'classes/icerink.csv',
    'classes/commercialarea.csv',
    'classes/garden.csv',
    'classes/dam.csv',
    'classes/railroad.csv',
    'classes/highway.csv',
    'classes/river.csv',
    'classes/wetland.csv'
]
    

# classes numbered
#  0 tennis
#  1 skate
#  2 amfootball
#  3 swimming
#  4 cemetery
#  5 garage
#  6 golf
#  7 roundabout
#  8 parkinglot
#  9 supermarket
# 10 school
# 11 marina
# 12 baseball
# 13 fall
# 14 pond
# 15 airport
# 16 beach
# 17 bridge
# 18 religious
# 19 residential
# 20 warehouse
# 21 office
# 22 farmland
# 23 university
# 24 forest
# 25 lake
# 26 naturereserve
# 27 park
# 28 sand
# 29 soccer
# 30 equestrian
# 31 shooting
# 32 icerink
# 33 commercialarea
# 34 garden
# 35 dam
# 36 railroad
# 37 highway
# 38 river
# 39 wetland