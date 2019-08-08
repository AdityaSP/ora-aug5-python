
class A():
	def f1(self):
		print("From A")
class B(A):
	def f1(self):
		print("From B")
    pass
class C(A):
	def f1(self):
		print("From C")
    pass
class D(B, C):
    pass
        
objb = B()
objb.f1() #---> From B
objc = C()
objc.f1() #---> From C
objd = D()
objd.f1() #--->? error/FromB/FromC/FromA Ans: FromB

# Linearization of Multi Derived Classes
# Method Resolution Order
print(D.mro())

