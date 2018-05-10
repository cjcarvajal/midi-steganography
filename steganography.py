import sys
import midi

# Transforms a string into its ascii representation
# putting all numbers into a list
def message_to_ascii(message):
	return [ord(c) for c in message]

# Takes the first ProgramChangeEvent instance on the first track of the pattern
# then insert the ascci characters as the data of ProgramChangeEvents one event
# per each character, then insert the original event on the track.
# As the ProgramChangeEvent are not notes event they doesn't affect the song.
def hide_message(song,message):
	ascii_chars = message_to_ascii(message)
	pattern = midi.read_midifile(song)

	for track in pattern:
		for event in track:
	 		if isinstance(event,midi.events.ProgramChangeEvent):
				actual_change = event
				
				for ascii in ascii_chars:
					track.append(midi.ProgramChangeEvent(tick=0, channel=1, data=[ascii]))
				track.append(actual_change)
				midi.write_midifile("hidden_message.mid", pattern)
				return

# The first parameter should be the path to the song and the second is the 
# message to hide
hide_message(sys.argv[1],sys.argv[2])