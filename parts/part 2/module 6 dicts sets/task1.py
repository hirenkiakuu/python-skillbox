violator_songs = {
'World in My Eyes': 4.86,
'Sweetest Perfection': 4.43,
'Personal Jesus': 4.56,
'Halo': 4.9,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.20,
'Policy of Truth': 4.76,
'Blue Dress': 4.29,
'Clean': 5.83
}

amount = int(input('Сколько песен выбрать? '))
sum = 0

for i_song in range(amount):
    i_song = input(f'Название {i_song + 1}-й песни: ')
    sum += violator_songs[i_song]

print(f'Общее время звучания песен: {sum:.2f} минуты')



