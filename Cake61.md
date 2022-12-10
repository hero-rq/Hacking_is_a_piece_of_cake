0x00007fffffffd6d8│+0x0000: 0x00007ffff7e5d89a  →  <_IO_file_underflow+378> test rax, rax        ← $rsp                                                                                   
0x00007fffffffd6e0│+0x0008: 0x0000000000000000                                               
0x00007fffffffd6e8│+0x0010: 0x0000000200010000                                               
0x00007fffffffd6f0│+0x0018: 0x00007ffff7fa1508  →  0x00007ffff7fa1000  →  0x00007ffff7ddc000  →  0x03010102464c457f                                                                       
0x00007fffffffd6f8│+0x0020: 0x00007ffff7f9a980  →  0x00000000fbad208b                                                                                                                     
0x00007fffffffd700│+0x0028: 0x00007ffff7f9c4a0  →  0x0000000000000000                                                                                                                     
0x00007fffffffd708│+0x0030: 0x0000000000000000                                               
0x00007fffffffd710│+0x0038: 0x00007ffff7f9b4a0  →  0x00007ffff7f976a0  →  0x00007ffff7f67b72  →  0x636d656d5f5f0043 ("C"?)                                                                
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── code:x86:64 ────                                                                                                          
   0x7ffff7ecae88 <read+8>         test   eax, eax                                           
   0x7ffff7ecae8a <read+10>        jne    0x7ffff7ecaea0 <__GI___libc_read+32>                                                                                                            
   0x7ffff7ecae8c <read+12>        syscall                                                                          
 → 0x7ffff7ecae8e <read+14>        cmp    rax, 0xfffffffffffff000                                                   
   0x7ffff7ecae94 <read+20>        ja     0x7ffff7ecaef0 <__GI___libc_read+112>                                                                                                                                                         
   0x7ffff7ecae96 <read+22>        ret                                                                              
   0x7ffff7ecae97 <read+23>        nop    WORD PTR [rax+rax*1+0x0]                                                                                                                                                                      
   0x7ffff7ecaea0 <read+32>        sub    rsp, 0x28                                                                 
   0x7ffff7ecaea4 <read+36>        mov    QWORD PTR [rsp+0x18], rdx    
