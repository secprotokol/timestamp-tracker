import os, time, sys, shutil
from prettytable import PrettyTable
from datetime import datetime
import zipfile
from random import randint
data_result_table = []

def show_mac(file_name):
    modify_time = os.path.getmtime(file_name)
    access_time = os.path.getatime(file_name)
    create_time = os.path.getctime(file_name)
    modify_time_d = datetime.fromtimestamp(modify_time).strftime('%Y-%m-%d %H:%M:%S')
    access_time_d = datetime.fromtimestamp(access_time).strftime('%Y-%m-%d %H:%M:%S')
    create_time_d = datetime.fromtimestamp(create_time).strftime('%Y-%m-%d %H:%M:%S')
    response = f"""M: {modify_time_d} -> ({modify_time}) 
A: {access_time_d} -> ({access_time}) 
C: {create_time_d} -> ({create_time})"""
    return response

def create_file(file_name):
    if os.path.exists(file_name):
        print(f"(!) File {file_name} sudah ada")
        new_data_table = {"action": "File original", "mac": show_mac(file_name)}
        data_result_table.append(new_data_table)
        rant = randint(1, 4)
        print(f"(!) Jeda {rant} detik....")
        time.sleep(int(rant))
    else:
        with open(file_name, 'w') as file:
            datenow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"File baru.\nFile ini dibuat pada {datenow}")
        print(f"(-) Membuat file {file_name}")
        new_data_table = {"action": "Membuat file", "mac": show_mac(file_name)}
        data_result_table.append(new_data_table)
        rant = randint(1, 4)
        print(f"(!) Jeda {rant} detik....")
        time.sleep(int(rant))

def copy(file_name):
    copy_file = "copy_"+file_name
    shutil.copy2(file_name, copy_file)
    print(f"(-) Copy file {file_name} ke dir sama")
    new_data_table = {"action": "Copy file ke dir yang sama", "mac": show_mac(copy_file)}    
    data_result_table.append(new_data_table)
    rant = randint(1, 4)
    print(f"(!) Jeda {rant} detik....")
    time.sleep(int(rant))
    #---------------------------------------
    shutil.copy2(file_name, "dir_copy/"+copy_file)
    print(f"(-) Copy file {file_name} ke dir dir_copy/{copy_file}")
    new_data_table = {"action": f"Copy file ke dir dir_copy/{copy_file}", "mac": show_mac("dir_copy/"+copy_file)}    
    data_result_table.append(new_data_table)
    rant = randint(1, 4)
    print(f"(!) Jeda {rant} detik....")
    time.sleep(int(rant))

def modify(file_name):
    with open(file_name, 'a') as file:
        file.write("Tambah data baru....\nhmmmmmmmmm" + '\n')
    print(f"(-) Modifikasi file {file_name} (menambah text)")
    new_data_table = {"action": f"Modifikasi file {file_name} (menambah text)", "mac": show_mac(file_name)}    
    data_result_table.append(new_data_table)
    rant = randint(1, 4)
    print(f"(!) Jeda {rant} detik....")
    time.sleep(int(rant))
    with open(file_name, 'r+') as f:
        lines = f.readlines()
        if len(lines) > 0:
            f.seek(0)
            f.writelines(lines[:-1])
            f.truncate()
    print(f"(-) Modifikasi file {file_name} (menghapus text)")
    new_data_table = {"action": f"Modifikasi file {file_name} (menghapus text)", "mac": show_mac(file_name)}    
    data_result_table.append(new_data_table)
    rant = randint(1, 4)
    print(f"(!) Jeda {rant} detik....")
    time.sleep(int(rant))

def rename(file_name):
    os.rename(file_name, 'baru_'+file_name)
    print(f"(-) Rename file {file_name} menjadi baru_{file_name}")
    new_data_table = {"action": f"Rename file {file_name} menjadi baru_{file_name}", "mac": show_mac('baru_'+file_name)}    
    data_result_table.append(new_data_table)
    rant = randint(1, 4)
    print(f"(!) Jeda {rant} detik....")
    time.sleep(int(rant))
    return 'baru_'+file_name

def change_ext(file_name):
    base = os.path.splitext(file_name)[0]
    new_file = base + '.pdf'
    os.rename(file_name, new_file)
    print(f"(-) Rubah ekstensi file {file_name} menjadi {new_file}")
    new_data_table = {"action": f"Rubah ekstensi file {file_name} menjadi {new_file}", "mac": show_mac(new_file)}    
    data_result_table.append(new_data_table)
    rant = randint(1, 4)
    print(f"(!) Jeda {rant} detik....")
    time.sleep(int(rant))
    return new_file

def compress(file_name):
    base = os.path.splitext(file_name)[0]
    with zipfile.ZipFile(base+'.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        if os.path.isfile(file_name):
            zipf.write(file_name, os.path.basename(file_name))
    print(f"(-) Kompresi file {file_name} menjadi {base}.zip")
    new_data_table = {"action": f"Kompresi file {file_name} menjadi {base}.zip", "mac": show_mac(base+'.zip')}    
    data_result_table.append(new_data_table)
    rant = randint(1, 4)
    print(f"(!) Jeda {rant} detik....")
    time.sleep(int(rant))
    with zipfile.ZipFile(base+'.zip', 'r') as zipf:
        os.makedirs('hasil_compress_file', exist_ok=True)
        zipf.extractall('hasil_compress_file')
    print(f"(-) Ekstraksi file {base}.zip")
    new_data_table = {"action": f"Ekstraksi file {base}.zip", "mac": show_mac('hasil_compress_file/'+file_name)}    
    data_result_table.append(new_data_table)
    rant = randint(1, 4)
    print(f"(!) Jeda {rant} detik....")
    time.sleep(int(rant))

def show_table(data):
    table = PrettyTable()
    table.field_names = ["No", "Tindakan", "MAC"]
    table.align = "l"
    table.hrules = True
    for index, entry in enumerate(data, start=1):
        table.add_row([index, entry["action"], entry["mac"]])
    print(table)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python timestamp.py <nama_file>")
        sys.exit(1)

    file_name = sys.argv[1]
    create_file(file_name)
    copy(file_name)
    modify(file_name)
    file_name_new = rename(file_name)
    file_name_new = change_ext(file_name_new)
    compress(file_name_new)
    show_table(data_result_table)

