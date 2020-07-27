print("Приветствую! Данная программа приобразует количество введенных секунд по принципу чч.мм.сс")
sec_user = int(input("Введите количество секунд"))
hourse = sec_user // 3600
minutes = (sec_user - hourse * 3600) // 60
seconds = sec_user - (hourse * 3600 + minutes * 60)
print(f"Время {hourse} : {minutes} : {seconds}")
