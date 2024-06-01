// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from pupper_interfaces:srv/GoPupper.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "pupper_interfaces/srv/detail/go_pupper__rosidl_typesupport_introspection_c.h"
#include "pupper_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "pupper_interfaces/srv/detail/go_pupper__functions.h"
#include "pupper_interfaces/srv/detail/go_pupper__struct.h"


// Include directives for member types
// Member `command`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void pupper_interfaces__srv__GoPupper_Request__rosidl_typesupport_introspection_c__GoPupper_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  pupper_interfaces__srv__GoPupper_Request__init(message_memory);
}

void pupper_interfaces__srv__GoPupper_Request__rosidl_typesupport_introspection_c__GoPupper_Request_fini_function(void * message_memory)
{
  pupper_interfaces__srv__GoPupper_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember pupper_interfaces__srv__GoPupper_Request__rosidl_typesupport_introspection_c__GoPupper_Request_message_member_array[1] = {
  {
    "command",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(pupper_interfaces__srv__GoPupper_Request, command),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers pupper_interfaces__srv__GoPupper_Request__rosidl_typesupport_introspection_c__GoPupper_Request_message_members = {
  "pupper_interfaces__srv",  // message namespace
  "GoPupper_Request",  // message name
  1,  // number of fields
  sizeof(pupper_interfaces__srv__GoPupper_Request),
  pupper_interfaces__srv__GoPupper_Request__rosidl_typesupport_introspection_c__GoPupper_Request_message_member_array,  // message members
  pupper_interfaces__srv__GoPupper_Request__rosidl_typesupport_introspection_c__GoPupper_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  pupper_interfaces__srv__GoPupper_Request__rosidl_typesupport_introspection_c__GoPupper_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t pupper_interfaces__srv__GoPupper_Request__rosidl_typesupport_introspection_c__GoPupper_Request_message_type_support_handle = {
  0,
  &pupper_interfaces__srv__GoPupper_Request__rosidl_typesupport_introspection_c__GoPupper_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_pupper_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pupper_interfaces, srv, GoPupper_Request)() {
  if (!pupper_interfaces__srv__GoPupper_Request__rosidl_typesupport_introspection_c__GoPupper_Request_message_type_support_handle.typesupport_identifier) {
    pupper_interfaces__srv__GoPupper_Request__rosidl_typesupport_introspection_c__GoPupper_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &pupper_interfaces__srv__GoPupper_Request__rosidl_typesupport_introspection_c__GoPupper_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "pupper_interfaces/srv/detail/go_pupper__rosidl_typesupport_introspection_c.h"
// already included above
// #include "pupper_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "pupper_interfaces/srv/detail/go_pupper__functions.h"
// already included above
// #include "pupper_interfaces/srv/detail/go_pupper__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void pupper_interfaces__srv__GoPupper_Response__rosidl_typesupport_introspection_c__GoPupper_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  pupper_interfaces__srv__GoPupper_Response__init(message_memory);
}

void pupper_interfaces__srv__GoPupper_Response__rosidl_typesupport_introspection_c__GoPupper_Response_fini_function(void * message_memory)
{
  pupper_interfaces__srv__GoPupper_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember pupper_interfaces__srv__GoPupper_Response__rosidl_typesupport_introspection_c__GoPupper_Response_message_member_array[1] = {
  {
    "executed",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(pupper_interfaces__srv__GoPupper_Response, executed),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers pupper_interfaces__srv__GoPupper_Response__rosidl_typesupport_introspection_c__GoPupper_Response_message_members = {
  "pupper_interfaces__srv",  // message namespace
  "GoPupper_Response",  // message name
  1,  // number of fields
  sizeof(pupper_interfaces__srv__GoPupper_Response),
  pupper_interfaces__srv__GoPupper_Response__rosidl_typesupport_introspection_c__GoPupper_Response_message_member_array,  // message members
  pupper_interfaces__srv__GoPupper_Response__rosidl_typesupport_introspection_c__GoPupper_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  pupper_interfaces__srv__GoPupper_Response__rosidl_typesupport_introspection_c__GoPupper_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t pupper_interfaces__srv__GoPupper_Response__rosidl_typesupport_introspection_c__GoPupper_Response_message_type_support_handle = {
  0,
  &pupper_interfaces__srv__GoPupper_Response__rosidl_typesupport_introspection_c__GoPupper_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_pupper_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pupper_interfaces, srv, GoPupper_Response)() {
  if (!pupper_interfaces__srv__GoPupper_Response__rosidl_typesupport_introspection_c__GoPupper_Response_message_type_support_handle.typesupport_identifier) {
    pupper_interfaces__srv__GoPupper_Response__rosidl_typesupport_introspection_c__GoPupper_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &pupper_interfaces__srv__GoPupper_Response__rosidl_typesupport_introspection_c__GoPupper_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "pupper_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "pupper_interfaces/srv/detail/go_pupper__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers pupper_interfaces__srv__detail__go_pupper__rosidl_typesupport_introspection_c__GoPupper_service_members = {
  "pupper_interfaces__srv",  // service namespace
  "GoPupper",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // pupper_interfaces__srv__detail__go_pupper__rosidl_typesupport_introspection_c__GoPupper_Request_message_type_support_handle,
  NULL  // response message
  // pupper_interfaces__srv__detail__go_pupper__rosidl_typesupport_introspection_c__GoPupper_Response_message_type_support_handle
};

static rosidl_service_type_support_t pupper_interfaces__srv__detail__go_pupper__rosidl_typesupport_introspection_c__GoPupper_service_type_support_handle = {
  0,
  &pupper_interfaces__srv__detail__go_pupper__rosidl_typesupport_introspection_c__GoPupper_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pupper_interfaces, srv, GoPupper_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pupper_interfaces, srv, GoPupper_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_pupper_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pupper_interfaces, srv, GoPupper)() {
  if (!pupper_interfaces__srv__detail__go_pupper__rosidl_typesupport_introspection_c__GoPupper_service_type_support_handle.typesupport_identifier) {
    pupper_interfaces__srv__detail__go_pupper__rosidl_typesupport_introspection_c__GoPupper_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)pupper_interfaces__srv__detail__go_pupper__rosidl_typesupport_introspection_c__GoPupper_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pupper_interfaces, srv, GoPupper_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pupper_interfaces, srv, GoPupper_Response)()->data;
  }

  return &pupper_interfaces__srv__detail__go_pupper__rosidl_typesupport_introspection_c__GoPupper_service_type_support_handle;
}
