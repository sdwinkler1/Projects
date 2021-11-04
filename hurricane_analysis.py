# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# Update damage list to float:

updated_damages = []  
for i in damages:
    if 'recorded' in i:
        updated_damages.append(i)
    elif 'M' in i:
        new = i.split('M')
        updated_damages.append(float(new[0])*1000000)
    elif 'B' in i:
        new2 = i.split('B')
        updated_damages.append(float(new2[0])*1000000000)
    else:
        updated_damages.append(float(i))
print(updated_damages)
	  

# Dictionary with name as primary key:

def create_dict1(primary, list1, list2, list3, list4, list5, list6):
    diclen = list(range(len(primary)))
    newdict = {}
    for i in diclen:
        newdict[primary[i]] = {"Name": primary[i], "Months": list1[i], "Year": list2[i],
                                "Max Sustained Winds": list3[i], "Areas Affected": list4[i], 
                                "Damages": list5[i], "Deaths": list6[i]}
    return newdict
hurricanes = create_dict1(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)


# New dictionary with year as primary key:
def dict_format(dic):
    hurricane_by_year ={}
    for name, info in dic.items():
        if info["Year"] not in hurricane_by_year:
            current_year = info["Year"]
            current_cane = [dic[name]]
            hurricane_by_year[current_year] = current_cane
        elif info["Year"] in hurricane_by_year:
            current_cane.append(dic[name])
            hurricane_by_year[info["Year"]]= current_cane
            
    return hurricane_by_year

h_by_year = dict_format(hurricanes)

# Number of times each area was affected:
def locationfreq(dic):
    locations = {}
    for name, info in dic.items():
        for i in info["Areas Affected"]:
                if i not in locations:
                    count = 1
                    locations[i] = count
                elif i in locations:
                    count += 1
                    locations[i] = count
    return locations
affected_area = locationfreq(hurricanes)

#most affected area:
def maxarea(dic):
    values = dic.values()
    maxvalue = max(values)
    for area, value in dic.items():
        if value == maxvalue:
            current_area = area
    return current_area, maxvalue

maxarea(affected_area)

# greatest number of deaths:
def maxdeath(dic):
    deathvalues = []
    for name, info in dic.items():
        deathvalues.append(info["Deaths"])
    m_death = max(deathvalues)
    for name, info in dic.items():
        if info["Deaths"] == m_death:
            current_name = info["Name"]
            return current_name, m_death
maxdeath(hurricanes)

# Dictionary with mortality scale as primary key:
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   1000: 3,
                   10000: 4,
                   10001: 5}
def rating(dic):
    hurricane_ratings = {}
    for name, info in dic.items():
        if info["Deaths"] > 0 and info["Deaths"] <= 100:
            if 1 not in hurricane_ratings:
                current_name = [info["Name"]]
                hurricane_ratings[1] = current_name
            elif 1 in hurricane_ratings:
                current_name.append(info["Name"])
                hurricane_ratings[1]=current_name
    for name, info in dic.items():
        if info["Deaths"] > 100 and info["Deaths"] <= 500:
            if 2 not in hurricane_ratings:
                current_name = [info["Name"]]
                hurricane_ratings[2] = current_name
            elif 2 in hurricane_ratings:
                current_name.append(info["Name"])
                hurricane_ratings[2]= current_name
    for name, info in dic.items():
        if info["Deaths"] > 500 and info["Deaths"] <= 1000:
            if 3 not in hurricane_ratings:
                current_rating = 3
                current_name = [info["Name"]]
                hurricane_ratings[current_rating] = current_name
            elif 3 in hurricane_ratings:
                current_rating = 3
                current_name.append(info["Name"])
                hurricane_ratings[current_rating] = current_name
    for name, info in dic.items():
        if info["Deaths"] > 1000 and info["Deaths"] <=10000:
            if 4 not in hurricane_ratings:
                current_rating = 4
                current_name = [info["Name"]]
                hurricane_ratings[current_rating] = current_name
            elif 4 in hurricane_ratings:
                current_rating = 4
                current_name.append(info["Name"])
                hurricane_ratings[current_rating] = current_name
    for name, info in dic.items():
        if info["Deaths"] > 10000:
            if 5 not in hurricane_ratings:
                current_name = [info["Name"]]
                hurricane_ratings[5] = current_name
    for name, info in dic.items():
        if info["Deaths"] == 0: 
            if mortality_scale[0] not in hurricane_ratings:
                current_name = [name]
                hurricane_ratings[0] = current_name
            elif mortality_scale[0] in hurricane_ratings:
                current_name.append(name)
                hurricane_ratings[0] = current_name
    return hurricane_ratings
hurricane_by_mortality=rating(hurricanes)

#greatest damage:
def max_damage(dic):
    max_damage = 0
    for name, info in dic.items():
        if info["Damages"] == "Damages not recorded":
            continue
        elif info["Damages"] > max_damage:
            max_damage = info["Damages"]
            cane = info["Name"]
    return cane, max_damage
max_damage(hurricanes)

# Dictionary with damage rating (1 = lowest) as primary key:

def damrating(dic):
    dam_ratings = {}
    for name, info in dic.items():
        if info["Damages"] == "Damages not recorded":
            continue
        elif info["Damages"] > 0 and info["Damages"] <= 100000000:
            if 1 not in dam_ratings:
                current_name = [info["Name"]]
                dam_ratings[1] = current_name
            elif 1 in dam_ratings:
                current_name.append(info["Name"])
                dam_ratings[1]=current_name
    for name, info in dic.items():
        if info["Damages"] == "Damages not recorded":
            continue
        elif info["Damages"] > 100000000 and info["Damages"] <= 1000000000:
            if 2 not in dam_ratings:
                current_name = [info["Name"]]
                dam_ratings[2] = current_name
            elif 2 in dam_ratings:
                current_name.append(info["Name"])
                dam_ratings[2]= current_name
    for name, info in dic.items():
        if info["Damages"] == "Damages not recorded":
            continue
        elif info["Damages"] > 1000000000 and info["Damages"] <= 10000000000:
            if 3 not in dam_ratings:
                current_name = [info["Name"]]
                dam_ratings[3] = current_name
            elif 3 in dam_ratings:
                current_name.append(info["Name"])
                dam_ratings[3] = current_name
    for name, info in dic.items():
        if info["Damages"] == "Damages not recorded":
            continue
        elif info["Damages"] > 10000000000 and info["Damages"] <=50000000000:
            if 4 not in dam_ratings:
                current_name = [info["Name"]]
                dam_ratings[4] = current_name
            elif 4 in dam_ratings:
                current_name.append(info["Name"])
                dam_ratings[4] = current_name
    for name, info in dic.items():
        if info["Damages"] == "Damages not recorded":
            continue
        elif info["Damages"] > 50000000000:
            if 5 not in dam_ratings:
                current_name = [info["Name"]]
                dam_ratings[5] = current_name
            elif 5 in dam_ratings:
                current_name.append(info["Name"])
                dam_ratings[5] = current_name
    for name, info in dic.items():
        if info["Damages"] == "Damages not recorded":
            continue
        elif info["Damages"] == 0.0:
            if 0.0 not in dam_ratings:
                current_name = [name]
                dam_ratings[0] = current_name
            elif 0.0 in dam_ratings:
                current_name.append(name)
                dam_ratings[0] = current_name
    return dam_ratings
damrating(hurricanes)
