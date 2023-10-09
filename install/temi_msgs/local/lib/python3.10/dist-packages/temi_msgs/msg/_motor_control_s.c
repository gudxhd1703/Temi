// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from temi_msgs:msg/MotorControl.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "temi_msgs/msg/detail/motor_control__struct.h"
#include "temi_msgs/msg/detail/motor_control__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool temi_msgs__msg__motor_control__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[42];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("temi_msgs.msg._motor_control.MotorControl", full_classname_dest, 41) == 0);
  }
  temi_msgs__msg__MotorControl * ros_message = _ros_message;
  {  // velocity
    PyObject * field = PyObject_GetAttrString(_pymsg, "velocity");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->velocity = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // direction_fr
    PyObject * field = PyObject_GetAttrString(_pymsg, "direction_fr");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->direction_fr = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // direction_fl
    PyObject * field = PyObject_GetAttrString(_pymsg, "direction_fl");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->direction_fl = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // direction_br
    PyObject * field = PyObject_GetAttrString(_pymsg, "direction_br");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->direction_br = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // direction_bl
    PyObject * field = PyObject_GetAttrString(_pymsg, "direction_bl");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->direction_bl = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * temi_msgs__msg__motor_control__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of MotorControl */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("temi_msgs.msg._motor_control");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "MotorControl");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  temi_msgs__msg__MotorControl * ros_message = (temi_msgs__msg__MotorControl *)raw_ros_message;
  {  // velocity
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->velocity);
    {
      int rc = PyObject_SetAttrString(_pymessage, "velocity", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // direction_fr
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->direction_fr);
    {
      int rc = PyObject_SetAttrString(_pymessage, "direction_fr", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // direction_fl
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->direction_fl);
    {
      int rc = PyObject_SetAttrString(_pymessage, "direction_fl", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // direction_br
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->direction_br);
    {
      int rc = PyObject_SetAttrString(_pymessage, "direction_br", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // direction_bl
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->direction_bl);
    {
      int rc = PyObject_SetAttrString(_pymessage, "direction_bl", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
