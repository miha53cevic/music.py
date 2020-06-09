import sys
import argparse

# remove pygame welcome message
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1';

# import music player
import pygame as pg

# import metadata reading library
from mutagen.mp3 import MP3
############################################################################

def ClockFormat(time):
	if (time < 10):
		return f"0{time}";
	else: 
		return time;

def loadAudio(file, volume=1.0):

	if os.path.exists(file):
		# initialize the music player
		pg.mixer.init();
		pg.mixer_music.load(file);
		pg.mixer_music.set_volume(volume);
		pg.mixer_music.play();

		total_seconds = int(MP3(file).info.length);
		total_minutes = int(total_seconds / 60);
		total_seconds %= 60;

		total_seconds = ClockFormat(total_seconds);
		total_minutes = ClockFormat(total_minutes);

		print(f"\nPlaying... {file} at volume: {volume}");

		# play the file
		while pg.mixer_music.get_busy():
			miliseconds = pg.mixer_music.get_pos();
			seconds = int(miliseconds / 1000) % 60;
			minutes = int((miliseconds / 1000) / 60);

			seconds = ClockFormat(seconds);
			minutes = ClockFormat(minutes);

			# \r escape sequences goes back to the begining of the line 
			# that is why we use \n\r 
			# end="" makes sure it doesn't end with a new line
			print(f"\r>> Time: {minutes}:{seconds} - {total_minutes}:{total_seconds}", end="");

		print("\n\n>>> Song end! <<<");

	else:
		print(">>> Can not open audio file! <<<");

# if module is used as main
if __name__ == "__main__":

	try:
		parser = argparse.ArgumentParser();
		parser.add_argument("audiofile", help=".wav or .mp3");
		parser.add_argument("--volume", "-v", help="set volume 0.0 - 1.0");

		if len(sys.argv) > 1:
			# parse arguments
			args = parser.parse_args();
			
			if (args.audiofile is not None):
				if (args.volume is not None):
					loadAudio(args.audiofile, float(args.volume));
				else:
					loadAudio(args.audiofile);
			else:
				print(">>> No audiofile given! <<<");
		else:
			print(">>> No arguments given! <<<");
			print(parser.print_help());

	except KeyboardInterrupt:
		print("\n>>> CTRL-C called, exiting... <<<");
		pass;