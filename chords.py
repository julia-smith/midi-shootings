import datetime
from miditime.MIDITime import MIDITime

# Instantiate the class with a tempo (120bpm is the default), an output file destination, number of seconds to represent a year, base octave (5 is Middle C), and octave range.
#mymidi = MIDITime(120, 'chords.mid')
mymidi = MIDITime(120, 'chords.mid', 12, 3, 4)

# Create a list of notes. Each note is a list: [time, pitch, attack, duration]
# midinotes = [
#     [0, 60, 200, 3],  #At 0 beats (the start), Middle C with attack 200, for 3 beats
#     [10, 61, 200, 4]  #At 10 beats (12 seconds from start), C#5 with attack 200, for 4 beats
# ]


my_data = [
    {'event_date': '20-07-2012', 'fatalities': 1.0},
    {'event_date': '20-07-2012', 'fatalities': 2.0},
    {'event_date': '20-07-2012', 'fatalities': 3.0},
    {'event_date': '20-07-2012', 'fatalities': 4.0},
    {'event_date': '20-07-2012', 'fatalities': 5.0},
    {'event_date': '20-07-2012', 'fatalities': 6.0},
    {'event_date': '20-07-2012', 'fatalities': 7.0},
    {'event_date': '20-07-2012', 'fatalities': 8.0},
    {'event_date': '20-07-2012', 'fatalities': 9.0},
    {'event_date': '20-07-2012', 'fatalities': 10.0},
    {'event_date': '20-07-2012', 'fatalities': 11.0},
    {'event_date': '20-07-2012', 'fatalities': 12.0},
    {'event_date': '05-08-2012', 'fatalities': 1.0},
    {'event_date': '05-08-2012', 'fatalities': 2.0},
    {'event_date': '05-08-2012', 'fatalities': 3.0},
    {'event_date': '05-08-2012', 'fatalities': 4.0},
    {'event_date': '05-08-2012', 'fatalities': 5.0},
    {'event_date': '05-08-2012', 'fatalities': 6.0},
    {'event_date': '05-08-2012', 'fatalities': 7.0},
    {'event_date': '27-09-2012', 'fatalities': 1.0},
    {'event_date': '27-09-2012', 'fatalities': 2.0},
    {'event_date': '27-09-2012', 'fatalities': 3.0},
    {'event_date': '27-09-2012', 'fatalities': 4.0},
    {'event_date': '27-09-2012', 'fatalities': 5.0},
    {'event_date': '27-09-2012', 'fatalities': 6.0},
    {'event_date': '27-09-2012', 'fatalities': 7.0},
    {'event_date': '14-12-2012', 'fatalities': 1.0},
    {'event_date': '14-12-2012', 'fatalities': 2.0},
    {'event_date': '14-12-2012', 'fatalities': 3.0},
    {'event_date': '14-12-2012', 'fatalities': 4.0},
    {'event_date': '14-12-2012', 'fatalities': 5.0},
    {'event_date': '14-12-2012', 'fatalities': 6.0},
    {'event_date': '14-12-2012', 'fatalities': 7.0},
    {'event_date': '14-12-2012', 'fatalities': 8.0},
    {'event_date': '14-12-2012', 'fatalities': 9.0},
    {'event_date': '14-12-2012', 'fatalities': 10.0},
    {'event_date': '14-12-2012', 'fatalities': 11.0},
    {'event_date': '14-12-2012', 'fatalities': 12.0},
    {'event_date': '14-12-2012', 'fatalities': 13.0},
    {'event_date': '14-12-2012', 'fatalities': 14.0},
    {'event_date': '14-12-2012', 'fatalities': 15.0},
    {'event_date': '14-12-2012', 'fatalities': 16.0},
    {'event_date': '14-12-2012', 'fatalities': 17.0},
    {'event_date': '14-12-2012', 'fatalities': 18.0},
    {'event_date': '14-12-2012', 'fatalities': 19.0},
    {'event_date': '14-12-2012', 'fatalities': 20.0},
    {'event_date': '14-12-2012', 'fatalities': 21.0},
    {'event_date': '14-12-2012', 'fatalities': 22.0},
    {'event_date': '14-12-2012', 'fatalities': 23.0},
    {'event_date': '14-12-2012', 'fatalities': 24.0},
    {'event_date': '14-12-2012', 'fatalities': 25.0},
    {'event_date': '14-12-2012', 'fatalities': 26.0},
    {'event_date': '14-12-2012', 'fatalities': 27.0},
    {'event_date': '07-06-2013', 'fatalities': 1.0},
    {'event_date': '07-06-2013', 'fatalities': 2.0},
    {'event_date': '07-06-2013', 'fatalities': 3.0},
    {'event_date': '07-06-2013', 'fatalities': 4.0},
    {'event_date': '07-06-2013', 'fatalities': 5.0},
    {'event_date': '07-06-2013', 'fatalities': 6.0},
    {'event_date': '16-09-2013', 'fatalities': 1.0},
    {'event_date': '16-09-2013', 'fatalities': 2.0},
    {'event_date': '16-09-2013', 'fatalities': 3.0},
    {'event_date': '16-09-2013', 'fatalities': 4.0},
    {'event_date': '16-09-2013', 'fatalities': 5.0},
    {'event_date': '16-09-2013', 'fatalities': 6.0},
    {'event_date': '16-09-2013', 'fatalities': 7.0},
    {'event_date': '16-09-2013', 'fatalities': 8.0},
    {'event_date': '16-09-2013', 'fatalities': 9.0},
    {'event_date': '16-09-2013', 'fatalities': 10.0},
    {'event_date': '16-09-2013', 'fatalities': 11.0},
    {'event_date': '16-09-2013', 'fatalities': 12.0},
    {'event_date': '16-09-2013', 'fatalities': 13.0},
    {'event_date': '23-05-2014', 'fatalities': 1.0},
    {'event_date': '23-05-2014', 'fatalities': 2.0},
    {'event_date': '23-05-2014', 'fatalities': 3.0},
    {'event_date': '23-05-2014', 'fatalities': 4.0},
    {'event_date': '23-05-2014', 'fatalities': 5.0},
    {'event_date': '23-05-2014', 'fatalities': 6.0},
    {'event_date': '23-05-2014', 'fatalities': 7.0},
    {'event_date': '18-06-2015', 'fatalities': 1.0},
    {'event_date': '18-06-2015', 'fatalities': 2.0},
    {'event_date': '18-06-2015', 'fatalities': 3.0},
    {'event_date': '18-06-2015', 'fatalities': 4.0},
    {'event_date': '18-06-2015', 'fatalities': 5.0},
    {'event_date': '18-06-2015', 'fatalities': 6.0},
    {'event_date': '18-06-2015', 'fatalities': 7.0},
    {'event_date': '18-06-2015', 'fatalities': 8.0},
    {'event_date': '18-06-2015', 'fatalities': 9.0},
    {'event_date': '16-07-2015', 'fatalities': 1.0},
    {'event_date': '16-07-2015', 'fatalities': 2.0},
    {'event_date': '16-07-2015', 'fatalities': 3.0},
    {'event_date': '16-07-2015', 'fatalities': 4.0},
    {'event_date': '16-07-2015', 'fatalities': 5.0}
]

my_data_epoched = [{'days_since_epoch': mymidi.days_since_epoch(datetime.datetime.strptime(d['event_date'], '%d-%m-%Y')), 'fatalities': d['fatalities']} for d in my_data]

my_data_timed = [{'beat': mymidi.beat(d['days_since_epoch']), 'fatalities': d['fatalities']} for d in my_data_epoched]

start_time = my_data_timed[0]['beat']

def mag_to_pitch_tuned(fatalities):
    # Where does this data point sit in the domain of your data? (I.E. the min fatalities is 5, the max in 27). In this case the optional 'True' means the scale is reversed, so the highest value will return the lowest percentage.
    scale_pct = mymidi.linear_scale_pct(0, 27, fatalities, True)

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
    #print note

    #Translate that note to a MIDI pitch
    midi_pitch = mymidi.note_to_midi_pitch(note)

    return midi_pitch

def mag_to_duration(fatalities):
    # Where does this data point sit in the domain of your data? (I.E. the min fatalities is 5, the max in 27). In this case the optional 'True' means the scale is reversed, so the highest value will return the lowest percentage.
    scale_pct = mymidi.linear_scale_pct(0, 28, fatalities, True)

    # Another option: Linear scale, reverse order
    # scale_pct = mymidi.linear_scale_pct(3, 5.7, fatalities, True)

    # Another option: Logarithmic scale, reverse order
    # scale_pct = mymidi.log_scale_pct(3, 5.7, fatalities, True)

    #Translate that note to a MIDI duration
    midi_duration = scale_pct*5

    return midi_duration


note_list = []

for d in my_data_timed:
    #for x in xrange(0, int(d['fatalities'])):
    #fatalityID = x + 1

    note_list.append([
        d['beat'] - start_time,
        mag_to_pitch_tuned(d['fatalities']),
        100,  # attack
        1 #mag_to_duration(d['fatalities']) #1  # duration, in beats
    ])



# Add a track with those notes
#mymidi.add_track(midinotes)
mymidi.add_track(note_list)

# Output the .mid file
mymidi.save_midi()