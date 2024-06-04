std=['아이유', '폴킴', '황인욱']

std.append('청하')
print(f"(1)=> {std}")
std.insert(2, '폴킴')
print(f"(2)=> {std}")
print(f"(3)=> {std.count('폴킴')}")
std.remove('황인욱')
print(f"(4)=> {std}")
std[1:2]=[]
print(f"(5)=> {std}")
std.sort(reverse=True)
print(f"(6)=> {std}")
