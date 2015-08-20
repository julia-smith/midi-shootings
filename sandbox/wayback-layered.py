import datetime
from miditime.MIDITime import MIDITime

# Instantiate the class with a tempo (120bpm is the default), an output file destination, number of seconds to represent a year, base octave (5 is Middle C), and octave range.
#mymidi = MIDITime(120, 'chords.mid')
mymidi = MIDITime(120, 'wayback.mid', 6, 3, 5) #4 was good for # of seconds for year

# Create a list of notes. Each note is a list: [time, pitch, attack, duration]
# midinotes = [
#     [0, 60, 200, 3],  #At 0 beats (the start), Middle C with attack 200, for 3 beats
#     [10, 61, 200, 4]  #At 10 beats (12 seconds from start), C#5 with attack 200, for 4 beats
# ]


my_data = [
    {
        "eventdate": "08-20-1982",
        "fatalityid": 1,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-20-1982",
        "fatalityid": 2,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-20-1982",
        "fatalityid": 3,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-20-1982",
        "fatalityid": 4,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-20-1982",
        "fatalityid": 5,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-20-1982",
        "fatalityid": 6,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-20-1982",
        "fatalityid": 7,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-20-1982",
        "fatalityid": 8,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-18-1983",
        "fatalityid": 1,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-18-1983",
        "fatalityid": 2,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-18-1983",
        "fatalityid": 3,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-18-1983",
        "fatalityid": 4,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-18-1983",
        "fatalityid": 5,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-18-1983",
        "fatalityid": 6,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-18-1983",
        "fatalityid": 7,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-18-1983",
        "fatalityid": 8,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-18-1983",
        "fatalityid": 9,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-18-1983",
        "fatalityid": 10,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-18-1983",
        "fatalityid": 11,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-18-1983",
        "fatalityid": 12,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-18-1983",
        "fatalityid": 13,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-29-1984",
        "fatalityid": 1,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-29-1984",
        "fatalityid": 2,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-29-1984",
        "fatalityid": 3,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-29-1984",
        "fatalityid": 4,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-29-1984",
        "fatalityid": 5,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-29-1984",
        "fatalityid": 6,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-18-1984",
        "fatalityid": 1,
        "total": 21,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-18-1984",
        "fatalityid": 2,
        "total": 21,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-18-1984",
        "fatalityid": 3,
        "total": 21,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-18-1984",
        "fatalityid": 4,
        "total": 21,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-18-1984",
        "fatalityid": 5,
        "total": 21,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-18-1984",
        "fatalityid": 6,
        "total": 21,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-18-1984",
        "fatalityid": 7,
        "total": 21,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-18-1984",
        "fatalityid": 8,
        "total": 21,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-18-1984",
        "fatalityid": 9,
        "total": 21,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-18-1984",
        "fatalityid": 10,
        "total": 21,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-18-1984",
        "fatalityid": 11,
        "total": 21,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-18-1984",
        "fatalityid": 12,
        "total": 21,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-18-1984",
        "fatalityid": 13,
        "total": 21,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-18-1984",
        "fatalityid": 14,
        "total": 21,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-18-1984",
        "fatalityid": 15,
        "total": 21,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-18-1984",
        "fatalityid": 16,
        "total": 21,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-18-1984",
        "fatalityid": 17,
        "total": 21,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-18-1984",
        "fatalityid": 18,
        "total": 21,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-18-1984",
        "fatalityid": 19,
        "total": 21,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-18-1984",
        "fatalityid": 20,
        "total": 21,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-18-1984",
        "fatalityid": 21,
        "total": 21,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-20-1986",
        "fatalityid": 1,
        "total": 15,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-20-1986",
        "fatalityid": 2,
        "total": 15,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-20-1986",
        "fatalityid": 3,
        "total": 15,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-20-1986",
        "fatalityid": 4,
        "total": 15,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-20-1986",
        "fatalityid": 5,
        "total": 15,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-20-1986",
        "fatalityid": 6,
        "total": 15,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-20-1986",
        "fatalityid": 7,
        "total": 15,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-20-1986",
        "fatalityid": 8,
        "total": 15,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-20-1986",
        "fatalityid": 9,
        "total": 15,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-20-1986",
        "fatalityid": 10,
        "total": 15,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-20-1986",
        "fatalityid": 11,
        "total": 15,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-20-1986",
        "fatalityid": 12,
        "total": 15,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-20-1986",
        "fatalityid": 13,
        "total": 15,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-20-1986",
        "fatalityid": 14,
        "total": 15,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-20-1986",
        "fatalityid": 15,
        "total": 15,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-23-1987",
        "fatalityid": 1,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-23-1987",
        "fatalityid": 2,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-23-1987",
        "fatalityid": 3,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-23-1987",
        "fatalityid": 4,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-23-1987",
        "fatalityid": 5,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-23-1987",
        "fatalityid": 6,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-23-1987",
        "fatalityid": 7,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-16-1988",
        "fatalityid": 1,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-16-1988",
        "fatalityid": 2,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-16-1988",
        "fatalityid": 3,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-16-1988",
        "fatalityid": 4,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-16-1988",
        "fatalityid": 5,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-16-1988",
        "fatalityid": 6,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-16-1988",
        "fatalityid": 7,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-17-1989",
        "fatalityid": 1,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-17-1989",
        "fatalityid": 2,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-17-1989",
        "fatalityid": 3,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-17-1989",
        "fatalityid": 4,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-17-1989",
        "fatalityid": 5,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-14-1989",
        "fatalityid": 1,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-14-1989",
        "fatalityid": 2,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-14-1989",
        "fatalityid": 3,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-14-1989",
        "fatalityid": 4,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-14-1989",
        "fatalityid": 5,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-14-1989",
        "fatalityid": 6,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-14-1989",
        "fatalityid": 7,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-14-1989",
        "fatalityid": 8,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-18-1990",
        "fatalityid": 1,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-18-1990",
        "fatalityid": 2,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-18-1990",
        "fatalityid": 3,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-18-1990",
        "fatalityid": 4,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-18-1990",
        "fatalityid": 5,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-18-1990",
        "fatalityid": 6,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-18-1990",
        "fatalityid": 7,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-18-1990",
        "fatalityid": 8,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-18-1990",
        "fatalityid": 9,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-18-1990",
        "fatalityid": 10,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-11-1991",
        "fatalityid": 1,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-11-1991",
        "fatalityid": 2,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-11-1991",
        "fatalityid": 3,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-11-1991",
        "fatalityid": 4,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-11-1991",
        "fatalityid": 5,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-11-1991",
        "fatalityid": 6,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 1,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 2,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 3,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 4,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 5,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 6,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 7,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 8,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 9,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 10,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 11,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 12,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 13,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 14,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 15,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 16,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 17,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 18,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 19,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 20,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 21,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 22,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 23,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-16-1991",
        "fatalityid": 24,
        "total": 24,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-14-1991",
        "fatalityid": 1,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-14-1991",
        "fatalityid": 2,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-14-1991",
        "fatalityid": 3,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-14-1991",
        "fatalityid": 4,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-14-1991",
        "fatalityid": 5,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "05-01-1992",
        "fatalityid": 1,
        "total": 4,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "05-01-1992",
        "fatalityid": 2,
        "total": 4,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "05-01-1992",
        "fatalityid": 3,
        "total": 4,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "05-01-1992",
        "fatalityid": 4,
        "total": 4,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-15-1992",
        "fatalityid": 1,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-15-1992",
        "fatalityid": 2,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-15-1992",
        "fatalityid": 3,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-15-1992",
        "fatalityid": 4,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-15-1992",
        "fatalityid": 5,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-01-1993",
        "fatalityid": 1,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-01-1993",
        "fatalityid": 2,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-01-1993",
        "fatalityid": 3,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-01-1993",
        "fatalityid": 4,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-01-1993",
        "fatalityid": 5,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-01-1993",
        "fatalityid": 6,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-01-1993",
        "fatalityid": 7,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-01-1993",
        "fatalityid": 8,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-06-1993",
        "fatalityid": 1,
        "total": 4,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-06-1993",
        "fatalityid": 2,
        "total": 4,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-06-1993",
        "fatalityid": 3,
        "total": 4,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-06-1993",
        "fatalityid": 4,
        "total": 4,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-07-1993",
        "fatalityid": 1,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-07-1993",
        "fatalityid": 2,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-07-1993",
        "fatalityid": 3,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-07-1993",
        "fatalityid": 4,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-07-1993",
        "fatalityid": 5,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-07-1993",
        "fatalityid": 6,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-14-1993",
        "fatalityid": 1,
        "total": 4,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-14-1993",
        "fatalityid": 2,
        "total": 4,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-14-1993",
        "fatalityid": 3,
        "total": 4,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-14-1993",
        "fatalityid": 4,
        "total": 4,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-20-1994",
        "fatalityid": 1,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-20-1994",
        "fatalityid": 2,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-20-1994",
        "fatalityid": 3,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-20-1994",
        "fatalityid": 4,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-20-1994",
        "fatalityid": 5,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-03-1995",
        "fatalityid": 1,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-03-1995",
        "fatalityid": 2,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-03-1995",
        "fatalityid": 3,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-03-1995",
        "fatalityid": 4,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-03-1995",
        "fatalityid": 5,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-03-1995",
        "fatalityid": 6,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-09-1996",
        "fatalityid": 1,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-09-1996",
        "fatalityid": 2,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-09-1996",
        "fatalityid": 3,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-09-1996",
        "fatalityid": 4,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-09-1996",
        "fatalityid": 5,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-09-1996",
        "fatalityid": 6,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-18-1997",
        "fatalityid": 1,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-18-1997",
        "fatalityid": 2,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-18-1997",
        "fatalityid": 3,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-18-1997",
        "fatalityid": 4,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-18-1997",
        "fatalityid": 5,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-15-1997",
        "fatalityid": 1,
        "total": 4,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-15-1997",
        "fatalityid": 2,
        "total": 4,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-15-1997",
        "fatalityid": 3,
        "total": 4,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-15-1997",
        "fatalityid": 4,
        "total": 4,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-06-1998",
        "fatalityid": 1,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-06-1998",
        "fatalityid": 2,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-06-1998",
        "fatalityid": 3,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-06-1998",
        "fatalityid": 4,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-06-1998",
        "fatalityid": 5,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-24-1998",
        "fatalityid": 1,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-24-1998",
        "fatalityid": 2,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-24-1998",
        "fatalityid": 3,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-24-1998",
        "fatalityid": 4,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-24-1998",
        "fatalityid": 5,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "05-21-1998",
        "fatalityid": 1,
        "total": 4,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "05-21-1998",
        "fatalityid": 2,
        "total": 4,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "05-21-1998",
        "fatalityid": 3,
        "total": 4,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "05-21-1998",
        "fatalityid": 4,
        "total": 4,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-20-1999",
        "fatalityid": 1,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-20-1999",
        "fatalityid": 2,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-20-1999",
        "fatalityid": 3,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-20-1999",
        "fatalityid": 4,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-20-1999",
        "fatalityid": 5,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-20-1999",
        "fatalityid": 6,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-20-1999",
        "fatalityid": 7,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-20-1999",
        "fatalityid": 8,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-20-1999",
        "fatalityid": 9,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-20-1999",
        "fatalityid": 10,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-20-1999",
        "fatalityid": 11,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-20-1999",
        "fatalityid": 12,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-20-1999",
        "fatalityid": 13,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-29-1999",
        "fatalityid": 1,
        "total": 12,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-29-1999",
        "fatalityid": 2,
        "total": 12,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-29-1999",
        "fatalityid": 3,
        "total": 12,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-29-1999",
        "fatalityid": 4,
        "total": 12,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-29-1999",
        "fatalityid": 5,
        "total": 12,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-29-1999",
        "fatalityid": 6,
        "total": 12,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-29-1999",
        "fatalityid": 7,
        "total": 12,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-29-1999",
        "fatalityid": 8,
        "total": 12,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-29-1999",
        "fatalityid": 9,
        "total": 12,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-29-1999",
        "fatalityid": 10,
        "total": 12,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-29-1999",
        "fatalityid": 11,
        "total": 12,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-29-1999",
        "fatalityid": 12,
        "total": 12,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-15-1999",
        "fatalityid": 1,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-15-1999",
        "fatalityid": 2,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-15-1999",
        "fatalityid": 3,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-15-1999",
        "fatalityid": 4,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-15-1999",
        "fatalityid": 5,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-15-1999",
        "fatalityid": 6,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-15-1999",
        "fatalityid": 7,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-02-1999",
        "fatalityid": 1,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-02-1999",
        "fatalityid": 2,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-02-1999",
        "fatalityid": 3,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-02-1999",
        "fatalityid": 4,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-02-1999",
        "fatalityid": 5,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-02-1999",
        "fatalityid": 6,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-02-1999",
        "fatalityid": 7,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-26-2000",
        "fatalityid": 1,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-26-2000",
        "fatalityid": 2,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-26-2000",
        "fatalityid": 3,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-26-2000",
        "fatalityid": 4,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-26-2000",
        "fatalityid": 5,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-26-2000",
        "fatalityid": 6,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-26-2000",
        "fatalityid": 7,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-05-2001",
        "fatalityid": 1,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-05-2001",
        "fatalityid": 2,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-05-2001",
        "fatalityid": 3,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-05-2001",
        "fatalityid": 4,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-05-2001",
        "fatalityid": 5,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-08-2003",
        "fatalityid": 1,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-08-2003",
        "fatalityid": 2,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-08-2003",
        "fatalityid": 3,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-08-2003",
        "fatalityid": 4,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-08-2003",
        "fatalityid": 5,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-08-2003",
        "fatalityid": 6,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-08-2003",
        "fatalityid": 7,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-08-2004",
        "fatalityid": 1,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-08-2004",
        "fatalityid": 2,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-08-2004",
        "fatalityid": 3,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-08-2004",
        "fatalityid": 4,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-08-2004",
        "fatalityid": 5,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-21-2005",
        "fatalityid": 1,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-21-2005",
        "fatalityid": 2,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-21-2005",
        "fatalityid": 3,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-21-2005",
        "fatalityid": 4,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-21-2005",
        "fatalityid": 5,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-21-2005",
        "fatalityid": 6,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-21-2005",
        "fatalityid": 7,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-21-2005",
        "fatalityid": 8,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-21-2005",
        "fatalityid": 9,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-21-2005",
        "fatalityid": 10,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-03-2005",
        "fatalityid": 1,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-03-2005",
        "fatalityid": 2,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-03-2005",
        "fatalityid": 3,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-03-2005",
        "fatalityid": 4,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-03-2005",
        "fatalityid": 5,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-03-2005",
        "fatalityid": 6,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-03-2005",
        "fatalityid": 7,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-30-2006",
        "fatalityid": 1,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-30-2006",
        "fatalityid": 2,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-30-2006",
        "fatalityid": 3,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-30-2006",
        "fatalityid": 4,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-30-2006",
        "fatalityid": 5,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-30-2006",
        "fatalityid": 6,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-30-2006",
        "fatalityid": 7,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-30-2006",
        "fatalityid": 8,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-25-2006",
        "fatalityid": 1,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-25-2006",
        "fatalityid": 2,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-25-2006",
        "fatalityid": 3,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-25-2006",
        "fatalityid": 4,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-25-2006",
        "fatalityid": 5,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-25-2006",
        "fatalityid": 6,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-25-2006",
        "fatalityid": 7,
        "total": 7,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-02-2006",
        "fatalityid": 1,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-02-2006",
        "fatalityid": 2,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-02-2006",
        "fatalityid": 3,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-02-2006",
        "fatalityid": 4,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-02-2006",
        "fatalityid": 5,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-12-2007",
        "fatalityid": 1,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-12-2007",
        "fatalityid": 2,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-12-2007",
        "fatalityid": 3,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-12-2007",
        "fatalityid": 4,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-12-2007",
        "fatalityid": 5,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 1,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 2,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 3,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 4,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 5,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 6,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 7,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 8,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 9,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 10,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 11,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 12,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 13,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 14,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 15,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 16,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 17,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 18,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 19,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 20,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 21,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 22,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 23,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 24,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 25,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 26,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 27,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 28,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 29,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 30,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 31,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 32,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-16-2007",
        "fatalityid": 33,
        "total": 33,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-07-2007",
        "fatalityid": 1,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-07-2007",
        "fatalityid": 2,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-07-2007",
        "fatalityid": 3,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-07-2007",
        "fatalityid": 4,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-07-2007",
        "fatalityid": 5,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-07-2007",
        "fatalityid": 6,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-05-2007",
        "fatalityid": 1,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-05-2007",
        "fatalityid": 2,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-05-2007",
        "fatalityid": 3,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-05-2007",
        "fatalityid": 4,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-05-2007",
        "fatalityid": 5,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-05-2007",
        "fatalityid": 6,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-05-2007",
        "fatalityid": 7,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "12-05-2007",
        "fatalityid": 8,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-07-2008",
        "fatalityid": 1,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-07-2008",
        "fatalityid": 2,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-07-2008",
        "fatalityid": 3,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-07-2008",
        "fatalityid": 4,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-07-2008",
        "fatalityid": 5,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-07-2008",
        "fatalityid": 6,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-14-2008",
        "fatalityid": 1,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-14-2008",
        "fatalityid": 2,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-14-2008",
        "fatalityid": 3,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-14-2008",
        "fatalityid": 4,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-14-2008",
        "fatalityid": 5,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-14-2008",
        "fatalityid": 6,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-25-2008",
        "fatalityid": 1,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-25-2008",
        "fatalityid": 2,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-25-2008",
        "fatalityid": 3,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-25-2008",
        "fatalityid": 4,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-25-2008",
        "fatalityid": 5,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "06-25-2008",
        "fatalityid": 6,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-10-2009",
        "fatalityid": 1,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-10-2009",
        "fatalityid": 2,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-10-2009",
        "fatalityid": 3,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-10-2009",
        "fatalityid": 4,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-10-2009",
        "fatalityid": 5,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-10-2009",
        "fatalityid": 6,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-10-2009",
        "fatalityid": 7,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-10-2009",
        "fatalityid": 8,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-10-2009",
        "fatalityid": 9,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-10-2009",
        "fatalityid": 10,
        "total": 10,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-29-2009",
        "fatalityid": 1,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-29-2009",
        "fatalityid": 2,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-29-2009",
        "fatalityid": 3,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-29-2009",
        "fatalityid": 4,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-29-2009",
        "fatalityid": 5,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-29-2009",
        "fatalityid": 6,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-29-2009",
        "fatalityid": 7,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "03-29-2009",
        "fatalityid": 8,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-03-2009",
        "fatalityid": 1,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-03-2009",
        "fatalityid": 2,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-03-2009",
        "fatalityid": 3,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-03-2009",
        "fatalityid": 4,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-03-2009",
        "fatalityid": 5,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-03-2009",
        "fatalityid": 6,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-03-2009",
        "fatalityid": 7,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-03-2009",
        "fatalityid": 8,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-03-2009",
        "fatalityid": 9,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-03-2009",
        "fatalityid": 10,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-03-2009",
        "fatalityid": 11,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-03-2009",
        "fatalityid": 12,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "04-03-2009",
        "fatalityid": 13,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-05-2009",
        "fatalityid": 1,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-05-2009",
        "fatalityid": 2,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-05-2009",
        "fatalityid": 3,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-05-2009",
        "fatalityid": 4,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-05-2009",
        "fatalityid": 5,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-05-2009",
        "fatalityid": 6,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-05-2009",
        "fatalityid": 7,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-05-2009",
        "fatalityid": 8,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-05-2009",
        "fatalityid": 9,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-05-2009",
        "fatalityid": 10,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-05-2009",
        "fatalityid": 11,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-05-2009",
        "fatalityid": 12,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "11-05-2009",
        "fatalityid": 13,
        "total": 13,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-19-2010",
        "fatalityid": 1,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-19-2010",
        "fatalityid": 2,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-19-2010",
        "fatalityid": 3,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-19-2010",
        "fatalityid": 4,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-19-2010",
        "fatalityid": 5,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-19-2010",
        "fatalityid": 6,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-19-2010",
        "fatalityid": 7,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-19-2010",
        "fatalityid": 8,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-03-2010",
        "fatalityid": 1,
        "total": 9,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-03-2010",
        "fatalityid": 2,
        "total": 9,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-03-2010",
        "fatalityid": 3,
        "total": 9,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-03-2010",
        "fatalityid": 4,
        "total": 9,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-03-2010",
        "fatalityid": 5,
        "total": 9,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-03-2010",
        "fatalityid": 6,
        "total": 9,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-03-2010",
        "fatalityid": 7,
        "total": 9,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-03-2010",
        "fatalityid": 8,
        "total": 9,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "08-03-2010",
        "fatalityid": 9,
        "total": 9,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-08-2011",
        "fatalityid": 1,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-08-2011",
        "fatalityid": 2,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-08-2011",
        "fatalityid": 3,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-08-2011",
        "fatalityid": 4,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-08-2011",
        "fatalityid": 5,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "01-08-2011",
        "fatalityid": 6,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-06-2011",
        "fatalityid": 1,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-06-2011",
        "fatalityid": 2,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-06-2011",
        "fatalityid": 3,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-06-2011",
        "fatalityid": 4,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "09-06-2011",
        "fatalityid": 5,
        "total": 5,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-14-2011",
        "fatalityid": 1,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-14-2011",
        "fatalityid": 2,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-14-2011",
        "fatalityid": 3,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-14-2011",
        "fatalityid": 4,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-14-2011",
        "fatalityid": 5,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-14-2011",
        "fatalityid": 6,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-14-2011",
        "fatalityid": 7,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "10-14-2011",
        "fatalityid": 8,
        "total": 8,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "02-22-2012",
        "fatalityid": 1,
        "total": 5,
        "eventname": "Atlanta"
    },
    {
        "eventdate": "02-22-2012",
        "fatalityid": 2,
        "total": 5,
        "eventname": "Atlanta"
    },
    {
        "eventdate": "02-22-2012",
        "fatalityid": 3,
        "total": 5,
        "eventname": "Atlanta"
    },
    {
        "eventdate": "02-22-2012",
        "fatalityid": 4,
        "total": 5,
        "eventname": "Atlanta"
    },
    {
        "eventdate": "02-22-2012",
        "fatalityid": 5,
        "total": 5,
        "eventname": "Atlanta"
    },
    {
        "eventdate": "04-02-2012",
        "fatalityid": 1,
        "total": 7,
        "eventname": "Oikos University"
    },
    {
        "eventdate": "04-02-2012",
        "fatalityid": 2,
        "total": 7,
        "eventname": "Oikos University"
    },
    {
        "eventdate": "04-02-2012",
        "fatalityid": 3,
        "total": 7,
        "eventname": "Oikos University"
    },
    {
        "eventdate": "04-02-2012",
        "fatalityid": 4,
        "total": 7,
        "eventname": "Oikos University"
    },
    {
        "eventdate": "04-02-2012",
        "fatalityid": 5,
        "total": 7,
        "eventname": "Oikos University"
    },
    {
        "eventdate": "04-02-2012",
        "fatalityid": 6,
        "total": 7,
        "eventname": "Oikos University"
    },
    {
        "eventdate": "04-02-2012",
        "fatalityid": 7,
        "total": 7,
        "eventname": "Oikos University"
    },
    {
        "eventdate": "05-20-2012",
        "fatalityid": 1,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "05-20-2012",
        "fatalityid": 2,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "05-20-2012",
        "fatalityid": 3,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "05-20-2012",
        "fatalityid": 4,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "05-20-2012",
        "fatalityid": 5,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "05-20-2012",
        "fatalityid": 6,
        "total": 6,
        "eventname": "Incident Name"
    },
    {
        "eventdate": "07-20-2012",
        "fatalityid": 1,
        "total": 12,
        "eventname": "Aurora"
    },
    {
        "eventdate": "07-20-2012",
        "fatalityid": 2,
        "total": 12,
        "eventname": "Aurora"
    },
    {
        "eventdate": "07-20-2012",
        "fatalityid": 3,
        "total": 12,
        "eventname": "Aurora"
    },
    {
        "eventdate": "07-20-2012",
        "fatalityid": 4,
        "total": 12,
        "eventname": "Aurora"
    },
    {
        "eventdate": "07-20-2012",
        "fatalityid": 5,
        "total": 12,
        "eventname": "Aurora"
    },
    {
        "eventdate": "07-20-2012",
        "fatalityid": 6,
        "total": 12,
        "eventname": "Aurora"
    },
    {
        "eventdate": "07-20-2012",
        "fatalityid": 7,
        "total": 12,
        "eventname": "Aurora"
    },
    {
        "eventdate": "07-20-2012",
        "fatalityid": 8,
        "total": 12,
        "eventname": "Aurora"
    },
    {
        "eventdate": "07-20-2012",
        "fatalityid": 9,
        "total": 12,
        "eventname": "Aurora"
    },
    {
        "eventdate": "07-20-2012",
        "fatalityid": 10,
        "total": 12,
        "eventname": "Aurora"
    },
    {
        "eventdate": "07-20-2012",
        "fatalityid": 11,
        "total": 12,
        "eventname": "Aurora"
    },
    {
        "eventdate": "07-20-2012",
        "fatalityid": 12,
        "total": 12,
        "eventname": "Aurora"
    },
    {
        "eventdate": "08-05-2012",
        "fatalityid": 1,
        "total": 7,
        "eventname": "Oak Creek"
    },
    {
        "eventdate": "08-05-2012",
        "fatalityid": 2,
        "total": 7,
        "eventname": "Oak Creek"
    },
    {
        "eventdate": "08-05-2012",
        "fatalityid": 3,
        "total": 7,
        "eventname": "Oak Creek"
    },
    {
        "eventdate": "08-05-2012",
        "fatalityid": 4,
        "total": 7,
        "eventname": "Oak Creek"
    },
    {
        "eventdate": "08-05-2012",
        "fatalityid": 5,
        "total": 7,
        "eventname": "Oak Creek"
    },
    {
        "eventdate": "08-05-2012",
        "fatalityid": 6,
        "total": 7,
        "eventname": "Oak Creek"
    },
    {
        "eventdate": "08-05-2012",
        "fatalityid": 7,
        "total": 7,
        "eventname": "Oak Creek"
    },
    {
        "eventdate": "09-27-2012",
        "fatalityid": 1,
        "total": 7,
        "eventname": "Minneapolis"
    },
    {
        "eventdate": "09-27-2012",
        "fatalityid": 2,
        "total": 7,
        "eventname": "Minneapolis"
    },
    {
        "eventdate": "09-27-2012",
        "fatalityid": 3,
        "total": 7,
        "eventname": "Minneapolis"
    },
    {
        "eventdate": "09-27-2012",
        "fatalityid": 4,
        "total": 7,
        "eventname": "Minneapolis"
    },
    {
        "eventdate": "09-27-2012",
        "fatalityid": 5,
        "total": 7,
        "eventname": "Minneapolis"
    },
    {
        "eventdate": "09-27-2012",
        "fatalityid": 6,
        "total": 7,
        "eventname": "Minneapolis"
    },
    {
        "eventdate": "09-27-2012",
        "fatalityid": 7,
        "total": 7,
        "eventname": "Minneapolis"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 1,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 2,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 3,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 4,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 5,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 6,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 7,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 8,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 9,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 10,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 11,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 12,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 13,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 14,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 15,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 16,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 17,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 18,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 19,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 20,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 21,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 22,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 23,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 24,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 25,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 26,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "12-14-2012",
        "fatalityid": 27,
        "total": 27,
        "eventname": "Sandy Hook"
    },
    {
        "eventdate": "03-13-2013",
        "fatalityid": 1,
        "total": 5,
        "eventname": "Herkimer"
    },
    {
        "eventdate": "03-13-2013",
        "fatalityid": 2,
        "total": 5,
        "eventname": "Herkimer"
    },
    {
        "eventdate": "03-13-2013",
        "fatalityid": 3,
        "total": 5,
        "eventname": "Herkimer"
    },
    {
        "eventdate": "03-13-2013",
        "fatalityid": 4,
        "total": 5,
        "eventname": "Herkimer"
    },
    {
        "eventdate": "03-13-2013",
        "fatalityid": 5,
        "total": 5,
        "eventname": "Herkimer"
    },
    {
        "eventdate": "04-21-2013",
        "fatalityid": 1,
        "total": 5,
        "eventname": "Federal Way"
    },
    {
        "eventdate": "04-21-2013",
        "fatalityid": 2,
        "total": 5,
        "eventname": "Federal Way"
    },
    {
        "eventdate": "04-21-2013",
        "fatalityid": 3,
        "total": 5,
        "eventname": "Federal Way"
    },
    {
        "eventdate": "04-21-2013",
        "fatalityid": 4,
        "total": 5,
        "eventname": "Federal Way"
    },
    {
        "eventdate": "04-21-2013",
        "fatalityid": 5,
        "total": 5,
        "eventname": "Federal Way"
    },
    {
        "eventdate": "06-07-2013",
        "fatalityid": 1,
        "total": 6,
        "eventname": "Santa Monica"
    },
    {
        "eventdate": "06-07-2013",
        "fatalityid": 2,
        "total": 6,
        "eventname": "Santa Monica"
    },
    {
        "eventdate": "06-07-2013",
        "fatalityid": 3,
        "total": 6,
        "eventname": "Santa Monica"
    },
    {
        "eventdate": "06-07-2013",
        "fatalityid": 4,
        "total": 6,
        "eventname": "Santa Monica"
    },
    {
        "eventdate": "06-07-2013",
        "fatalityid": 5,
        "total": 6,
        "eventname": "Santa Monica"
    },
    {
        "eventdate": "06-07-2013",
        "fatalityid": 6,
        "total": 6,
        "eventname": "Santa Monica"
    },
    {
        "eventdate": "07-26-2013",
        "fatalityid": 1,
        "total": 6,
        "eventname": "Hialeah"
    },
    {
        "eventdate": "07-26-2013",
        "fatalityid": 2,
        "total": 6,
        "eventname": "Hialeah"
    },
    {
        "eventdate": "07-26-2013",
        "fatalityid": 3,
        "total": 6,
        "eventname": "Hialeah"
    },
    {
        "eventdate": "07-26-2013",
        "fatalityid": 4,
        "total": 6,
        "eventname": "Hialeah"
    },
    {
        "eventdate": "07-26-2013",
        "fatalityid": 5,
        "total": 6,
        "eventname": "Hialeah"
    },
    {
        "eventdate": "07-26-2013",
        "fatalityid": 6,
        "total": 6,
        "eventname": "Hialeah"
    },
    {
        "eventdate": "09-16-2013",
        "fatalityid": 1,
        "total": 13,
        "eventname": "Navy Yard"
    },
    {
        "eventdate": "09-16-2013",
        "fatalityid": 2,
        "total": 13,
        "eventname": "Navy Yard"
    },
    {
        "eventdate": "09-16-2013",
        "fatalityid": 3,
        "total": 13,
        "eventname": "Navy Yard"
    },
    {
        "eventdate": "09-16-2013",
        "fatalityid": 4,
        "total": 13,
        "eventname": "Navy Yard"
    },
    {
        "eventdate": "09-16-2013",
        "fatalityid": 5,
        "total": 13,
        "eventname": "Navy Yard"
    },
    {
        "eventdate": "09-16-2013",
        "fatalityid": 6,
        "total": 13,
        "eventname": "Navy Yard"
    },
    {
        "eventdate": "09-16-2013",
        "fatalityid": 7,
        "total": 13,
        "eventname": "Navy Yard"
    },
    {
        "eventdate": "09-16-2013",
        "fatalityid": 8,
        "total": 13,
        "eventname": "Navy Yard"
    },
    {
        "eventdate": "09-16-2013",
        "fatalityid": 9,
        "total": 13,
        "eventname": "Navy Yard"
    },
    {
        "eventdate": "09-16-2013",
        "fatalityid": 10,
        "total": 13,
        "eventname": "Navy Yard"
    },
    {
        "eventdate": "09-16-2013",
        "fatalityid": 11,
        "total": 13,
        "eventname": "Navy Yard"
    },
    {
        "eventdate": "09-16-2013",
        "fatalityid": 12,
        "total": 13,
        "eventname": "Navy Yard"
    },
    {
        "eventdate": "09-16-2013",
        "fatalityid": 13,
        "total": 13,
        "eventname": "Navy Yard"
    },
    {
        "eventdate": "02-20-2014",
        "fatalityid": 1,
        "total": 4,
        "eventname": "Alturas"
    },
    {
        "eventdate": "02-20-2014",
        "fatalityid": 2,
        "total": 4,
        "eventname": "Alturas"
    },
    {
        "eventdate": "02-20-2014",
        "fatalityid": 3,
        "total": 4,
        "eventname": "Alturas"
    },
    {
        "eventdate": "02-20-2014",
        "fatalityid": 4,
        "total": 4,
        "eventname": "Alturas"
    },
    {
        "eventdate": "05-23-2014",
        "fatalityid": 1,
        "total": 7,
        "eventname": "Isla Vista"
    },
    {
        "eventdate": "05-23-2014",
        "fatalityid": 2,
        "total": 7,
        "eventname": "Isla Vista"
    },
    {
        "eventdate": "05-23-2014",
        "fatalityid": 3,
        "total": 7,
        "eventname": "Isla Vista"
    },
    {
        "eventdate": "05-23-2014",
        "fatalityid": 4,
        "total": 7,
        "eventname": "Isla Vista"
    },
    {
        "eventdate": "05-23-2014",
        "fatalityid": 5,
        "total": 7,
        "eventname": "Isla Vista"
    },
    {
        "eventdate": "05-23-2014",
        "fatalityid": 6,
        "total": 7,
        "eventname": "Isla Vista"
    },
    {
        "eventdate": "05-23-2014",
        "fatalityid": 7,
        "total": 7,
        "eventname": "Isla Vista"
    },
    {
        "eventdate": "10-24-2014",
        "fatalityid": 1,
        "total": 5,
        "eventname": "Marysville"
    },
    {
        "eventdate": "10-24-2014",
        "fatalityid": 2,
        "total": 5,
        "eventname": "Marysville"
    },
    {
        "eventdate": "10-24-2014",
        "fatalityid": 3,
        "total": 5,
        "eventname": "Marysville"
    },
    {
        "eventdate": "10-24-2014",
        "fatalityid": 4,
        "total": 5,
        "eventname": "Marysville"
    },
    {
        "eventdate": "10-24-2014",
        "fatalityid": 5,
        "total": 5,
        "eventname": "Marysville"
    },
    {
        "eventdate": "06-18-2015",
        "fatalityid": 1,
        "total": 9,
        "eventname": "Charleston"
    },
    {
        "eventdate": "06-18-2015",
        "fatalityid": 2,
        "total": 9,
        "eventname": "Charleston"
    },
    {
        "eventdate": "06-18-2015",
        "fatalityid": 3,
        "total": 9,
        "eventname": "Charleston"
    },
    {
        "eventdate": "06-18-2015",
        "fatalityid": 4,
        "total": 9,
        "eventname": "Charleston"
    },
    {
        "eventdate": "06-18-2015",
        "fatalityid": 5,
        "total": 9,
        "eventname": "Charleston"
    },
    {
        "eventdate": "06-18-2015",
        "fatalityid": 6,
        "total": 9,
        "eventname": "Charleston"
    },
    {
        "eventdate": "06-18-2015",
        "fatalityid": 7,
        "total": 9,
        "eventname": "Charleston"
    },
    {
        "eventdate": "06-18-2015",
        "fatalityid": 8,
        "total": 9,
        "eventname": "Charleston"
    },
    {
        "eventdate": "06-18-2015",
        "fatalityid": 9,
        "total": 9,
        "eventname": "Charleston"
    },
    {
        "eventdate": "07-16-2015",
        "fatalityid": 1,
        "total": 5,
        "eventname": "Chattanooga"
    },
    {
        "eventdate": "07-16-2015",
        "fatalityid": 2,
        "total": 5,
        "eventname": "Chattanooga"
    },
    {
        "eventdate": "07-16-2015",
        "fatalityid": 3,
        "total": 5,
        "eventname": "Chattanooga"
    },
    {
        "eventdate": "07-16-2015",
        "fatalityid": 4,
        "total": 5,
        "eventname": "Chattanooga"
    },
    {
        "eventdate": "07-16-2015",
        "fatalityid": 5,
        "total": 5,
        "eventname": "Chattanooga"
    }
]

my_data_epoched = [{'days_since_epoch': mymidi.days_since_epoch(datetime.datetime.strptime(d['eventdate'], '%m-%d-%Y')), 'fatalityid': d['fatalityid'], 'total': d['total']} for d in my_data]

my_data_timed = [{'beat': mymidi.beat(d['days_since_epoch']), 'fatalityid': d['fatalityid'], 'total': d['total']} for d in my_data_epoched]

start_time = my_data_timed[0]['beat']

def mag_to_pitch_tuned(fatalities):
    # Where does this data point sit in the domain of your data? (I.E. the min fatalities is 5, the max in 27). In this case the optional 'True' means the scale is reversed, so the highest value will return the lowest percentage.
    scale_pct = mymidi.linear_scale_pct(1, 33, fatalities, True)

    # Another option: Linear scale, reverse order
    # scale_pct = mymidi.linear_scale_pct(3, 5.7, fatalities, True)

    # Another option: Logarithmic scale, reverse order
    # scale_pct = mymidi.log_scale_pct(3, 5.7, fatalities, True)

    # Pick a range of notes. This allows you to play in a key.
    c_major = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    c_minor = ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb']
    chromatic = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    c_penta_major = ['C', 'D', 'E', 'G', 'A']
    c_penta_minor = ['C', 'Eb', 'F', 'G', 'Bb']

    #Find the note that matches your data point
    note = mymidi.scale_to_note(scale_pct, c_minor)

    #Translate that note to a MIDI pitch
    midi_pitch = mymidi.note_to_midi_pitch(note)

    return midi_pitch

def mag_to_duration(fatalities):
    # Where does this data point sit in the domain of your data? (I.E. the min fatalities is 5, the max in 27). In this case the optional 'True' means the scale is reversed, so the highest value will return the lowest percentage.
    scale_pct = mymidi.linear_scale_pct(0, 34, fatalities, False)

    # Another option: Linear scale, reverse order
    # scale_pct = mymidi.linear_scale_pct(3, 5.7, fatalities, True)

    # Another option: Logarithmic scale, reverse order
    # scale_pct = mymidi.log_scale_pct(3, 5.7, fatalities, True)

    #Translate that note to a MIDI duration
    midi_duration = 10 + scale_pct*20

    return midi_duration

def mag_to_attack(total):
    # Where does this data point sit in the domain of your data? (I.E. the min fatalities is 5, the max in 27). In this case the optional 'True' means the scale is reversed, so the highest value will return the lowest percentage.
    scale_pct = mymidi.linear_scale_pct(0, 34, total, False)

    #Translate that note to a MIDI duration
    midi_attack = 50 + scale_pct*70

    return midi_attack


note_list = []

#for d in my_data_timed:
for index, d in enumerate(my_data_timed):

    note_list.append([
        (d['beat'] + index*.075 - start_time), #multiply by negative 1 to reverse midi track (start at present, go to past) GO BACK IN TIME
        mag_to_pitch_tuned(float(d['fatalityid'])),
        mag_to_attack(float(d['fatalityid'])),
        #mag_to_attack(float(d['total'])),#50,  # attack
        mag_to_duration(float(d['total']))#16 #mag_to_duration(d['fatalities']) #1  # duration, in beats
    ])

    # create csv with any data you want to use in the browser
    print str(my_data[index]['eventdate']) + ', ' + str(d['beat'] + index*.075 - start_time) + ', ' + str(d['fatalityid']) + ', ' + str(d['total']) + ', ' + str(my_data[index]['eventname'])

#print len(note_list)


# Add a track with those notes
#mymidi.add_track(note_list)

# Output the .mid file
mymidi.save_midi()