section .data
str: db "Hello, world!", 0xa
str_len: equ $ - str

section .text

global _main

_main:
  mov rax, 0x2000004
  mov rdi, 1
  mov rdx, str_len
  mov rsi, str
  syscall

  mov rax, 0x2000001
  mov rdi, 42
  syscall
