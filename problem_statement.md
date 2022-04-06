## Introduction
The purpose of this project is to test an applicant's coding and software design abilities. To that end, you may use online documentation and resources just as you would in your day-to-day work. This project is designed to be completed within a few hours.

## Project Story

The customer occasionally remembers a few words from a poem they once memorized.  When this happens they'd like help identifying the exact line that they are distantly recalling.  Included in this repository is [lepanto.txt](lepanto.txt), the text of a poem by G.K. Chesterton.  Your task is to write a program that prompts the user to enter the words they remember, then prints the line of the poem which you believe is the most likely match.

Here's what a hypothetical session might look like:

```
$ ./my_solution
>his head a flag
Holding his head up for a flag of all the free.
```

How you implement the "match" model is up to you but be prepared to justify the choices you make.  Assume the user doesn't have perfect recall and will confuse words from different lines on occasion.

## Implementation Notes

* The code can be written in the language of your choice.
* You can use libraries written by others as long as you can explain what they're doing.
* Your solution must run on Debian Buster (linux).  Use Docker if you need to.
* Provide clear instructions for how to compile/run your code, along with any required packages that are not installed by default on Debian Buster.
* If you find these requirements to be ambiguous, go with your best guess and document your decision.

## Submission Process

* Create a repository on Github with your code and email us a link.
* The repository should include a README.md that clearly describes how to compile and run your code.

## Review Criteria
In the code review we'll cover:

* Simplicity (how complicated is your design?)
* Clarity (how easy is it to understand _what_ your code is doing and _why_ it's doing it?)
* Alternatives (what other approaches did you consider? Why didn't you go with one of them?)
* Performance (the poem is not long, your runtime shouldn't be either)
