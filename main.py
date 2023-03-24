import re
import time
from pydub import AudioSegment
from pydub.generators import Sine
import simpleaudio as sa

def extract_chords_and_lyrics(song: str):
    chords_and_lyrics = []
    lines = song.splitlines()

    for line in lines:
        chords_in_line = re.findall(r'\b[A-G][#|b]?m?\b', line)
        if chords_in_line:
            chords_and_lyrics.append(chords_in_line)
    
    return chords_and_lyrics

def play_chords(chords_and_lyrics):
    chord_frequencies = {
        'A': 440.00,
        'A#': 466.16,
        'B': 493.88,
        'C': 523.25,
        'C#': 554.37,
        'D': 587.33,
        'D#': 622.25,
        'E': 659.25,
        'F': 698.46,
        'F#': 739.99,
        'G': 783.99,
        'G#': 830.61
    }

    for line in chords_and_lyrics:
        for chord in line:
            root = chord_frequencies[chord[:-1]] if chord[-1] == 'm' else chord_frequencies[chord]
            sine_wave = Sine(root)
            audio_segment = sine_wave.to_audio_segment(duration=1000)  # 1000ms = 1s
            play_obj = sa.play_buffer(audio_segment.raw_data, 1, 2, audio_segment.frame_rate)
            play_obj.wait_done()
            time.sleep(0.5)  # Add a short pause between chords

song = '''
Title: "Midnight Whispers"

[Verse 1]
Am F C G
Dark streets, under the moon's embrace,
Am F C G
Our shadows dancing, hearts in a race.
Am F C G
Lost in your eyes, in a neon haze,
Am F C G
We'll set the night on fire, come what may.

[Pre-Chorus]
F G
Whisper to me sweet Angel,
Em Am
Tell me secrets only we know,
F G E
Let the rhythm guide us, in love's shadow.

[Chorus]
Am F C G
Midnight whispers, our love's a flame,
Am F C G
In this moment, we'll live like fame,
Am F C G
Hearts colliding, like waves they sway,
Am F C G
Angel, oh, just let us play.

[Verse 2]
Am F C G
Soft breezes, through the city's soul,
Am F C G
Two hearts racing, we'll never grow old.
Am F C G
Stars above us, like diamonds they glow,
Am F C G
In your embrace, I'll never let go.

[Pre-Chorus]
F G
Whisper to me sweet Angel,
Em Am
Tell me secrets only we know,
F G E
Let the rhythm guide us, in love's shadow.

[Chorus]
Am F C G
Midnight whispers, our love's a flame,
Am F C G
In this moment, we'll live like fame,
Am F C G
Hearts colliding, like waves they sway,
Am F C G
Angel, oh, just let us play.

[Bridge]
Dm
Hold me close, in the moonlight,
Em
We'll dance, defy the hands of time,
F
This love, eternal, endless,
G
Angel, my paradise.

[Chorus]
Am F C G
Midnight whispers, our love's a flame,
Am F C G
In this moment, we'll live like fame,
Am F C G
Hearts colliding, like waves they sway,
Am F C G
Angel, oh, just let us play.

[Outro]
Am F C G
Together, we'll walk through the night,
Am F C G
In your arms, everything feels right,
Am F C G
Midnight whispers, our love's ballet,
Am F C G
Angel, forever we'll stay.
'''

chords_and_lyrics = extract_chords_and_lyrics(song)
play_chords(chords_and_lyrics)
