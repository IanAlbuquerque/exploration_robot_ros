# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "homography: 0 messages, 1 services")

set(MSG_I_FLAGS "-Isensor_msgs:/opt/ros/indigo/share/sensor_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/indigo/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(homography_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-bc/final_proj/src/homography/srv/ImageSrv.srv" NAME_WE)
add_custom_target(_homography_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "homography" "/home/cc/ee106a/fa15/class/ee106a-bc/final_proj/src/homography/srv/ImageSrv.srv" "std_msgs/Header:sensor_msgs/Image"
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(homography
  "/home/cc/ee106a/fa15/class/ee106a-bc/final_proj/src/homography/srv/ImageSrv.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/sensor_msgs/cmake/../msg/Image.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/homography
)

### Generating Module File
_generate_module_cpp(homography
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/homography
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(homography_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(homography_generate_messages homography_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-bc/final_proj/src/homography/srv/ImageSrv.srv" NAME_WE)
add_dependencies(homography_generate_messages_cpp _homography_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(homography_gencpp)
add_dependencies(homography_gencpp homography_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS homography_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(homography
  "/home/cc/ee106a/fa15/class/ee106a-bc/final_proj/src/homography/srv/ImageSrv.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/sensor_msgs/cmake/../msg/Image.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/homography
)

### Generating Module File
_generate_module_lisp(homography
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/homography
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(homography_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(homography_generate_messages homography_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-bc/final_proj/src/homography/srv/ImageSrv.srv" NAME_WE)
add_dependencies(homography_generate_messages_lisp _homography_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(homography_genlisp)
add_dependencies(homography_genlisp homography_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS homography_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(homography
  "/home/cc/ee106a/fa15/class/ee106a-bc/final_proj/src/homography/srv/ImageSrv.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/sensor_msgs/cmake/../msg/Image.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/homography
)

### Generating Module File
_generate_module_py(homography
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/homography
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(homography_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(homography_generate_messages homography_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-bc/final_proj/src/homography/srv/ImageSrv.srv" NAME_WE)
add_dependencies(homography_generate_messages_py _homography_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(homography_genpy)
add_dependencies(homography_genpy homography_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS homography_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/homography)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/homography
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(homography_generate_messages_cpp sensor_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/homography)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/homography
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(homography_generate_messages_lisp sensor_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/homography)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/homography\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/homography
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(homography_generate_messages_py sensor_msgs_generate_messages_py)
