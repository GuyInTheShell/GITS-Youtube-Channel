Hello everyone, GuyInTheShell here.

This video is an introduction to the assembly language.

The reason I'm doing that is not that I want to be able to write assembly code myself, that is too
cumbersome, but rather that I want to have enough understanding to be able to do CTF, that is to say
Capture The Flag challenges, that involve Reverse Engineering a binary program.

Today, we'll see how to write a hello world program in assembly. That'll teach us:
- the basics of the assembly language
- the all important `syscall` instruction
- playing with registers
- as well as compiling and running assembly code

---

First thing first: what's assembly? Assembly is the language that is closest to the machine. While
languages like C and Python need to be heavily translated for the computer to understand and
execute, assembly is basically the language that your processor speaks.

There are actually several types of assembly languages. Each processor architecture has its own.
In 2020, most processors in desktop and laptop computers are of the x86 family. If we look at the
wikipedia page for x86, we find all Intel and AMD processors.

There is one other family of general purpose processors that is well known and exists broadly, it's
the ARM. This is the processor family that powers most mobile phones and tablets, as well as the
recent Apple M1 computers. While the concepts are the same, the details might be different. For the
intent of my videos, we'll look into x86 assembly.  

---

I just said before that assembly was basically machine code. While it's very close, it's not
completely true. It's still slightly adapted, typically to use short mnemonics that are more human
readable than number codes. As such, since it's a representation of machine code, there are several
manners or syntaxes to show it. The most common ones are the Intel syntax and the AT&T syntax. We can
see a sample of the 2 flavors in the x86 assembly language wikipedia page. For my videos, we'll use
the Intel flavor that I find a bit terser. However, there is no real difference between the two and
you should feel free to use the AT&T syntax if you prefer it. Note that the compiler we'll use only
supports the Intel syntax.

We'll learn a few concepts one step at a time. Just so you know, we'll work under linux. I'll likely
a complementary video to do the same thing on MacOs at a later time. In my shell, on the left I'm in
my mac terminal configured with all the bells and whistles for my code editor. On a right I'm in a
Kali linux docker container that has access to the same file and that's where we'll compile and run
it.

First thing first, in my linux container, let's install `nasm` if not already done. `nasm` is an
assembly compiler that supports the intel syntax.

---

Before writing anything, we need to know 2 things on top of the assembly language that we'll
discover and those are registers and syscalls.

Registers are places where you can store data. Those places are used by the computer to perform
operations or transfer data. You can think of the registers a bit like variable in a programming
language with major caveats:
- Registers are limited in number
- Registers have a fixed size: 64bits or 8 bytes on modern 64 bits architecture
You should also note that some registers have a special meaning.

The X86 Assembly wikibook has all the information you need, in particular:
- Each register has a name
- In 64 bits architecture, register names start with the letter 'R'
- There are 8 general purpose registers.
- You can reference a subpart of the 64 bits register with another name. For example `EAX` is the 32
  least significant bits of the `RAX` register.
- There is an instruction pointer `RIP` that holds the address of the currently executed program
  instruction
- 64 bits architectures add 8 general purpose registers `R8` to `R15`

That's enough about registers.

---

Let's talk about syscalls. Syscalls are a way to call functions.
Those functions are provided by the kernel and are invoked following very specific conventions. Here
again, the X86 Assembly wikibook has it all. In particular it states:
- That all information that needs to be passed to syscalls are to be put in General Purpose
  Registers
- That each syscall is referenced by a number
- That the syscall number should be placed in the `RAX` register
- That there are 2 ways to invoke a syscall:
  - Via an interruption, by setting everything up and then calling `int 0x80`
  - Via a more recently created `syscall` instruction.
  You'll note that the registers used by the interruption method and the `syscall` instruction
  method are not the same.  
  Also the function reference numbers those method use are not the same either.  
  In this video, we'll only work with the `syscall` instruction, which is the most common way
  nowadays

Now we have all the concepts we need and we can start to write some assembly code.

---

Let's first simply write a program that exits with a specific exit code.  
We can go to a nice website that references the linux syscalls and look for exit. We find that it is
syscall number 60. So we need to put the value 60 in register `RAX`. By double-clicking on the line,
we can also see that it expects 1 parameter, the code with which to exit, and that this should be
put in `RDI`. We'll use exit code 42 to prove that what we do works.

Let's open a text editor. The assembly instruction to change the value of a register is `MOV`
followed by the register to change, a comma, and then the value to set.  
So we put 60 in `rax` and 42 in `rdi`, and then we call the `syscall` instruction:
```nasm
mov rax, 60
mov rdi, 42
syscall
```

---

Let's try to compile that with `nasm`. We tell `nasm` which compilation target we want: in our case
we want a 64bits linux executable, we give the output file, which is a so-called object file, and
finally we give the source file.  

```shell
nasm -f elf64 -o hello.o hello.nasm
```
So, yeah it fails. It complains that it did not find the `_start` symbol. The `_start` symbol is
used to indicate where the program starts. It the entrypoint that `nasm` uses by convention.  
Indeed, the code does not necessarily start at the top of the file, like we'll see later.

```nasm
_start:
  mov rax, 60
  mov rdi, 42
  syscall
```

---

It still does not work because we additionally have to declare the symbol `_start` as global so that
`nasm` will export it in the object file, for the linker to see.


```nasm
global _start

_start:
  mov rax, 60
  mov rdi, 42
  syscall
```

Don't worry too much about that. Just know that with `nasm`, you need a `_start` symbol at the start
of your program and that it needs to be declared as `global`.

Now it compiles. We can now link the object file. Again, I'm not going to talk about it. Suffice it
to say for this video that you use a linker (`ld`) to transform an object file into an executable
binary

```shell
ld -o hello hello.o
```

---

Now we can see that it produced a binary (note that it is marked as an executable file already) and
we can run it

```shell
ls -l
./hello
```

Since we only coded that it should exit, it feels like it did not do anything. Let's check the
return code though. In a shell, the return code of the latest run command is stored in the special
global variable `?`. If you have not run anything at all since running `./hello`, then you can do
```shell
echo $?
```
and you should get `42` which is what we expected!

---

We were able to control the exit syscall. Let's now write something on the standard output. Back to
our syscall table, we find that
- `write` is syscall 1
- it expects a file descriptor in `rdi`
- a pointer to a string in `rsi`
- and the size of the string in `rdx`
For the file descriptor, that easy enough. We want to write to the standard output which by
convention is file descriptor 1.  
The size of the string, I guess we can count manually.
But what about the pointer? So the thing is, the string you want to write on the standard output
might not fit in an 8 bytes register. Knowing that each character is encoded by 1 byte, you can only
fit 8 characters in a register. To work around this limit, `write` expect to receive in `rsi` not
the string to write but the address in memory where it can find the string. In memory, this string
can occupy an arbitrary length. That's the reason why the `write` syscall expects a size. It needs
to know where the string finishes so as not to print things from the memory that are coming from
elsewhere.

---

This means now that we have to put some value in memory.

We are going to do it the hard way, very manually, in order to discover more things.

We have an assembly instruction called `push`. This intruction pushes the value that is inside a
registry to the top of the stack. Let's play with that. We'll construct the string "Hello world"
one character at a time.  

---

First we want to put the letter H on the stack. If we use python quickly, we can find that the
letter upper case 'H' is 72 or 0x48.  
```python
ord('H')

hex(ord('H'))
```

---

So we'll put this value in a General Purpose Register, say `r8`, then we'll push `r8` onto the
stack. Now the top of the stack is our letter H. So we can give the address of the top of the stack
to the write syscall. Luckily, there is a special register that keeps track of the top of the stack
and that is `rsp`, "sp" meaning stack pointer.
```nasm
global _start

_start:
  mov  r8, 0x48  ; 'H'
  push r8
  mov  rax, 1
  mov  rdi, 1
  mov  rsi, rsp
  mov  rdx, 1
  syscall

  mov  rax, 60
  mov  rdi, 42
  syscall
```

---

We compile, link and run, and it works. We get our 'H' on STDOUT! You'll note that because we did
not write any newline character, the next prompt is rendered on the same line. We'll take care about
that when we have the full string.

Let's do the same thing to add 'e'. e is 0x65. Remember also that modern computer architecture are
64 bits. This means that registers are 64 bits, or 8 bytes, wide.  
We only used one byte for the 'H' value. So we can put the 'e' next to it in the same operation.
Let's also not forget to increment the `rdx` register. We now have 2 characters to print.
```nasm
global _start

_start:
  mov  r8, 0x4865  ; 'He'
  push r8
  mov  rax, 1
  mov  rsi, rsp
  mov  rdx, 2
  syscall

  mov  rax, 60
  mov  rdi, 42
  syscall
```
---

We compile, link, run and ... wait. Now that's interesting. Instead of getting 'He' as we expected
we get 'eH'. The reason for that is that our processor architecture is using so-called little
endian storage. To put it simply, it means that in a register that contains several bytes, the bytes
are arranged in reverse order. For a string, that is written byte by byte, that means the character
appear reversed. With this new knowledge, we can fix it
```nasm
global _start

_start:
  mov  r8, 0x6548  ; 'He'
  push r8
  mov  rax, 1
  mov  rsi, rsp
  mov  rdx, 2
  syscall

  mov  rax, 60
  mov  rdi, 42
  syscall
```
---

Now it works. Let's do the same thing for the next 6 characters (remember, a register holds 8 bytes)
```nasm
global _start

_start:
  mov  r8, 0x77202c6f6c6c6548  ; 'Hello, w'
  push r8
  mov  rax, 1
  mov  rsi, rsp
  mov  rdx, 8
  syscall

  mov  rax, 60
  mov  rdi, 42
  syscall
```

---

Let's add the rest of the string.
```nasm
global _start

_start:
  mov  r8, 0x77202c6f6c6c6548  ; 'Hello, w'
  push r8
  mov  r8, 0x0a21646c726f  ; 'orld!\n'
  push r8
  mov  rax, 1
  mov  rsi, rsp
  mov  rdx, 14
  syscall

  mov  rax, 60
  mov  rdi, 42
  syscall
```

---

Wait, an ordering issue again! The problem is different though. We want the Hello part to be
displayed first. That means that the write function needs to read it first. For that, it needs to be
on the top of the stack. And for it to be on top, we need to push it last on the stack.
```nasm
global _start

_start:
  mov  r8, 0x0a21646c726f  ; 'orld!\n'
  push r8
  mov  r8, 0x77202c6f6c6c6548  ; 'Hello, w'
  push r8
  mov  rax, 1
  mov  rsi, rsp
  mov  rdx, 14
  syscall

  mov  rax, 60
  mov  rdi, 42
  syscall
```
---

So we took the manual, difficult road there, but I wanted to show you:
- push register values onto the stack
- how little-endianess works
- and the fact that the stack is, well, a stack, which is to say a last in first out construct.

For the easy way, we can use a data byte. It's basically a variable. Such constants are
generally put in a different section of the program. Let's change the code to use this data byte.

We'll first add a `.data` section and a `.text` section which contains the code (we should actually
have done that before), but it was not strictly mandatory.

---

Now we define a `str` label referencing this location and then we define the data byte itself with
`db`.

We can also remove the manual construction of the string. And put `str` in `rsi`. That is because a label in an
assembly source file stores the address at which it is located. Here `str` stores the address where
the data byte is defined. It's not on the string anymore, it's somewhere in the program.

```nasm
section .data
str: db 'Hello, world!', 0xa    ; 0xa is a newline

section .text
global _start

_start:
  mov  rax, 1
  mov  rsi, str
  mov  rdx, 14
  syscall

  mov  rax, 60
  mov  rdi, 42
  syscall
```

---

I'll conclude with another trick. We should not compute by hand the length of the string we want to
display. This is a dangerous practice. If we pass too big a number, we'll expose some data from the
stack that we did not intend to show to users, and that in turn could be used by an attacker.

The trick consist in playing with addresses. We have seen that `str` stores the address of the data
byte. Now say we put a label next to the data byte and call it `str_len`. Now because those things
are contiguous in memory, the length of the data byte is address `str_len` minus address `str`. This
is a length in bytes. And it's also the length of the string since 1 character takes 1 byte of
storage.

So the value that is stored at the `str_len` address is a number: we'll introduce that with the
`equ` keyword. Now we said it's equal to the current address, which is denoted by `$`, minus the
`str` address. And here we are.

---

```nasm
section .data
str: db 'Hello, world!', 0xa    ; 0xa is a newline
str_len: equ $ - str

section .text
global _start

_start:
  mov  rax, 1
  mov  rsi, str
  mov  rdx, str_len
  syscall

  mov  rax, 60
  mov  rdi, 42
  syscall
```

And that's it for today.

We saw:
- That assembly is a language very close to the one the machine understand
- what registers are and what syscalls are
- We saw how to structure a simple assembly program
- How to compile it and run it

As a bonus, I'll do a couple of short videos to:
- Build the same program with the AT&T syntax and the standard GNU `as` compiler
- Build the same program on Mac

# References

Processor list:
  https://en.wikipedia.org/wiki/X86#Current_implementations  

Intel vs AT&T:
  https://en.wikipedia.org/wiki/X86_assembly_language#Syntax

Registers:
  https://en.wikibooks.org/wiki/X86_Assembly/X86_Architecture

How to perform a syscall:
  https://en.wikibooks.org/wiki/X86_Assembly/Interfacing_with_Linux

Linux syscalls:
  https://filippo.io/linux-syscall-table/

X86 instructions:
  https://www.cs.virginia.edu/~evans/cs216/guides/x86.html

Mac syscalls:
  https://opensource.apple.com/source/xnu/xnu-1504.3.12/bsd/kern/syscalls.master
