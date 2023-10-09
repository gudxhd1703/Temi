// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from temi_msgs:msg/MotorControl.idl
// generated code does not contain a copyright notice
#include "temi_msgs/msg/detail/motor_control__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "temi_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "temi_msgs/msg/detail/motor_control__struct.h"
#include "temi_msgs/msg/detail/motor_control__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _MotorControl__ros_msg_type = temi_msgs__msg__MotorControl;

static bool _MotorControl__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _MotorControl__ros_msg_type * ros_message = static_cast<const _MotorControl__ros_msg_type *>(untyped_ros_message);
  // Field name: velocity
  {
    cdr << ros_message->velocity;
  }

  // Field name: direction_fr
  {
    cdr << ros_message->direction_fr;
  }

  // Field name: direction_fl
  {
    cdr << ros_message->direction_fl;
  }

  // Field name: direction_br
  {
    cdr << ros_message->direction_br;
  }

  // Field name: direction_bl
  {
    cdr << ros_message->direction_bl;
  }

  return true;
}

static bool _MotorControl__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _MotorControl__ros_msg_type * ros_message = static_cast<_MotorControl__ros_msg_type *>(untyped_ros_message);
  // Field name: velocity
  {
    cdr >> ros_message->velocity;
  }

  // Field name: direction_fr
  {
    cdr >> ros_message->direction_fr;
  }

  // Field name: direction_fl
  {
    cdr >> ros_message->direction_fl;
  }

  // Field name: direction_br
  {
    cdr >> ros_message->direction_br;
  }

  // Field name: direction_bl
  {
    cdr >> ros_message->direction_bl;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_temi_msgs
size_t get_serialized_size_temi_msgs__msg__MotorControl(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _MotorControl__ros_msg_type * ros_message = static_cast<const _MotorControl__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name velocity
  {
    size_t item_size = sizeof(ros_message->velocity);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name direction_fr
  {
    size_t item_size = sizeof(ros_message->direction_fr);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name direction_fl
  {
    size_t item_size = sizeof(ros_message->direction_fl);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name direction_br
  {
    size_t item_size = sizeof(ros_message->direction_br);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name direction_bl
  {
    size_t item_size = sizeof(ros_message->direction_bl);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _MotorControl__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_temi_msgs__msg__MotorControl(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_temi_msgs
size_t max_serialized_size_temi_msgs__msg__MotorControl(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: velocity
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: direction_fr
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: direction_fl
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: direction_br
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: direction_bl
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _MotorControl__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_temi_msgs__msg__MotorControl(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_MotorControl = {
  "temi_msgs::msg",
  "MotorControl",
  _MotorControl__cdr_serialize,
  _MotorControl__cdr_deserialize,
  _MotorControl__get_serialized_size,
  _MotorControl__max_serialized_size
};

static rosidl_message_type_support_t _MotorControl__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_MotorControl,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, temi_msgs, msg, MotorControl)() {
  return &_MotorControl__type_support;
}

#if defined(__cplusplus)
}
#endif
