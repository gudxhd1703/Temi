// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from temi_msgs:msg/MotorControl.idl
// generated code does not contain a copyright notice

#ifndef TEMI_MSGS__MSG__DETAIL__MOTOR_CONTROL__BUILDER_HPP_
#define TEMI_MSGS__MSG__DETAIL__MOTOR_CONTROL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "temi_msgs/msg/detail/motor_control__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace temi_msgs
{

namespace msg
{

namespace builder
{

class Init_MotorControl_direction_bl
{
public:
  explicit Init_MotorControl_direction_bl(::temi_msgs::msg::MotorControl & msg)
  : msg_(msg)
  {}
  ::temi_msgs::msg::MotorControl direction_bl(::temi_msgs::msg::MotorControl::_direction_bl_type arg)
  {
    msg_.direction_bl = std::move(arg);
    return std::move(msg_);
  }

private:
  ::temi_msgs::msg::MotorControl msg_;
};

class Init_MotorControl_direction_br
{
public:
  explicit Init_MotorControl_direction_br(::temi_msgs::msg::MotorControl & msg)
  : msg_(msg)
  {}
  Init_MotorControl_direction_bl direction_br(::temi_msgs::msg::MotorControl::_direction_br_type arg)
  {
    msg_.direction_br = std::move(arg);
    return Init_MotorControl_direction_bl(msg_);
  }

private:
  ::temi_msgs::msg::MotorControl msg_;
};

class Init_MotorControl_direction_fl
{
public:
  explicit Init_MotorControl_direction_fl(::temi_msgs::msg::MotorControl & msg)
  : msg_(msg)
  {}
  Init_MotorControl_direction_br direction_fl(::temi_msgs::msg::MotorControl::_direction_fl_type arg)
  {
    msg_.direction_fl = std::move(arg);
    return Init_MotorControl_direction_br(msg_);
  }

private:
  ::temi_msgs::msg::MotorControl msg_;
};

class Init_MotorControl_direction_fr
{
public:
  explicit Init_MotorControl_direction_fr(::temi_msgs::msg::MotorControl & msg)
  : msg_(msg)
  {}
  Init_MotorControl_direction_fl direction_fr(::temi_msgs::msg::MotorControl::_direction_fr_type arg)
  {
    msg_.direction_fr = std::move(arg);
    return Init_MotorControl_direction_fl(msg_);
  }

private:
  ::temi_msgs::msg::MotorControl msg_;
};

class Init_MotorControl_velocity
{
public:
  Init_MotorControl_velocity()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MotorControl_direction_fr velocity(::temi_msgs::msg::MotorControl::_velocity_type arg)
  {
    msg_.velocity = std::move(arg);
    return Init_MotorControl_direction_fr(msg_);
  }

private:
  ::temi_msgs::msg::MotorControl msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::temi_msgs::msg::MotorControl>()
{
  return temi_msgs::msg::builder::Init_MotorControl_velocity();
}

}  // namespace temi_msgs

#endif  // TEMI_MSGS__MSG__DETAIL__MOTOR_CONTROL__BUILDER_HPP_
