# # This is for singleton. The _instance is only going to be instantiated here and for the first time
# if _instance is already instantiated, it will be returned if not, it will be instantiated via the function.
# the client only called Tigger() function infact not the class. you can think of it as a trick
#
#
#
class _Tigger:
	def __str__(self):
		return "I'm the only one!"
	
	def roar(self):
		return "Grrr!"


_instance = None


def Tigger():
	global _instance
	if _instance is None:
		_instance = _Tigger()
	return _instance
