import sys, getopt, json

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
   return secret

if __name__ == "__main__":
   secretdataviaparam = main(sys.argv[1:])
   print("returned: " + secretdataviaparam)
   index = secretdataviaparam.find("\\")
   if index != -1:
      print("\\ is found")
      print(secretdataviaparam[index + 1])
      if secretdataviaparam[index + 1] != "\\":
         print("modification required in file")


   

   secretfile = "secret.json"
   #encodedUnicode = json.dumps(unicodeData, ensure_ascii=False).encode('utf-8')
   secretfileobj = open(secretfile)
   f = open(secretfile,)
   print(f.readline())
   encodedUnicode = json.dumps(secretdataviaparam, ensure_ascii=True).encode('utf-8')
   print (encodedUnicode)
   data = json.loads(encodedUnicode)
   print(type(data))
   #print(data['TypeSecret'])
   f.close()




