import sys, getopt

def main(argv):
   choice = ''
   text = ''
   secret = ''
   opts, args = getopt.getopt(argv,"hc:t:s:",["cp=","tp=","sp="])
   for opt, arg in opts:
      if opt == '-h':
         print ('readparam.py -c <choiceparam> -t <textparam> -s <secretparam>')
         sys.exit()
      elif opt in ("-c", "--cp"):
         choice = arg
      elif opt in ("-t", "--tp"):
         text = arg
      elif opt in ("-s", "--sp"):
         secret = arg
   print ('Input param is ', choice)
   print ('Output param is ', text)
   print ('Output param is ', secret)

if __name__ == "__main__":
   main(sys.argv[1:])
