import discord
from discord.utils import get
from discord.ext.commands import has_permissions
import json

class User:
	def __init__(self, id):
		self.id = id
		self.found = []
		self.score = 1
		self.rank = 999
		self.accesses = []


	#Décorateurs
		
	#Vérifie si un membre accès à une énigme
	def verif_access(e_number):
		def decorator_1(func):
			def wrapper_1():
				
				if e_number in everyone_access :
						return func()
				
				if e_number in self.access :
					return func()
				
			return wrapper_1
		return decorator_1

		
	#Getter et Setter

	#id
	@property
	def id(self):
		return self.id

	@id.setter
	def id(self, new_id):
		self.id = new_id
		print("L'id est désormais " + id)


	#found
	@property
	def found(self):
		return self.found

	@found.setter
	@verif_access
	def found(self, new_found):
		if new_found in self.found :
			print("Vous avez déjà trouvé la réponse à cette énigme")
		else :
		 self.found.append(new_found)


	#score
	@property
	def score(self):
		return self.score

	#A FAIRE APRES ENIGMES
	@score.setter
	def score(self):
		pass


	#rank
		#A FAIRE APRES LESYSTEME DE RANK
	@property
	def rank(self):
		pass

	@rank.setter
	def rank(self, new_rank):
		self.rank = new_rank
		print("Nouvelle place de l'utilisateur : " + self.rank)
		return self.rank

	
	#accesses
	@property
	def accesses(self) :
		return self.accesses

	@accesses.setter
	def accesses(self, new_access):
		if new_access in self.accesses :
			print("L'utilisateur avait déjà accès à lénigme n°" + new_access)
		
		else :
			self.accesses.append(new_access)
			print("L'utilisateur a désormais accès à l'énigme n°" + new_acccess)
			return self.accesses




#Changer la position d'un élément dans une liste ; la nouvelle position doit être donnée en partant de 1
def set_pos_in_list(list, new_position, element):
	def decorator_2(func):
		def wrapper_2():
			enigmas.remove(element)
				if len(enigmas) < new_number :
					enigmas.append(element)
		
				else :
					enigmas[new_number:] = enigmas[new_number - 1:]
					enigmas[new_number - 1] = element
				return func()
		return wrapper_2
	return decorator_2




class Enigma:
	def __init__(self, name, difficulty, statement, answer, explanation):
		self.name = name
		enigmas.append(self)
		self.number = len(enigmas) + 1
		self.difficulty = difficulty
		self.statement = statement
		self.answer = answer
		self.explanations = expalantions


		#Décorateurs


		#Getter et Setter
		
		#name
		@property
		def name(self):
			return self.name

		@name.setter
		def name(self, new_name):
			self.name = new_name
			print("Le nom a été changé en " + self.name)
			return self.name


		#number
		@property
		def number(self):
			self.number = enigmas.index(self)
			return self.number

		@number.setter
		@set_pos_in_list
		def number(enigmas, new_number, self):
			
		
		




enigmas = []
everyone_access = []
