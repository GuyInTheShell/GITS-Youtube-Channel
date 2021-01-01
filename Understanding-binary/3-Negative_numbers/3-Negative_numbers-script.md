Hello everyone, GuyInTheShell here.

Today we'll talk about negative integers.

In previous videos, we talked about binary counting, and why hexadecimal was practical as a
representation when we work with bytes.

We saw that the binary notation can be interpreted with Math to represent integer. For example, we
said that with 8 bits, we can represent the numbers from 0 to 255.

Similarly, we said that with a dictionary, or mapping table, like ASCII for example, we could use a
byte to represent a character and therefore encode text into binary.

Now, to expand a bit what we can represent, we should try to represent negative integers.

For the sake of simplicity, we won't work with full 8 bits but limit ourselves to 3 bits. So with
our previous understanding that we can represent positive integers, with 3 bits, we can represent 2
to the power of 3 = 8 values, that is to say numbers from 0 to 7.

Now if we want those 8 values to represent signed integer rather, and if we want to keep it logical
and symetrical, that is to say centered on 0, we can represent numbers from -3 to +3. That's 7
numbers, so we can also represent either -4 or +4. We'll see later which one we'll get.

So it's symetrical, so half of the numbers represented by those 3 bits are positive and half are
negative. A very simple way to represent the sign of the number could be to use the most significant
bit. When 0, it's a positive number, when 1, a negative number.

With this notation, we would have 0-00 to 0-11 representing 0 to 3.  
Similarly we would have 1-00 to 1-11 representing 0 to -3.  
Note that this would logically mean 0 can be represented by 000 (+0) or 100 (-0), which is a bit of
a waste.

This convention would be very practical. As a human, I use the sign to determine the sign, and then
I read the number with the rest of the bits. Easy.

Unfortunately, this is not the one that is conventionally used. The reason for that, once again is
math. It would be great that -1 + 1 = 0. But with the above convention -1 + 1 would be in binary 101
+ 001 which would equal 110 which is -2. That's too bad. So we'll use a different convention

We'll use a visual representation to understand this convention. Let's put all the values on a
circle. The circle representation makes sense. Indeed, the number after 111 should be 1000. But if
we have only 3 bits to store data, then the leading 1 in the fourth bit gets lost and so 000 is
after 111.

On this wheel, we can put our unsigned integer. Nothing special there.

Let's try to put our signed integers now. First let's split the circle in the middle. We still want
half the values to be position and half negative.

We can now start placing the numbers. 000 is 0, easy. 001 is still 1. OK. So we want to place -1
so that -1 + 1 is equal to 0. For that, we put -1 at 111. indeed, 111 + 001 is 1000, which encoded
on 3 bits only is 000. That makes sense, right?

We can now continue to place the numbers: 2, -2, 3 and -3. Now as mentioned earlier, we have one
binary value that is left. Which number should we give it? Again this is about chosing a convention.
And the logic is as-is. Because of how binary work, we can see that all the negative numbers have
their most significant bit set to 1. And the value left, 100, starts with a 1. So we'll chose that
it's equal to -4 rather than +4.

So with respect to our original naive representation, what's cool is that the first bit still
represent the sign as our intuition was suggesting. The rest of the bytes however are not easily
readable. To interpret a negative number, you have to take its two's complement.

Before diving a little deeper on two's complements, let's first prove that what we just said is true
and works as we think. For that, we can use Java. For a few years now, java comes with an
interactive shell `jshell`. We'll use Java, because according to its documentation, the default
primitive type to store integers is `int` which is a 32 bits signed integer.

Let's open a shell. If we declare an `int` value that is equal to 1, we get 1. ok. Now let's define
a variable that store the highest value possible in 32 bits. 32 bits is 4 bytes, which is 8
hexadecimal characters. So the maximum value for 32 bits is 0xFFFFFFFF in hexadecimal. If we define
such a variable is java, we get an integer that is equal to -1! Well, that's what we saw on our
wheel of numbers.

Ok let's find the middle now. According to our previous understanding, the biggest positive number
we can represent is the one that starts with a 0 and is followed by 31 ones. That means the first 4
bits are 0111 which in hexadecimal is 0x7, while the rest are all ones, i.e. 0xF. The biggest number
on 32 bits that start with the first bit set to 0 is therefore 0x7FFFFFFF. Using java, we can see
this number is 2147483647. That makes sense. The next number (positive) would be in binary 1
followed by 31 zeros. Therefore 1 times 2 to the power of 31. We can see that it's 2147483648, that
is to say one more than the number we just got in the variable. The world still makes sense.

Now if all is logical, we can take the symetrical number on the wheel. That's the number that starts
with a one, has all zeros and finishes with a 1. In hexadecimal, that's 0x80000001. If we give that
to `java` we get -2147483647. Ok, our wheel thing makes sense.

Last thing to check is what's the value of the number in the middle of the wheel at the bottom. The
number that in binary starts with a 1 and then is all zeros. That's 0x80000000. Give that to `java`
we do get negative 2147483648, as we discussed.

Cool, so our wheel representation and understanding works.

Now let's see how to use this two's complement construct. Typically, I want to be able to do 2
things: given a negative number, I want to know how I'm supposed to represent it in binary; and
given a binary number that starts with a 1, I want to know what it's equal to.

There are sereval algorithmic way to make that work. But we'll use the way that feels to me the most
logical and that is enough for us to play.

First, there is an easy way. Let's use java. We just saw java uses signed integers. So given a
binary value, say 0xA1234567, we put that into an `int` and get its value.  
Conversely, given a negative `int`, we can ask for its binary value (in hexadecimal notation)
through the `Integer.toHexString()` function. Pretty easy.

Let's look at what it would look like in our go-to scription language: python.

Python does not constrain itself with bytes, 32 bits or 64 bits to store numbers. It can store
arbitrarily long integers. So if you ask for the hexadecimal representation of, say, -100, you'll
get the hexadecimal value for 100 preceded by a '-' sign. Not helping us.

Let's construct it a bit more manually. Back to our 3 bits wheel. Let's say we want -3. We can't
start at 0, because python will tell us that 0 - 3 is equal to -3. So let's start with our knowledge
that since we code with 3 bits, the biggest value is 111 which is -1. Now -3 is -1 minus 3 plus 1.
So we start at -1. We do minus 1, 2, 3 and then we add one back. If we put our overlay back, it
worked, we ended at -3 and we found the binary value.

Now in Python, with bigger numbers. Say we are working, like java, with 32 bits. 32 bits stops at
0xFFFFFFFF which again is -1. If we want to represent -100, we say that -100 is equal to 0xFFFFFFFF
- 100 + 1 which is 0xFFFFFF9C. Let's check in java. This works.

Now the reverse operation. Say we want to know what 110 is. We know it's negative because it start
with 1. The trick is to find an operation That will end us on the positive side of the wheel. Let's
call our unknown quantity X. If we do -1 minus X + 1, we get X. And that will land us on the
positive side of the wheel. Let's use our unsigned integer interpretation. 110 is 6. We start at -1.
Minus 1, 2, 3, 4, 5, 6, and plus 1. And we end up on 2, which is the symetrical value to the one we
started from. 110 is minus 2.

Now again in python with bigger numbers. Still with 32 bits. We take a negative number. It starts
with a 1 in binary. Say 0xA1234567. Apply our formula. -1 would be 0xFFFFFFFF. So 0xFFFFFFFF -
0xA1234567 + 1. And if we check in java, that's the same!

And that's how it works.

Now the last thing I can say is to exercise caution. When you see a binary value, you can't know how
to interpret it without context. As we have seen, python uses arbitrarily long integers by default,
so any hexadecimal value will be interpreted as a position integer. Java on the other hand uses
signed 32 bits integer for its `int` type. So it's all about context. Be mindful of that before
assigning meaning to a strings of bits!

And that's all I have for you today.

See you next time.

Bye Bye.


# References

Java documentation:
  https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html
