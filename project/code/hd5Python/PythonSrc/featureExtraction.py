import hdf5_getters as h5get

practice = "/Users/multivax/Documents/PhD/2.spring.17/Classifications-Of-Songs-via-Homology-of-Chroma-Features/project/code/MillionSongSubset/data/B/B/B/TRBBBEA128F93391BA.h5"
h5 = h5get.open_h5_file_read(practice)
duration = h5get.get_duration(h5)
sampleRate = h5get.get_analysis_sample_rate(h5)
artist = h5get.get_artist_name(h5)
title = h5get.get_title(h5)
h5.close()
print(duration)
print(sampleRate)
print(artist)
print(title)
