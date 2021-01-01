In the previous video entitled "Understanding binary", we talked about the binary and the decimal
notation. So what is hexadecimal now and why do we need yet another notation? Decimal is for human,
binary is for computers, do we really need another one?

When we interact with a computer to give it instructions, we store values in memory. To do that, we
do not operate with individual bits. Indeed, we saw that bits can represent only 2 values or states,
so they are rather useless in isolation. We instead use "bytes". A byte is a group of bits that go
together and that cannot be broken down. When you send instructions to the processor, you send
bytes. When you access memory, you access it through a byte address. Address 1 point to byte 1.
Address 2 points to byte 2, not bit 2. Bits themselves have no address.  
For a long time now, the convention has been that a byte is 8 bits of information. We'll see in this
video that this size is practical for at least 2 reasons: first, the ASCII table, which needs 7 bits,
fits nicely in there, meaning that any character can be represented by a byte, with little waste.
Secondly, the fact that 8 is a power of 2 will come in handy.  
That's the first piece of the puzzle for today's video. This is how modern computer work.

The second piece of the puzzle is the hexadecimal notation. Building up on the concepts that we saw
in the previous video, the hexadecimal notation is base 16. In this base, we use 16 characters to
represent numbers: the usual 0 to 9 numbers to which we add the letters A, B, C, D, E and F which
respectively represent 10, 11, 12, 13, 14 and 15.

Like in the previous video, we can take an hexadecimal number, say A5E and convert it to base 10.  
E is in position 0. That's 14 times 16 to the power of 0, so 14.  
5 is in position 1. That's 5 times 16 to the power of 1, so 80.  
A is in position 2. That's 10 times 16 to the power of 2, so 2,560.  
We sum it all and it gives 2,654.

Now that we have our second piece of the puzzle, let's see how it all fits.

We've have seen first that we use a convention to use data 8 bits at a time and that this is called
a byte. This means that a byte can hold numbers from 0 to 255.

First, it's not practical in term of alignment of characters. A decimal number represented by a bytes can use 1, 2
or 3 characters to be represented in decimal. This can however be solved by always writing the leading 0, even
if we are not used to that.

Second, it does not neatly align in term of usage. If we take the number 10, first decimal number
that needs 2 characters, its binary representation has nothing special. The same goes for 100. And a
full byte in binary is 11111111 where we exhaust all our characters. In decimal that 255, which is
about a fourth of the way in the numbers that can be written with 3 digits.

And last and most important, it's not easy to read. I can't reason with bytes in binary. 8
characters representing 255 values that's too much for me. And while I know how to decode it, it's
cumbersome.

That's where hexadecimal comes in. So we have seen that 8 bits can represent 2 to the power of 8
values. Hexadecimal now, is base 16, which is 2 to the power of 4!  And 2 to the power of 8 is 2 to
the power of 4 times 2 to the power of 4! This means that binary and hexadecimal notation align.

If we take 4 bits and enumerate all the values they can represent, we get exactly all the values
that a single hexadecimal character can represent:  
from 0000 = 0
to   1111 = F

This in turns means that a byte of 8 bits can be exactly represented by 2 hexadecimal character,
each encoding half of the byte value.

Here 1010 1110 in binary is equal to AE in hexadecimal. This means that when I see byte, I can split
it in the middle and easily convert it to hexadecimal. There are only 16 values so you recognize
them pretty fast. Even better, a 2 characters hexadecimal number is reasonably easy to decode to
decimal by hand. You just have one multiplication by 16 (up to 16 times 16) and an addition. With a
bit of practice, it becomes easy.

And that what makes the hexadecimal notation so practical.

You might know that if you try to open a binary file in a text editor, you get a lot of garbage.
This is because the content of the file, that is organized in bytes, is not meant to be interpreted
as text using the ASCII table like we saw in the previous video. Instead those bytes are numbers
that represent instructions for our computer.  
Now, if we take an hexadecimal reader, like `xxd` for example that is often included in linux
distributions, we can open binary files and see what's inside without trying to decode it in text.
Such editor usually have 3 parts. On the left you have addresses. We don't care about that today. On
the right, you have the text representation. But for binary files, we just said that this is mostly
garbage, so we'll ignore it. What's interesting is the middle part. That's where each byte of data
is represent as a single 2 digits hexadecimal number. Now we start to be able to read binary file,
although we don't yet really know what those value mean and we'll discuss that in future videos.

Finally, I wanted to show you how you can play with hexadecimal numbers in python. We saw last time
that numbers are interpreted as base 10 by default, like this 10 value. We can tell python that we
mean 10 to be a binary value by prefixing it with `0b` in which case python will say that it sees
the number 2. Similarly, we can tell python that we mean this 10 to be hexadecimal by prefixing `0x`
this time, in which case python will tell us that it sees 16.

We also saw that python can give us the binary representation of a decimal number through the `bin`
function. `bin(10)` gives `'0b1010'`. In the same fashion, we have the `hex` function to ask for the
hexadecimal representation of a number. `hex(10)` gives `0xA`.

And finally, we saw that we could use the `int` function to convert a non-prefixed string into a
number. We say that by default it uses base 10: `int('10')` is `10`. But we could give the base as a
second parameter. `int('10', 2)` is `2`. `int('10', 16)` is `16`.

And that's it for today. I hope you enjoyed it. As a reminder, I did the binary and the hexadecimal
video as an introduction to the serie I want to do about reversing binaries. In this serie, we'll
use hexadecimal a lot, and since this is not a day to day thing for most of us, a refresher sounded
like a good idea.

I hope I'll catch you in my next video.

Bye Bye.
