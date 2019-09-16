import pexpect

from pprint import pprint


def default_gateway_find():
    try:
        session = pexpect.spawn("su tester")
        i=session.expect([r"P|password: "], timeout=5)
        if i == 0:
            session.sendline("test@123")
            j = session.expect([r"\$"],timeout=5)
            if j == 0:
                session.sendline("netstat | grep tcp")
                j = session.expect(["\$"], timeout=5)
                if j==0:
                    x=session.before
                    print(x.decode('utf-8'))

            else:
                print("Command didn't executed")
        else:
            print("Access denied")

    except pexpect.ExceptionPexpect as p:
        print(p)
        print(session.read())
    finally:
        session.close()

if __name__ == '__main__':
    default_gateway_find()


