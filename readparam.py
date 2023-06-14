import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-c", "--ifile"):
         choice = arg
      elif opt in ("-t", "--ofile"):
         text = arg
      elif opt in ("-s", "--ofile"):
         secret = arg
   print ('Input file is ', choice)
   print ('Output file is ', text)
   print ('Output file is ', secret)

if __name__ == "__main__":
   main(sys.argv[1:])
