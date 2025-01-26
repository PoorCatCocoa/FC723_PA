"""
#Pseudocode of the Euclidean Algorithm:

User input: a, b;
While b != 0{		Use the Euclidean Algorithm to find the GCD(a) when b = 0
	r = a % b;
	a = b;
	b = r;
}
return a;
"""

class EuclideanAlgorithm:		#Trans the pseudocode to python code with OOP
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def gcd(self):
		while self.b != 0:
			r = self.a % self.b
			self.a = self.b
			self.b = r
		return self.a

a = EuclideanAlgorithm(12, 15)
print(a.gcd())