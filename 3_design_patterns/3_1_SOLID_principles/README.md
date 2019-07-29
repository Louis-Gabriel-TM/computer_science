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

**Illustration:** `srp.py`

**Anti-pattern:** God objects

### Open-Closed Principle

_"A class / module / function / ... should be open for extension [of the behaviors], but closed for modification [of the source code]."_

**_Inheritance_** helps to observe this principle, especially by using **_abstract base classes_**.

**Useful patterns:** Enterprise pattern _Specification_, _Combinator_

**Illustration:** `ocp.py`

### Liskov Substitution Principle

### Interface Segregation Principle

### Dependency Inversion Principle
