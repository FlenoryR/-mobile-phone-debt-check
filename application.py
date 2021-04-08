def create_object_handler():
    my_object = {}

    with open('my_file.txt') as my_file:
        content = my_file.read()

        for number in content.split('\n'):
            number, sum = number.split(',')
            
            if number in my_object:
                my_object[number] += int(sum)
            else:
                my_object[number] = int(sum)

    return my_object

def main():
    my_object = create_object_handler()
    input_phone_number = input('Введите номер мобильного телефона: ')

    if input_phone_number in my_object:
        print(f'Номер мобильного телефона: {input_phone_number}. Сумма: {my_object[input_phone_number]}.')
    else:
        print('Данный мобильный телефон отсутствует.')

if __name__ == '__main__':
    main()
    
