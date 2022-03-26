# this is an easier way to read HTML than socket_communication with the urllib library
import urllib.request
import urllib.error

f_hand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in f_hand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)


