import fileinput
import os
import sys

dependent_paths = ['src/ar_track_alvar/launch/webcam_track.launch',
                    'src/homography/launch/run_cam.launch']
proj_path =  os.path.dirname(os.path.realpath(__file__)) + '/'

print proj_path


for path in dependent_paths:
    for line in fileinput.input(path, inplace=1):
        if 'name="camera_info_url"' in line:
            print '<param name="camera_info_url" value="file:///' + proj_path + 'lifecam.yml" />'
        else:
            print line,



