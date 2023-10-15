# Intro to SCM

Hi everyone,

This is the first episode of a GIT serie. By talking about what GIT is and how it works, we'll
discover how to use it in powerful way.

GIT is one of the main tools of the software engineer and like every craftsman, the engineer should
know his tools. The quality of his work depends on it.

So what are we going to talk about in this serie? I don't have a strict agenda yet and things will
possibly change, but overall we'll see
- What an SCM is?
- What are commits and how they work
- What are branches, and other references, as well as remotes
- What's a merge and how we go about dealing with conflicts
- What's a rebase and the numerous thing it can do for you
- ... and certainly more


You might think that the first few parts are known to you, or of little interest, but I too often
find colleagues that have actually not mastered those basics and who therefore can't figure out
their way through complex situations that might arise when using more advanced, although daily-used,
features like merge and rebase.

# SCM

We shall therefore start by talking about what an SCM is. SCM means Source Code Management. It's
also known as Version Control, Revision Control or Source Control.

Source code management makes it sound like a software thing, only for developers, but it's not.
Version or Revision Control is a broader definition giving an additional applicability to the usage
of SCM. To take an example, Washington DC is using an SCM (GIT hosted on GitHub) to track and
publish their laws (statutes and codes).
(https://github.com/DCCouncil/law-xml)

We need an SCM for 2 reasons in particular.
- The first one is to keep track of change. This is useful in software development, but with the
  exmaple of the law above, it's even more useful for such context where an audit trail is really
  necessary. Think about legal contracts or specification documents for example.

  For such usage however, you might have other, maybe simpler, solutions than GIT or an SCM.

- The second reason to use an SCM is to allow collaborative work on a set of files, for example the
  source code of a software product.

# Collaborative work

Let's talk then about how we work collaboratively with computer tools, and let's start by forgetting
software development.

Not so long ago, when you would work on documents, spreadsheets or presentations as a group, you
would either
- do so one at a time. "Guys, I'm working on the XXX file, please don't touch it until I'm done".
- or work each on a part and someone would integrate. "Alice, you'll work on slides 1 through 5.
  I'll work on slides 6 through 10. When you are done, send me your copy of the file and I'll merge
  both"

The drawbacks are obvious. It was hard to work in parallel. It required orchestration of who does
what where and additional work, in the form of merging documents.

A first evolution, when the web started to be a common tool, was the Wiki. A wiki is a single space
that host documents that multiple people can edit.
Early wiki might have taken care only of the orchestration problem: when someone is editing the
page, nobody else can.
But modern wiki allow several people to edit the same page at the same time and will then do its
best to merge automatically the multiple sources of changes.

The problem here is that you are still working in a bubble. You do not know if someone is trying to
reorganize the document, change some style or other. What you are changing right now might not be
consistent with what someone else is changing at the same moment.

The final technological shift was collaborative editing. I think it came first from Google with
Wave, but made its way now into such things as Google documents or Office 365. With collaborative
editing everybody is in the same document and you can see in live the edits made by someone else.

Now collaborative editing is great when you want to work on different parts of a presentation and
easily share assets, see what the other is doing, or when multiple people are proof reading a
document for example.

It is not, unfortunately, a solution that works in all the contexts.
- First, the is no tracking of versions. While some software allow you to take snapshots of
  documents or do it automatically for you, the fact that multiple people are editing the document
  in parallel means that you cannot track individual granular updates to the document. You cannot
  say "yesterday morning, Alice added amendment 1. yesterday afternoon Bob added picture 1.3. Today
  Alice proof read the introduction"; but just "it was like that yesterday. It is like that today".
- Finally, if your work requires the documents to settle in a certain state for you to do something
  with them, then it might not be appropriate. This is particularly true if we are talking about
  documents plural. In a collaborative editing context where everybody can change everything always,
  how do you know if the Appendix 1 mentioned in the text is the actual Appendix 1 file or someone
  is currently rearranging stuff?

In software development for example, we need the set of documents (the source code) to settle to
something consistent so that we can build and test the application to check that our change had the
expected result. This is not something you can do in a world where everybody changes all the
documents always, in which case the source code would never be stable.
