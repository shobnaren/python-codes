import pexpect as pe
from pprint import pprint

import logging

#logging.basicConfig(filename='app.log', filemode='w',
#                    format='%(name)s - %(levelname)s - %(message)s')
c_handler = logging.StreamHandler()

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(c_handler)
# https://realpython.com/python-logging/
login_cmd = "su tester"
passwd = "test@123"
def ls_command():
    try:
        session = pe.spawn(login_cmd)
        j = session.expect([r"[P|p]assword:", "something"], timeout=5)
        if j == 0:
            log.debug(" {} \n....\n {}".format(session.before, session.after))
            log.info("Sending password")
            session.sendline(passwd)
        else:
            print("something else came up {}".format(session.before))
            raise Exception("Authentication did NOT happen")
        j = session.expect([r"\$|#"], timeout=5)
        if j == 0:
            log.debug("try to execute the ls command")
            session.sendline('whoami')
            # log.critical(session.after)
        else:
            raise Exception("did NOT get prompt")
        j = session.expect([r"\$ $"], timeout=20)
        if j == 0:
            log.debug("Try to get back the prompt")
            out = session.before
            out = out.decode('utf-8')
            log.info("BEFORE: {}".format(out))
            log.error("AFTER: {}".format(session.after))
        else:
            out = ""
            raise Exception("Nothing to parse")
        # log.debug(out)
    except pe.ExceptionPexpect as p:
        log.debug("error:")
        log.debug(repr(p))
        log.debug(session.read())
    finally:
        session.close()


if __name__ == '__main__':
    ls_command()
