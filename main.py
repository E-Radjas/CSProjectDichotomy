"""
1 : demander target, low et high number
2 : construire la liste sorted avec pour borne : low and high
3 : calculer la moyenne de la liste
4 : faire boucle while pour trouver si le target est dans la 1ere moitie ou dans la 2e
5 : Dans la boucle, si c'est dans la 1ere moitie, reduire la borne high jusqu'a mid
6 : Faire de meme pour cas contraire
7 : Faire dans la boucle un compteur pour savoir combien de boucle il a fallu pour trouver le target
8 : Dans la boucle, si target trouver, finir la boucle en annoncant le nombre target et le total de boucle demander pour le trouver
9 :
"""


def binary_search(sorted_list, target):
    the_list = []
    target = int(input("Give a target number: "))
    low = int(input("Give a lower number: "))
    high = int(input("Give a higher number: "))

    the_list = the_list.insert(0, low) and the_list.insert(-1, high)
    sorted_list = sorted(the_list)                 # il faut sorted la liste sous forme de nombre entier entre le 'low' et le 'high'

    mid = (low + high)//2


    while mid != target:
        if target > mid:
            low += mid - low
            the_list = the_list.insert(0, low) and the_list.insert(-1, high)
            return the_list
        elif target < mid:
            high -= mid + high
            the_list = the_list.insert(0, low) and the_list.insert(-1, high)
            return the_list
        else:
            result = target
            return print("Your target number is ", mid)

        counter += 1
        print(counter)
