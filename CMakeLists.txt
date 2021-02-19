cmake_minimum_required(VERSION 2.8.11)
project(hidapi)


if(WIN32)	
add_library(hidapi SHARED hid_win.c)
target_link_libraries(hidapi "setupapi.lib")
endif(WIN32)

if(UNIX)
add_library(hidapi SHARED hid_mac.c)
target_link_libraries(hidapi "setupapi.lib")	
endif(UNIX)

if(LINUX)
add_library(hidapi SHARED hid_linux.c)
target_link_libraries(hidapi "setupapi.lib")
endif(LINUX)

target_include_directories(hidapi PUBLIC inc)
