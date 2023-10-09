// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from temi_msgs:msg/MotorControl.idl
// generated code does not contain a copyright notice
#include "temi_msgs/msg/detail/motor_control__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
temi_msgs__msg__MotorControl__init(temi_msgs__msg__MotorControl * msg)
{
  if (!msg) {
    return false;
  }
  // velocity
  // direction_fr
  // direction_fl
  // direction_br
  // direction_bl
  return true;
}

void
temi_msgs__msg__MotorControl__fini(temi_msgs__msg__MotorControl * msg)
{
  if (!msg) {
    return;
  }
  // velocity
  // direction_fr
  // direction_fl
  // direction_br
  // direction_bl
}

bool
temi_msgs__msg__MotorControl__are_equal(const temi_msgs__msg__MotorControl * lhs, const temi_msgs__msg__MotorControl * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // velocity
  if (lhs->velocity != rhs->velocity) {
    return false;
  }
  // direction_fr
  if (lhs->direction_fr != rhs->direction_fr) {
    return false;
  }
  // direction_fl
  if (lhs->direction_fl != rhs->direction_fl) {
    return false;
  }
  // direction_br
  if (lhs->direction_br != rhs->direction_br) {
    return false;
  }
  // direction_bl
  if (lhs->direction_bl != rhs->direction_bl) {
    return false;
  }
  return true;
}

bool
temi_msgs__msg__MotorControl__copy(
  const temi_msgs__msg__MotorControl * input,
  temi_msgs__msg__MotorControl * output)
{
  if (!input || !output) {
    return false;
  }
  // velocity
  output->velocity = input->velocity;
  // direction_fr
  output->direction_fr = input->direction_fr;
  // direction_fl
  output->direction_fl = input->direction_fl;
  // direction_br
  output->direction_br = input->direction_br;
  // direction_bl
  output->direction_bl = input->direction_bl;
  return true;
}

temi_msgs__msg__MotorControl *
temi_msgs__msg__MotorControl__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  temi_msgs__msg__MotorControl * msg = (temi_msgs__msg__MotorControl *)allocator.allocate(sizeof(temi_msgs__msg__MotorControl), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(temi_msgs__msg__MotorControl));
  bool success = temi_msgs__msg__MotorControl__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
temi_msgs__msg__MotorControl__destroy(temi_msgs__msg__MotorControl * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    temi_msgs__msg__MotorControl__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
temi_msgs__msg__MotorControl__Sequence__init(temi_msgs__msg__MotorControl__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  temi_msgs__msg__MotorControl * data = NULL;

  if (size) {
    data = (temi_msgs__msg__MotorControl *)allocator.zero_allocate(size, sizeof(temi_msgs__msg__MotorControl), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = temi_msgs__msg__MotorControl__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        temi_msgs__msg__MotorControl__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
temi_msgs__msg__MotorControl__Sequence__fini(temi_msgs__msg__MotorControl__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      temi_msgs__msg__MotorControl__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

temi_msgs__msg__MotorControl__Sequence *
temi_msgs__msg__MotorControl__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  temi_msgs__msg__MotorControl__Sequence * array = (temi_msgs__msg__MotorControl__Sequence *)allocator.allocate(sizeof(temi_msgs__msg__MotorControl__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = temi_msgs__msg__MotorControl__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
temi_msgs__msg__MotorControl__Sequence__destroy(temi_msgs__msg__MotorControl__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    temi_msgs__msg__MotorControl__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
temi_msgs__msg__MotorControl__Sequence__are_equal(const temi_msgs__msg__MotorControl__Sequence * lhs, const temi_msgs__msg__MotorControl__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!temi_msgs__msg__MotorControl__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
temi_msgs__msg__MotorControl__Sequence__copy(
  const temi_msgs__msg__MotorControl__Sequence * input,
  temi_msgs__msg__MotorControl__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(temi_msgs__msg__MotorControl);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    temi_msgs__msg__MotorControl * data =
      (temi_msgs__msg__MotorControl *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!temi_msgs__msg__MotorControl__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          temi_msgs__msg__MotorControl__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!temi_msgs__msg__MotorControl__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
