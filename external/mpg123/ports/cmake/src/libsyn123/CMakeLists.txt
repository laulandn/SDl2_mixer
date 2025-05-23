cmake_minimum_required(VERSION 3.12)

configure_file("${CMAKE_CURRENT_SOURCE_DIR}/../../../../src/libsyn123/syn123.h.in" syn123.h)

include_directories("${CMAKE_CURRENT_BINARY_DIR}" "${CMAKE_CURRENT_SOURCE_DIR}/../../../src/libsyn123/")

set(TARGET libsyn123)
add_library(${TARGET}
    "${CMAKE_CURRENT_SOURCE_DIR}/../../../../src/libsyn123/pinknoise.c"
    "${CMAKE_CURRENT_SOURCE_DIR}/../../../../src/libsyn123/geiger.c"
    "${CMAKE_CURRENT_SOURCE_DIR}/../../../../src/libsyn123/libsyn123.c"
    "${CMAKE_CURRENT_SOURCE_DIR}/../../../../src/libsyn123/volume.c"
    "${CMAKE_CURRENT_SOURCE_DIR}/../../../../src/libsyn123/resample.c"
    "${CMAKE_CURRENT_SOURCE_DIR}/../../../../src/libsyn123/filter.c"
    "${CMAKE_CURRENT_SOURCE_DIR}/../../../../src/libsyn123/sampleconv.c"
    $<TARGET_OBJECTS:compat_str>)

set_target_properties(${TARGET} PROPERTIES OUTPUT_NAME syn123)
if(BUILD_SHARED_LIBS AND WIN32)
    # FIXME: keep soversion in sync with autotools
    set_property(TARGET ${TARGET} PROPERTY RUNTIME_OUTPUT_NAME "syn123-0")
    # Requires CMake 3.27, so not sufficient
    set_property(TARGET ${TARGET} PROPERTY DLL_NAME_WITH_SOVERSION FALSE)
endif()

target_include_directories(${TARGET} INTERFACE
    "$<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>"
    "$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>")

target_link_libraries(${TARGET} PRIVATE
    $<$<BOOL:${HAVE_M}>:m>
    $<$<BOOL:${WANT_WIN32_UNICODE}>:shlwapi>)

install(TARGETS ${TARGET} EXPORT targets
    ARCHIVE DESTINATION "${CMAKE_INSTALL_LIBDIR}/"
    LIBRARY DESTINATION "${CMAKE_INSTALL_LIBDIR}/"
    RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}/")
install(FILES "${CMAKE_CURRENT_BINARY_DIR}/syn123.h"
    DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}")
