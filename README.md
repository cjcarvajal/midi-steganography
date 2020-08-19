# Steganography in Midi

## Hiding Messages in a Midi

You can check the midi file structure [here](http://www.music.mcgill.ca/~ich/classes/mumt306/StandardMIDIfileformat.html). To give a short brief, a midi song follows this structure:

* Pattern
  * Track
    * ProgramChangeEvent
    * NoteOn
    * NoteOff

The pattern indicates the root of the song, you have a Track for each instrument in the Pattern. The notes events indicates notes on each instrument, so this events can be listened when the song is played. On the other hand the ProgramChangeEvent indicates which instrument is going to be used on this track, so according to the value you give to this event you select a guitar or a banjo. But the ProgramChangeEvent is not perceptible, so you can have many events of this kind and none of them will alter the song until a note event appears. 

What do you need:

* [python-midi](https://github.com/vishnubob/python-midi)
* [Python](https://www.python.org/)

If you have errors installing python-midi check this [link](https://github.com/vishnubob/python-midi/issues/154).

### The Components

* **steganography.py** is a python script that receives a path to a midi file and a message and then write the message in the midi file using ProgramChangeEvent instances, it finds the first track on the midi pattern and then finds the ProgramChangeEvent instance for that track, then translates the message to its ascii representation and hides each character in ascii in the data section of the ProgramChangeEvent like this:

```python
ascii = translate_char_to_ascii(some_char)
track.append(midi.ProgramChangeEvent(tick=0, channel=1, data=[ascii]))
```

As can be seen each ProgramChangeEvent with a message char is appended to the track, finally the original ProgramChangeEvent is appended so the previous doesn't affect the song.

* **steganography_show.py** is a python script that receives a path to a midi file with a hidden message produced with the steganography.py script and let you read the message. This script searches on all the tracks and finds the one with more that one ProgramChangeEvent, more than one instance indicates a hidden message, s for n ProgramChangeEvent it takes the first n - 1 instances (the last instance is not part of the message as stated in the previous script explanation), extracts the data of each one and translates using ascii to a char representation, then join all chars and shows the original message.

### Execution

Once you installed python-midi you can execute each script on this way:

```bash
python3 steganography.py  /path/to/file.mid "Your message goes here"
```

The scripts creates a file named hidden_message.mid, to show the message you execute:

```bash
python3 steganography_show.py hidden_message.mid
```