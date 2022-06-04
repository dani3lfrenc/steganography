

# © Daniel Franchini


# Siple program to write and see "hide" message inside images

# !!!ALLERT!!! For now the program work right only with JPEG image extension. 

# You can see hidden message in PNG file for example but the terminal send for the output all the code and the message is at the end


def writemessage():

	MESSAGGIO = input("\nMessage to hide: ")

	PATH = input("\nPath of the image: ")

	with open(PATH, 'ab') as f:

		my_str_as_bytes = str.encode(MESSAGGIO)

		f.write(my_str_as_bytes)

	print("\nOperation completed...")

	main()





def seemessage():

	PATH = input("\nPath of the image: ")

	with open(PATH, 'rb') as f:

		content = f.read()

		offset = content.index(bytes.fromhex('FFD9'))

		f.seek(offset + 2)

		print(f.read())

	main()


def main():

	choice = input("Welcome, would you like to write a hidden message or read it?: \n\nWrite (1) for write\n\nWrite (2) for see\n\nWrite (3) for exit\n\nYour choise: ")

	if choice == "1":

		writemessage()

	elif choice == "2":

		seemessage()

	elif choice == "3":

		print("\nThank you, bye!!!")


main()

