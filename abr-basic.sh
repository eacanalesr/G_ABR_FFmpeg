#!/bin/bash
##
# Enable the ffmpeg filter to split, scale, create several outputs
# For this basic example, any filter is applied only to video. 

INPUT="<path where your video file is"
OUTPUT_DIR="path where the HLS chunks have been stored"

mkdir -p "$OUTPUT_DIR"

ffmpeg \
-i "$INPUT" \
-filter_complex "
[0:v]split=3[v1][v2][v3];
[v1]scale=1920:1080[v1080];
[v2]scale=1280:720[v720];
[v3]scale=854:480[v480]
" \
-map "[v1080]" \
-map "[v720]" \
-map "[v480]" \
-f hls \
-var_stream_map "v:0 v:1 v:2" \
-master_pl_name master.m3u8 \
"$OUTPUT_DIR/output_%v.m3u8"
