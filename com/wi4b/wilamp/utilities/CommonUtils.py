# (C) Wi4B S.r.l. P.IVA : 02951211206 Mailto: info@wi4b.it
#This document contains confidential and proprietary information.
#Reproduction and / or disclosure through any means is prohibited unless expressed, written consent of authorized representative of Wi4b s.r.l. is obtained
import random
import socket
import inspect
import string
import threading
import traceback
import struct
import binascii
import os

import math

import dateutil
import pytz

import urllib
import datetime
import time
import shutil
import collections

try:
    import json
    JSONAvailable = True
except:
    JSONAvailable = False


class Struct(object):
    def __init__(self, adict):
        """Convert a dictionary to a class

        @param :adict Dictionary
        """
        self.__dict__.update(adict)
        for k, v in adict.items():
            if isinstance(v, dict):
                self.__dict__[k] = Struct(v)


def defaultJSON(obj):
    """Default JSON serializer."""
    import calendar, datetime

    if isinstance(obj, datetime.datetime):
        if obj.utcoffset() is not None:
            obj = obj - obj.utcoffset()
        millis = int(
            calendar.timegm(obj.timetuple()) * 1000 +
            obj.microsecond / 1000
        )
        return millis

    raise TypeError('Not sure how to serialize %s' % (obj,))



class CommonUtilities:
    def __init__(self):
        self.logger = None
        self.u8CRC8Table = [
                              0x00, 0x07, 0x0e, 0x09, 0x1c, 0x1b, 0x12, 0x15, 
                              0x38, 0x3f, 0x36, 0x31, 0x24, 0x23, 0x2a, 0x2d, 
                              0x70, 0x77, 0x7e, 0x79, 0x6c, 0x6b, 0x62, 0x65, 
                              0x48, 0x4f, 0x46, 0x41, 0x54, 0x53, 0x5a, 0x5d, 
                              0xe0, 0xe7, 0xee, 0xe9, 0xfc, 0xfb, 0xf2, 0xf5, 
                              0xd8, 0xdf, 0xd6, 0xd1, 0xc4, 0xc3, 0xca, 0xcd, 
                              0x90, 0x97, 0x9e, 0x99, 0x8c, 0x8b, 0x82, 0x85, 
                              0xa8, 0xaf, 0xa6, 0xa1, 0xb4, 0xb3, 0xba, 0xbd, 
                              0xc7, 0xc0, 0xc9, 0xce, 0xdb, 0xdc, 0xd5, 0xd2, 
                              0xff, 0xf8, 0xf1, 0xf6, 0xe3, 0xe4, 0xed, 0xea, 
                              0xb7, 0xb0, 0xb9, 0xbe, 0xab, 0xac, 0xa5, 0xa2, 
                              0x8f, 0x88, 0x81, 0x86, 0x93, 0x94, 0x9d, 0x9a, 
                              0x27, 0x20, 0x29, 0x2e, 0x3b, 0x3c, 0x35, 0x32, 
                              0x1f, 0x18, 0x11, 0x16, 0x03, 0x04, 0x0d, 0x0a, 
                              0x57, 0x50, 0x59, 0x5e, 0x4b, 0x4c, 0x45, 0x42, 
                              0x6f, 0x68, 0x61, 0x66, 0x73, 0x74, 0x7d, 0x7a, 
                              0x89, 0x8e, 0x87, 0x80, 0x95, 0x92, 0x9b, 0x9c, 
                              0xb1, 0xb6, 0xbf, 0xb8, 0xad, 0xaa, 0xa3, 0xa4, 
                              0xf9, 0xfe, 0xf7, 0xf0, 0xe5, 0xe2, 0xeb, 0xec, 
                              0xc1, 0xc6, 0xcf, 0xc8, 0xdd, 0xda, 0xd3, 0xd4, 
                              0x69, 0x6e, 0x67, 0x60, 0x75, 0x72, 0x7b, 0x7c, 
                              0x51, 0x56, 0x5f, 0x58, 0x4d, 0x4a, 0x43, 0x44, 
                              0x19, 0x1e, 0x17, 0x10, 0x05, 0x02, 0x0b, 0x0c, 
                              0x21, 0x26, 0x2f, 0x28, 0x3d, 0x3a, 0x33, 0x34, 
                              0x4e, 0x49, 0x40, 0x47, 0x52, 0x55, 0x5c, 0x5b, 
                              0x76, 0x71, 0x78, 0x7f, 0x6A, 0x6d, 0x64, 0x63, 
                              0x3e, 0x39, 0x30, 0x37, 0x22, 0x25, 0x2c, 0x2b, 
                              0x06, 0x01, 0x08, 0x0f, 0x1a, 0x1d, 0x14, 0x13, 
                              0xae, 0xa9, 0xa0, 0xa7, 0xb2, 0xb5, 0xbc, 0xbb, 
                              0x96, 0x91, 0x98, 0x9f, 0x8a, 0x8D, 0x84, 0x83, 
                              0xde, 0xd9, 0xd0, 0xd7, 0xc2, 0xc5, 0xcc, 0xcb, 
                              0xe6, 0xe1, 0xe8, 0xef, 0xfa, 0xfd, 0xf4, 0xf3
                              ]
        self.crc16tab = (0x0000, 0xC0C1, 0xC181, 0x0140, 0xC301, 0x03C0, 0x0280,
                        0xC241, 0xC601, 0x06C0, 0x0780, 0xC741, 0x0500, 0xC5C1, 0xC481,
                        0x0440, 0xCC01, 0x0CC0, 0x0D80, 0xCD41, 0x0F00, 0xCFC1, 0xCE81,
                        0x0E40, 0x0A00, 0xCAC1, 0xCB81, 0x0B40, 0xC901, 0x09C0, 0x0880,
                        0xC841, 0xD801, 0x18C0, 0x1980, 0xD941, 0x1B00, 0xDBC1, 0xDA81,
                        0x1A40, 0x1E00, 0xDEC1, 0xDF81, 0x1F40, 0xDD01, 0x1DC0, 0x1C80,
                        0xDC41, 0x1400, 0xD4C1, 0xD581, 0x1540, 0xD701, 0x17C0, 0x1680,
                        0xD641, 0xD201, 0x12C0, 0x1380, 0xD341, 0x1100, 0xD1C1, 0xD081,
                        0x1040, 0xF001, 0x30C0, 0x3180, 0xF141, 0x3300, 0xF3C1, 0xF281,
                        0x3240, 0x3600, 0xF6C1, 0xF781, 0x3740, 0xF501, 0x35C0, 0x3480,
                        0xF441, 0x3C00, 0xFCC1, 0xFD81, 0x3D40, 0xFF01, 0x3FC0, 0x3E80,
                        0xFE41, 0xFA01, 0x3AC0, 0x3B80, 0xFB41, 0x3900, 0xF9C1, 0xF881,
                        0x3840, 0x2800, 0xE8C1, 0xE981, 0x2940, 0xEB01, 0x2BC0, 0x2A80,
                        0xEA41, 0xEE01, 0x2EC0, 0x2F80, 0xEF41, 0x2D00, 0xEDC1, 0xEC81,
                        0x2C40, 0xE401, 0x24C0, 0x2580, 0xE541, 0x2700, 0xE7C1, 0xE681,
                        0x2640, 0x2200, 0xE2C1, 0xE381, 0x2340, 0xE101, 0x21C0, 0x2080,
                        0xE041, 0xA001, 0x60C0, 0x6180, 0xA141, 0x6300, 0xA3C1, 0xA281,
                        0x6240, 0x6600, 0xA6C1, 0xA781, 0x6740, 0xA501, 0x65C0, 0x6480,
                        0xA441, 0x6C00, 0xACC1, 0xAD81, 0x6D40, 0xAF01, 0x6FC0, 0x6E80,
                        0xAE41, 0xAA01, 0x6AC0, 0x6B80, 0xAB41, 0x6900, 0xA9C1, 0xA881,
                        0x6840, 0x7800, 0xB8C1, 0xB981, 0x7940, 0xBB01, 0x7BC0, 0x7A80,
                        0xBA41, 0xBE01, 0x7EC0, 0x7F80, 0xBF41, 0x7D00, 0xBDC1, 0xBC81,
                        0x7C40, 0xB401, 0x74C0, 0x7580, 0xB541, 0x7700, 0xB7C1, 0xB681,
                        0x7640, 0x7200, 0xB2C1, 0xB381, 0x7340, 0xB101, 0x71C0, 0x7080,
                        0xB041, 0x5000, 0x90C1, 0x9181, 0x5140, 0x9301, 0x53C0, 0x5280,
                        0x9241, 0x9601, 0x56C0, 0x5780, 0x9741, 0x5500, 0x95C1, 0x9481,
                        0x5440, 0x9C01, 0x5CC0, 0x5D80, 0x9D41, 0x5F00, 0x9FC1, 0x9E81,
                        0x5E40, 0x5A00, 0x9AC1, 0x9B81, 0x5B40, 0x9901, 0x59C0, 0x5880,
                        0x9841, 0x8801, 0x48C0, 0x4980, 0x8941, 0x4B00, 0x8BC1, 0x8A81,
                        0x4A40, 0x4E00, 0x8EC1, 0x8F81, 0x4F40, 0x8D01, 0x4DC0, 0x4C80,
                        0x8C41, 0x4400, 0x84C1, 0x8581, 0x4540, 0x8701, 0x47C0, 0x4680,
                        0x8641, 0x8201, 0x42C0, 0x4380, 0x8341, 0x4100, 0x81C1, 0x8081,
                        0x4040)

    
    def node_calculate_intmac(self,mac):		
        mac1p = mac[0:4]
        mac2p = mac[4:8]
        mac3p = mac[8:12]
        mac4p = mac[12:16]
        hmac1p = self.hex2dec(mac1p)
        hmac2p = self.hex2dec(mac2p)
        hmac3p =self.hex2dec(mac3p)
        hmac4p = self.hex2dec(mac4p)
        return str(hmac1p)+":"+str(hmac2p)+":"+str(hmac3p)+":"+str(hmac4p)

    def proccrc8(self,CRC, u8Data): 
        return self.u8CRC8Table[(CRC ^ u8Data) & 0xff]; 

    def crc16(self,data, mask=0xA001):
        # data_length = len(data)
        # unpackFormat = '%db' % data_length
        # unpackedData = struct.unpack(unpackFormat, data)
        crc = 0x0000
        for char in data:
            c = ord(char)
            #c = byte
            c = c << 8
        
        for j in xrange(8):
            if (crc ^ c) & 0x8000:
                crc = (crc << 1) ^ mask
            else:
                crc = crc << 1
                c = c << 1
        
        return crc & 0xffff

    def crc16fast(self, s):
        crcValue=0x0000
        
        for ch in s:
            tmp=crcValue^(ord(ch))
            crcValue=(crcValue>> 8)^self.crc16tab[(tmp & 0xff)]
        return crcValue

    def dec2hex(self,n):
        """return the hexadecimal string representation of integer n"""
        return "%X" % n
    
    def hex2dec(self,s):
        """return the integer value of a hexadecimal string s"""
        return int(s, 16)
        
    def byte2hex(self,byteStr):
        """
        Convert a byte string to it's hex string representation e.g. for output.
        """
        
        # Uses list comprehension which is a fractionally faster implementation than
        # the alternative, more readable, implementation below
        #   
        #    hex = []
        #    for aChar in byteStr:
        #        hex.append( "%02X " % ord( aChar ) )
        #
        #    return ''.join( hex ).strip()        
    
        return ''.join( [ "%02X " % ord( x ) for x in byteStr ] ).strip()
        
    def hex2byte(self,hexStr):
        """
        Convert a string hex byte values into a byte string. The Hex Byte values may
        or may not be space separated.
        """
        
        # The list comprehension implementation is fractionally slower in this case    
        #
        #    hexStr = ''.join( hexStr.split(" ") )
        #    return ''.join( ["%c" % chr( int ( hexStr[i:i+2],16 ) ) \
        #                                   for i in range(0, len( hexStr ), 2) ] )
     
        bytes = []
    
        hexStr = ''.join( hexStr.split(" ") )
    
        for i in range(0, len(hexStr), 2):
            bytes.append( chr( int (hexStr[i:i+2], 16 ) ) )
    
        return ''.join( bytes )

    def chars2float(self, charString):
        try:
            hexVal = binascii.hexlify(charString)
            value = struct.unpack('<f', hexVal.decode('hex'))[0]
            return value        
        except Exception:
            return 0
    
    def chars2floatLE(self, charString):
        try:
            hexVal = binascii.hexlify(charString)
            value = struct.unpack('!f', hexVal.decode('hex'))[0]
            return value        
        except Exception:
            return 0

    def mac2double(self,macaddress,encoding):
        try:
            unpackedMAC =  struct.unpack(encoding+"8B",Utils.hex2byte(macaddress))
            repackedMAC = struct.pack(encoding+''+'8B',*unpackedMAC)
            unpackedMAC = struct.unpack("!d",repackedMAC)
            return unpackedMAC[0]
        except:
            Utils.raiseException()
            return 0
    
    def getLocalIPAddress(self):
        try:
            import commands
            return commands.getoutput("/sbin/ifconfig").split("\n")[1].split()[1][5:]
        except:
            Utils.raiseException()
            return self.getLocalIPAddressOLD()
        
    def getLocalIPAddressOLD(self):
        try:
            httpd_port = "unknown"
            local_ip = ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1])
            if local_ip.count > 0 :
                local_ip=str(local_ip[0])
            print ("Local IP: " + str(local_ip) +":"+str(httpd_port))
        except:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("gmail.com",80))
                local_ip = s.getsockname()[0]
                s.close()
            except:
                local_ip = "127.0.0.1"
        return local_ip
    
    def getHostname(self):
        try:
            with open ("/etc/hostname", "r") as hostname:
                return hostname.read().replace('\n', '')
        except:
            return "wilampgw"
    
    def getUUID(self):
        try:
            with open ("/etc/uuid", "r") as uuid:
                return uuid.read().replace('\n', '')
        except:
            try:
                import uuid
                uuid_str = str(uuid.uuid1())
                with open ("/etc/uuid", "w") as uuid:
                    uuid.write(uuid_str)
                return uuid_str
            except:
                return "00000000-0000-0000-0000-000000000001"
            

    def getVPNIPAddress(self):
        try:
            import commands
            intf = 'tun0'
            intf_ip = commands.getoutput("ip address show dev " + intf).split()
            intf_ip = intf_ip[intf_ip.index('inet') + 1].split('/')[0]
            return intf_ip

        except:
            return "unknown"
    
    def whoami(self):
        return inspect.stack()[1][3]
    def myparams(self):
        frame = inspect.currentframe()
        frame = inspect.stack()[1]
        stack = inspect.stack()
        args, _, _, values = inspect.getargvalues(inspect.stack()[1][0])
        #for i in args:
        #    print "    %s = %s" % (i, values[i])
        return [(i, values[i]) for i in args]
    def whosdaddy(self,fullDaddy=True):
        try:
            stack = inspect.stack()
            daddy = stack[2][3]
            if fullDaddy:
                for stackEl in stack[3:]:
                    daddy+="<-"+str(stackEl[3])
            return daddy
        except:
            traceback.print_exc()
    
    def raiseException(self,text=None):
        try:
            if text is None:
                text = "Exception in " + self.whosdaddy()+": "+ str(traceback.format_exc())
            print (text)
            try:
                if self.whosdaddy() != "addLog" and self.whosdaddy() != "truncate_records":
                    self.logger.addLog(text)
            except:	"NOTHING"
            
        except:
            #traceback.print_exc()
            print ("Exception in raiseException")
                
    def getNetworkIp(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('www.google.it', 0))
        return s.getsockname()[0]


    def trace(self,frame, event, arg):
        print ("%s, %s:%d" % (event, frame.f_code.co_filename, frame.f_lineno))
        return self.trace
    
    def todict(self,obj, classkey=None):
        try:
            if isinstance(obj, dict):
                for k in obj.keys():
                    obj[k] = self.todict(obj[k], classkey)
                return obj
            elif hasattr(obj, "__iter__"):
                return [self.todict(v, classkey) for v in obj]
            elif hasattr(obj, "__dict__"):
                data = dict([(key, self.todict(value, classkey)) 
                    for key, value in obj.__dict__.iteritems() 
                    if not callable(value) and not key.startswith('_')])
                if classkey is not None and hasattr(obj, "__class__"):
                    data[classkey] = obj.__class__.__name__
                return data
            else:
                return obj
        except:
            Utils.raiseException()
            
    def writeLineToFile(self,text,file,useTimestamp = False):
        try:
            file = open(file,'a')
            if useTimestamp:
                timestamp=Utils.getLocalizedNow().strftime("%Y-%m-%d %H:%M:%S")
                text = timestamp+" - "+text+"\r\n"
            file.writelines(text)
            file.close()
        except:
            self.raiseException()
            
    def isTrue(self,sentence):
        try:
            if type(sentence) is int or type(sentence) is float:
                if int(sentence) == 1: return True
                else: return False
            if type(sentence) is str:
                if str(sentence).lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']:
                    return True
                else: return False
            if type(sentence) is bool:
                return sentence
            return bool(sentence)
        except:
            Utils.raiseException()
            return False


    def isAck(self,ack):
        try:
            if isinstance(ack,dict):
                if "ack" in ack:
                    return ack["ack"]
            if "ACK" in ack and not "NACK" in ack:
                return True
            else: return False
        except:
            Utils.raiseException()
            return False


    def boolToInt(self,value):
        try:
            if self.isTrue(value): return 1
            else: return 0
        except:
            Utils.raiseException()
            return 0

    def chmod(self,file,mode):
        try:
            ""
            os.chmod(file,mode)
        except:
            Utils.raiseException()

    def toJSON(self,value):
        try:
            ""
            try:
                value = value.__dict__
            except:
                ""
            if JSONAvailable:
                jsonString = json.dumps(value)
                return jsonString
            else: return None
        except:
            Utils.raiseException()
            return None

    def getFreeMemory(self):
        try:
            """
            Get node total memory and memory usage
            """
            with open('/proc/meminfo', 'r') as mem:
                ret = {}
                tmp = 0
                for i in mem:
                    sline = i.split()
                    if str(sline[0]) == 'MemTotal:':
                        ret['total'] = int(sline[1])
                    elif str(sline[0]) in ('MemFree:', 'Buffers:', 'Cached:'):
                        tmp += int(sline[1])
                ret['free'] = tmp
                ret['used'] = int(ret['total']) - int(ret['free'])
            return ret
        except:
            ret = {}
            ret['free'] = 0
            ret['used'] = 0
            Utils.raiseException()
            return ret

    def getParameterFromFile(self,parameter):
        try:
            ""
            return "Not implemented"
                        
        except:
            Utils.raiseException()

    def uniqid(self,prefix='', more_entropy=False):
        m = time.time()
        uniqid = '%8x%05x' %(math.floor(m),(m-math.floor(m))*1000000)
        if more_entropy:
            valid_chars = list(set(string.hexdigits.lower()))
            entropy_string = ''
            for i in range(0,10,1):
                entropy_string += random.choice(valid_chars)
            uniqid = uniqid + entropy_string
        uniqid = prefix + uniqid
        return uniqid

    def valuesAreEqual(self,value1,value2):
        try:
            try:
                value1 = self.convertUnicode(value1)
                value2 = self.convertUnicode(value2)
                try:
                    value1Conv = float(value1)
                except:
                    value1Conv = value1

                try:
                    value2Conv = float(value2)
                except:
                    value2Conv = value2
                return value1Conv == value2Conv
            except:
                Utils.raiseException()
                return value1 == value2

        except:
            Utils.raiseException()
            return False

    def sleepRandom(self,range=None):
        try:
            if range:
                if len(range)==2:
                    sleepTime = random.uniform(range[0],range[1])
                else:
                    sleepTime = random.uniform(0, 0.2)
            else:
                #sleepTime = random.random()
                sleepTime = random.uniform(0, 0.2)
            time.sleep(sleepTime)
        except:
            time.sleep(0.2)
            ""
            #Utils.raiseException()

    def isBitSet(self,byteval,idx):
        """
        Check if a bit in position idx is set given a bitmask
        :param byteval: the bitmask
        :param idx: bit index to check
        :return: The status of the bit
        :rtype: bool
        """
        try:
            byteval = int(byteval)
            return (byteval&(1<<idx)!=0)
        except:
            return False

    def millisecSinceEpoch(self,dt=None):
        """
        Millisecond since epoch of a given datetime
        :param dt: datetime
        :return: millisecond since epoch
        """
        try:
            if not dt: dt = Utils.getLocalizedNow()
            if isinstance(dt, str):
                dt = datetime.datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")

            #epoch = datetime.datetime.utcfromtimestamp(0)
            #delta = Utils.getLocalizedNow() - datetime.datetime(1970, 1, 1)
            #print "DELTA " + str(int(delta.total_seconds() * 1000))
            #print "epoch " + str(int((dt - epoch).total_seconds() * 1000.0))

            #print "UNIX TIMESTAMP: "  + str(int(time.time() * 1000))
            #print "MKTIME APPROACH: " + str(int((time.mktime(dt.timetuple()) + dt.microsecond / 1E6)*1000))

            result = int((time.mktime(dt.timetuple()) + dt.microsecond / 1E6)*1000)
            return result
        except:
            return None


    def millisecSinceEpochUTC(self,dt=None):
        """
        Millisecond since epoch of a given datetime
        :param dt: datetime
        :return: millisecond since epoch
        """
        try:
            if not dt: dt = datetime.datetime.utcnow()
            if isinstance(dt, str):
                dt = datetime.datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
            dt = self.fromLocalTimeToUTC(dt)
            #epoch = datetime.datetime.utcfromtimestamp(0)
            #delta = datetime.datetime.now() - datetime.datetime(1970, 1, 1)
            #print "DELTA " + str(int(delta.total_seconds() * 1000))
            #print "epoch " + str(int((dt - epoch).total_seconds() * 1000.0))

            #print "UNIX TIMESTAMP: "  + str(int(time.time() * 1000))
            #print "MKTIME APPROACH: " + str(int((time.mktime(dt.timetuple()) + dt.microsecond / 1E6)*1000))
            mic1=  int((dt - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)
            return mic1

            epoch = datetime.datetime(1970, 1, 1)
            td = dt - epoch
            # return td.total_seconds()
            mic2= (td.microseconds + (td.seconds + td.days * 86400) * 10 ** 6) / 10 ** 6

            result = int((time.mktime(dt.timetuple()) + dt.microsecond / 1E6)*1000)
            return result
        except:
            return None

    def fromLocalTimeToUTC(self,localDateTime, setUtcInfo=False):
        try:
            microseconds = localDateTime.microsecond
            localDateTimeTuple = localDateTime.timetuple()
            secs = time.mktime(localDateTimeTuple)
            result_utc_time =  time.gmtime(secs)
            resultDateTime = datetime.datetime(*result_utc_time[:6])
            resultDateTime = resultDateTime + datetime.timedelta(microseconds=microseconds)
            if setUtcInfo:
                result = resultDateTime.replace(tzinfo=pytz.utc)

            return resultDateTime
        except:
            Utils.raiseException()
            return None

    def dateTimeFromEpoch(self,epoch):
        """
        Get datetime object from milliseconds since epoch
        :param epoch:
        :return: datetime
        """
        try:
            s = epoch / 1000.0
            #print datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S')
            return datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S')
            #return datetime.datetime.utcfromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S')

        except:
            Utils.raiseException()
            return epoch

    def getLocalizedNow(self,includeUtcZoneInfo = True):
        try:
            return datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
            return pytz.utc.localize(datetime.datetime.now())
        except:
            Utils.raiseException()

    def getLocalizedUTC(self,dateDT):
        try:
            return dateDT.replace(tzinfo=pytz.UTC)
        except:
            Utils.raiseException()
            return None

    def dateTimeStructFromEpoch(self,epoch,setUtcInfo=False):
        """
        Get datetime object from milliseconds since epoch
        :param epoch:
        :return: datetime
        """
        try:
            s = epoch / 1000.0
            result = datetime.datetime.fromtimestamp(s)
            if setUtcInfo:
                result = result.replace(tzinfo=pytz.utc)
            return result
            #return datetime.datetime.utcfromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S')

        except:
            Utils.raiseException()
            return epoch

    def dateTimeStructFromEpochUTC(self,epoch,setUtcInfo=False):
        if isinstance(epoch, datetime.datetime):
            return epoch
        return self.fromLocalTimeToUTC(self.dateTimeStructFromEpoch(epoch), setUtcInfo=setUtcInfo)

    def getIntelRadarMacFromDeviceId(self,deviceId):
        try:
            deviceId = Utils.convertUnicode(deviceId)
            mask = "RAD             "
            result = mask[0:16-len(deviceId[0:12])] + deviceId[0:12]
            return result

        except:
            return "RAD         " + deviceId[0:4]


    def getLocalizedNow(self):
        try:
            return datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
            return pytz.utc.localize(datetime.datetime.now())
        except:
            Utils.raiseException()

    def tryToParseDate(self, string):
        try:
            return dateutil.parser.parse(string) if string and isinstance(
                string, str) else string if string else None
        except:
            return string

def defaultJSON(obj):
    """Default JSON serializer."""
    import calendar, datetime

    if isinstance(obj, datetime.datetime):
        if obj.utcoffset() is not None:
            obj = obj - obj.utcoffset()
        millis = int(
            calendar.timegm(obj.timetuple()) * 1000 +
            obj.microsecond / 1000
        )
        return millis

    #if isinstance(obj, WiLampGraphField):
    #    return obj.__dict__


    raise TypeError('Not sure how to serialize %s' % (obj,))


Utils = CommonUtilities()