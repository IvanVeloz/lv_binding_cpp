cmake_minimum_required(VERSION 3.10)

project(lv_binding_cpp VERSION 0.1)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)
add_compile_definitions(CONFIG_EXAMPLES)
add_compile_definitions(CONFIG_EXAMPLE_HELLO)
add_compile_definitions(CONFIG_EXAMPLE_FLEX)

find_package(SDL2 REQUIRED)

file(GLOB_RECURSE SOURCES ./*.cpp)
add_executable(lv_cpp_examples
    ${PROJECT_SOURCE_DIR}/examples.cpp
    ${PROJECT_SOURCE_DIR}/FlexEx.cpp
    ${PROJECT_SOURCE_DIR}/HelloEx.cpp
)

target_include_directories(lvgl PUBLIC ${PROJECT_SOURCE_DIR} ${SDL2_INCLUDE_DIRS})
target_link_libraries(lv_cpp_examples PRIVATE lv_binding_cpp ${SDL2_LIBRARIES})
