"""

================================================================
Python OOP Concepts : Inheritance

=================================================================

Inheritance -->
Inheritance allows one class [child/derived class]
to accquire the properties and methods of another class
[parent /base class]

It promotes code reuseability and modular design.

Why use Inheritance ?
1. Avoids code duplication
2. Promotes reuseability and maintainability
3. Helps in designing real-world models

Types of Inheritance in Python
-----------------------------------------------------------------

1. Single Inheritance - One child inherits from one parent.
2. Multiple Inheritance - One Child inherits from multiple parents.
3. Multilevel Inheritance - A chain of inheritance (child -> Parent -> Grandparent)
4. Hierarchical Inheritance - Multiple Children inherit from one parent.
5. Hybrid INHERITANCE - Combination of different inheritance types.

Python uses Method Resolution Order [MRO] to decide which parent's 
method to call in multiple inheritance.

Check MRO using : print(ClassName.mro())

=============================================================================

"""

#====================================================
#1. Single Inheritance
#==============================================================

print("\n ------------------- Single Inheritance Examples ----------------------")

# Example 1 : Animal -> Dog
class Animal:
    # parent method
    def speak(self):
        print("Animals can make sound")
        

class Dog(Animal):  #dog inherits from animal
    # child method
    def bark(self):
        print('Dog barks! Woof! Woof!')
        

dog = Dog()
dog.speak()   # inherited from Animal
dog.bark()


# 2. Multiple Inheritance
print("\n Multiple Inheritance Examples")

# Example 1 : Father + Mother -> Child
class Father:
    def skill(self):
        print("Father : Knows Driving")
        
class Mother:
    def talent(self):
        print("Mother knows Cooking")
        
class Child(Mother,Father):
    def hobby(self):
        print('Child Loves Painting')
        
        
c = Child()
c.hobby()
c.talent()
c.skill()

# ==================================================
# 3. MULTILEVEL INHERITANCE
# ==================================================
print("\n--- Multilevel Inheritance Examples ---")

# Example 1 : Grandparent -> Parent -> Child
class Grandparent:
    def legacy(self):
        print('Grandparent : Passes traditions')
        
class Parent(Grandparent):
    def responsibility(self):
        print('Parent: Takes care of children')
        
class Child(Parent):
    def learn(self):
        print('Child: Learns from elders')
        
        
c = Child()
c.learn()
c.responsibility()
c.legacy()

# ==================================================
# 4. HIERARCHICAL INHERITANCE
# ==================================================
print("\n -- Hierarchial Inheritance Examples:")

# Example 1 - Parent -> Child1 ,Child 2
class Parent:
    def guide(self):
        print("Parent guides Children")
        
class Child1(Parent):
    def play(self):
        print('Child1 is playing')
        
class Child2(Parent):
    def study(self):
        print('Child 2 is Studying')
        
c1 = Child1()
c2 = Child2()
c1.guide();c2.guide()
c1.play();c2.study()

# ==================================================
# 5. HYBRID INHERITANCE
# ==================================================
print("\n--- Hybrid Inheritance Examples ---")

# Example 1 : Multiple + Hierarchical 
class A:
    def featureA(self):
        print('Feature A')
        
class B(A):
    def featureB(self):
        print('Feature B')

class C(A):
    def featureC(self):
        print('Feature C')
        
class D(B,C):
    def featureD(self):
        print('Feature D')
        
d= D()
d.featureA()
d.featureB()
d.featureC()
d.featureD()

        
        
        
        
        
        
        
        
        