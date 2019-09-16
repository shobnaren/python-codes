import pexpect
from pprint import pformat
import pdb

def nslukup(list_of_url):
    session = pexpect.spawn('nslookup')
    try:
        i = session.expect(['>'],timeout=5)
        if i == 0 :
            print('hurray.. landed in nslookup prompt')
            pdb.set_trace()
            for each in list_of_url:
                session.sendline(each)
                j = session.expect(['>'], timeout=5)
                if j == 0:
                     x = session.before
                     addr = [a.decode('utf-8') for a in x.splitlines() if 'ddress' in a.decode('utf-8')]
                     print('filter out the addresses \n{}'.format(pformat(addr)))
                else:
                    print('something wrong')
            # at the end give exit..
            session.sendline('exit')
            return True
        else:
            print('something seriously wrong')
    except pexpect.EOF:
        print ("EOF")
    except pexpect.TIMEOUT:
        print ("TIMEOUT")
    else:
        r = session.read()
        print (r)
    session.close()

if __name__ == "__main__":
    nslukup(['google.com','amazon.com', 'jibberish'])
