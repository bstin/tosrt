# tosrt
Simple Python Script to Convert Subtitles from VTT format to SRT.

This file would be helpful if you are backing up or transcoding video files and you have subtitles in WebVTT format and want to convert them to SRT format. For instance, Plex may work better with .mkv files with embedded SRT files - therefore this script can be helpful to get the subtitles into that format. 

Specifically, the script accomplishes two main things:

* Converts time to radix format
* Inserts Caption block numbers (autoincremented) 

# Usage:
    python tosrt.py [filename]

Where `filename` is subtitle file in VTT format

Output will be written to name `filename.srt`
