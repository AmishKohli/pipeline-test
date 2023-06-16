import sys
import getopt
import json
import re

def main(argv):
    choice = ''
    text = ''
    secret = ''
    opts, args = getopt.getopt(argv,"hc:t:s:",["cp=","tp=","sp="])

    for opt, arg in opts:
        if opt == '-h':
            print('readparam.py -c <choiceparam> -t <textparam> -s <secretparam>')
            sys.exit()
        elif opt in ("-c", "--cp"):
            choice = arg
        elif opt in ("-t", "--tp"):
            text = arg
        elif opt in ("-s", "--sp"):
            secret = arg
    

if __name__ == "__main__":
    secretdataviaparam = main(sys.argv[1:])

    print("returned:", secretdataviaparam)

    secretfile = "secret.json"
    secretfileobj = open(secretfile)
    f = open(secretfile)
    if re.search(r'\\', f.readline()):
        print("\\ is found")
        print("\\ is found - Warning: Modification may be required in the file.")
        sys.exit()
    print("new",f.readline())
    print('secretData',secretdataviaparam)
    encodedUnicode = json.dumps(secretdataviaparam, ensure_ascii=True).encode('utf-8')
    print(encodedUnicode)
    data = json.loads(encodedUnicode)
    print("encoded", type(data))
    f.close()
    
