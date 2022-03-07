import os

TARGET_DIR = 'D:/Таня/КПРС/target_dir'
#for el in os.walk(TARGET_DIR):
#    print(el)
folder = []
p = ''
##for dirs,folders,files in os.walk(TARGET_DIR):
##    print('Выбранный каталог: ', dirs)
##    print('Вложенные папки: ', folders)
##    print('Файлы в папке: ', files)
##    print('\n')
##    folder.append(i)

##for folder in folders:
##    full_path = f'{TARGET_DIR}/{folder}'
##    print(full_path)
##    for dirs,folders,files in os.walk(full_path):
##        print('Файлы в папке: ', files)
       
for i in os.walk(TARGET_DIR):
    if i[2]:
        p += f'{os.path.basename(i[0])}_'
        print(f'Вложенные файлы: {i[2]}\n')
        for file in i[2]:
            print(f'путь: {os.path.split(os.path.abspath(file))[0]}\n')
            if os.path.split(file)[0] != TARGET_DIR:
                new_name = f'{p}{file}'
                print(f'Старое имя файла: {file}, новое - {new_name}\n')
                t = i[0] + '/' + file
                os.rename(t, new_name)
                print('\n')
    if not i[1]:
        p = f''
        





##
##for address, dirs, files in folder:
##    for file in files:
##        print(address+'/'+file)
##        new_name = f'_{file}'
##        print(new_name)
                    #os.rename

##for el in folder:
##    print(el)
##            #os.rename
