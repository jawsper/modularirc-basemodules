from modularirc import BaseModule


class Module(BaseModule):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs, has_commands=False)