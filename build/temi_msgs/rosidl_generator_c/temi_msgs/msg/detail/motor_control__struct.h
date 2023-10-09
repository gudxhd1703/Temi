// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from temi_msgs:msg/MotorControl.idl
// generated code does not contain a copyright notice

#ifndef TEMI_MSGS__MSG__DETAIL__MOTOR_CONTROL__STRUCT_H_
#define TEMI_MSGS__MSG__DETAIL__MOTOR_CONTROL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/MotorControl in the package temi_msgs.
typedef struct temi_msgs__msg__MotorControl
{
  double velocity;
  double direction_fr;
  double direction_fl;
  double direction_br;
  double direction_bl;
} temi_msgs__msg__MotorControl;

// Struct for a sequence of temi_msgs__msg__MotorControl.
typedef struct temi_msgs__msg__MotorControl__Sequence
{
  temi_msgs__msg__MotorControl * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} temi_msgs__msg__MotorControl__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TEMI_MSGS__MSG__DETAIL__MOTOR_CONTROL__STRUCT_H_
