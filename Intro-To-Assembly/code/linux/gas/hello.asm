.data
str: .string "Hello, world!\n"
str_len = . - str

.text

.globl _start

_start:
  movq $1, %rax
  movq $1, %rdi
  movq $str_len, %rdx
  movq $str, %rsi
  syscall

  movq $60, %rax
  movq $42, %rdi
  syscall
