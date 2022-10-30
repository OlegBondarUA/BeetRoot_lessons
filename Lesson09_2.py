from functools import reduce

STATES_DATA = [
    {
        "name": "California",
        "population": 39512223,
        "growth_change": 6.1
    },
    {
        "name": "Texas",
        "population": 28995881,
        "growth_change": 15.3
    },
    {
        "name": "Florida",
        "population": 21477737,
        "growth_change": 14.2
    },
    {
        "name": "New York",
        "population": 19453561,
        "growth_change": 0.4
    },
    {
        "name": "Pennsylvania",
        "population": 12801989,
        "growth_change": 0.8
    },
    {
        "name": "Illinois",
        "population": 12671821,
        "growth_change": -1.2
    },
    {
        "name": "Ohio",
        "population": 11689100,
        "growth_change": 1.3
    },
    {
        "name": "Georgia",
        "population": 10617423,
        "growth_change": 9.6
    },
    {
        "name": "North Carolina",
        "population": 10488084,
        "growth_change": 10.0
    },
    {
        "name": "Michigan",
        "population": 9986857,
        "growth_change": 1.0
    },
    {
        "name": "New Jersey",
        "population": 8882190,
        "growth_change": 1.0
    },
    {
        "name": "Virginia",
        "population": 8535519,
        "growth_change": 6.7
    },
    {
        "name": "Washington",
        "population": 7614893,
        "growth_change": 13.2
    },
    {
        "name": "Arizona",
        "population": 7278717,
        "growth_change": 13.9
    },
    {
        "name": "Massachusetts",
        "population": 6949503,
        "growth_change": 5.3
    },
    {
        "name": "Tennessee",
        "population": 6833174,
        "growth_change": 7.6
    },
    {
        "name": "Indiana",
        "population": 6732219,
        "growth_change": 3.8
    },
    {
        "name": "Missouri",
        "population": 6137428,
        "growth_change": 2.5
    },
    {
        "name": "Maryland",
        "population": 6045680,
        "growth_change": 4.7
    },
    {
        "name": "Wisconsin",
        "population": 5822434,
        "growth_change": 2.4
    },
    {
        "name": "Colorado",
        "population": 5758736,
        "growth_change": 14.5
    },
    {
        "name": "Minnesota",
        "population": 5639632,
        "growth_change": 6.3
    },
    {
        "name": "South Carolina",
        "population": 5148714,
        "growth_change": 11.3
    },
    {
        "name": "Alabama",
        "population": 4903185,
        "growth_change": 2.6
    },
    {
        "name": "Louisiana",
        "population": 4648794,
        "growth_change": 2.5
    },
    {
        "name": "Kentucky",
        "population": 4467673,
        "growth_change": 3.0
    },
    {
        "name": "Oregon",
        "population": 4217737,
        "growth_change": 10.1
    },
    {
        "name": "Oklahoma",
        "population": 3956971,
        "growth_change": 5.5
    },
    {
        "name": "Connecticut",
        "population": 3565287,
        "growth_change": -0.2
    },
    {
        "name": "Utah",
        "population": 3205958,
        "growth_change": 16.0
    },
    {
        "name": "Puerto Rico",
        "population": 3193694,
        "growth_change": -14.3
    },
    {
        "name": "Iowa",
        "population": 3155070,
        "growth_change": 3.6
    },
    {
        "name": "Nevada",
        "population": 3080156,
        "growth_change": 14.1
    },
    {
        "name": "Arkansas",
        "population": 3017825,
        "growth_change": 3.5
    },
    {
        "name": "Mississippi",
        "population": 2976149,
        "growth_change": 0.3
    },
    {
        "name": "Kansas",
        "population": 2913314,
        "growth_change": 2.1
    },
    {
        "name": "New Mexico",
        "population": 2096829,
        "growth_change": 1.8
    },
    {
        "name": "Nebraska",
        "population": 1934408,
        "growth_change": 5.9
    },
    {
        "name": "Idaho",
        "population": 1787065,
        "growth_change": 14.0
    },
    {
        "name": "West Virginia",
        "population": 1792147,
        "growth_change": -3.3
    },
    {
        "name": "Hawaii",
        "population": 1415872,
        "growth_change": 4.1
    },
    {
        "name": "New Hampshire",
        "population": 1359711,
        "growth_change": 3.3
    },
    {
        "name": "Maine",
        "population": 1344212,
        "growth_change": 1.2
    },
    {
        "name": "Montana",
        "population": 1068778,
        "growth_change": 8.0
    },
    {
        "name": "Rhode Island",
        "population": 1059361,
        "growth_change": 0.6
    },
    {
        "name": "Delaware",
        "population": 973764,
        "growth_change": 8.4
    },
    {
        "name": "South Dakota",
        "population": 884659,
        "growth_change": 8.7
    },
    {
        "name": "North Dakota",
        "population": 762062,
        "growth_change": 13.3
    },
    {
        "name": "Alaska",
        "population": 731545,
        "growth_change": 3.0
    },
    {
        "name": "District of Columbia",
        "population": 705749,
        "growth_change": 17.3
    },
    {
        "name": "Vermont",
        "population": 623989,
        "growth_change": -0.3
    },
    {
        "name": "Wyoming",
        "population": 578759,
        "growth_change": 2.7
    },
    {
        "name": "Guam",
        "population": 165718,
        "growth_change": 4.0
    },
    {
        "name": "U.S. Virgin Islands",
        "population": 104914,
        "growth_change": -1.4
    },
    {
        "name": "American Samoa",
        "population": 55641,
        "growth_change": 0.22
    }
]

STATES_DATA.sort(key=lambda x: x["growth_change"], reverse=True)
print('\nЗростанням населення у спадаючому порядку', STATES_DATA)

STATES_DATA = sorted(STATES_DATA, key=lambda x: x["population"])
print('\nКількість населення у зростаючому порядку', STATES_DATA)

result = reduce(lambda x, value: x + value['population'] // len(STATES_DATA), STATES_DATA, 0)
res = list(filter(lambda x: x['population'] >= result, STATES_DATA))
print('\nШтати у яких населення більше за середнє значення по країні',  res)

wer = list(map(lambda x: x["name"] + " населення зростає"if x["growth_change"] > 0 else x["name"]
        + " населення зменшується", STATES_DATA))
print('\n"Населення зростає", "Населення зменшується"', wer)

STATES_DATA = reduce(lambda x, value: x + value['population'], STATES_DATA, 0)
print('\nВсе населення:', STATES_DATA)



