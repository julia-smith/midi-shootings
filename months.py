import datetime
from miditime.MIDITime import MIDITime

# Instantiate the class with a tempo (120bpm is the default), an output file destination, number of seconds to represent a year, base octave (5 is Middle C), and octave range.
#mymidi = MIDITime(120, 'main.mid')
mymidi = MIDITime(320, 'clicktrack-50.mid', 12, 3, 3)

# Create a list of notes. Each note is a list: [time, pitch, attack, duration]
# midinotes = [
#     [0, 60, 200, 3],  #At 0 beats (the start), Middle C with attack 200, for 3 beats
#     [10, 61, 200, 4]  #At 10 beats (12 seconds from start), C#5 with attack 200, for 4 beats
# ]


my_data = [
    {'event_date': '01-05-2012', 'fatalities': 1}, #extra
    {'event_date': '01-06-2012', 'fatalities': 1}, #extra
    {'event_date': '01-07-2012', 'fatalities': 1},
    {'event_date': '01-08-2012', 'fatalities': 1},
    {'event_date': '01-09-2012', 'fatalities': 1},
    {'event_date': '01-10-2012', 'fatalities': 1},
    {'event_date': '01-11-2012', 'fatalities': 1},
    {'event_date': '01-12-2012', 'fatalities': 1},
    {'event_date': '01-01-2013', 'fatalities': 1},
    {'event_date': '01-02-2013', 'fatalities': 1},
    {'event_date': '01-03-2013', 'fatalities': 1},
    {'event_date': '01-04-2013', 'fatalities': 1},
    {'event_date': '01-05-2013', 'fatalities': 1},
    {'event_date': '01-06-2013', 'fatalities': 1},
    {'event_date': '01-07-2013', 'fatalities': 1},
    {'event_date': '01-08-2013', 'fatalities': 1},
    {'event_date': '01-09-2013', 'fatalities': 1},
    {'event_date': '01-10-2013', 'fatalities': 1},
    {'event_date': '01-11-2013', 'fatalities': 1},
    {'event_date': '01-12-2013', 'fatalities': 1},
    {'event_date': '01-01-2014', 'fatalities': 1},
    {'event_date': '01-02-2014', 'fatalities': 1},
    {'event_date': '01-03-2014', 'fatalities': 1},
    {'event_date': '01-04-2014', 'fatalities': 1},
    {'event_date': '01-05-2014', 'fatalities': 1},
    {'event_date': '01-06-2014', 'fatalities': 1},
    {'event_date': '01-07-2014', 'fatalities': 1},
    {'event_date': '01-08-2014', 'fatalities': 1},
    {'event_date': '01-09-2014', 'fatalities': 1},
    {'event_date': '01-10-2014', 'fatalities': 1},
    {'event_date': '01-11-2014', 'fatalities': 1},
    {'event_date': '01-12-2014', 'fatalities': 1},
    {'event_date': '01-01-2015', 'fatalities': 1},
    {'event_date': '01-02-2015', 'fatalities': 1},
    {'event_date': '01-03-2015', 'fatalities': 1},
    {'event_date': '01-04-2015', 'fatalities': 1},
    {'event_date': '01-05-2015', 'fatalities': 1},
    {'event_date': '01-06-2015', 'fatalities': 1},
    {'event_date': '01-07-2015', 'fatalities': 1},
    {'event_date': '01-08-2015', 'fatalities': 1}
]

my_data_epoched = [{'days_since_epoch': mymidi.days_since_epoch(datetime.datetime.strptime(d['event_date'], '%d-%m-%Y')), 'fatalities': d['fatalities']} for d in my_data]

my_data_timed = [{'beat': mymidi.beat(d['days_since_epoch']), 'c': d['fatalities']} for d in my_data_epoched]

start_time = my_data_timed[0]['beat']


def mag_to_pitch_tuned(fatalities):
    # Where does this data point sit in the domain of your data? (I.E. the min fatalities is 5, the max in 27). In this case the optional 'True' means the scale is reversed, so the highest value will return the lowest percentage.
    scale_pct = mymidi.linear_scale_pct(0, 45, fatalities, True)

    # Another option: Linear scale, reverse order
    # scale_pct = mymidi.linear_scale_pct(3, 5.7, fatalities, True)

    # Another option: Logarithmic scale, reverse order
    # scale_pct = mymidi.log_scale_pct(3, 5.7, fatalities, True)

    # Pick a range of notes. This allows you to play in a key.
    #c_major = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    c_minor = ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb']

    #Find the note that matches your data point
    note = mymidi.scale_to_note(scale_pct, c_minor)
    #print note

    #Translate that note to a MIDI pitch
    midi_pitch = mymidi.note_to_midi_pitch(note)

    return midi_pitch

def mag_to_duration(fatalities):
    # Where does this data point sit in the domain of your data? (I.E. the min fatalities is 5, the max in 27). In this case the optional 'True' means the scale is reversed, so the highest value will return the lowest percentage.
    scale_pct = mymidi.linear_scale_pct(0, 45, fatalities, False)

    # Another option: Linear scale, reverse order
    # scale_pct = mymidi.linear_scale_pct(3, 5.7, fatalities, True)

    # Another option: Logarithmic scale, reverse order
    # scale_pct = mymidi.log_scale_pct(3, 5.7, fatalities, True)

    #Translate that note to a MIDI duration
    midi_duration = scale_pct*5

    return midi_duration


note_list = []

for d in my_data_timed:
    note_list.append([
        (d['beat'] - start_time)*-1, 
        50, #mag_to_pitch_tuned(d['fatalities']),
        100,  # attack
        .25 #1  # duration, in beats
    ])

print note_list

# Add a track with those notes
#mymidi.add_track(midinotes)
mymidi.add_track(note_list)

# Output the .mid file
mymidi.save_midi()