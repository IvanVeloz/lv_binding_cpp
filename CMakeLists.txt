cmake_minimum_required(VERSION 3.10)

set(CMAKE_TRY_COMPILE_TARGET_TYPE "STATIC_LIBRARY")

project(lv_binding_cpp VERSION 0.2)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

include(${CMAKE_CURRENT_LIST_DIR}/mkrules.cmake)

file(GLOB_RECURSE SOURCES ./lv_cpp/*.cpp ./lv_cpp/custom/drivers/*.c ./lv_conf.h)
add_library(lv_binding_cpp ${SOURCES})

add_subdirectory(lvgl ./lvgl)
add_subdirectory(lv_drivers ./lv_drivers)
add_subdirectory(lv_cpp_examples ./lv_cpp_examples)

target_include_directories (lvgl PUBLIC ${CMAKE_SOURCE_DIR})
target_include_directories (lv_drivers PUBLIC ${CMAKE_SOURCE_DIR})
target_include_directories (lv_cpp_examples PUBLIC ${CMAKE_SOURCE_DIR})
target_include_directories (lv_binding_cpp PUBLIC ${CMAKE_SOURCE_DIR})

target_link_libraries(lv_binding_cpp lvgl lv_drivers)


# create targets for generated files
#all_lv_bindings()

