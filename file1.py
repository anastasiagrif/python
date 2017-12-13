#Python- - язык с динамической типизацией. Тип переменной определяется в ходе работы с ней, ее значением
import os #подключение модуля - взаимодействие с операционной системой пользователя
import psutil # модуль, взаимодействующий с процессами, запущенными на компьютере пользователя 
import sys #доступ к переменным и функциям, взаимодействующим с интерпретатором python
import shutil

os.chdir("C:\\Users\\Анастасия\\Desktop\\python") #смена текуще директории
print("Текущая директория: ", os.getcwd())    # название текущей директории

print("My first program")
print("Hello word")
name = input("Your name:") #переменная name
print(name, ", welcome in Python")

answer = ""
while answer != 'q':
	answer = input("Давайте порабатаем? (Y/N/q)")

	if answer == "Y":
		print("Что Вы хотите? Вывести файлы - 1, вывести информацию о системе - 2, узнать id процесссов, запущенных на компьютере - 3, дублировать файлы в текущей директории - 4, удаление файлов в текущей директории - 5")
		reply =  int(input("Выберите действие: ")) # int преобразует строковые данные в числовые
		
		if reply == 1:
			print(os.listdir())
			
		elif reply == 2:
			print("Имя операционной системы:")
			print(os.name)
			print("Информация об операционной системы:")
			print(sys.platform)
			print("Кодировка файловой системы:") 
			print(sys.getfilesystemencoding())
			print("Имя пользователя:")
			print(os.getlogin())
			print("Имя текущей директории:") 
			print(os.getcwd())
			print("Список файлов и директорий в папке:")
			print(os.listdir())
			print("Статистика использования системной памяти:") 
			print(psutil.virtual_memory())
		elif reply == 3:
			print(psutil.pids())
	
		elif reply == 4:
			print("Дублирование файлов в текущей директории = ") 
			file_list = os.listdir()
			i = 0     
			# переменная i - счетчик цикла
			
			while i < len(file_list):
				new_file  = file_list[i] + '.dupl'
				print(file_list[i] + " -> " + new_file) # выводит названия новых, продублированных файлов
				shutil.copy(file_list[i], new_file)
				i += 1
		elif reply == 5:
			print("Удаление файлов в текущей директории = ") 
			file_list = os.listdir()
			i = 0     
			# переменная i - счетчик цикла
			
			while i < len(file_list):
				if file_list[i].endswith('.dupl'):     #endswith('.dupl')- оканчивающиеся на ('')
					print("Delete: " + file_list[i])
					os.remove(file_list[i])
				i += 1		
		else:
			print("До свидания!")
			
	elif answer == "N":
		print("GoodBye")
	else: 
		print("Неизвестный ответ")
		print("Уточните, пожалуйста")
	
	
	


"""if условие истинности:
	действия при истинности
elif дополнительное условие:
	действия при дополнительном условии
else:
	действия при неистинности
pass пустое действие """

"""if answer == "Y":
	print("Вам премия!")
elif answer == "N":
	print("GoodBye")
else: 
	print("Неизвестный ответ")"""
	
""" while условие работы:
	тело цикла """
	
# Функция type выводит информацию о типе переменной (объекта)
# Функция dir показывает внутреннее содержимое переменной (объекта) - атрибуты, методы
# Функция help выводит встронную справку об объекте
	