import json
import phon_book

# # task 01


with open('my_file.txt', 'r+') as file1:
    # file.write("Hello file world!")
    file1 = file1.readlines()
print(list(file1))


# task 02


def phonebook():
    with open('phone_numbers.json', 'r') as file:
        data = json.load(file)
        print('phonebook:', data)

        while True:
            user = input('enter the command: search by (name), (number) or '
                         '(city).work with contacts: (del), (edit) or (add). '
                         'output = q :')

            if user == 'q':
                break
            if user == 'name':
                phon_book.serch_name()
            elif user == 'number':
                phon_book.serch_number()
            elif user == 'city':
                phon_book.serch_city()
            elif user == 'add':
                phon_book.add_contact()
            elif user == 'del':
                phon_book.del_contact()
            elif user == 'edit':
                phon_book.edit_contact()
            else:
                print('wrong command')


phonebook()
