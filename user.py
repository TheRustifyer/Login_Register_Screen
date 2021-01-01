from database import Database

class User:

	want_exit_popup_anymore = False

	def __init__(self):

		self.user_id = None
		self.username = None
		self.password = None

		self.database = Database()

	def is_logged(self):

		if self.username != None:

			return True


	def set_user(self, username, password):

		self.username = username
		self.password = password


	def check_user_in_db(self, reg=False):

		self.database.connect_to_db('database.db')

		query_to_db = f"""

		SELECT * FROM user_data
		WHERE username = '{self.username}'
		"""


		if reg:

			query_to_db += f" AND password = '{self.password}'"

		data = self.database.get_data(query_to_db)

		self.database.close_connection()

		return data

	def new_user(self):

		self.database.connect_to_db('database.db')
		
		self.user_id = self.database.insert('user_data', 
			['username', 'password'], [self.username, self.password])

		self.database.close_connection()
