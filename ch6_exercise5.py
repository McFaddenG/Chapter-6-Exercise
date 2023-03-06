line = 'X-DSPAM-Confidence: 0.8475'

start = line.find(':')
ns = line[start+1:].strip()
n = float(ns)

print(n)