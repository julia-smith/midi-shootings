import datetime
from miditime.MIDITime import MIDITime

# Instantiate the class with a tempo (120bpm is the default), an output file destination, number of seconds to represent a year, base octave (5 is Middle C), and octave range.
#mymidi = MIDITime(120, 'y-axis.mid')
mymidi = MIDITime(120, 'y-axis.mid', 10, 2, 3)

# Create a list of notes. Each note is a list: [time, pitch, attack, duration]
# midinotes = [
#     [0, 60, 200, 3],  #At 0 beats (the start), Middle C with attack 200, for 3 beats
#     [10, 61, 200, 4]  #At 10 beats (12 seconds from start), C#5 with attack 200, for 4 beats
# ]


my_data = [
    {'event_date': '20-07-2012', 'beat': 1},
    {'event_date': '20-08-2012', 'beat': 1},
    {'event_date': '20-09-2012', 'beat': 1},
    {'event_date': '20-10-2012', 'beat': 1},
    {'event_date': '20-11-2012', 'beat': 1},
    {'event_date': '20-12-2012', 'beat': 1},
    {'event_date': '20-01-2013', 'beat': 1},
    {'event_date': '20-02-2013', 'beat': 1},
    {'event_date': '20-03-2013', 'beat': 1},
    {'event_date': '20-04-2013', 'beat': 1},
    {'event_date': '20-05-2013', 'beat': 1},
    {'event_date': '20-06-2013', 'beat': 1},
    {'event_date': '20-07-2013', 'beat': 1},
    {'event_date': '20-08-2013', 'beat': 1},
    {'event_date': '20-09-2013', 'beat': 1},
    {'event_date': '20-10-2013', 'beat': 1},
    {'event_date': '20-11-2013', 'beat': 1},
    {'event_date': '20-12-2013', 'beat': 1},
    {'event_date': '20-01-2014', 'beat': 1},
    {'event_date': '20-02-2014', 'beat': 1},
    {'event_date': '20-03-2014', 'beat': 1},
    {'event_date': '20-04-2014', 'beat': 1},
    {'event_date': '20-05-2014', 'beat': 1},
    {'event_date': '20-06-2014', 'beat': 1},
    {'event_date': '20-07-2014', 'beat': 1},
    {'event_date': '20-08-2014', 'beat': 1},
    {'event_date': '20-09-2014', 'beat': 1},
    {'event_date': '20-10-2014', 'beat': 1},
    {'event_date': '20-11-2014', 'beat': 1},
    {'event_date': '20-12-2014', 'beat': 1},
    {'event_date': '20-01-2015', 'beat': 1},
    {'event_date': '20-02-2015', 'beat': 1},
    {'event_date': '20-03-2015', 'beat': 1},
    {'event_date': '20-04-2015', 'beat': 1},
    {'event_date': '20-05-2015', 'beat': 1},
    {'event_date': '20-06-2015', 'beat': 1},
    {'event_date': '20-07-2015', 'beat': 1},
    {'event_date': '20-08-2015', 'beat': 1},
    {'event_date': '20-09-2015', 'beat': 1},
    {'event_date': '20-10-2015', 'beat': 1},
    {'event_date': '20-11-2015', 'beat': 1},
    {'event_date': '20-12-2015', 'beat': 1}
]

my_data_epoched = [{'days_since_epoch': mymidi.days_since_epoch(datetime.datetime.strptime(d['event_date'], '%d-%m-%Y')), 'beat': d['beat']} for d in my_data]

my_data_timed = [{'beat': mymidi.beat(d['days_since_epoch']), 'beat': d['beat']} for d in my_data_epoched]

start_time = my_data_timed[0]['beat']

def mag_to_pitch_tuned(beat):
    # Where does this data point sit in the domain of your data? (I.E. the min fatalities is 5, the max in 27). In this case the optional 'True' means the scale is reversed, so the highest value will return the lowest percentage.
    scale_pct = mymidi.linear_scale_pct(0, 1, beat, True)

    # Another option: Linear scale, reverse order
    # scale_pct = mymidi.linear_scale_pct(3, 5.7, fatalities, True)

    # Another option: Logarithmic scale, reverse order
    # scale_pct = mymidi.log_scale_pct(3, 5.7, fatalities, True)

    # Pick a range of notes. This allows you to play in a key.
    #c_major = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    c_minor = ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb']

    #Find the note that matches your data point
    note = mymidi.scale_to_note(scale_pct, c_minor)

    #Translate that note to a MIDI pitch
    midi_pitch = mymidi.note_to_midi_pitch(note)

    return midi_pitch

def mag_to_duration(beat):
    # Where does this data point sit in the domain of your data? (I.E. the min fatalities is 5, the max in 27). In this case the optional 'True' means the scale is reversed, so the highest value will return the lowest percentage.
    scale_pct = mymidi.linear_scale_pct(4, 28, beat, False)
    print scale_pct

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
        d['beat'] - start_time,
        mag_to_pitch_tuned(d['beat']),
        100,  # attack
        1  # duration, in beats
    ])



# Add a track with those notes
#mymidi.add_track(midinotes)
mymidi.add_track(note_list)

# Output the .mid file
mymidi.save_midi()