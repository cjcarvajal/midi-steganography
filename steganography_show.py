import sys
import midi

# Takes the data of the event_messages and translate them to
# ascii representation, removes the last character as it belongs
# to the original ProgramChangeEvent.
def message_to_ascii(event_messages):
	message =  [chr(event.data[0]) for event in event_messages]
	message = message[:-1]
	return ''.join(message)

# Searches for two consecutives events of type ProgramChangeEvent
# this means the song has a hidden message, then stores these 
# consecutive events in a list and returns it 
def get_hidden_message_events(song):
	pattern = midi.read_midifile(song)

	events_message_list = []

	for track in pattern:
		for event in track:
	 		if isinstance(event,midi.events.ProgramChangeEvent):
	 			events_message_list.append(event)
	 		else:
	 			if len(events_message_list) > 1:
	 				return events_message_list
	 			else:
	 				events_message_list = []

	return events_message_list

# Receives the song with the hidden message and extract the message
event_messages = get_hidden_message_events(sys.argv[1])
print message_to_ascii (event_messages)