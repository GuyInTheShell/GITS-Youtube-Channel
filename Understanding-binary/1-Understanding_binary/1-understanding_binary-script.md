Hello everyone, GuyInTheShell here to talk about Understanding binary. I felt like doing this very
introductory episode because if we want to dive into rather low level topics, binary, as well as
hexadecimal that we'll talk about in the next episode, comes in very handy. And since most people
don't use this day to day, a refresher is a good idea.

Let's dive in.

We use binary because that's how the hardware powering our computers work. An electronic component
can either be activated or not, that is to say whether it receives a current or not. On a magnetic
hard drive, used to store data without active current, in each data cell, we can store only 1 of 2
states. So you get binary, A world in which everything is in 1 of 2 states.

|-|
Now we needed a representation to talk about those states. Since we have 2, we needed 2 characters.
We chose 0 and 1.  
|-|Conventionally, 0 is the OFF state, the one where there is no current, and 1 is the ON state.  


Each time we need to transfer or store information, we can use a bit and it's value is either 0 or
1.  
Now, obviously, storing only 2 values is not very useful. That is why, when you store information,
you use several bits.

|-|With 2 bits, you can store the values 00, 01, 10 and 11. That is to say with 2 bits you can
represent 4 different states or values. You can do the same gymnastic with 3 bits, and you'll get 8
distinct states or values. |-|Math allows you to generalize this. Knowing that a bit can
have only 2 values, if you take N bits, you can represent 2 to the power of N states or values.

Now we have a mean to process or store more meaningful data.

Wait meaningful? Yes, by stringing bits together, we can represent things that can take a lot of
different states or values. |-|For example, with 8 bits, we can represent 2 to the power of 8, that is
to say 256 states or values. But what do those states mean? |-|what does the binary string 01001101
mean?

One way to assign meaning to those strings of zeroes and ones would be to have some sort of
dictionary that would map a binary string to a letter for example. But this is going too fast.
First, we need to realize that a binary string has a meaning in Math and represent a number! Spoiler
alert, 01001101 is 77!

|-|But let's forget about binary for a little bit and let's review how we usually use numbers and how
we count. Some time in the past, we arbitrarily decided to use 10 characters to represent numbers.
Those characters are the well known 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9. It's important to understand
that it was arbitrary. Romans used a completely different way to represent numbers. One, by the way,
that was not practical for maths. And yes, it's very possible that we use 10 characters to do math,
because we have 10 fingers. But still it's arbitrary and with this explanation, we could also have
used 5 characters (one hand). Anyway.

|-|So to count, we use those characters one at a time. When we don't have any left, we introduce a
second character in front of them, starting at 1. When we exhaust the characters on the right again,
we just go to the next character on the left and start over. And when we have exhausted both
characters for the left and right position, we again add one character and start over again. This
allows us to represent any number we want, in a systematic way.

This feels very mechanical and logical. This is because that's what we have learned and use every
day. But math again can explain this "notation". We said that we use 10 characters. That's the
decimal system. In math, you say that you represent the number in base 10.

|-|If we take a random number written as 1 3 5 8, we can interpret it with the base decoding formula.
|-|You take each character, and you multiply it by the base elevated to the power of the position of
the character. Then you sum all the numbers you got.  
Let's do it.  
|-|8 is the first character, at position 0. So we do 8 times 10 to the power of 0. 10 to the power of 0
is 1, so it's 8 times 1, that is to say 8.  
|-|Next is 5 in position 1. That's 5 times 10 to the power of 1, so 50.  
|-|Next is 3 in position 2. That's 3 times 10 to the power of 2, so 300.  
|-|Next is 1 in position 3. That's 1 times 10 to the power of 3, so 1000.  
|-|Sum it all and you get 1358.  
So it's a bit stupid and obvious. It's how numbers work right? And what we just did is to interpret
is base 10 a base 10 numbers. So we got 1358 = 1358. But now we'll return to binary and it will all
make sense.

|-|Back to binary. Binary counting uses only 2 characters to represent numbers, those are 0 and 1. In
math, we call that base 2.  
|-|The way we count with those numbers follow the same rule as the decimal representation. We first
enumerate all our characters, 0 and 1. When we don't have any left, we add one new character on the
left and continue. Of course having only 2 characters, the representation soon grows rather long.

|-|Let's take the binary number written as 1 0 1 1 and apply the base changing formula to it to see
what it means in our standard decimal representation.  
|-|First is 1 in position 0. That's 1 times 2 to the power of 0, so 1.  
|-|Next is 1 in position 1. That's 1 times 2 to the power of 1, so 2.  
|-|Next is 0 in position 2. That's 0 times 2 to the power of 2, so 0.  
|-|Next is 1 in position 3. That's 1 times 2 to the power of 3, so 8.  
|-|Therefore the number we are looking at is 11!

Because all of this is math and just arbitrary representation, we can also do addition of binary
numbers the way we learned to add decimal numbers!  
|-|Let's add 1001 to 1101.  
|-|We first add the first 2 digits. That's 1 and 1. In binary that would be 10. We write 0 and carry
the 1 over.  
|-|Then we have 0 and 0, and the 1 we carried over. That's 1.  
|-|Then 0 and 1, that's 1.  
|-|And finally 1 and 1. That's 10. We put 0, carry the 1 over. It's on its own. So that's one.  
If we apply our base changing to read those numbers in base 10, we would see that we did |-|9 + |-|13 = |-|22

That's all there is to it. We use the binary notation to represent numbers and we, humans, can do
maths with them. But our computers can too! Now that we have numbers, how to we represent text? |-|Well
now we need a dictionary that maps a number to a character. The most common and very widely used
one is the ASCII table. It's an arbitrary dictionary that tells you that upper case A is 65, upper
case B is 66 (they follow each other). Lower case a is 97. We also see that the character 1, not the
number 1, is represented by the number 49! With that mapping table, we can now not only store and
process numbers, but also text. We can encode text into numbers, store it, and then decode it when
we retrieve it from storage.

To conclude, I'd like to show you briefly how you can play with those concepts we just learned today
using the python language.

Python is meant to interact with humans. So by default, it uses the decimal system to represent
numbers. If we feed it the number 10, it gives this number back as is. If we ask 9 + 13, it will
say 22. This is true in decimal notation only!

Now let's input a binary number. We can tell python that the number we are entering is binary if we
prefix it by "0b". If we enter 0b10110, we get 22. Python does not have a way to explicitly say
that a number is in base 10, but other systems might understand the notation "0d".  
We can make python understand that something we give to it is binary. If we want python to give us
back a number in binary, we can use the `bin` function. Careful that it will give the answer as a
string, since it only represents numbers in decimal.

We have another way to have python interpret numbers from different bases. This is by giving a
non-prefixed string to the `int` function. The `int` function takes a string, and converts it to a
number. Because it understand an un-prefixed notation only, it needs a base. By default, it assumes
that we are working in base 10. Therefore it would interpret the string '10110' as 10,110. If we
want `int` to read the string as a binary, we have to explicitly tell it which base to use.

That's for numbers. Let's look briefly at the ASCII table a bit. Python provides 2 functions. One to
go from a character to its ASCII number representation. This function is `ord`. We can use it.  
The second function does the opposite. It takes a number and returns the associated character. This
function is `chr`. Playing a bit with those, we can see that some values in the small numbers have
no characters mapping. Similarly, the mapping table stops at 126. While what I'm saying is true for
ASCII, it's not strictly true for the `chr` and `ord` function, but we won't go there today.

And that closes today's discussion about binary.  
We saw
- That binary is a notation that uses only 0 and 1
- That it can be used to represent numbers, in "base 2"
- How to use binary numbers and even add them
- That the ASCII table gives us a convention mapping a number to a character
- That we can use python to play with binary numbers, decimal numbers and the ascii table

Hope you enjoyed it. See you in the next video to talk about hexadecimal this time.

Bye Bye.
