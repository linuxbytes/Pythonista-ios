class SecretString:
	"""
	A not-at-all secure way to store a secret string
	"""
	def __init__(self, plain_string,pass_phrase):
		self.__plain_string = plain_string
		self.__pass_phrase = pass_phrase
	
	def decrypt(self, pass_phase):
		"""
		Only show the string if the pass_pharse is correct
		"""
		if pass_phase == self.__pass_phrase:
			return self.__plain_string
			
		else:
			return ""
			


secret_string = SecretString("ACME: Top Secret", "antwerp")

print(secret_string.decrypt("antwerp"))

#print(secret_string.__plain_string)

print(secret_string._SecretString__plain_string)
