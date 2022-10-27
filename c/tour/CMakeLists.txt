cmake_minimum_required(VERSION 3.7)
project(tour)

set(CMAKE_C_STANDARD 11)

set(SOURCE_FILES main.c objects.c)
add_executable(tour ${SOURCE_FILES})