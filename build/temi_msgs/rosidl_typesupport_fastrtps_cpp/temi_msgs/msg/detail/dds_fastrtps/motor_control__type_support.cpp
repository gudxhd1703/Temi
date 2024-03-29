// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from temi_msgs:msg/MotorControl.idl
// generated code does not contain a copyright notice
#include "temi_msgs/msg/detail/motor_control__rosidl_typesupport_fastrtps_cpp.hpp"
#include "temi_msgs/msg/detail/motor_control__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace temi_msgs
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_temi_msgs
cdr_serialize(
  const temi_msgs::msg::MotorControl & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: velocity
  cdr << ros_message.velocity;
  // Member: direction_fr
  cdr << ros_message.direction_fr;
  // Member: direction_fl
  cdr << ros_message.direction_fl;
  // Member: direction_br
  cdr << ros_message.direction_br;
  // Member: direction_bl
  cdr << ros_message.direction_bl;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_temi_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  temi_msgs::msg::MotorControl & ros_message)
{
  // Member: velocity
  cdr >> ros_message.velocity;

  // Member: direction_fr
  cdr >> ros_message.direction_fr;

  // Member: direction_fl
  cdr >> ros_message.direction_fl;

  // Member: direction_br
  cdr >> ros_message.direction_br;

  // Member: direction_bl
  cdr >> ros_message.direction_bl;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_temi_msgs
get_serialized_size(
  const temi_msgs::msg::MotorControl & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: velocity
  {
    size_t item_size = sizeof(ros_message.velocity);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: direction_fr
  {
    size_t item_size = sizeof(ros_message.direction_fr);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: direction_fl
  {
    size_t item_size = sizeof(ros_message.direction_fl);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: direction_br
  {
    size_t item_size = sizeof(ros_message.direction_br);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: direction_bl
  {
    size_t item_size = sizeof(ros_message.direction_bl);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_temi_msgs
max_serialized_size_MotorControl(
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


  // Member: velocity
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: direction_fr
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: direction_fl
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: direction_br
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: direction_bl
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  return current_alignment - initial_alignment;
}

static bool _MotorControl__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const temi_msgs::msg::MotorControl *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _MotorControl__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<temi_msgs::msg::MotorControl *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _MotorControl__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const temi_msgs::msg::MotorControl *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _MotorControl__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_MotorControl(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _MotorControl__callbacks = {
  "temi_msgs::msg",
  "MotorControl",
  _MotorControl__cdr_serialize,
  _MotorControl__cdr_deserialize,
  _MotorControl__get_serialized_size,
  _MotorControl__max_serialized_size
};

static rosidl_message_type_support_t _MotorControl__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_MotorControl__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace temi_msgs

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_temi_msgs
const rosidl_message_type_support_t *
get_message_type_support_handle<temi_msgs::msg::MotorControl>()
{
  return &temi_msgs::msg::typesupport_fastrtps_cpp::_MotorControl__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, temi_msgs, msg, MotorControl)() {
  return &temi_msgs::msg::typesupport_fastrtps_cpp::_MotorControl__handle;
}

#ifdef __cplusplus
}
#endif
