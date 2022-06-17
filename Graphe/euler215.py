#!/usr/bin/env python3
# THEG 2021 -- Alexandre Duret-Lutz <adl@lrde.epita.fr>

from numpy import zeros
from numpy.linalg import matrix_power


# Build a list of possible configurations for each layers of a wall of
# size "width" built from bricks of width 2 or 3.
#
# The configurations are represented in binary form by concatenating
# 001 and 01.  The last one 1 is removed.  For instance the wall
# [2][3][3][2][2] is coded in base two as 01001001010
def possible_layers(width):
    configs = []

    def rec(partial):
        for brick in ('01', '001'):
            wall = partial + brick
            size = len(wall)
            if size == width:
                configs.append(int(wall[:-1], 2))
            elif size < width:
                rec(wall)

    rec('')
    return configs


# Decide if two layers are compatible.
def compatible(layer1, layer2):
    return layer1 & layer2 == 0


def compatible1(layer1, layer2, layer3):
    return (layer1 & layer2 & layer3) == 0


# Compute the number of possible walls of size width*height.
def W(width, height):
    configs = possible_layers(width)
    configs_num = len(configs)

    m = zeros((configs_num, configs_num), dtype='int')

    for i in range(configs_num):
        for j in range(i + 1, configs_num):
            if compatible(configs[i], configs[j]):
                m[i, j] = m[j, i] = 1

    # We will improve this computation in two weeks.
    return sum(sum(matrix_power(m, height - 1)))


# Compute the number of possible walls of size width*height.
def W_2(width, height):
    configs = possible_layers(width)
    configs_num = len(configs)
    m = zeros((configs_num, configs_num), dtype='int')

    for i in range(configs_num):
        for j in range(i + 1, configs_num):
            m[i, j] = m[j, i] = 1
            # for z in range(j + 1, configs_num):
            #     if compatible1(configs[i], configs[j], configs[z]):
            #         m[z, j] = m[j, z] = m[z, i] = m[i, z] = 1

    for i in range(configs_num):
        for j in range(i + 1, configs_num):
            for z in range(j + 1, configs_num):
                if not compatible1(configs[i], configs[j], configs[z]):
                    m[z, j] = 0

    # m[i, j] = m[j, i] = 0
    # m[j, i] = m[j, i] = 0
    # m[i, j] = m[j, i] = 1
    # m[i, j] = m[j, i] = m[i, z] = m[z, i] = m[z, j] = m[j, z] = 1

    # We will improve this computation in two weeks.
    return sum(sum(matrix_power(m, height - 1)))


#
# a = int('01100000', 2)
# b = int('00100110', 2)
# c = int('10010010', 2)
# print(bin(a & c & b))

# assert W(9, 3) == 8
# print(W(12, 11))
print(W_2(11, 5))
# Note that this version would take a very long
# time to compute W(32,10).


# Example of 9x3 wall that should be rejected because it contains a running crack of length 3.
#
# There are W′(9,3)=66
#
# possible 9x3 walls in which the maximal length of running cracks is 2 or 1.
#
# There are W′(10,4)=650
#
# possible 10x4 walls in which the maximal length of running cracks is 2 or 1.
#
# There are W′(11,5)=8954
#
# possible 11x5 walls in which the maximal length of running cracks is 2 or 1.
#
# Compute the value of W′(12,11)
