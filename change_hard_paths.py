import fileinput
import os
import sys

# AR_TAG_SIZE_ = str(8) #ar tags for the zumys
AR_TAG_SIZE_ = str(5.5) #test ar tag size

yml_dependent_paths = ['src/ar_track_alvar/launch/webcam_track.launch',
                    'src/homography/launch/run_cam.launch']

proj_path =  os.path.dirname(os.path.realpath(__file__)) + '/'

print proj_path
print "ar tag size: " + AR_TAG_SIZE_


for path in yml_dependent_paths:
    for line in fileinput.input(path, inplace=1):
        if 'name="camera_info_url"' in line:
            print '    <param name="camera_info_url" value="file:///' + proj_path + 'lifecam.yml" />'
        else:
            print line,

for line in fileinput.input('scripts/set_env.sh', inplace=1):
    if 'setup.bash' in line:
        print "source " + proj_path + "devel/setup.bash"
    else:
        print line,

for line in fileinput.input('src/ar_track_alvar/launch/webcam_track.launch', inplace=1):
    if 'name="marker_size"' in line:
        print '  <arg name="marker_size" default="' + AR_TAG_SIZE_ + '" />'
    else:
        print line,



