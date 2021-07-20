from pydub import AudioSegment
import os
import sys
import subprocess
from pathlib import Path

import os
print(os.getcwd())

x = Path('./')
print('path current')
print(list(filter(lambda y:y.is_file(), x.iterdir())))

sys.path.append('/Users/kaushik/codebase/webmtomp3/ffmpeg')

directory = "/Users/kaushik/Downloads/Kau Songs"
target_dir = "/Users/kaushik/Downloads/Kau Songs Mp3"
for filename in os.listdir(directory):
    if filename.endswith(".webm"):
    	in_file_path = f"{directory}/{filename}"
    	print(in_file_path)
    	filename = filename.rsplit('.')[0] + '.mp3'
    	target_path = f"{target_dir}/{filename}"    	
    	subprocess.run([f'"/Users/kaushik/codebase/webmtomp3/ffmpeg" -i "{in_file_path}" -vn "./{filename}"'])


