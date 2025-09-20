print('==== BONUS KARYAWAN ====')

nama_karyawan = input('Nama karyawan : ')
lama_bekerja = int(input('Lama bekerja : '))
performa = int(input('Performa : ')) / 100

# cek apakah memenuhi syarat ( boolean )
isMemenuhiSyarat = lama_bekerja >= 2 and performa >= 0.7
# menghitung bonus
besar_bonus = ((lama_bekerja*500000) + (performa*10000 if isMemenuhiSyarat else 0)) if isMemenuhiSyarat else 0

kategori = ''

if lama_bekerja < 5:
    kategori = 'Junior'
elif 5 <= lama_bekerja <= 10:
    kategori = 'Senior'
else:
    kategori = 'Veteran'

alasan_tidak_dapat = ''

if isMemenuhiSyarat == False and lama_bekerja < 2:
    alasan_tidak_dapat += 'lama bekerja kurang dari 2 tahun. '
if isMemenuhiSyarat == False and performa < 0.7:
    alasan_tidak_dapat += 'performa kurang dari 70%. '

print('\n==== LAPORAN BONUS KARYAWAN ====')
print(f'Nama Karyawan : {nama_karyawan}')
print(f'Lama Bekerja : {lama_bekerja} Tahun ({kategori})')
print(f'Performa : {int(performa*100)}%')
print(f'Status Bonus: {'Memenuhi syarat.' if isMemenuhiSyarat else f'Tidak memenuhi syarat. ({alasan_tidak_dapat})'}')
print(f'Besar bonus: Rp{int(besar_bonus):,}')
print(f'================================')