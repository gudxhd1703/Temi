// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from temi_msgs:msg/MotorControl.idl
// generated code does not contain a copyright notice

#ifndef TEMI_MSGS__MSG__DETAIL__MOTOR_CONTROL__STRUCT_HPP_
#define TEMI_MSGS__MSG__DETAIL__MOTOR_CONTROL__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__temi_msgs__msg__MotorControl __attribute__((deprecated))
#else
# define DEPRECATED__temi_msgs__msg__MotorControl __declspec(deprecated)
#endif

namespace temi_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct MotorControl_
{
  using Type = MotorControl_<ContainerAllocator>;

  explicit MotorControl_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->velocity = 0.0;
      this->direction_fr = 0.0;
      this->direction_fl = 0.0;
      this->direction_br = 0.0;
      this->direction_bl = 0.0;
    }
  }

  explicit MotorControl_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->velocity = 0.0;
      this->direction_fr = 0.0;
      this->direction_fl = 0.0;
      this->direction_br = 0.0;
      this->direction_bl = 0.0;
    }
  }

  // field types and members
  using _velocity_type =
    double;
  _velocity_type velocity;
  using _direction_fr_type =
    double;
  _direction_fr_type direction_fr;
  using _direction_fl_type =
    double;
  _direction_fl_type direction_fl;
  using _direction_br_type =
    double;
  _direction_br_type direction_br;
  using _direction_bl_type =
    double;
  _direction_bl_type direction_bl;

  // setters for named parameter idiom
  Type & set__velocity(
    const double & _arg)
  {
    this->velocity = _arg;
    return *this;
  }
  Type & set__direction_fr(
    const double & _arg)
  {
    this->direction_fr = _arg;
    return *this;
  }
  Type & set__direction_fl(
    const double & _arg)
  {
    this->direction_fl = _arg;
    return *this;
  }
  Type & set__direction_br(
    const double & _arg)
  {
    this->direction_br = _arg;
    return *this;
  }
  Type & set__direction_bl(
    const double & _arg)
  {
    this->direction_bl = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    temi_msgs::msg::MotorControl_<ContainerAllocator> *;
  using ConstRawPtr =
    const temi_msgs::msg::MotorControl_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<temi_msgs::msg::MotorControl_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<temi_msgs::msg::MotorControl_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      temi_msgs::msg::MotorControl_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<temi_msgs::msg::MotorControl_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      temi_msgs::msg::MotorControl_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<temi_msgs::msg::MotorControl_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<temi_msgs::msg::MotorControl_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<temi_msgs::msg::MotorControl_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__temi_msgs__msg__MotorControl
    std::shared_ptr<temi_msgs::msg::MotorControl_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__temi_msgs__msg__MotorControl
    std::shared_ptr<temi_msgs::msg::MotorControl_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MotorControl_ & other) const
  {
    if (this->velocity != other.velocity) {
      return false;
    }
    if (this->direction_fr != other.direction_fr) {
      return false;
    }
    if (this->direction_fl != other.direction_fl) {
      return false;
    }
    if (this->direction_br != other.direction_br) {
      return false;
    }
    if (this->direction_bl != other.direction_bl) {
      return false;
    }
    return true;
  }
  bool operator!=(const MotorControl_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MotorControl_

// alias to use template instance with default allocator
using MotorControl =
  temi_msgs::msg::MotorControl_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace temi_msgs

#endif  // TEMI_MSGS__MSG__DETAIL__MOTOR_CONTROL__STRUCT_HPP_
