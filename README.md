# How to Run

	python scrambler/scramble.py yoursound.wav
^ this will perform 2 actions on your sound:

1) chop your sound up into chunks of equal length (80 milliseconds each)
2) randomly scramble up the order of those chunks so they're all out of sequence

then it will put the product of those actions into a new file called `80ms-scrmbL-yoursound.wav`

	python scrambler/scramble.py yoursound.wav --chunk-size 1000
^ you can also specify the `--chunk-size` parameter.
this is the length of each audio chunk, in millisconds, that is then scrmbLd up by the script.
so here, instead of the default 80 milliseconds, we are passing in `1000` milliseconds (or 1 second).
