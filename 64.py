'''Usage:
   64.py [--encode TEXT]
   64.py [--decode TEXT]
   64.py -h --help

Options:
   -e --encode     Encode text with Base64.
   -d --decode     Decode Base64 text.
'''

import docopt
import base64

def B64(args):
    text = bytes(args['TEXT'], 'utf-8')
    if(args['--encode'] == True):        
        output = base64.b64encode(text)
        output = bytes.decode(output, 'utf-8')
    if(args['--decode'] == True):
        output = base64.b64decode(text)
        output = bytes.decode(output, 'utf-8')            
    return output

if __name__ == "__main__":
    try:
        args = docopt.docopt(__doc__)
        data = B64(args)
        if(args['--encode'] == True):
            print('Encoded Text: \n', data)
        if(args['--decode'] == True):
            print('Decoded Text: \n', data)     
    except docopt.DocoptExit as e:
	    print(e.usage)