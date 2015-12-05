// Generated by gencpp from file homography/matrix3_3.msg
// DO NOT EDIT!


#ifndef HOMOGRAPHY_MESSAGE_MATRIX3_3_H
#define HOMOGRAPHY_MESSAGE_MATRIX3_3_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace homography
{
template <class ContainerAllocator>
struct matrix3_3_
{
  typedef matrix3_3_<ContainerAllocator> Type;

  matrix3_3_()
    : e00(0.0)
    , e01(0.0)
    , e02(0.0)
    , e10(0.0)
    , e11(0.0)
    , e12(0.0)
    , e20(0.0)
    , e21(0.0)
    , e22(0.0)  {
    }
  matrix3_3_(const ContainerAllocator& _alloc)
    : e00(0.0)
    , e01(0.0)
    , e02(0.0)
    , e10(0.0)
    , e11(0.0)
    , e12(0.0)
    , e20(0.0)
    , e21(0.0)
    , e22(0.0)  {
    }



   typedef double _e00_type;
  _e00_type e00;

   typedef double _e01_type;
  _e01_type e01;

   typedef double _e02_type;
  _e02_type e02;

   typedef double _e10_type;
  _e10_type e10;

   typedef double _e11_type;
  _e11_type e11;

   typedef double _e12_type;
  _e12_type e12;

   typedef double _e20_type;
  _e20_type e20;

   typedef double _e21_type;
  _e21_type e21;

   typedef double _e22_type;
  _e22_type e22;




  typedef boost::shared_ptr< ::homography::matrix3_3_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::homography::matrix3_3_<ContainerAllocator> const> ConstPtr;

}; // struct matrix3_3_

typedef ::homography::matrix3_3_<std::allocator<void> > matrix3_3;

typedef boost::shared_ptr< ::homography::matrix3_3 > matrix3_3Ptr;
typedef boost::shared_ptr< ::homography::matrix3_3 const> matrix3_3ConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::homography::matrix3_3_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::homography::matrix3_3_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace homography

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/indigo/share/sensor_msgs/cmake/../msg'], 'homography': ['/home/cc/ee106a/fa15/class/ee106a-bc/final_proj/src/homography/msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::homography::matrix3_3_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::homography::matrix3_3_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::homography::matrix3_3_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::homography::matrix3_3_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::homography::matrix3_3_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::homography::matrix3_3_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::homography::matrix3_3_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d934169a54456b96185ffceeb96721ab";
  }

  static const char* value(const ::homography::matrix3_3_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd934169a54456b96ULL;
  static const uint64_t static_value2 = 0x185ffceeb96721abULL;
};

template<class ContainerAllocator>
struct DataType< ::homography::matrix3_3_<ContainerAllocator> >
{
  static const char* value()
  {
    return "homography/matrix3_3";
  }

  static const char* value(const ::homography::matrix3_3_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::homography::matrix3_3_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 e00\n\
float64 e01\n\
float64 e02\n\
float64 e10\n\
float64 e11\n\
float64 e12\n\
float64 e20\n\
float64 e21\n\
float64 e22\n\
";
  }

  static const char* value(const ::homography::matrix3_3_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::homography::matrix3_3_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.e00);
      stream.next(m.e01);
      stream.next(m.e02);
      stream.next(m.e10);
      stream.next(m.e11);
      stream.next(m.e12);
      stream.next(m.e20);
      stream.next(m.e21);
      stream.next(m.e22);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct matrix3_3_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::homography::matrix3_3_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::homography::matrix3_3_<ContainerAllocator>& v)
  {
    s << indent << "e00: ";
    Printer<double>::stream(s, indent + "  ", v.e00);
    s << indent << "e01: ";
    Printer<double>::stream(s, indent + "  ", v.e01);
    s << indent << "e02: ";
    Printer<double>::stream(s, indent + "  ", v.e02);
    s << indent << "e10: ";
    Printer<double>::stream(s, indent + "  ", v.e10);
    s << indent << "e11: ";
    Printer<double>::stream(s, indent + "  ", v.e11);
    s << indent << "e12: ";
    Printer<double>::stream(s, indent + "  ", v.e12);
    s << indent << "e20: ";
    Printer<double>::stream(s, indent + "  ", v.e20);
    s << indent << "e21: ";
    Printer<double>::stream(s, indent + "  ", v.e21);
    s << indent << "e22: ";
    Printer<double>::stream(s, indent + "  ", v.e22);
  }
};

} // namespace message_operations
} // namespace ros

#endif // HOMOGRAPHY_MESSAGE_MATRIX3_3_H
