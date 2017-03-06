# -*-coding: utf8 -*-

class Config:

	ROOT = ""
	SOURCES = "src/"
	PARSED = "csv/"
	DIST = "dist/"

	@staticmethod
	def root(d):
		d = d.replace("\\", "/")
		part = d.rpartition("/")
		Config.ROOT = part[0] + "/"
		return True