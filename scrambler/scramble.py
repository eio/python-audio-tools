import random
import argparse
from pydub import AudioSegment

if __name__ == "__main__":
    print("Scrambling...")
    parser = argparse.ArgumentParser()
    parser.add_argument("wavfile", help="Filepath to WAV file")
    parser.add_argument(
        "--chunk-size", help="Size of chunk in milliseconds", default=80
    )
    args = parser.parse_args()

    chunk_size = int(args.chunk_size)
    sound = AudioSegment.from_wav(args.wavfile)

    # number of chunks in audio file
    num_chunks = int(len(sound) / chunk_size)

    # split up audio into chunks
    # and assign each chunk a number
    index = 0
    chunks = {}
    for i in range(0, num_chunks):
        chunks[i] = sound[index : index + chunk_size]
        index += chunk_size

    # at this point, we have:
    #
    #    chunks = {
    #       0: first_audio_chunk,
    #       1: second_audio_chunk,
    #       2: third_audio_chunk,
    #       ...
    #    }
    #

    # get array of our chunk numbers/keys: [0,1,2,...]
    chunk_keys = list(chunks.keys())
    # scramble the array, yielding something like: [2,0,1,...]
    random.shuffle(chunk_keys)

    # generate new empty AudioSegment
    # as the starting point for our output file
    newsound = AudioSegment.silent(duration=0)

    # iterate through our randomized `chunk_keys` array
    # and concatenate the randomized audio chunks
    # into a new, scrambled AudioSegment
    for i in chunk_keys:
        newsound += chunks[i]

    # simple export
    outname = "{}ms-scramble-{}".format(chunk_size, args.wavfile)
    output_file = newsound.export(outname, format="wav")
    print("Output to: `{}`".format(outname))
