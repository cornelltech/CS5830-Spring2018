### Syllabus for CS 5830

# Syllabus for CS 5830

Welcome to CS 5830, Cryptography. We will be studying cryptography, both the
theory and how it is used in practice. By the end of the course you should
understand the basics of cryptography, how cryptographers analyze the
security of cryptographic schemes, and how to implement suitable
cryptographic algorithms within broader projects. 


Instructors: Rafael Pass (http://www.cs.cornell.edu/~rafael/) and Tom Ristenpart (https://rist.tech.cornell.edu)
TA: ??? 


### Pre-requisites

Students should have programming experience (we will be focusing on Python),
understand basic probability, know binary representations (ASCII), operations on
bit strings (XOR), have some background on computer networking, file systems,
etc. If in doubt shoot the instructor an email.



### Requirements

The class will involve a combination of lectures, in-class group exercises,
homeworks, a prelim, and a final. You'll be graded according to the following:

* Participation: 10%
* Homeworks:  50% (each homework will count an equal amount)
* Prelim:  20% 
* Final:  20% 

There will be several opportunities for extra credit, as well.


### One unit project

Those enrolling for an extra unit of credit will conduct a semester-long
project. We will provide example project ideas in the first two weeks of class,
and work with students to refine the projects. Projects could be a deep-dive into some specific area of cryptography, 
an implementation project for some state-of-the-art cryptography, or augmenting
some other project of your interest with cryptographic mechanisms. 

### Background reading

The following books should be helpful, but none are required if you don't want to spend the money:

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


# Jan 25 (Intro) 

* Introduction to cryptography.
* One-time pads 
* Shannon's perfect secrecy
* Computational cryptography



# Jan 30 (One-way functions)

* Computational reductions



# Feb 1 (Background on CNT)

* Computational number theory
* Modular arithmetic to RSA


# Feb 6  (RSA and discrete log as OWFs)

* RSA problem 
* Discrete log problem
* Building OWFs


# Feb 13 (Towards symmetric encryption)

* Constructing symmetric encryption from OWF attempts
* Computational indistinguishability
* Pseudorandomness
* Yao + hardcore bits


# Feb 15 (Pseudorandom generators)

* Expansion of randomness via PRGs. 

# Feb 20 (No class -- Fall break)


# Feb 22 (Single-message secure encryption)

* Construction from PRG

# Feb 27 (Multi-message secure encryption)

* Pseudorandom functions (PRFs)
* Encryption from PRFs

# Mar 1 (CTR mode)

* CTR mode as PRG, built from PRF
* Towards fast PRFs?

# Mar 6 (Blockciphers)

* The goal and cryptanalysis basics
* DES, AES
* Feistel construction

* In-class exercise: replace CMAC with HMAC in AE scheme

# Mar 8 (Feistel and Luby-Rackoff)

* Theoretical support for DES-type constructions
* Birthday bound and analysis of 3-round Feistel
* Format-preserving encryption


# Mar 13 (Blockcipher modes)

* CTR mode from block ciphers
* PRP/PRF switching lemma
* CBC mode


# Mar 15 (Chosen-ciphertext attacks)

* Padding oracle attacks against CBC
* Real-world examples



# Mar 20 (Authenticated encryption)

* Message authentication codes (MACs)
* AE from encryption plus MACs


# Mar 22 (Hash functions)

* Collision resistance, one-wayness
* Blockcipher-based failures
* Use in symmetric crypto: HMAC, KDFs

# Mar 27 (Asymmetric cryptography)

* Public-key encryption
* PKE from trapdoor permutations

# Mar 29 (Digital signatures)

* 

# Apr 3 (No class -- Spring break)

# Apr 5 (No class -- Spring break)

# Apr 10
# Apr 12
# Apr 17
# Apr 19
# Apr 24
# Apr 26
# May 1
# May 3

