#incorporating cli with socket programming

__author__ = "a9393j"
import argparse
from argparse import RawTextHelpFormatter
from sock import MySocket

def parse_args():
	parser = argparse.ArgumentParser(description="read arbitary data from one socket"
		"and write it to another",formatter_class=RawTextHelpFormatter)
	parser.add_argument("-p",action="store",dest="port",required=True,
						type=int,help="port for listening the traffic(client)")
	parser.add_argument("-socket",action="store",dest="sock_type",
						help="type of socket (TCP/UDP):\n"
							"tcp\ttcp socket will be employed,\n"
							"udp\tudp socket will be employed.\n"
							"By default TCP will be imployed.\n")
	parser.add_argument("-inp",action="store",dest="inp_length",
						help="length of the input. Default set to 1024")
	return parser.parse_args()

def main():
	opts = parse_args()
	sockProg = MySocket(port=opts.port,
						sock_type=opts.sock_type,
						inp_length=opts.inp_length,
						count=opts.count)
	sockProg.start() # start the TCP/UDP server
	return
	
if __name__== "__main__":
	main()