class Point:
	"Represents a pointin two-dimensional geometirc coordinates"
	def __init__(self, x, y):
		"""
		In intialize the postion of a new point.
		The x and y coordinates can be specified. if they
		are not, point defaults to the origins.
		"""
		self.move(x, y)

	def move(self, x, y):
		self.x = x
		self.y = y

	def reset(self):
		self.move(0, 0)
	
	def calculate_distance(self, other_point):	
		"""
		Calculate thr distance
		"""	
#	Contructing a Point

point = Point(3, 5)

print(point.x, point.y)

