// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from temi_msgs:msg/MotorControl.idl
// generated code does not contain a copyright notice

#ifndef TEMI_MSGS__MSG__DETAIL__MOTOR_CONTROL__TRAITS_HPP_
#define TEMI_MSGS__MSG__DETAIL__MOTOR_CONTROL__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "temi_msgs/msg/detail/motor_control__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace temi_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const MotorControl & msg,
  std::ostream & out)
{
  out << "{";
  // member: velocity
  {
    out << "velocity: ";
    rosidl_generator_traits::value_to_yaml(msg.velocity, out);
    out << ", ";
  }

  // member: direction_fr
  {
    out << "direction_fr: ";
    rosidl_generator_traits::value_to_yaml(msg.direction_fr, out);
    out << ", ";
  }

  // member: direction_fl
  {
    out << "direction_fl: ";
    rosidl_generator_traits::value_to_yaml(msg.direction_fl, out);
    out << ", ";
  }

  // member: direction_br
  {
    out << "direction_br: ";
    rosidl_generator_traits::value_to_yaml(msg.direction_br, out);
    out << ", ";
  }

  // member: direction_bl
  {
    out << "direction_bl: ";
    rosidl_generator_traits::value_to_yaml(msg.direction_bl, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MotorControl & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: velocity
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "velocity: ";
    rosidl_generator_traits::value_to_yaml(msg.velocity, out);
    out << "\n";
  }

  // member: direction_fr
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "direction_fr: ";
    rosidl_generator_traits::value_to_yaml(msg.direction_fr, out);
    out << "\n";
  }

  // member: direction_fl
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "direction_fl: ";
    rosidl_generator_traits::value_to_yaml(msg.direction_fl, out);
    out << "\n";
  }

  // member: direction_br
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "direction_br: ";
    rosidl_generator_traits::value_to_yaml(msg.direction_br, out);
    out << "\n";
  }

  // member: direction_bl
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "direction_bl: ";
    rosidl_generator_traits::value_to_yaml(msg.direction_bl, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MotorControl & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace temi_msgs

namespace rosidl_generator_traits
{

[[deprecated("use temi_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const temi_msgs::msg::MotorControl & msg,
  std::ostream & out, size_t indentation = 0)
{
  temi_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use temi_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const temi_msgs::msg::MotorControl & msg)
{
  return temi_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<temi_msgs::msg::MotorControl>()
{
  return "temi_msgs::msg::MotorControl";
}

template<>
inline const char * name<temi_msgs::msg::MotorControl>()
{
  return "temi_msgs/msg/MotorControl";
}

template<>
struct has_fixed_size<temi_msgs::msg::MotorControl>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<temi_msgs::msg::MotorControl>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<temi_msgs::msg::MotorControl>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // TEMI_MSGS__MSG__DETAIL__MOTOR_CONTROL__TRAITS_HPP_
