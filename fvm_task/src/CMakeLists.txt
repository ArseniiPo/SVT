cmake_minimum_required(VERSION 3.5)
project(inmost_project)

# set(INMOST_DIR "/home/arsenii/inmost-root") # uncomment and set location manually if needed

find_package(inmost REQUIRED)

link_directories(${INMOST_LIBRARY_DIRS})
include_directories(${INMOST_INCLUDE_DIRS})
add_definitions(${INMOST_DEFINITIONS})

add_executable(fvm fvm.cpp)

target_link_libraries(fvm ${INMOST_LIBRARIES})
