# importing modules
from pydub import AudioSegment
from mutagen.mp3 import MP3
import math
import re

# where the input is, where the output will be created, how long should each new file be
input_path = input("wher is the file (include file name an extension, escape backslashes)\n")
output_path = input("where should the new file go (new named infered, escape backslashes) \n")
chunks_second = int(input("How long should each new file be (in seconds) \n"))

# extracting the name of the file
slashes = re.findall(r"[^\\]*$", input_path)[0]
output_name = re.split("\\.", slashes)[0]

# creating the path for file creation
output_base = output_path + "\\" + output_name 

# reading the input as a mp3 and extracting its length
mp3_file = MP3(input_path)
length_seconds = math.floor(mp3_file.info.length)

# creating the cutoff points. "chunck_second" is the length of each output file in seconds
time_steps = range(0, length_seconds, chunks_second)
cutoffs = []
for i in time_steps:
    cutoffs.append(i)

# creating a vector of numbers for naming the output
name_steps = range(0, 100, 1)
names = []
for i in name_steps:
    names.append(i)


# generating the final output
for cutoff, name in zip(cutoffs, names):
    segment = AudioSegment.from_file(input_path, 
    format = "mp3", start_second= cutoff, duration=chunks_second)
    with open(f"{output_base}-{name}.mp3", "wb") as f:
        segment.export(f, format = "mp3")
