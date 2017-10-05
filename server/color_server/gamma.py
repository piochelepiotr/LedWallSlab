#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gamma correction module
Useful to make the LED luminosity proportional to the command
"""

import numpy as np


class Gamma:
    @staticmethod
    def gamma_table(gamma):
        """
        This function generate corrected values according to the given gamma
        :param gamma: gamma coefficient
        :return: 256 length values table
        """

        l = np.ndarray(256)
        for i in range(256):
            v = pow(i / 255, gamma) * 255
            v = int(round(v))
            l[i] = v
        return l

    @staticmethod
    def gamma_matrix(gamma_coefs):
        """
        This function generate the gamma matrix using numpy
        :param gamma_coefs: [[gammaR, gammaG, gammaB], ..., [gammaR, gammaG, gammaB]]
        :return: Matrix with corrected values for each color of each slabs
        """
        matrix = np.ndarray([len(gamma_coefs), 3, 256], dtype=int)

        # gamma_coefs contains an [R, G, B] gamma table for each slab
        for i, slab in enumerate(gamma_coefs):
            for j, color in enumerate(slab):
                for k in range(256):
                    v = pow(k / 255, color) * 255
                    v = int(round(v))
                    matrix[i, j, k] = v
        return matrix
