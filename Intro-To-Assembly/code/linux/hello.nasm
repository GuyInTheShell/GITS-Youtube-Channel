section .data
str: db "Hello, world!", 0xa
str_len: equ $ - str

section .text

global _start

_start:
  mov rax, 1
  mov rdi, 1
  mov rdx, str_len
  mov rsi, str
  syscall

  mov rax, 60
  mov rdi, 42
  syscall
