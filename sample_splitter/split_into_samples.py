from pydub import AudioSegment
import os

# Load the audio file
sound = AudioSegment.from_wav("sounds.wav")

# Set parameters for silence detection and cropping
silence_threshold = -35  # Adjust this value based on your audio
minimum_silence_duration = 500  # in milliseconds
output_folder = "output/"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to save audio clips
def save_clip(audio, index):
    output_file = os.path.join(output_folder, f"{str(index).zfill(4)}.wav")
    audio.export(output_file, format="wav")


# Iterate through the audio and detect sound events
start_trim = 0
end_trim = 0
last_sound = 0
for i, chunk in enumerate(sound):
    print(f"Processing chunk {i} with dBFS {chunk.dBFS}")
    if chunk.dBFS < silence_threshold:
        if start_trim == 0:
            start_trim = i
        end_trim = i
        print(f"Silence detected. Start trim: {start_trim}, End trim: {end_trim}")
    else:
        if start_trim != 0 and (end_trim - start_trim) > minimum_silence_duration:
            sound_event = sound[last_sound:end_trim]
            save_clip(sound_event, last_sound)
            print(
                f"Sound event detected. Saving sound event from {last_sound} to {end_trim}"
            )
            last_sound = end_trim
            start_trim = 0
            end_trim = 0
            print("Resetting start and end trim.")

# Save the last sound event
if last_sound != end_trim:
    sound_event = sound[last_sound:end_trim]
    save_clip(sound_event, last_sound)
    print(f"Saving the last sound event from {last_sound} to {end_trim}")
