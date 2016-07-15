#!/usr/bin/env python
'''Quick script to convert vtt to srt.
   Usage: python tosrt.py filename
   Will write new filename.srt file in SRT format
'''

import re, sys, string

try:
  filename = sys.argv[1]
except:
  print "No filename specified. Exit"
  sys.exit(1)

if string.lower(filename[len(filename)-3:])=='vtt':
  outfile=filename[0:len(filename)-3]+"srt"
else:
  outfile=filename+'.srt'
print "Writing output to file: %s" % (outfile)

f = open(filename,'r')
out = open(outfile,'w')

count = 1
for line in f.readlines():
  if line[:6] == 'WEBVTT':
    continue
  # convert timestamp radix
  line = re.sub(r'(:\d+)\.(\d+)', r'\1,\2', line)
  if line == '\n':
    out.write('\n')
    out.write(str(count)+'\n')
    count += 1
  else:
    out.write(line.strip()+'\n')
