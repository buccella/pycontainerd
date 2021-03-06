# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from containerd.services.introspection.v1 import introspection_pb2 as containerd_dot_services_dot_introspection_dot_v1_dot_introspection__pb2


class IntrospectionStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Plugins = channel.unary_unary(
        '/containerd.services.introspection.v1.Introspection/Plugins',
        request_serializer=containerd_dot_services_dot_introspection_dot_v1_dot_introspection__pb2.PluginsRequest.SerializeToString,
        response_deserializer=containerd_dot_services_dot_introspection_dot_v1_dot_introspection__pb2.PluginsResponse.FromString,
        )


class IntrospectionServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Plugins(self, request, context):
    """Plugins returns a list of plugins in containerd.

    Clients can use this to detect features and capabilities when using
    containerd.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_IntrospectionServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Plugins': grpc.unary_unary_rpc_method_handler(
          servicer.Plugins,
          request_deserializer=containerd_dot_services_dot_introspection_dot_v1_dot_introspection__pb2.PluginsRequest.FromString,
          response_serializer=containerd_dot_services_dot_introspection_dot_v1_dot_introspection__pb2.PluginsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'containerd.services.introspection.v1.Introspection', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
