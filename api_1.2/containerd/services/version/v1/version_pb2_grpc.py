# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from containerd.services.version.v1 import version_pb2 as containerd_dot_services_dot_version_dot_v1_dot_version__pb2
from containerd.vendor.google.protobuf import empty_pb2 as containerd_dot_vendor_dot_google_dot_protobuf_dot_empty__pb2


class VersionStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Version = channel.unary_unary(
        '/containerd.services.version.v1.Version/Version',
        request_serializer=containerd_dot_vendor_dot_google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=containerd_dot_services_dot_version_dot_v1_dot_version__pb2.VersionResponse.FromString,
        )


class VersionServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Version(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_VersionServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Version': grpc.unary_unary_rpc_method_handler(
          servicer.Version,
          request_deserializer=containerd_dot_vendor_dot_google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=containerd_dot_services_dot_version_dot_v1_dot_version__pb2.VersionResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'containerd.services.version.v1.Version', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
