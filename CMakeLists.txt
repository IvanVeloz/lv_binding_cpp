cmake_minimum_required(VERSION 3.10)

set(CMAKE_TRY_COMPILE_TARGET_TYPE "STATIC_LIBRARY")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/build/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/build/lib)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/build/lib)


project(lv_binding_cpp VERSION 0.2)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

include(${CMAKE_CURRENT_LIST_DIR}/mkrules.cmake)

file(GLOB_RECURSE SOURCES ./lv_cpp/*.cpp ./lv_cpp/custom/drivers/*.c)
add_library(lv_binding_cpp STATIC ${SOURCES})

add_subdirectory(lvgl)
add_subdirectory(lv_drivers)
add_subdirectory(lv_cpp_examples)

target_include_directories (lvgl PUBLIC ${CMAKE_SOURCE_DIR})
target_include_directories (lv_drivers PUBLIC ${CMAKE_SOURCE_DIR})
target_include_directories (lv_cpp_examples PUBLIC ${CMAKE_SOURCE_DIR})
target_include_directories (lv_binding_cpp PUBLIC ${CMAKE_SOURCE_DIR})

target_link_libraries(lv_binding_cpp lvgl lv_drivers)


# create targets for generated files
all_lv_bindings()

