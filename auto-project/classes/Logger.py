import time
import sys

from colorama import init
init()

class Logger:

	def __init__(self):
		self.default = "logs.txt"

	def log(self, text, color="", file_name=""):

		colors = {
			'red': {
				'start': '\033[91m',
				'end': '\033[00m'
			},
			'green': {
				'start': '\033[92m',
				'end': '\033[00m'
			},
			'yellow': {
				'start': '\033[93m',
				'end': '\033[00m'
			},
			'cyan': {
				'start': '\033[96m',
				'end': '\033[00m'
			}
		}

		try:
			start = colors[color]['start']
			end = colors[color]['end']
		except KeyError:
			start = ""
			end = ""

		ts = time.strftime("%H:%M:%S")
		string = "[{}] {}{}{}\n".format(ts, start, text, end)
		
		sys.stdout.write(string)
		sys.stdout.flush()

		if file_name:
			if file_name == self.default:
				with open(self.default, "a") as f:
					f.write("[{}] {}\n".format(ts, text))
			else:
				with open(file_name, "a") as f:
					f.write("[{}] {}\n".format(ts, text))
