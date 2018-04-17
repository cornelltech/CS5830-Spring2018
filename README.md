### Syllabus for CS 5830

# Syllabus for CS 5830

Welcome to CS 5830, Cryptography. We will be studying cryptography, both the
theory and how it is used in practice. By the end of the course you should
understand the basics of cryptography, how cryptographers analyze the
security of cryptographic schemes, and how to implement suitable
cryptographic algorithms within broader projects. 

Classroom: B61

Instructor: Rafael Pass (http://www.cs.cornell.edu/~rafael/) and

Office hours: By appointment

Instructor: Tom Ristenpart (https://rist.tech.cornell.edu)

Office hours: By appointment

TA: Siqiu Yao (sy657@cornell.edu)

Office hours: Fri. 2:30pm - 3:30pm, Gates Hall 406 via Zoom at https://cornell.zoom.us/j/7690848411.
(Since I am TAing remotely. I recommend you to ask questions via email or Slack!)


### Pre-requisites

Students should have programming experience (we will be focusing on Python),
understand basic probability, know binary representations (ASCII), operations on
bit strings (XOR), have some background on computer networking, file systems,
etc.  Equivalent of CS2800 (Discrete Mathematics) and comfort with reasoning
about algorithms, such as proving their correctness and analyzing their running
times, or permission of instructor.  The main skill that will be assumed is the
ability to understand and write formal mathematical definitions and proofs. It
is also important that you are familiar with basic probability (although we will
recall some basic concepts); please refresh yourself by reading Chapter 5 in the
following lecture notes: http://www.cs.cornell.edu/~rafael/discmath.pdf) If in
doubt talk to the instructors.


### Requirements

The class will involve a combination of lectures, in-class group exercises,
homeworks, a prelim, and a final. You'll be graded according to the following:

* Participation: 10%
* Homeworks:  60% (each homework will count an equal amount)
* Final:  30% 

There will be several opportunities for extra credit, as well.


### One unit project

Those enrolling for an extra unit of credit will conduct a semester-long
project. We will provide example project ideas in the first two weeks of class,
and work with students to refine the projects. Projects could be a deep-dive into some specific area of cryptography, 
an implementation project for some state-of-the-art cryptography, or augmenting
some other project of your interest with cryptographic mechanisms. 

### Background reading and Lecture notes

The following books should be helpful, but none are required if you don't want to spend the money:


* Portions of the course will take advantage of these lecture notes: http://www.cs.cornell.edu/courses/cs4830/2010fa/lecnotes.pdf
* [Cryptography 101 by Houtven](https://www.crypto101.io/). Free, but not complete. Feel free to send helpful feedback to the author.

* [Cryptography Engineering by Ferguson, Schneier, and Kohno](https://www.schneier.com/books/cryptography_engineering/). A gentle
  introduction to cryptography.

* [Modern Cryptography by Katz and Lindell](http://www.cs.umd.edu/~jkatz/imc.html). A formal treatment of cryptography.
  We will make reference to, but not go into detail on, topics they treat in
  more detail.


## Lecture schedule

A very preliminary schedule is below to give a taste of the scope of
what we're hoping to cover.  Homeworks will be due on the due date by
11:59:59pm EST. You can use in total 3 late days throughout the semeseter. 



## Lecture schedule

Preliminary schedule is below. This will surely evolve


| Date |  Topic  |  Note |
|------|---------|--------|
| Jan 25 | Intro & one-time-pads |  |
| Jan 30 | One-way functions, computational reductions |  |
| Feb 1 |  Background on computational number theory |  |
| Feb 6 |  RSA and discrete log as OWFs  |  |
| Feb 8 |  Towards symmetric encryption | |
| Feb 13 | Symmetric encryption via OWFs |  |
| Feb 15 | Pseudorandom generators (PRGs) |   |
| Feb 20 | No Lecture (February break)  |  |
| Feb 22 | Single-message symmetric encryption from PRG |  |
| Feb 27 | Multi-message symmetric encryption (PRFs) |  |
| Mar 1 |  |  |
| Mar 6 |   |  |
| Mar 8 |   |  |
| Mar 13 | Blockciphers   | [Slides](slides/blockciphers.pdf) |
| Mar 15 | Length-preserving encryption | [Slides](slides/blockciphers2.pdf) |
| Mar 20 |  Class cancelled | |
| Mar 22 |  Blockcipher modes of operation | [Slides](slides/modes.pdf) |
| Mar 27 |  Chosen-ciphertext attacks  | [Slides](slides/modes2.pdf)  |
| Mar 39 | Message authentication and authenticated encryption | [Slides](slides/msgauth.pdf)  |
| Apr 3 | No lecture (Spring break) |  |
| Apr 5 | No lecture (Spring break) | |
| Apr 10 | Hash functions | [Slides](slides/hash.pdf) |
| Apr 12 | Password hashing  | [Slides](slides/ae-pwae.pdf)|
| Apr 17 | Public-key cryptography    | [Slides](slides/rsa.pdf) |
| Apr 29 |Digital signatures & PKI  |  |
| Apr 24 | Key exchange  | |
| Apr 26 | Hybrid encryption & ElGamal | |
| May 1 |  RNGs |  |
| May 3 | Cryptographic backdoors |  |
| May 9 |  |  |

