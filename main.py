import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Funkcja wypisująca dane
def print_data(data):
    #Obliczanie średniej
    avg = np.mean(data, axis=0)

    #Obliczanie odchylenia standardowego
    std = np.std(data, axis=0)

    #Obliczanie wartości minimalnej
    min = np.min(data, axis=0)

    #Obliczanie wartości maksymalnej 
    max = np.max(data, axis=0)
    
    print("Średnia tluszcz = ", avg[0])
    #print("Avg wsk. trzustkowy = ", avg[1]))
    print("Średnia FFM = ", avg[2])
    print("Średnia FFMI = ", avg[3])

    print("Odchylenie standardowe tluszcz = ", std[0])
    #print("Odchylenie standardowe wsk. trzustkowy = ", std[1])
    print("Odchylenie standardowe FFM = ", std[2])
    print("Odchylenie standardowe FFMI = ", std[3])

    print("Min tluszcz = ", min[0])
    #print("Min wsk. trzustkowy = ", min[1])
    print("Min FFM = ", min[2])
    print("Min FFMI = ", min[3])

    print("Max tluszcz = ", max[0])
    #print("Max wsk. trzustkowy = ", max[1])
    print("Max FFM = ", max[2])
    print("Max FFMI = ", max[3])

#Funkcja tworząca wykresy średnich
def display_plot(y_tluszcz, y_FFM, y_FFMI):
    #Tworzenie osi X dla każdego wskaźnika
    x=[i+1 for i in range(10)]
    
    plt.figure(0)

    #Tworzenie wykresu
    plt.bar(x, y_tluszcz)

    #Skalowanie osi X
    plt.xticks(np.arange(1, 11, step=1))

    #Skalowanie osi Y
    plt.yticks(np.arange(0, 30, step=2))

    #Dodanie tytułu i etykiet
    plt.title('Wykres średniej % tłuszczu w zależności od wskaźnika trzustki')
    plt.xlabel('Wskaźnik trzustki')
    plt.ylabel('Średnia tłuszczu [%]')

    plt.figure(1)

    #Tworzenie wykresu
    plt.bar(x, y_FFM, color='limegreen')

    #Skalowanie osi X
    plt.xticks(np.arange(1, 11, step=1))

    #Skalowanie osi Y
    plt.yticks(np.arange(0, 80, step=5))

    #Dodanie tytułu i etykiet
    plt.title('Wykres średniej FFM w zależności od wskaźnika trzustki')
    plt.xlabel('Wskaźnik trzustki')
    plt.ylabel('Średnia FFM')

    plt.figure(2)

    #Tworzenie wykresu
    plt.bar(x, y_FFMI, color='orangered')

    #Skalowanie osi X
    plt.xticks(np.arange(1, 11, step=1))

    #Skalowanie osi Y
    plt.yticks(np.arange(0, 23, step=2))

    #Dodanie tytułu i etykiet
    plt.title('Wykres średniej FFMI w zależności od wskaźnika trzustki')
    plt.xlabel('Wskaźnik trzustki')
    plt.ylabel('Średnia FFMI')

    plt.show()

#Funkcja tworząca plot box
def display_plot_box(array):
    plt.figure(3)

    box = plt.boxplot([array[i][0] for i in range(10)], patch_artist=True)
    for patch in box['boxes']:
        patch.set_facecolor('skyblue')

    #Skalowanie osi X
    plt.xticks(np.arange(1, 11, step=1))

    #Skalowanie osi Y
    plt.yticks(np.arange(0, 34, step=2))

    #Dodanie tytułu i etykiet
    plt.title('Analiza wskaźnika trzustkowego w zależności od zawartości tłuszczu')
    plt.xlabel('Wskaźnik trzustki')
    plt.ylabel('Zawartość tłuszczu [%]')

    plt.figure(4)

    #Tworzenie wykresu
    box = plt.boxplot([array[i][1] for i in range(10)], patch_artist=True)
    for patch in box['boxes']:
        patch.set_facecolor('lightgreen')

    #Skalowanie osi X
    plt.xticks(np.arange(1, 11, step=1))

    #Skalowanie osi Y
    plt.yticks(np.arange(0, 91, step=5))

    #Dodanie tytułu i etykiet
    plt.title('Analiza wskaźnika trzustkowego w zależności od FFM')
    plt.xlabel('Wskaźnik trzustki')
    plt.ylabel('FFM')

    plt.figure(5)

    #Tworzenie wykresu
    box = plt.boxplot([array[i][2] for i in range(10)], patch_artist=True)
    for patch in box['boxes']:
        patch.set_facecolor('salmon')

    #Skalowanie osi X
    plt.xticks(np.arange(1, 11, step=1))

    #Skalowanie osi Y
    plt.yticks(np.arange(0, 25, step=2))

    #Dodanie tytułu i etykiet
    plt.title('Analiza wskaźnika trzustkowego w zależności od FMMI')
    plt.xlabel('Wskaźnik trzustki')
    plt.ylabel('FFMI')
    plt.show()

#Ścieżka do pliku Excel
file_path = './projekty_wprowadzenie.xlsx'

#Wczytanie danych z arkusza
dfs = pd.read_excel(file_path, sheet_name='Projekt7')
array = dfs.values.tolist()

#Tworzenie tablicy podzielonej na poszczególne wskaźniki
wsk = [[[] for _ in range(3)] for _ in range(10)]
for i in range(len(array)):
    index = int(array[i][1] - 1)
    wsk[index][0].append(array[i][0])
    wsk[index][1].append(array[i][2])
    wsk[index][2].append(array[i][3])

print_data(array)

tluszcz_avg = [np.mean(wsk[i][0]) for i in range(10)]
FFM_avg = [np.mean(wsk[i][1]) for i in range(10)]
FFMI_avg = [np.mean(wsk[i][2]) for i in range(10)]

#display_plot(tluszcz_avg, FFM_avg, FFMI_avg)
 
display_plot_box(wsk)