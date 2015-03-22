import msgpack
import random

packFile = open("../input.txt", "wb")

num_of_seq = 5
print "Number of sequence: %d" % num_of_seq
msgpack.pack(num_of_seq, packFile)

for i in range(num_of_seq):
	seq_length = random.randint(1, 10)
	seq = [random.randrange(1000000) for x in range(seq_length)]

	print "Sequence %d (length=%d):" % (i, seq_length)
	print "\t", seq
	msgpack.pack(seq, packFile)

packFile.close()
