# chat_client.py
# -*- coding: utf-8 -*-

import sys
sys.path.append("lib")

# from ProcessSupport import *
from ClientSupport import *
import socket
import select
import os
import time


class clientChat:
    def __init__(self):
        print """


	\nChào mừng đến với chat online X


	"""

    def chat_client(self):
        if(len(sys.argv) < 2):
            print Colors.BOLD + Colors.FAIL + \
                'Cú pháp : python client.py <SERVER IP>' + Colors.ENDC + "\n\n"
            sys.exit()

        host = sys.argv[1]
        command = ''
        s = connect_to_server()
        try:
            if s:
                if try_to_server(s, host):
                    print Colors.BOLD + Colors.OKBLUE + \
                        'Kết nối đến máy chủ thành công, Bây giờ bạn có thể chém gió ' + Colors.ENDC
                    print Colors.BOLD + Colors.FAIL + '#exit: Thoát \n\n' + Colors.ENDC

                    try:
                        user_valid, user_name = make_new_user()
                        if user_valid is False:
                            print 'Invalid username'
                            sys.exit()
                    except KeyboardInterrupt:
                        s.send("#exit")
                        print "\nĐóng chat!!!"
                        sys.exit()

                    usr_info = "#user: %s" % user_name
                    s.send(usr_info)
                    sys.stdout.write('>')
                    sys.stdout.flush()

                    while True:
                        # recv data from keyboard
                        socket_list = [sys.stdin, s]

                        # get the list sockets which are readable
                        ready_to_read, ready_to_write, in_error = select.select(
                            socket_list, [], [])

                        for sock in ready_to_read:
                            stream_data(sock, s)
                else:
                    os.system('clear')
                    print "\nKhông thể kết nối đến Server\n"

        except KeyboardInterrupt:
            s.send("#exit")
            print "\nĐóng chat!!!"


if __name__ == "__main__":
    chat = clientChat()
    sys.exit(chat.chat_client())
