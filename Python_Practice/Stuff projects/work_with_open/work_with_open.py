

def main():
    with open(r'C:\Gregory\Coding\Python Practice\Stuff projects\work_with_open\file_to_read.txt',
            'r', encoding="UTF-8") as f:
        text = f.read()
        key_to_find = 'Имя клиента:'
        foundet_index = text.find(key_to_find)
        a = text[foundet_index+len(key_to_find) : foundet_index+50].split('.')
        name = a[0].strip()
        text = text.replace(name, 'Григорий')
        f.close()
        print(name)

    with open(r'C:\Gregory\Coding\Python Practice\Stuff projects\work_with_open\file_to_read.txt',
            'w', encoding="UTF-8") as f:    
        f.write(text)
        f.close


def start():
    main()

if __name__ == "__main__":
    start()
