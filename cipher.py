#/usr/bin/python3
import crypt
def testpassword(cryptPass):
    salt=cryptPass[0:2]
    print(salt)
    dictFile=open('dict.txt','r')
    for word in dictFile.readlines():
        word=word.strip('\n')
        cryptWord=crypt.crypt(word,salt)
        if cryptWord==cryptPass:
            print('[+] Found Password: '+word)
            return
    print('[-] Password Not Found')
    return
def main():
    passFile=open('passwords.txt','r')
    for line in passFile.readlines():
        if ':' in line:
            user=line.split(':')[0]
            cryptPass=line.split(':')[1].strip(' ')
            print('[*] Cracking Password For: '+user)
            testpassword(cryptPass)
if __name__=='__main__':
    main()
            



