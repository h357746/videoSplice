#jkeditor.py
#coding:utf-8
#需要有ffmepg
import sys
import os
import re
import shutil
import subprocess
from datetime import datetime, timedelta

TIME_FROMAT = '%H:%M:%S'


def do_cut(file_input, file_output, s1_time, s2_time):
    start_time = s1_time.strftime(TIME_FROMAT)
    end_time = s2_time.strftime(TIME_FROMAT)
    cmd = 'ffmpeg -i ' + file_input + ' -ss ' + start_time + ' -to ' + end_time + '  -c:v copy -c:a copy ' + file_output
    print("cmd=", cmd)
    subprocess.call(cmd, shell=True)


def do_edit():
    file_input = sys.argv[1]
    output_dir = sys.argv[2]
    start_time = sys.argv[3]
    end_time = sys.argv[4]
    slice_duration = int(sys.argv[5])
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.mkdir(output_dir)
    (filepath, tempfilename) = os.path.split(file_input)
    (filename, extension) = os.path.splitext(tempfilename)

    s_time = datetime.strptime(start_time, TIME_FROMAT)
    e_time = datetime.strptime(end_time, TIME_FROMAT)
    n_slice = (int)((e_time - s_time).total_seconds() / slice_duration)
    print("n_slice=", n_slice)

    s1_time = s_time
    for i in range(0, n_slice):
        s2_time = s1_time + timedelta(seconds=slice_duration)
        file_output = output_dir + '/' + filename + str(i) + extension
        do_cut(file_input, file_output, s1_time, s2_time)
        s1_time = s2_time


def usage():
    print("usage:", sys.argv[0],
          "<input> <output_dir> <start_time> <end_time> <slice_duration>")
    # exit(0)


if __name__ == "__main__":
    if len(sys.argv) != 6:
        usage()
    else:
        do_edit()