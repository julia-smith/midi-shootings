import datetime

my_data = [
    {
        "date": "08-20-1982",
        "fatalities": 8,
        "location": "Miami, Florida"
    },
    {
        "date": "06-29-1984",
        "fatalities": 6,
        "location": "Dallas, Texas"
    },
    {
        "date": "07-18-1984",
        "fatalities": 22,
        "location": "San Ysidro, California"
    },
    {
        "date": "08-20-1986",
        "fatalities": 15,
        "location": "Edmond, Oklahoma"
    },
    {
        "date": "04-23-1987",
        "fatalities": 6,
        "location": "Palm Bay, Florida"
    },
    {
        "date": "02-16-1988",
        "fatalities": 7,
        "location": "Sunnyvale, California"
    },
    {
        "date": "01-17-1989",
        "fatalities": 6,
        "location": "Stockton, California"
    },
    {
        "date": "09-14-1989",
        "fatalities": 9,
        "location": "Louisville, Kentucky"
    },
    {
        "date": "06-18-1990",
        "fatalities": 10,
        "location": "Jacksonville, Florida"
    },
    {
        "date": "10-16-1991",
        "fatalities": 24,
        "location": "Killeen, Texas"
    },
    {
        "date": "11-01-1991",
        "fatalities": 6,
        "location": "Iowa City, Iowa"
    },
    {
        "date": "11-14-1991",
        "fatalities": 5,
        "location": "Royal Oak, Michigan"
    },
    {
        "date": "05-01-1992",
        "fatalities": 4,
        "location": "Olivehurst, California"
    },
    {
        "date": "10-15-1992",
        "fatalities": 5,
        "location": "Watkins Glen, New York"
    },
    {
        "date": "07-01-1993",
        "fatalities": 9,
        "location": "San Francisco, California"
    },
    {
        "date": "08-06-1993",
        "fatalities": 4,
        "location": "Fayetteville, North Carolina"
    },
    {
        "date": "12-07-1993",
        "fatalities": 6,
        "location": "Garden City, New York"
    },
    {
        "date": "12-14-1993",
        "fatalities": 4,
        "location": "Aurora, Colorado"
    },
    {
        "date": "06-20-1994",
        "fatalities": 5,
        "location": "Fairchild Air Force Base, Washington"
    },
    {
        "date": "04-03-1995",
        "fatalities": 6,
        "location": "Corpus Christi, Texas"
    },
    {
        "date": "02-09-1996",
        "fatalities": 6,
        "location": "Fort Lauderdale, Florida"
    },
    {
        "date": "09-15-1997",
        "fatalities": 4,
        "location": "Aiken, South Carolina"
    },
    {
        "date": "12-18-1997",
        "fatalities": 5,
        "location": "Orange, California"
    },
    {
        "date": "03-06-1998",
        "fatalities": 5,
        "location": "Newington, Connecticut"
    },
    {
        "date": "03-24-1998",
        "fatalities": 5,
        "location": "Jonesboro, Arkansas"
    },
    {
        "date": "05-21-1998",
        "fatalities": 4,
        "location": "Springfield, Oregon"
    },
    {
        "date": "04-20-1999",
        "fatalities": 15,
        "location": "Littleton, Colorado"
    },
    {
        "date": "07-29-1999",
        "fatalities": 9,
        "location": "Atlanta, Georgia"
    },
    {
        "date": "09-15-1999",
        "fatalities": 8,
        "location": "Fort Worth, Texas"
    },
    {
        "date": "11-02-1999",
        "fatalities": 7,
        "location": "Honolulu, Hawaii"
    },
    {
        "date": "12-30-1999",
        "fatalities": 5,
        "location": "Tampa, Florida"
    },
    {
        "date": "12-26-2000",
        "fatalities": 7,
        "location": "Wakefield, Massachusetts"
    },
    {
        "date": "02-05-2001",
        "fatalities": 5,
        "location": "Melrose Park, Illinois"
    },
    {
        "date": "07-08-2003",
        "fatalities": 7,
        "location": "Meridian, Mississippi"
    },
    {
        "date": "12-08-2004",
        "fatalities": 5,
        "location": "Columbus, Ohio"
    },
    {
        "date": "03-12-2005",
        "fatalities": 7,
        "location": "Brookfield, Wisconsin"
    },
    {
        "date": "03-21-2005",
        "fatalities": 10,
        "location": "Red Lake, Minnesota"
    },
    {
        "date": "01-30-2006",
        "fatalities": 8,
        "location": "Goleta, California"
    },
    {
        "date": "03-25-2006",
        "fatalities": 7,
        "location": "Seattle, Washington"
    },
    {
        "date": "10-02-2006",
        "fatalities": 6,
        "location": "Lancaster County, Pennsylvania"
    },
    {
        "date": "02-12-2007",
        "fatalities": 6,
        "location": "Salt Lake City, Utah"
    },
    {
        "date": "04-16-2007",
        "fatalities": 33,
        "location": "Blacksburg, Virginia"
    },
    {
        "date": "10-07-2007",
        "fatalities": 6,
        "location": "Crandon, Wisconsin"
    },
    {
        "date": "12-05-2007",
        "fatalities": 9,
        "location": "Omaha, Nebraska"
    },
    {
        "date": "02-07-2008",
        "fatalities": 6,
        "location": "Kirkwood, Missouri"
    },
    {
        "date": "02-14-2008",
        "fatalities": 6,
        "location": "DeKalb, Illinois"
    },
    {
        "date": "06-25-2008",
        "fatalities": 6,
        "location": "Henderson, Kentucky"
    },
    {
        "date": "03-29-2009",
        "fatalities": 8,
        "location": "Carthage, North Carolina"
    },
    {
        "date": "04-03-2009",
        "fatalities": 14,
        "location": "Binghamton, New York"
    },
    {
        "date": "11-05-2009",
        "fatalities": 13,
        "location": "Fort Hood, Texas"
    },
    {
        "date": "11-29-2009",
        "fatalities": 4,
        "location": "Parkland, Washington"
    },
    {
        "date": "08-03-2010",
        "fatalities": 9,
        "location": "Manchester, Connecticut"
    },
    {
        "date": "01-08-2011",
        "fatalities": 6,
        "location": "Tucson, Arizona"
    },
    {
        "date": "09-06-2011",
        "fatalities": 5,
        "location": "Carson City, Nevada"
    },
    {
        "date": "10-14-2011",
        "fatalities": 8,
        "location": "Seal Beach, California"
    },
    {
        "date": "02-22-2012",
        "fatalities": 5,
        "location": "Norcross, Georgia"
    },
    {
        "date": "04-02-2012",
        "fatalities": 7,
        "location": "Oakland, California"
    },
    {
        "date": "05-20-2012",
        "fatalities": 6,
        "location": "Seattle, Washington"
    },
    {
        "date": "07-20-2012",
        "fatalities": 12,
        "location": "Aurora, Colorado"
    },
    {
        "date": "08-05-2012",
        "fatalities": 7,
        "location": "Oak Creek, Wisconsin"
    },
    {
        "date": "09-27-2012",
        "fatalities": 7,
        "location": "Minneapolis, Minnesota"
    },
    {
        "date": "12-14-2012",
        "fatalities": 28,
        "location": "Newtown, Connecticut"
    },
    {
        "date": "03-13-2013",
        "fatalities": 5,
        "location": "Herkimer County, New York"
    },
    {
        "date": "04-21-2013",
        "fatalities": 5,
        "location": "Federal Way, Washington"
    },
    {
        "date": "06-07-2013",
        "fatalities": 6,
        "location": "Santa Monica, California"
    },
    {
        "date": "07-26-2013",
        "fatalities": 7,
        "location": "Hialeah, Florida"
    },
    {
        "date": "09-16-2013",
        "fatalities": 13,
        "location": "Washington, D.C."
    },
    {
        "date": "02-20-2014",
        "fatalities": 4,
        "location": "Alturas, CA"
    },
    {
        "date": "10-24-2014",
        "fatalities": 5,
        "location": "Marysville, WA"
    },
    {
        "date": "06-17-2015",
        "fatalities": 9,
        "location": "Charleston, SC"
    },
    {
        "date": "07-16-2015",
        "fatalities": 5,
        "location": "Chattanooga, TN"
    }
]

data_by_frequency = []

for d in my_data:
    for x in xrange(0, int(d['fatalities'])):
        #csv
        print str( d['date'] ) + ", " + str(float(x+1)) + ", " + str(d['fatalities']) + ", " + str(d['location'])


