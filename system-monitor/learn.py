import os
mem = "MemTotal:"
memfree = "MemFree:"

with open('/proc/meminfo', 'r') as f:
    for line in f:
        if line.startswith(mem):
            parts_mem = line.split()
            memory = int(parts_mem[1])
        if line.startswith(memfree):
            parts_memfree = line.split()
            memory_free = int(parts_memfree[1])
with open('/proc/swaps', 'r') as f:
    for line in f:
        if line.startswith('/dev/'):
            parts_swap = line.split()
            swap_size = int(parts_swap[2])
            swap_used = int(parts_swap[3])
print('==Memory==')
print(f'Всего: {memory / 1024:.2f}MB')
print(f'Свободно: {memory_free / 1024:.2f}MB')
print('==Swap==')
print(f'Всего: {swap_size / 1024:.2f}MB')
print(f'Использовано: {swap_used / 1024:.2f}MB')
if memory_free / 1024 < 1000:
    check_procces = input("Слишком мало памяти! Хотите посмотреть процессы, которые едят много памяти?(y-yes, n-no): ")
    if check_procces == 'y':
        process = []
        for pid in os.listdir('/proc'):
            if not pid.isdigit():
                continue
            try:
                with open(f'/proc/{pid}/status', 'r') as f:
                    for line in f:
                        if line.startswith('VmRSS:'):
                            parts_process_mem = line.split()
                            memory_use_proc = int(parts_process_mem[1]) / 1024
                        if line.startswith('Name:'):
                            parts_process_name = line.split()
                            name_process = parts_process_name[1]
                    if memory_use_proc > 0:
                        process.append((name_process, memory_use_proc))
            except (FileNotFoundError, ProcessLookupError):
                continue
        process.sort(key=lambda x: x[1], reverse=True)
        return_process = process[:7]
        print('==Большие процессы==')
        for proc in return_process:
            if proc != []:
                print(f'Имя: {proc[0]}')
                print(f'Заняло памяти: {proc[1]}')
