from m4atowav import format_converter

# Folder Paths containing recording in m4a format
path = ["Jason/", "Ruchit/", "Rifa/", "Karina/"]
# convert to wav
for i in path:
    format_converter(i)