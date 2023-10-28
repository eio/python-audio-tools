import mido

# Create a new MIDI file with a tempo of 120 beats per minute
mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)

# Set tempo and time signature
track.append(mido.MetaMessage("time_signature", numerator=3, denominator=4, time=0))
track.append(
    mido.MetaMessage("set_tempo", tempo=500000, time=0)
)  # Tempo in microseconds per quarter note

# Add a repeating pulse (kick drum on every beat) for 1 minute
ticks_per_beat = mid.ticks_per_beat
ticks_per_quarter_note = ticks_per_beat * 3  # For 3/4 time signature
total_ticks = ticks_per_quarter_note * 3  # 3 quarter notes in 3/4 time
kick_note = 36  # MIDI note for a kick drum

for i in range(0, 60 * 3):  # 60 seconds * 3 beats per second
    note_on = mido.Message("note_on", note=kick_note, velocity=64, time=0)
    note_off = mido.Message(
        "note_off", note=kick_note, velocity=64, time=total_ticks // 2
    )  # Note duration is half the beat
    track.append(note_on)
    track.append(note_off)

# Save the MIDI file
mid.save("repeating_pulse.mid")
