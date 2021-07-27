import datetime


class Database:
	
	entries = []

	def add_todo_db(self, todo):
		self.entries.append(todo)
		print("\nჩანაწერი წარმატებით დამატებულია!")


	def edit_todo_db(self, position, newTodo):
		self.entries[position] = newTodo
		print("\nჩანაწერი წარმატებით შეცვლილია!")


	def delete_todo_db(self, position):
		self.entries.pop(position)
		print("\nჩანაწერი წარმატებით ამოშლილია!")


	def show_all_db(self):
		return self.entries


class Todo:
	
	def __init__(self, text):
		self.text = text
		self.date = datetime.datetime.now()


	def __str__(self):
		return f'Date: {self.date.strftime("%d/%m/%Y %H:%M")}\nTodo: {self.text}'


class Manager:
	
	def __init__(self, db):
		self.database = db


	def add_todo(self, todo):
		self.database.add_todo_db(todo)


	def edit_todo(self, position, newTodo):
		self.database.edit_todo_db(position, newTodo)


	def delete_todo(self, position):
		self.database.delete_todo_db(position)


	def count_todo(self):
		return len(self.database.show_all_db())


	def show_all(self):
		data = self.database.show_all_db()

		for index, item in enumerate(data, 1):
			print("-" * 25 + str(index) + "-" * 25)
			print(item)
			print("-" * 51)


def user_input(manager):

	while True:
		position = input("აირჩიეთ ჩანაწერი ჩასანაცვლებლად: ")

		if not position.isdigit():
			print("გთხოვთ შეიტანოთ რიცხვი!")
			continue

		if int(position) > manager.count_todo() or int(position) < 0:
			print("გთხოვთ აირჩიოთ დადებითი მნიშვნელობა დიაპაზონში")
			continue

		position = int(position) - 1
		break

	return position




def menu():
	
	choice = None

	db = Database()
	manager = Manager(db)


	while choice != "exit":
		print("\nToDo პროგრამის მენიუ:")
		print("1. ToDo-ს დამატება")
		print("2. ToDo-ს რედაქტირება")
		print("3. ToDo-ს ამოშლა")
		print("4. ჩანაწერების ჩვენება")
		print("პროგრამიდან გამოსასვლელად აკრიფეთ 'exit'")

		choice = input("\nაირჩიეთ მოქმედება: ")


		if choice == "1":
			
			text = input("შეიყვანეთ ტექსტი ToDo-სთვის: ")
			todo = Todo(text)

			manager.add_todo(todo)


		elif choice == "2":
			
			if manager.count_todo():
				manager.show_all()

				position = user_input(manager)

				newText = input("შეიტანეთ ახალი ტექსტი: ")
				newTodo = Todo(newText)

				manager.edit_todo(position, newTodo)


			else:
				print("ბაზაში ჩანაწერები ვერ მოიძებნა")


		elif choice == "3":
			
			if manager.count_todo():
				manager.show_all()

				position = user_input(manager)

				manager.delete_todo(position)


			else:
				print("ჩანაწერები ამოსაშლელად ვერ მოიძებნება")


		elif choice == "4":
			manager.show_all()

		else:
			print("გთხოვთ სწორად აირჩიოთ მენიუს პუნქტი!")		



menu()