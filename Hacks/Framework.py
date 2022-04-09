class Hack:
	def __init__(self):
		self.apply=None
		self.init=None
		self.test=None
		self.priority=0

	def hack(self,called):
		self.apply=called

	def initialiser(self,called):
		self.init=called

	def condition(self,called):
		self.test=called

class SimpleHack(Hack):
	def __init__(self,cmd,cmdhelp,negated=False):
		super().__init__()
		self.cmd=cmd
		self.cmdhelp=cmdhelp
		self.negated=negated

		@self.initialiser
		def addArg(self,parser):
			parser.add_argument("--"+self.cmd, help=cmdhelp,action="store_true")

		@self.condition
		def isArg(self,args):
			attr=getattr(args,self.cmd.replace("-","_"))
			return not attr if self.negated else attr

class Hacks:
	def __init__(self):
		self.hacks=[]

	def addHack(self,toAdd):
		self.hacks.append(toAdd)

hacks=Hacks()