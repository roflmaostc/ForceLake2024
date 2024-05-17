
import subprocess

def find_index(application="Spotify"):
    
    out = str(subprocess.check_output(["pacmd list-sink-inputs"], shell=True))
    indices = []
    for line in out.split("\\n"):
        line = line.strip()
        

        if line.startswith("index"):
            index = line.split()[-1] 
       
        if application in line:
            indices.append(index)

    return indices 

print(find_index("\"Chromium\""))
