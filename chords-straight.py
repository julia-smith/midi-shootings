import datetime
from miditime.MIDITime import MIDITime

# Instantiate the class with a tempo (120bpm is the default), an output file destination, number of seconds to represent a year, base octave (5 is Middle C), and octave range.
#mymidi = MIDITime(120, 'chords.mid')
mymidi = MIDITime(320, 'chords-50-sus.mid', 12, 4, 4)

# Create a list of notes. Each note is a list: [time, pitch, attack, duration]
# midinotes = [
#     [0, 60, 200, 3],  #At 0 beats (the start), Middle C with attack 200, for 3 beats
#     [10, 61, 200, 4]  #At 10 beats (12 seconds from start), C#5 with attack 200, for 4 beats
# ]


my_data = [
    {'event_date': '01-07-2012', 'fatalities': 5.0, 'total': 5.0}, #add extra to extend the midi file to the appropriate length (starting in Aug. 2015)
    {'event_date': '20-07-2012', 'fatalities': 1.0, 'total': 12.0},
    {'event_date': '20-07-2012', 'fatalities': 2.0, 'total': 12.0},
    {'event_date': '20-07-2012', 'fatalities': 3.0, 'total': 12.0},
    {'event_date': '20-07-2012', 'fatalities': 4.0, 'total': 12.0},
    {'event_date': '20-07-2012', 'fatalities': 5.0, 'total': 12.0},
    {'event_date': '20-07-2012', 'fatalities': 6.0, 'total': 12.0},
    {'event_date': '20-07-2012', 'fatalities': 7.0, 'total': 12.0},
    {'event_date': '20-07-2012', 'fatalities': 8.0, 'total': 12.0},
    {'event_date': '20-07-2012', 'fatalities': 9.0, 'total': 12.0},
    {'event_date': '20-07-2012', 'fatalities': 10.0, 'total': 12.0},
    {'event_date': '20-07-2012', 'fatalities': 11.0, 'total': 12.0},
    {'event_date': '20-07-2012', 'fatalities': 12.0, 'total': 12.0},
    {'event_date': '05-08-2012', 'fatalities': 1.0, 'total': 7.0},
    {'event_date': '05-08-2012', 'fatalities': 2.0, 'total': 7.0},
    {'event_date': '05-08-2012', 'fatalities': 3.0, 'total': 7.0},
    {'event_date': '05-08-2012', 'fatalities': 4.0, 'total': 7.0},
    {'event_date': '05-08-2012', 'fatalities': 5.0, 'total': 7.0},
    {'event_date': '05-08-2012', 'fatalities': 6.0, 'total': 7.0},
    {'event_date': '05-08-2012', 'fatalities': 7.0, 'total': 7.0},
    {'event_date': '27-09-2012', 'fatalities': 1.0, 'total': 7.0},
    {'event_date': '27-09-2012', 'fatalities': 2.0, 'total': 7.0},
    {'event_date': '27-09-2012', 'fatalities': 3.0, 'total': 7.0},
    {'event_date': '27-09-2012', 'fatalities': 4.0, 'total': 7.0},
    {'event_date': '27-09-2012', 'fatalities': 5.0, 'total': 7.0},
    {'event_date': '27-09-2012', 'fatalities': 6.0, 'total': 7.0},
    {'event_date': '27-09-2012', 'fatalities': 7.0, 'total': 7.0},
    {'event_date': '14-12-2012', 'fatalities': 1.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 2.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 3.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 4.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 5.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 6.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 7.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 8.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 9.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 10.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 11.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 12.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 13.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 14.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 15.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 16.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 17.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 18.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 19.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 20.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 21.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 22.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 23.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 24.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 25.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 26.0, 'total': 27.0},
    {'event_date': '14-12-2012', 'fatalities': 27.0, 'total': 27.0},
    {'event_date': '07-06-2013', 'fatalities': 1.0, 'total': 6.0},
    {'event_date': '07-06-2013', 'fatalities': 2.0, 'total': 6.0},
    {'event_date': '07-06-2013', 'fatalities': 3.0, 'total': 6.0},
    {'event_date': '07-06-2013', 'fatalities': 4.0, 'total': 6.0},
    {'event_date': '07-06-2013', 'fatalities': 5.0, 'total': 6.0},
    {'event_date': '07-06-2013', 'fatalities': 6.0, 'total': 6.0},
    {'event_date': '16-09-2013', 'fatalities': 1.0, 'total': 13.0},
    {'event_date': '16-09-2013', 'fatalities': 2.0, 'total': 13.0},
    {'event_date': '16-09-2013', 'fatalities': 3.0, 'total': 13.0},
    {'event_date': '16-09-2013', 'fatalities': 4.0, 'total': 13.0},
    {'event_date': '16-09-2013', 'fatalities': 5.0, 'total': 13.0},
    {'event_date': '16-09-2013', 'fatalities': 6.0, 'total': 13.0},
    {'event_date': '16-09-2013', 'fatalities': 7.0, 'total': 13.0},
    {'event_date': '16-09-2013', 'fatalities': 8.0, 'total': 13.0},
    {'event_date': '16-09-2013', 'fatalities': 9.0, 'total': 13.0},
    {'event_date': '16-09-2013', 'fatalities': 10.0, 'total': 13.0},
    {'event_date': '16-09-2013', 'fatalities': 11.0, 'total': 13.0},
    {'event_date': '16-09-2013', 'fatalities': 12.0, 'total': 13.0},
    {'event_date': '16-09-2013', 'fatalities': 13.0, 'total': 13.0},
    {'event_date': '23-05-2014', 'fatalities': 1.0, 'total': 7.0},
    {'event_date': '23-05-2014', 'fatalities': 2.0, 'total': 7.0},
    {'event_date': '23-05-2014', 'fatalities': 3.0, 'total': 7.0},
    {'event_date': '23-05-2014', 'fatalities': 4.0, 'total': 7.0},
    {'event_date': '23-05-2014', 'fatalities': 5.0, 'total': 7.0},
    {'event_date': '23-05-2014', 'fatalities': 6.0, 'total': 7.0},
    {'event_date': '23-05-2014', 'fatalities': 7.0, 'total': 7.0},
    {'event_date': '18-06-2015', 'fatalities': 1.0, 'total': 9.0},
    {'event_date': '18-06-2015', 'fatalities': 2.0, 'total': 9.0},
    {'event_date': '18-06-2015', 'fatalities': 3.0, 'total': 9.0},
    {'event_date': '18-06-2015', 'fatalities': 4.0, 'total': 9.0},
    {'event_date': '18-06-2015', 'fatalities': 5.0, 'total': 9.0},
    {'event_date': '18-06-2015', 'fatalities': 6.0, 'total': 9.0},
    {'event_date': '18-06-2015', 'fatalities': 7.0, 'total': 9.0},
    {'event_date': '18-06-2015', 'fatalities': 8.0, 'total': 9.0},
    {'event_date': '18-06-2015', 'fatalities': 9.0, 'total': 9.0},
    {'event_date': '16-07-2015', 'fatalities': 1.0, 'total': 5.0},
    {'event_date': '16-07-2015', 'fatalities': 2.0, 'total': 5.0},
    {'event_date': '16-07-2015', 'fatalities': 3.0, 'total': 5.0},
    {'event_date': '16-07-2015', 'fatalities': 4.0, 'total': 5.0},
    {'event_date': '16-07-2015', 'fatalities': 5.0, 'total': 5.0}
]

my_data_epoched = [{'days_since_epoch': mymidi.days_since_epoch(datetime.datetime.strptime(d['event_date'], '%d-%m-%Y')), 'fatalities': d['fatalities'], 'total': d['total']} for d in my_data]

my_data_timed = [{'beat': mymidi.beat(d['days_since_epoch']), 'fatalities': d['fatalities'], 'total': d['total']} for d in my_data_epoched]

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
    scale_pct = mymidi.linear_scale_pct(0, 28, fatalities, False)

    # Another option: Linear scale, reverse order
    # scale_pct = mymidi.linear_scale_pct(3, 5.7, fatalities, True)

    # Another option: Logarithmic scale, reverse order
    # scale_pct = mymidi.log_scale_pct(3, 5.7, fatalities, True)

    #Translate that note to a MIDI duration
    midi_duration = 10 + scale_pct*12

    return midi_duration

def mag_to_attack(total):
    # Where does this data point sit in the domain of your data? (I.E. the min fatalities is 5, the max in 27). In this case the optional 'True' means the scale is reversed, so the highest value will return the lowest percentage.
    scale_pct = mymidi.linear_scale_pct(0, 28, total, False)

    #Translate that note to a MIDI duration
    midi_attack = 50 + scale_pct*100
    print midi_attack

    return midi_attack


note_list = []

#print my_data_timed

for d in my_data_timed:

    note_list.append([
        (d['beat'] - start_time), #multiply by negative 1 to reverse midi track (start at present, go to past) GO BACK IN TIME
        mag_to_pitch_tuned(d['fatalities']),
        mag_to_attack(d['total']),#50,  # attack
        mag_to_duration(d['total'])#16 #mag_to_duration(d['fatalities']) #1  # duration, in beats
    ])



# Add a track with those notes
#mymidi.add_track(midinotes)
mymidi.add_track(note_list)

# Output the .mid file
mymidi.save_midi()