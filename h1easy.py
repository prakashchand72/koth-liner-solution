import signal,sys
try:
    from pwn import *
    print("\n[\033[1;32m+\033[1;37m] Autopwn Tyler ~ 0xASTUTE\n")
except:
    print('\n[\033[1;31m!\033[1;37m] this script requires sudo previlages\n\n[\033[1;31m!\033[1;37m] Try installing pwntools python library\n')
    exit(1)
def kill(sig, frame):
    print("\n[\033[1;31m-\033[1;37m] Bye ASTUTE \n")
    sys.exit(1)
target=sys.argv[1] 

print(f'\n[\033[1;32m+\033[1;37m] target -> {target}')
print('\n[\033[1;32m+\033[1;37m] for exploit upload php-reverse-shell on ' + 'http://'+target+':8002/lesson/1')
print('\n[\033[1;32m+\033[1;37m] pwnkit to exploit')