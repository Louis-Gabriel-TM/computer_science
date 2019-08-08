# Problem Solving Techniques

## Problem Solving in 5 steps

#### 1. Understand the Problem

Some questions to consider first:

- Can I restate the problem?
- What are the inputs? their types? their boundaries?
- What outputs should come from the solution?
- Have I enough informations to solve the problem?
- How should I label the data that are parts of the problem?

#### 2. Explore Concrete Examples

- Start with simple examples.
- Progress to more complex examples.
- Explore extreme examples like empty inputs.
- Explore examples with invalid inputs (particularly important in real project, to build a robust solution).

#### 3. Break It Down

- Explicitly write out the steps you need to take.
- You don't have to write a full pseudo-code, the purpose is to think about a the code before writing it.
- If you run out of time, you'll have at less a global view of the solution. It's particularly relevant in the case of a coding interview.

#### 4. Solve or Simplify

Solve the problem but, if you can't, solve a simpler version of the problem first.

To simplify:

- find the core difficulty,
- temporarily ignore that difficulty,
- write a simplified solution,
- then incorporate that difficulty back in.

In most case, solving the simpler problem helps dealing with the core difficulty.

#### 5. Look Back and Refactor

Some refactoring questions:

- can you check the result?
- can you obtain the result differently?
- can you understand the code at a glance?
- can you improve the performance of the solution?
- can you reuse the method for some other problem?
- how have other people solved this problem?

## Problem Solving Patterns

#### "Frequency Counter" Pattern

Using objects (JS), dictionaries or sets to collect frequencies of some values.

It often avoid nested loops or others O(n\*\*2) operations with arrays or strings.

**Examples:**

- `same_frequencies.js` | `same_frequencies.py`
- `no_repeat_char.py`
- `anagrams.js`(with one or two counters)
- `common_elements.py` (with sets)
- `most_frequent.py` (with a set or a counter)

#### "Multiples Pointers" Pattern

#### "Sliding Window" Pattern

#### "Divide and Conquer" Pattern

#### Dynamic Programming

#### Greedy Algorithms

#### Backtracking

## For Coding Interviews

##### _"Think like on paper"_

Before coding, imagine **how you may solve the problem on paper**. In the given case and in **extended cases** (bigger input, extreme inputs, ...).

Then think about **the right data structure** to use.

##### _"Big picture first, then details"_

Consider and explicit the main sub-problems or steps before going into details.

##### _"Communicate well with the interviewer"_

Verbalize your reflexions during the interview and ask for help if necessary.
