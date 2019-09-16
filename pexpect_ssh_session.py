from pexpect import pxssh
import getpass

from pprint import pprint


def default_gateway_find(hostname, user, password):
    try:
        session = pxssh.pxssh()
        #session.set_unique_prompt("$")

        session.login(hostname, user, password, original_prompt=r"\$",auto_prompt_reset=False)
        print(session.UNIQUE_PROMPT)
        ret = session.prompt(timeout=1)
        print("returning {}".format(ret))
        session.sendline("netstat | grep tcp")
        session.prompt(timeout=1)
        out = session.before
        print(out.decode('utf-8'))
        print("next command")
        session.sendline("pwd")
        session.prompt(timeout=1)
        out = session.before
        print(out.decode('utf-8'))
    except pxssh.ExceptionPxssh as p:
        print(p)

    finally:
        session.logout()


if __name__ == '__main__':
    hostname = 'localhost'
    user = 'tester'
    password = getpass.getpass('password: ')
    #password = 'test@123'
    default_gateway_find(hostname, user, password)


