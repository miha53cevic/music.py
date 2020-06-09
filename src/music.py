# contains argv which is a list so we know the length
import sys
# argument parsing
import argparse
# glob used for recursive searching
import glob
import random

# remove pygame welcome message
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1';
# import music player
import pygame as pg

# import metadata reading library
from mutagen.mp3 import MP3
############################################################################

class AudioPlayer:
	def __init__(self):
		self.volume = 1.0;
		self.loop = False;
		self.repeat = False;

	def setVolume(self, volume):
		self.volume = float(volume);

	def setLoop(self, loop):
		self.loop = bool(loop);

	def setRepeat(self, repeat):
		self.repeat = bool(repeat);

	def loadRandomAudio(self, file: str, ext: str):
		# get a list of tracks
		track_list = glob.glob(file + f"/**/*.{ext}", recursive=True);

		# check if no songs where found
		if (len(track_list) == 0):
			print(f"\n>>> Couldn't find any files in directory {file} with the extension .{ext}");
			return;

		# used if using the repeat option with --random
		self.repeatPath = file;
		self.repeatExt = ext;

		# otherwise get a random track and play it
		rand = random.randint(0, len(track_list) - 1);

		self.loadAudio(track_list[rand]);

	def loadAudio(self, file: str):

		if os.path.exists(file):
			# initialize the music player
			pg.mixer.init();
			pg.mixer_music.load(file);
			pg.mixer_music.set_volume(self.volume);
			pg.mixer_music.play();

			total_seconds = int(MP3(file).info.length);
			total_minutes = int(total_seconds / 60);
			total_seconds %= 60;

			# add 0 to times, example: 01:09
			ClockFormat = lambda time: f"0{time}" if time < 10 else time;
			
			total_seconds = ClockFormat(total_seconds);
			total_minutes = ClockFormat(total_minutes);

			# print info
			print(f"\nPlaying... {file} at volume: {self.volume}");
			print("-" * (len(file) + 28));

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

			# loop song or repeat the random search querry
			if (self.loop == True):
				self.loadAudio(file);
			elif (self.repeat == True):
				self.loadRandomAudio(self.repeatPath, self.repeatExt);

			print("\n\n>>> Song end! <<<");

		else:
			print(">>> Can not open audio file! <<<");



# if module is used as main
if __name__ == "__main__":

	try:
		parser = argparse.ArgumentParser();
		parser.add_argument("audiofile", help="audiofile or folder[when using --random] location");
		parser.add_argument("--volume", "-v", help="set volume 0.0 - 1.0");
		parser.add_argument("--loop", "-l", help="loop the song", action="store_true");
		# action="store_true" means that when not specifying it, it returns false otherwise it returns true
		parser.add_argument("--random", "-r", help="play random song in a given folder (search is recursive /**)", action="store_true");
		parser.add_argument("--extension", "-ext", help="Example: -ext mp3, used for --random");
		parser.add_argument("--repeat", "-rp", help="Used with --random, continues to play random songs", action="store_true");

		if len(sys.argv) > 1:
			# parse arguments
			args = parser.parse_args();

			# initialize AudioPlayer
			player = AudioPlayer();
			player.setVolume(args.volume or 1.0);

			if (args.random == True):
				# if args.extension is None it sends "mp3"
				player.setLoop(args.loop or False);
				player.setRepeat(args.repeat or False);
				player.loadRandomAudio(args.audiofile, args.extension or "mp3");
			else:
				player.setLoop(args.loop or False);
				player.loadAudio(args.audiofile);
		else:
			print(">>> No audiofile given! <<<");
			print(parser.print_help());

	except KeyboardInterrupt:
		print("\n>>> CTRL-C called, exiting... <<<");
		pass;