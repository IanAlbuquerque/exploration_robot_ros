// Generated by gencpp from file homography/ImageSrv.msg
// DO NOT EDIT!


#ifndef HOMOGRAPHY_MESSAGE_IMAGESRV_H
#define HOMOGRAPHY_MESSAGE_IMAGESRV_H

#include <ros/service_traits.h>


#include <homography/ImageSrvRequest.h>
#include <homography/ImageSrvResponse.h>


namespace homography
{

struct ImageSrv
{

typedef ImageSrvRequest Request;
typedef ImageSrvResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct ImageSrv
} // namespace homography


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::homography::ImageSrv > {
  static const char* value()
  {
    return "ba55116f263d40ea8759822097ad63d4";
  }

  static const char* value(const ::homography::ImageSrv&) { return value(); }
};

template<>
struct DataType< ::homography::ImageSrv > {
  static const char* value()
  {
    return "homography/ImageSrv";
  }

  static const char* value(const ::homography::ImageSrv&) { return value(); }
};


// service_traits::MD5Sum< ::homography::ImageSrvRequest> should match 
// service_traits::MD5Sum< ::homography::ImageSrv > 
template<>
struct MD5Sum< ::homography::ImageSrvRequest>
{
  static const char* value()
  {
    return MD5Sum< ::homography::ImageSrv >::value();
  }
  static const char* value(const ::homography::ImageSrvRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::homography::ImageSrvRequest> should match 
// service_traits::DataType< ::homography::ImageSrv > 
template<>
struct DataType< ::homography::ImageSrvRequest>
{
  static const char* value()
  {
    return DataType< ::homography::ImageSrv >::value();
  }
  static const char* value(const ::homography::ImageSrvRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::homography::ImageSrvResponse> should match 
// service_traits::MD5Sum< ::homography::ImageSrv > 
template<>
struct MD5Sum< ::homography::ImageSrvResponse>
{
  static const char* value()
  {
    return MD5Sum< ::homography::ImageSrv >::value();
  }
  static const char* value(const ::homography::ImageSrvResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::homography::ImageSrvResponse> should match 
// service_traits::DataType< ::homography::ImageSrv > 
template<>
struct DataType< ::homography::ImageSrvResponse>
{
  static const char* value()
  {
    return DataType< ::homography::ImageSrv >::value();
  }
  static const char* value(const ::homography::ImageSrvResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // HOMOGRAPHY_MESSAGE_IMAGESRV_H
