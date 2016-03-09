#!/bin/bash
rm -rf live*
killall python
python -m SimpleHTTPServer &

sleep 3

ffmpeg -v verbose -f video4linux2 -vcodec mjpeg -s 320x240 -r 15 -i /dev/video0 -vcodec libx264 -profile:v baseline -maxrate 400k -bufsize 1835k -pix_fmt yuv420p -flags -global_header -hls_time 5 -hls_list_size 5 -start_number 1 ./live.m3u8
