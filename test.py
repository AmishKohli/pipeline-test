import re

secretdataviaparam = '{"ID": "115","NAME": "Demo115","TypeData": "PlainTxt\","TypeSecret": "StandaloBoth"}'

if re.search(r'\\', secretdataviaparam):
    print("\\ is found")
else:
    print("\\ is not found")