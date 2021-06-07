import drop_to_cloud as dtc
import crypto as crp
import decrypt as decrp
import dropbox

Token = "jwqEoop4M6IAAAAAAAAAATqRP_UhTzJ2nk6QYRopYpwcg0ncnKbTE8cnwhwjUbb1"

dbx = dropbox.Dropbox(Token)

print("Программа успешно запущена!")

while(True):
	print("Выбирите действие:")
	print("[1] - Зашифровать и закинуть в облако")
	print("[2] - Скачать и дешифровать")
	print("[0] - Завершить программу\n")
	
	a = int(input("Ввод: "))

	if a == 0:
		break
	if a == 1:
		file_name = input("Введите название файла с расширением(Например: file.txt) ")
		loc = f"/Приложения/FOLDER_PYTHON_BACKUP/{file_name}"

		crp.encryption(file_name, input("Введите уникальной код для шифрования "))
		
		new_name = str(file_name) + "(Зашифрованный)"

		dtc.upload_file(dbx,loc,new_name)
	elif a == 2:
		file_name = input("Введите название файла с расширением(Например: file.txt) ")
		loc = f"/Приложения/FOLDER_PYTHON_BACKUP/{file_name}"

		dtc.download_file(dbx,loc,file_name)

		decrp.decryption(file_name, input("Введите уникальной код для шифрования "))