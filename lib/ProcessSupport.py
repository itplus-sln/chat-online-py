# process class
# -*- coding: utf-8 -*-

import time
import socket
import urllib
from sys import platform as _platform

# check valid username
def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def get_current_date_time(mode):
    try:
        if mode == 't':
            return time.strftime("%H:%M")
        elif mode == 'd':
            return time.strftime("%d-%m-%Y")
    except BaseException as e:
        print "Error", e
        return None

def get_public_ip():
    try:
        ip = urllib.urlopen('http://icanhazip.com/').read().strip('\n')
    except BaseException as e:
        print "Error", e
        try:
            ipraw = urllib.urlopen(
                'http://whatismyip.org').read().split("</span>")[1]
            ip2 = ipraw.split(">")[-1]
        except BaseException as e:
            print "Error", e
            return None
        else:
            return ip2
    else:
        return ip
    return None

def get_local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except BaseException as e:
        print "Error", e
        return None

def get_OS():
    if _platform == "linux" or _platform == "linux2":     # linux
        pass
    elif _platform == "darwin":                           # MAC OS X
        pass
    elif _platform == "win32" or _platform == "win64":    # Windows
        pass

def draw_line():
    print """

    > Sẵn sàng kết nối


    """
    print "-" * 50

def msg_server_online():
    status = 'Đang lấy IP...'
    message_wait = '%s[ %s ] - %s %s\n' % (Colors.INFO, get_current_date_time('t'), status, Colors.ENDC)

    print message_wait

    public_IP = get_public_ip()
    local_IP  = get_local_ip()

    status = "Offline!!!"
    if(public_IP is not None):
        status = "Online"
    else:
        public_IP = ""

    if(local_IP is None):
        local_IP = ""

    message_content = '%s[ %s ] - Server %s %s\n' % (Colors.INFO, get_current_date_time('t'), status, Colors.ENDC)
    message_content2 = 'Public IP: %s\nLocal IP: %s\n' % (public_IP, local_IP)

    print message_content
    print message_content2

# msg bind server
def msg_bind_server(port):
    status = "Khởi Tạo Server | CỔNG: %s" % port
    message_content = '%s[ %s ] - %s %s\n' % (Colors.INFO, get_current_date_time('t'), status, Colors.ENDC)

    print message_content

# msg server busy
def msg_server_busy(port):
    status = "SERVER ĐANG BẬN, THỬ CỔNG: %s" % port
    message_content = '%s[ %s ] - %s %s\n' % (Colors.INFO, get_current_date_time('t'), status, Colors.ENDC)

    print message_content

# msg server error
def msg_server_error(port):
    status = "KHÔNG THỂ TẠO SERVER: %s" % port
    message_content = '%s[ %s ] - %s %s\n' % (Colors.FAIL2, get_current_date_time('t'), status, Colors.ENDC)

    print message_content

# msg server information
def msg_server_status(mode):
    if (mode == 'on'):
        status = "Server Đã mở"
        color  = Colors.INFO
    elif (mode == 'off'):
        status = "Server Đã Off"
        color  = Colors.FAIL2

    message_content = '%s[ %s ] - %s %s\n' % (color, get_current_date_time('t'), status, Colors.ENDC)
    print message_content

def show(message_content):
    print message_content

def remove_user_from_chat(user_name, sock):
    list_user = user_name
    user = list_user[sock.getpeername()]
    for key, value in list_user.items():
        if value == user:
            list_user.pop(key)

    return list_user

# number of users
def msg_count_user_online(user_name):
    list_user = []
    Count = 0
    for key, value in user_name.items():
        Count += 1
        list_user.append(value)

    list_user = ",".join(list_user)

    message_content = Colors.BOLD + Colors.OKBLUE + "[ " + get_current_date_time(
        't') + " ]" + Colors.ENDC + Colors.OKGREEN + "- users đang online: " + str(Count) + "\n\t\t" + list_user + Colors.ENDC + "\n"
    return message_content

def msg_count_new_user(sock, new_user, Server):
    message_content = []
    msg_show = Colors.BOLD + Colors.OKBLUE + "[ " + get_current_date_time(
        't') + " ]" + Colors.ENDC + "-[ New Socket ] " + str(sock.getpeername()) + "\n"
    message = Colors.BOLD + Colors.OKBLUE + "[ " + get_current_date_time('t') + " ]" + Colors.ENDC + Colors.OKGREEN + "- [ SERVER " + \
        Server + " ]*****Chào mừng user: " + Colors.Cyan + new_user + Colors.OKGREEN + " đã vào phòng chat" + Colors.ENDC + "\n"
    message_content.append(msg_show + message)
    message_content.append(message)

    return message_content

def msg_user_is_exist(sock, new_user):
    message_content = []
    message = "[ " + get_current_date_time(
        't') + " ]- #Tên : " + new_user + " đã tồn tại, vui lòng nhập tên khác"
    message_content.append(str(sock.getpeername()) + message)
    message_content.append(message)

    return message_content

def msg_user_logout(user_name, sock):
    message_content = []
    message = Colors.BOLD + Colors.OKBLUE + "[ " + get_current_date_time(
        't') + " ]" + Colors.ENDC + Colors.FAIL + "- ***** Thành viên: " + Colors.Cyan + user_name[sock.getpeername()] + Colors.FAIL + " Đã thoát!!!" + Colors.ENDC + "\n"
    message_content.append(user_name[sock.getpeername()] + message)
    message_content.append(message)

    return message_content

def msg_handle_user(user_name, sock, recv_data):
    message_content = Colors.BOLD + Colors.OKBLUE + "[ " + get_current_date_time(
        't') + " ]" + Colors.ENDC + Colors.Cyan + "- " + user_name[sock.getpeername()] + " - " + Colors.White + recv_data.strip() + Colors.ENDC.replace("\r\n", "")

    return message_content


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    Purple = '\033[0;35m'       # Purple
    Cyan = '\033[0;36m'         # Cyan
    White = '\033[0;97m'        # White
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    INFO = '%s%s' % (BOLD, WARNING)
    FAIL2 = '%s%s' % (BOLD, FAIL)


class Msg:
    INTRO = """
      Đường phố thinh lặng,
      Chỉ còn cơn gió thoáng đưa một chút sương lạnh
      Làm buốt vai anh, chợt thấy đêm dài,
      Vì lòng thao thức muốn nghe từng phút cô đơn
      Khẽ trôi bềnh bồng.

      Và nghe em như kề bên
      Vòng tay thơ ấm êm
      Nói cười với anh
      Và nghe sâu trong lòng anh
      Yêu thương gọi tên em giữa khuya.

      Tình yêu đốt cháy tim này, trong một phút mong chờ
      Lạc trong đêm bên nỗi nhớ, lạnh đôi vai se buốt giá
      Ngoài kia phố vắng hiu quạnh, nơi tận cuối con đường
      Một người ngu ngơ bước đi, tìm quanh đâu đây bóng em
      """
