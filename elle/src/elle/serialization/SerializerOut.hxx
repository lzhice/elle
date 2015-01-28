#ifndef ELLE_SERIALIZATION_SERIALIZER_OUT_HXX
# define ELLE_SERIALIZATION_SERIALIZER_OUT_HXX

namespace elle
{
  namespace serialization
  {
    template <typename T>
    void
    SerializerOut::serialize_forward(T const& v)
    {
      this->Serializer::serialize_forward(const_cast<T&>(v));
    }
  }
}

#endif
