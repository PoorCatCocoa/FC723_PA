"""
#Pseudocode of the Euclidean Algorithm:

User input: a, b;
While b != 0{		Use the Euclidean Algorithm to find the GCD(a) when b = 0
	r = a % b;
	a = b;
	b = r;
return a;
"""


class EuclideanAlgorithm:		#Trans the pseudocode to python code with OOP
	def __init__(self, a: int, b: int):
		self.a = a
		self.b = b

	def gcd(self):
		if self.a & self.b != 0:		# Make sure all numbers are correct and can be executed
			while self.b != 0:
				r = self.a % self.b
				self.a = self.b
				self.b = r
			return print("The GCD is:", self.a)
		else:
			print("GCD(0,0) is undefined, GCD(a,0) = a, GCD(0,b) = b, Please try again with correct numbers.")

print("Welcome to the Euclidean Algorithm!\n"
	  "You can enter two numbers to find the greatest common divisor(GCD) of them.\n")

print(EuclideanAlgorithm(int(input("Please enter the first number\n")),
						 int(input("Please enter the second number\n"))).gcd())


