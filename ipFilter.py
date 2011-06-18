import socket
import struct

class IpFilter():
    def __init__(self):
        full = self.iptoint("255.255.255.255")
        self.mask_list = []
        for i in range(0,32):
            self.mask_list.append(full >> i << i)
        self.control_list = []
        f = open('list.txt')
        for line in f:
            self.control_list.append(line.split())
        
            
    def iptoint(self,ip):
        return socket.ntohl(struct.unpack("I",socket.inet_aton(ip))[0])

    def checkrange(self,ip,mask,target):
        if (self.iptoint(ip)>>self.mask_list.index(self.iptoint(mask)) == self.iptoint(target)>>self.mask_list.index(self.iptoint(mask))):
            return True
        else:
            return False
    def filter(self,target):
        for i in range(3,len(self.control_list)):
            if self.checkrange(self.control_list[i][0],self.control_list[i][2],target):
                return True
        return False


if __name__ == '__main__':
    f = IpFilter()
    print f.filter('220.181.111.86')
