Hello everyone, GuyInTheShell here to talk about CTF today.

I had been thinking about making videos for a long time. But I always felt it was too much work. I
also was lacking some focus and deep topics to cover. Starting CTF a few months ago was actually the
spark that led me to create this Youtube channel.

But what are CTF?

CTF, means Capture The Flag. CTFs are exercises, puzzles, challenges or events involving puzzles and
challenges. The principal is that some information, the Flag, is hidden somewhere and you need to
capture it. Capturing a flag can involve many different things and CTF challenges are often sorted
in categories.

Reverse Engineering challenges are puzzles in which you are given a program inside which there is a
flag to find. For example, it might be a simple program that takes a parameter as an input. If you
give the right parameter, that is to say the flag, the program congratulates you, otherwise it
encourages you to try again. Your goal in such a case is to reverse engineer the logic of the
program to extract the flag from it.

Cryptography challenges involve having a flag hidden in plain sight, protected by a code. Of cause
those challenge are solvable. This means that they might involve an old cryptography method that is
either well know or does not resist modern computers. Or it might involve a strong modern technique
but that is mis-used and therefore subject to attacks.

Web challenges involve a webserver that is generally badly protected. Your task is to enter the
website with an exploit to find the hidden information. For example, without any prior knowledge,
you might try to log into the website as an admin.  
But web challenges are just a subset of exploit challenges in which you are given a running system
(a server, a web application, a network socket answering to request) and have to find a flaw to
exploit it and extract hidden information

Forensics challenges involve digging through piles of data. You are given some data in which you are
told that a flag is hidden. The data might be an image, a java heap dump, a log of network traffic,
or anything else. You then have to apply tools to sift through this data.

Then you have a hodge podge of things where the flag might not be very hard to find but might
involve quite a bit of programming to reconstruct. The flag might need you to have good binary
knowledge to find. The flag might be basically given to you but in a weird format, and you just have
to figure out how you are supposed to read it.

Now that we know what CTFs are, why CTF?

I started doing CTF challenges just for the novelty of it. Discovering a bit the kind of problems
there are. What were my skills with respect to that, which were basically none to start with. But
then I discovered a lot of reasons to like CTFs.

There is first the obvious puzzle part. A challenge is a puzzle that someone built and that is
waiting to be solved, and this attracts me.

Then there is a knowledge you gain. I like knowing things. And a lot of CTF challenges require you
to have some experience, have seen the technology or the pattern already, know the right tools, ...

And finally, there is the usefulness of the knowledge acquired. You are basically broadly looking
into the world of security. It makes you realize how little you know about it and how strong
security mechanism, if badly used, can be circumvented.

When I'm not on Youtube, I'm a software engineer, working mostly on cloud SaaS applications. I use
to have some distant theoritical knowledge about buffer overflow, XSS, and such. Now that I have
used them, I have more appreciation for them and I can be more careful when securing my own
application and possibly spot better when security is not applied correctly.

Just a note of caution. CTF are not meant to teach you to hack real applications or services. This
is an illegal activity. Even without bad intentions, you should not apply any of the techniques you
are learning here on a real target, unless you own it, or unless you are participating as an ethical
hacker in a bug bounty program.

What if you want to learn CTF things now? Well there are a few ways. As with any learning,
practicing is the best. Then acquiring some knowledge by watching others is also interesting. The
best by far is to try your hard at a problem, and after some amount of effort, watch a write-up to
see how other people did it, what they did at the place where you were stuck, ... Looking at
write-ups is actually interesting even if you solved the challenge yourself, because it could show
you other ways or other tools that you might not know.

To train your hand, there are a few platforms on the web that propose challenge with increasing
difficulties and sometimes accompanied with tutorials. For example, I have myself tried CTFlearn
which is great to find very easy exercises to start with and progress, TryHackMe which has some
great quality tutorials and some interesting multi-step challenges. I'll also mention Exploit
Education and Hacker101 which look interesting but I have not had the time to check them out yet.

Once you have a bit of training, just try a CTF event. A lot of events are free and online. It's
possible, maybe even likely, that you won't go very far. But you will try your hand at real,
original and complex problems. You should take notes of the things you do along the way. And when
the event is finished, you can search the web for write-ups. You'll see what other people did for
solving the problems you were stuck on and that'll teach you a few new tricks for the next time.

Finally, I'll mention one project that really interest me. I'm sure there are others, but this is
the one I know. It is the game Pwnie Island. It is a 3d open world adventure game in which there a
exploitable bugs left there on purpose. If you are able to find them, you can maybe have unlimited
health, or unlimited money, maybe you can fly, ... who knows. And finding those exploits is
necessary to complete the game! This is something I want to try my hand on one day, but I think I'm
far from ready. If some time in the future you see write-ups about this game on this channel,
that'll mean I have come some way and I sticked to it, which would be awesome.

And that's all I have for you today. Following this introduction on CTF, I'll make some videos on
tools, techniques, and mock CTF problems so that you can learn with me.

See you next time

Bye Bye.

# References

CTFlearn:
  https://ctflearn.com/

TryHackMe:
  https://tryhackme.com/

Exploit Education:
  https://exploit.education/

Hacker101:
  https://ctf.hacker101.com/

Pwny Island:

CTFtime:
  https://ctftime.org/
