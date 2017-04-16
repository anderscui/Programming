# Let's Build a Simple Interpreter

"If you don't know how compilers work, then you don't know how computers work. If you're not 100% sure whether you know how compilers work, then you don't know how they work" - Steve Yegge

# [Part 1](https://ruslanspivak.com/lsbasi-part1/)

## Why to study interpretersf and compilers?

1. To write an interpreter or a compiler you have to have a lot of technical skills that you need to use together. Writing an interpreter or a compiler will help you improve those skills and become a better software developer. As well, the skills you will learn are useful in writing any software, not just interpreters or compilers.
2. You really want to know how computers work. Often interpreters and compilers look like magic. And you shouldn’t be comfortable with that magic. You want to demystify the process of building an interpreter and a compiler, understand how they work, and get in control of things.
3. You want to create your own programming language or domain specific language. If you create one, you will also need to create either an interpreter or a compiler for it.

The goal of an **interpreter** or a **compiler** is to **translate a source program in some high-level language into some other form**. Pretty vague, isn’t it? Just bear with me, later in the series you will learn exactly what the source program is translated into.

This project will create a simple interpreter for a large subset of [Pascal](https://en.wikipedia.org/wiki/Pascal_%28programming_language%29) language.

## Process

In order for the interpreter to actually understand what to do with that string it first needs to break the input "1+2" into components called **tokens**. A token is an object that has a type and value.

The process of breaking the input string into tokens is called **lexical analysis**. The first step of the interpreter is reading the input and convert it into **a stream of tokens**. The part of interpreter is called **lexical analyzer**, or **lexer** for short, other names are **scanner** or **tokenizer**.

A **lexeme** is a sequence of characters that form a token. e.g. 123 is an integer token.

The process of finding the structure in the stream of tokens, or put differently, the process of recognizing a phrase in the stream of tokens is called **parsing**. The part of an interpreter or compiler that performs that job is called a **parser**.





