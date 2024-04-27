import os
import pygame as pg
import random as r
def find(name):
    a = False
    for root, dirs, files in os.walk('main files/'):
        if name in files:
            a = True
        else:
            a = False
    return a
def save(directory, filename, file_data, main_directory):
    find(filename)
    new_path = os.path.dirname(os.path.realpath(__file__))
    if find(filename) == True:
        with open(os.path.join(new_path, main_directory, directory, filename), 'w') as file:
            file.write(file_data)
    elif find(filename) == False:
        find(os.path.join(new_path, main_directory, directory))
        if find(os.path.join(new_path, main_directory, directory)) == True:
            with open(os.path.join(new_path, main_directory, directory, filename), 'w') as file:
                file.write(file_data)
        elif find(os.path.join(new_path, main_directory, directory)) == False:
            os.mkdir(os.path.join(new_path, main_directory, directory))
            with open(os.path.join(new_path, main_directory, directory, filename), 'w') as file:
                file.write(file_data)
def download(filename):
    find(filename)
    if find(filename) == True:
        with open(os.path.join('main files', 'hs', filename), 'r') as b:
            b = int(b.read())
    elif find(filename) == False:
        print('Error: Could not find highscore file!')
    return b

