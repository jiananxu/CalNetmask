# !/usr/bin/python
# coding:utf-8


import re
import uuid
from socket import inet_aton
from struct import unpack
import socket
from IPy import IP


def _check_ip(ip_add):
    """
    检查ip合法性
    """
    p = re.compile(r'^(([01]?[\d]{1,2})|(2[0-4][\d])|(25[0-5]))' \
                   r'(\.(([01]?[\d]{1,2})|(2[0-4][\d])|(25[0-5]))){3}(\/(\d+))?$')

    return p.search(str(ip_add)) is not None

# print _check_ip('192.168.1.1')
def isValidMask(mask):
    """
    检查子网掩码合法性
    :param mask:
    :return:
    """
    try:
        if _check_ip(mask):
            mask_num, = unpack("!I", inet_aton(mask))
            if mask_num == 0:
                return False

            # get inverted
            mask_num = ~mask_num + 1
            binstr = bin(mask_num)[3:]
            # convert to positive integer
            binstr = '0b%s' % ''.join('1' if b == '0' else '0' for b in binstr)
            mask_num = int(binstr, 2) + 1
            # check 2^n
            return (mask_num & (mask_num - 1) == 0)
        return False
    except Exception:
        return False


#
# def netmask_check(netmask):
#     IPy._checkNetmask(netmask)

def subnet_ip(ip, mask_bit):
    '''
    返回子网ip地址     '192.168.1.1','3'-------> 192.0.0.0/3
    :param ip: ip地址
    :param mask_bit:　掩码位
    :return: IP
    '''
    try:
        if _check_ip(ip) and 0 <= int(mask_bit) <= 32:
            ips = ip + '/' + mask_bit
            ip_class = IP(ips, make_net=True)
            # print (ip_class)
            return ip_class
        else:
            return False
    except Exception:
        return False

# print subnet_ip('192.168.1.1',2)
# ??????传入的参数必须是str类型，否则会报错BaseException

def networkAddr(ip, mask_bit):
    # ip_list = ip.split('.')
    # net_list = netmask.split(".")
    # count = 0
    # newlist = []
    # netaddr = [int(m) & int(n) for m in ip_list for n in net_list]
    # for n in netaddr:
    #     if 0 == count % 5:
    #         newlist.append(n)
    #     count += 1
    # return str(newlist)
    '''
    计算网络地址     '192.168.1.1','3'------->192.0.0.0
    :param ip:
    :param mask_bit:
    :return:
    '''
    try:
        if _check_ip(ip) and 0 <= int(mask_bit) <= 32:
            return subnet_ip(ip, mask_bit).net()
        else:
            return 'ip地址错误'
    except Exception:
        return Exception.message


def host_num(mask_bit):
    '''
    计算可用主机数
    :param mask_bit:
    :return: host number
    '''
    try:
        if 0 <= int(mask_bit) <= 32:
            count = 32 - int(mask_bit)
            num = 2 ** count - 2
            return num
        else:
            return 'False'
    except Exception:
        return False


def netmask(ip, mask_bit):
    try:

        return subnet_ip(ip, mask_bit).netmask()
    except Exception:
        return False


# print netmask('192.168.1.1','23')


def broadcast(ip, mask_bit):
    try:
        return subnet_ip(ip, mask_bit).broadcast()
    except Exception:
        return False


def firstAvailAddr(ip, mask_bit):
    try:
        return subnet_ip(ip, mask_bit)[2]
    except Exception:
        return False


def lastAvailAddr(ip, mask_bit):
    try:
        return subnet_ip(ip, mask_bit)[-2]
    except Exception:
        return False


def net_list(ip, mask_bit):
    netaddr_list = []
    try:
        l = subnet_ip(ip, mask_bit)
        for i in l:
            netaddr_list.append(str(i))
        return netaddr_list
    except Exception:
        return 'False'


        # for i in net_list('192.168.1.1','3'):
        # print i


def netbit_to_netmask(netbit):
    dictionary = {'0': '0.0.0.0',
                  '1': '128.0.0.0',
                  '2': '192.0.0.0',
                  '3': '224.0.0.0',
                  '4': '240.0.0.0',
                  '5': '248.0.0.0',
                  '6': '252.0.0.0',
                  '7': '254.0.0.0',
                  '8': '255.0.0.0',  # A
                  '9': '255.128.0.0',
                  '10': '255.192.0.0',
                  '11': '255.224.0.0',
                  '12': '255.240.0.0',
                  '13': '255.248.0.0',
                  '14': '255.252.0.0',
                  '15': '255.254.0.0',
                  '16': '255.255.0.0',  # B
                  '17': '255.255.128.0',
                  '18': '255.255.192.0',
                  '19': '255.255.224.0',
                  '20': '255.255.240.0',
                  '21': '255.255.248.0',
                  '22': '255.255.252.0',
                  '23': '255.255.254.0',
                  '24': '255.255.255.0',  # C
                  '25': '255.255.255.128',
                  '26': '255.255.255.192',
                  '27': '255.255.255.224',
                  '28': '255.255.255.240',
                  '29': '255.255.255.248',
                  '30': '255.255.255.252',
                  '31': '255.255.255.254',
                  '32': '255.255.255.255',
                  }

    if netbit in dictionary.keys():
        return dictionary[netbit]
    else:
        return 'False'


# print netbit_to_netmask(str(3))


def exchange_mask(mask):
    '''
    转换子网掩码格式
    :param mask:
    :return:
    '''
    try:
        if isValidMask(mask):
            count_bit = lambda bin_str: len([i for i in bin_str if i == '1'])
            # print count_bit([1,1])
            mask_split = mask.split('.')
            mask_count = [count_bit((bin(int(m)))) for m in mask_split]
            # print mask_count
            # print count_bit
            return str(sum(mask_count))
        # print exchange_mask('255.255.255.0')
        else:
            return 'False'
    except Exception:
        return 'False'


def exchange_bit(bit):
    # bin_arr = ['0' for i in range(32)]
    # for i in range(bit):
    #     bin_arr[i] = '1'
    # tmpmask = [''.join(bin_arr[i * 8:i * 8 + 8]) for i in range(4)]
    # tmpmask = [str(int(tmpstr, 2)) for tmpstr in tmpmask]
    # return '.'.join(tmpmask)
    '''
    掩码位转换为子网掩码和十六进制   '32' ------>('255.255.255.255', 'FF.FF.FF.FF')
    :param bit:
    :return:
    '''
    try:
        if 0 <= int(bit) <= 32:
            netmask = netbit_to_netmask(bit)
            list_mask = netmask.split('.')
            netmask_hex = '.'.join([hex(int(m))[2:] for m in list_mask])
            return [netmask, netmask_hex.upper()]
        else:
            return ['False']
    except Exception:
        return ['False']


def exchange_ip(ip):
    '''
    ip转换位二进制和十六机制
    :param ip:
    :return:
    '''
    try:
        if _check_ip(ip):
            ips = IP(ip)
            ip_bin = ips.strBin()
            ip_hex = ips.strHex()
            return [ip_bin, ip_hex[2:].upper()]
        else:
            return ['False']
    except Exception:
        return ['False']
def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])
def get_ip_hostname():
    # 获取本机电脑名
    host_name = socket.getfqdn(socket.gethostname())
    # 获取本机ip
    myaddr = socket.gethostbyname(host_name)
    return host_name,myaddr
print get_mac_address()
print get_ip_hostname()[0]
# print exchange_ip('192.168.1.')
# print _check_ip('1')
# ip  = '192.2.240.3'
# print exchangge_ip(ip)
# ip = subnet_ip('202.202.3.1', '29')
# print subnet_ip('202.202.3.1', '3').net()
# print ip.netmask()
# print networkAddr('202.202.3.1', '3')
# print ip.net()
# print ip.broadcast()
# print ip.get_mac()
# print ip.int()
# print ip.prefixlen()
# print ip.len()
# print host_num(3)
# print ip[-1]  #broadcast
# print ip[1]
# print ip[0]
# print ip[-2]
# print "#####################"
# for i in ip:
#     print i
#
# print '$$$$$$$$$$$$$$$$$$$$$$'
#
# print ip.len()
