# The SOLID Principles

Five design principles brought out by Robert C. Martin (aka "Uncle Bob") in 2000:

- **S**ingle Responsibility Principle

- **O**pen-Closed Principle

- **L**iskov Substitution Principle

- **I**nterface Segregation Principle

- **D**ependency Inversion Principle

### Single Responsibility Principle (SRP)

_"A class should have only one reason to be changed / rewritten."_

A class should have one unique responsibility.

Similar to the **_Separation of Concerns (SOC)_** principle.

**Example:** `srp.py`

**Anti-pattern:** _God objects_

### Open-Closed Principle (OCP)

_"A class / module / function / ... should be open for extension [of the behaviors], but closed for modification [of the source code]."_

**_Inheritance_** helps to observe this principle, especially by using **_abstract base classes_**.

**Useful patterns:** Enterprise pattern _Specification_, _Combinator_

**Example:** `ocp.py`

### Liskov Substitution Principle

_"Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program."_

**Useful patterns:** _Factory_

**Example:** `lsp.py`

### Interface Segregation Principle

### Dependency Inversion Principle
