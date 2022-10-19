import sys
from typing import TextIO


def read_data(f: TextIO) -> tuple[int, list[int]]:
    C = int(f.readline())
    w = [int(linea) for linea in f.readlines()]
    return C, w


def process(C: int, w: list[int]) -> list[int]:
    nc = 0    # numero de contenedor
    free = C  # espacio libre
    contenedores = []
    for obj in w:
        if obj > free:
            nc += 1
            free = C
        free -= obj
        contenedores.append(nc)
    return contenedores


def show_results(contenedores: list[int]):
    for c in contenedores:
        print(c)


if __name__ == "__main__":
    C, w = read_data(sys.stdin)
    contenedores = process(C, w)
    show_results(contenedores)