from DetectedObject import *
import re


def ReadData(logname):

    with open(logname, "r", encoding="UTF8") as fp:
        logs = fp.readlines()

    numlines = 0
    scene_count = 0

    #'2(RSU-08)' DETECTION - 2017-04-04 11:13:00
    date_pattern = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3}")
    #[2017 - 04 - 04 11:13:00.036] meta.Radar2.Clients.Radar2Dispatcher - DEBUG > Move
    #ID: 7, Size: 3, Distance: 496, Angle: -2346, SNR: 0, Speed: -85

    obj_pattern = re.compile("Size: ([0-9]*), Distance: ([0-9]*), Angle: (-?[0-9]*), "
                   r"SNR: ([0-9]*), Speed: (-?[0-9]*)")

    bundle_scene = []
    single_scene = []
    szDate = ""
    for line in logs[1:]:
        m = obj_pattern.search(line)
        if m is not None:
            numlines += 1
            pdate = date_pattern.search(line)

            size = int(m.group(1))
            distance = int(m.group(2))
            angle = int(m.group(3))
            snr = int(m.group(4))
            speed = int(m.group(5))

            dobj = DetectedObject(distance, angle, speed, size, snr)
            dobj.date = pdate.group(0)
            single_scene.append(dobj)
        else:
            dt = date_pattern.search(line)
            if dt is not None:
                szDate = dt.group(0)
            bundle_scene.append(single_scene[:])
            single_scene.clear()
            scene_count += 1

    return bundle_scene
