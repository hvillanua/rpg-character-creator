# RPG Character Creator

This repository exists as a small teaching exercise in how the same program can evolve as someone learns more about software design.

The starting point was a beginner Python program that creates an RPG character by asking for a name, age and class, rolling random statistics, and applying a class-specific bonus. The original program worked largely as one script with repeated branches for each character class.

Rather than replacing it with a complicated architecture immediately, this repository contains two rewrites of the same idea at different levels.

## `simple`

The simple version stays close to beginner Python. It avoids classes and external dependencies while introducing some habits that are useful at any level:

- small functions with one clear responsibility
- descriptive function and variable names
- type hints
- avoiding duplicated logic
- representing repeated rules as data
- separating game logic from terminal input and output
- making randomness controllable so the logic can be tested
- simple tests using `assert`, without a testing framework

The goal is to show that code can become substantially easier to understand and change without requiring advanced language features.

## `professional`

The professional version solves the same problem using tools and structure that would be reasonable in a production Python codebase. It introduces:

- explicit domain models using dataclasses
- enums for constrained domain values
- immutable value objects
- protocols for dependency boundaries
- dependency injection for randomness
- separation between domain, application logic and CLI presentation
- pytest and parameterized tests
- standard Python project configuration

The goal is not to demonstrate the largest or most sophisticated architecture possible. It is to show what stronger modeling, boundaries and automated testing look like when applied proportionally to a very small problem.

## Why keep both?

The two implementations are intended to be read side by side.

The important lesson is not that the professional version is always the correct way to write a small script. The progression matters: first identify responsibilities, remove duplication and separate logic from presentation; then, once the concepts and the size of the program justify it, introduce stronger types, explicit abstractions and dedicated tooling.

Both versions therefore implement essentially the same RPG character creator while optimizing for different stages of learning.
