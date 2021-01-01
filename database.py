import sqlite3

class Database:
	
	def __init__(self):
	
		self.db_con = None
		
		self.cursor = None

		self.connect_to_db('database.db')
	

		create_user_data = '''
		CREATE TABLE IF NOT EXISTS user_data (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				username text NOT NULL,
				password text NOT NULL
		)
		'''
		
		self.query(create_user_data)
		self.save_data()
		self.close_connection()

	def connect_to_db(self, db_file):

		try:

			self.db_con = sqlite3.connect(db_file)
			self.cursor = self.db_con.cursor()

		except sqlite3.Error as e:

			raise e

	def close_connection(self):
		
		try:

			self.db_con.close()

		except sqlite3.Error as e:

			raise e

	def query(self, query):
		
		try:
			self.cursor.execute(query)

		except sqlite3.Error as e:

			raise e

	def get_data(self, query, mode='all'):

		try:

			self.cursor.execute(query)
			
			if mode == 'single':
				
				return self.cursor.fetchone()
			
			elif mode == 'all':
				
				return self.cursor.fetchall()
			
			else:
				
				raise Exception("Bad mode argument")

		except sqlite3.Error as e:

			raise e

	def insert(self, table, columns, data):

		try:
			

			columns = ','.join([f"{column_name}" for column_name in columns])
			
			data = ','.join([f"'{value}'" for value in data])

			query = f"INSERT INTO {table} ({columns}) VALUES({data});"

			self.query(query)
			
			self.save_data()

			user_id = self.cursor.lastrowid

			return user_id

		except sqlite3.Error as e:

			raise e


	def save_data(self):

		self.db_con.commit()
