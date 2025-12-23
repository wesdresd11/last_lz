

def volume(sqr_1, sqr_2, h):
    pyr_volume = (1/3)*h*(sqr_1 + sqr_2 + (sqr_1*sqr_2)**(1/2))
    return(pyr_volume)

def main():
    sqr_1 = int(input("Площадь нижнего основания: "))
    sqr_2 = int(input("Площадь верхнего основания: "))
    h = int(input("Введите высоту: "))
    print(volume(sqr_1, sqr_2, h))


if __name__ == "__main__":
    main()

