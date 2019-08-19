#coding:utf-8
import win32crypt
import binascii
import os
import Tkinter
import tkMessageBox
import tkFileDialog

def genRdpPasswd(passwd):
    #passwd must be unicode!!!!!!!!!!!!!!!!!!!!!!!!!!
    pwdHash = win32crypt.CryptProtectData(passwd, u'psw', None, None, None, 0)
    pwdHash_ok = binascii.hexlify(pwdHash)
    #print len(pwdHash_ok)
    #print pwdHash_ok
    return pwdHash_ok
    
def logIn():
    rdpStr = u'''screen mode id:i:2
use multimon:i:0
desktopwidth:i:1920
desktopheight:i:1080
session bpp:i:32
winposstr:s:0,1,917,8,1744,1003
compression:i:1
keyboardhook:i:2
audiocapturemode:i:0
videoplaybackmode:i:1
connection type:i:7
networkautodetect:i:1
bandwidthautodetect:i:1
displayconnectionbar:i:1
enableworkspacereconnect:i:0
disable wallpaper:i:0
allow font smoothing:i:0
allow desktop composition:i:0
disable full window drag:i:1
disable menu anims:i:1
disable themes:i:0
disable cursor setting:i:0
bitmapcachepersistenable:i:1
audiomode:i:0
redirectprinters:i:1
redirectcomports:i:0
redirectsmartcards:i:1
redirectclipboard:i:1
redirectposdevices:i:0
autoreconnection enabled:i:1
authentication level:i:2
prompt for credentials:i:0
negotiate security layer:i:1
remoteapplicationmode:i:0
alternate shell:s:
shell working directory:s:
gatewayhostname:s:
gatewayusagemethod:i:4
gatewaycredentialssource:i:4
gatewayprofileusagemethod:i:0
promptcredentialonce:i:0
gatewaybrokeringtype:i:0
use redirection server name:i:0
rdgiskdcproxy:i:0
kdcproxyname:s:
drivestoredirect:s:
'''
    ip = ipVar.get().decode('utf-8')
    username = usernameVar.get().decode('utf-8')
    passwd = passwdVar.get().decode('utf-8')
    passwd_encrypt = genRdpPasswd(passwd)
    print len(ip), ip
    print len(username), username
    print len(passwd), passwd
    print len(passwd_encrypt), passwd_encrypt
    rdpStr = rdpStr + "full address:s:%s\r\nusername:s:%s\r\npassword 51:b:%s\r\n"%(ip, username, passwd_encrypt)
    rdpFile = "%s+%s.rdp"%(ip, username)
    with open(rdpFile,"w") as f:
        f.write(rdpStr)
    #os.system('start "RemoteConsole %s %s" mstsc  AutoRdp.rdp /v:%s'%(ip, username, ip))
    os.system('start "RemoteConsole %s %s" mstsc  %s'%(ip, username, rdpFile))
    
if "__main__" == __name__:
    root = Tkinter.Tk()
    ipVar = Tkinter.StringVar()
    usernameVar = Tkinter.StringVar()
    passwdVar = Tkinter.StringVar()
    
    ipVar.set(u'YourIp')
    usernameVar.set(u'YourName')
    passwdVar.set(u'YourPasswd')
    
    root.title('AutoRdp')
    #root.withdraw()
    Tkinter.Label(root, text = 'IpAddr:').grid(row = 0, column = 0)
    Tkinter.Entry(root, textvariable = ipVar).grid(row = 0, column = 1)
    Tkinter.Label(root, text = 'UserName:').grid(row = 1, column = 0)
    Tkinter.Entry(root, textvariable = usernameVar).grid(row = 1, column = 1)
    Tkinter.Label(root, text = 'PassWord:').grid(row = 2, column = 0)
    Tkinter.Entry(root, textvariable = passwdVar).grid(row = 2, column = 1)
    Tkinter.Button(root, text = '远程登陆', command = logIn).grid(row = 3, column = 2)
    
    root.mainloop()
    
    
