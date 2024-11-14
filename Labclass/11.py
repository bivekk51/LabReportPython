class GrandParent:
    def grandparent_method(self):
        print("This is budo class")
class Parent(GrandParent):
    def parent_method(self):
        print("This is mature class")
class Child(Parent):
    def child_method(self):
        print("This is baccha class")
child1=Child()
child1.grandparent_method()
child1.parent_method()
child1.child_method()