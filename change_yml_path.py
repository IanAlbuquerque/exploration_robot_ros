import fileinput
import os

proj_path =  os.path.dirname(os.path.realpath(__file__))

for launch_path in fileinput.input('txts/yml_dependencies_path.txt', inplace=1):
    file_being_edited = fileinput.input(launch_path, inplace=1)
    print file_being_edited.filename()