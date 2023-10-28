import mido

# Create a new MIDI file with a tempo of 90 beats per minute
mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)

# Set tempo and time signature
track.append(mido.MetaMessage("time_signature", numerator=4, denominator=4, time=0))
track.append(
    mido.MetaMessage("set_tempo", tempo=666667, time=0)
)  # Tempo in microseconds per quarter note

# Add a 90s hip-hop beat pattern
ticks_per_beat = mid.ticks_per_beat
ticks_per_quarter_note = ticks_per_beat * 4  # For 4/4 time signature
kick_note = 36  # MIDI note for a kick drum
snare_note = 38  # MIDI note for a snare drum
hihat_note = 42  # MIDI note for a closed hi-hat

# Define the beat pattern
beat_pattern = [
    (kick_note, 0),
    (hihat_note, ticks_per_quarter_note // 2),
    (kick_note, 0),
    (hihat_note, ticks_per_quarter_note // 2),
    (kick_note, 0),
    (hihat_note, ticks_per_quarter_note // 2),
    (kick_note, 0),
    (hihat_note, ticks_per_quarter_note // 2),
    (snare_note, 0),
    (hihat_note, ticks_per_quarter_note // 2),
    (kick_note, 0),
    (hihat_note, ticks_per_quarter_note // 2),
    (kick_note, 0),
    (hihat_note, ticks_per_quarter_note // 2),
    (kick_note, 0),
    (hihat_note, ticks_per_quarter_note // 2),
]

# Add the beat pattern to the track
for note, time in beat_pattern:
    note_on = mido.Message("note_on", note=note, velocity=64, time=0)
    note_off = mido.Message("note_off", note=note, velocity=64, time=time)
    track.append(note_on)
    track.append(note_off)

# Save the MIDI file
mid.save("90s_hip_hop_beat.mid")
