## **What is Inheritance?**

Inheritance is a mechanism in object-oriented programming (OOP) that allows one class to inherit the properties and behavior of another class. The inheriting class, also known as the child or subclass, inherits all the
attributes and methods of the parent or superclass.

## **Types of Inheritance:**

### 1. **Single Inheritance**

- A child class inherits from a single parent class.
- The child class inherits all the attributes and methods of the parent class.

Example:

```markdown
class Parent:
def **init**(self):
self.parent_attribute = "I'm the parent"

class Child(Parent):
pass # The child class inherits all the attributes and methods from the parent class

# Output: I'm the parent (attribute inherited from parent)
```

### 2. **Multiple Inheritance**

- A child class inherits from more than one parent class.
- The child class inherits all the attributes and methods of both parent classes.

Example:

```markdown
class Parent1:
def **init**(self):
self.parent1_attribute = "I'm parent 1"

class Parent2:
def **init**(self):
self.parent2_attribute = "I'm parent 2"

class Child(Parent1, Parent2):
pass # The child class inherits all the attributes and methods from both parents

# Output: I'm parent 1 (attribute inherited from Parent1)

# I'm parent 2 (attribute inherited from Parent2)
```

### 3. **Multilevel Inheritance**

- A grandchild class inherits from a grandparent class, which in turn inherits from another class.
- The grandchild class inherits all the attributes and methods of both grandparents.

Example:

```markdown
class Grandparent:
def **init**(self):
self.grandparent_attribute = "I'm the grandparent"

class Parent(Grandparent):
def **init**(self):
super().**init**() # Inheriting from the grandparent class

class Child(Parent):
pass # The child class inherits all the attributes and methods from both grandparents

# Output: I'm the grandparent (attribute inherited from Grandparent)
```

### 4. **Hierarchical Inheritance**

- Multiple child classes inherit from a single parent class.
- Each child class inherits the attributes and methods of the parent class.

Example:

```markdown
class Parent:
def **init**(self):
self.parent_attribute = "I'm the parent"

class Child1(Parent):
pass # The first child class inherits all the attributes and methods from the parent

class Child2(Parent):
pass # The second child class inherits all the attributes and methods from the parent
```

### 5. **Hybrid Inheritance**

- A combination of two or more types of inheritance.
- A class inherits from another class, which itself inherits from another class.

Example:

```markdown
class Parent1:
def **init**(self):
self.parent1_attribute = "I'm parent 1"

class Parent2(Parent1): # Parent2 inherits from Parent1
pass

class Child(Parent2): # The child class inherits all the attributes and methods from Parent1, via Parent2
pass

# Output: I'm parent 1 (attribute inherited from Parent1)
```

**Key Takeaways:**

- Inheritance allows one class to inherit the properties and behavior of another class.
- There are five types of inheritance: single inheritance, multiple inheritance, multilevel inheritance, hierarchical inheritance, and hybrid inheritance.
