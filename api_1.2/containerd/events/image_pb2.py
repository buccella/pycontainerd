# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: containerd/events/image.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from containerd.protobuf.plugin import fieldpath_pb2 as containerd_dot_protobuf_dot_plugin_dot_fieldpath__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='containerd/events/image.proto',
  package='containerd.services.images.v1',
  syntax='proto3',
  serialized_options=_b('Z2github.com/containerd/containerd/api/events;events\240\364\036\001'),
  serialized_pb=_b('\n\x1d\x63ontainerd/events/image.proto\x12\x1d\x63ontainerd.services.images.v1\x1a*containerd/protobuf/plugin/fieldpath.proto\"\x92\x01\n\x0bImageCreate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x46\n\x06labels\x18\x02 \x03(\x0b\x32\x36.containerd.services.images.v1.ImageCreate.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x92\x01\n\x0bImageUpdate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x46\n\x06labels\x18\x02 \x03(\x0b\x32\x36.containerd.services.images.v1.ImageUpdate.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1b\n\x0bImageDelete\x12\x0c\n\x04name\x18\x01 \x01(\tB8Z2github.com/containerd/containerd/api/events;events\xa0\xf4\x1e\x01X\x00\x62\x06proto3')
  ,
  dependencies=[containerd_dot_protobuf_dot_plugin_dot_fieldpath__pb2.DESCRIPTOR,])




_IMAGECREATE_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='containerd.services.images.v1.ImageCreate.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='containerd.services.images.v1.ImageCreate.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='containerd.services.images.v1.ImageCreate.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=255,
)

_IMAGECREATE = _descriptor.Descriptor(
  name='ImageCreate',
  full_name='containerd.services.images.v1.ImageCreate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='containerd.services.images.v1.ImageCreate.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='containerd.services.images.v1.ImageCreate.labels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_IMAGECREATE_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=255,
)


_IMAGEUPDATE_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='containerd.services.images.v1.ImageUpdate.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='containerd.services.images.v1.ImageUpdate.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='containerd.services.images.v1.ImageUpdate.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=255,
)

_IMAGEUPDATE = _descriptor.Descriptor(
  name='ImageUpdate',
  full_name='containerd.services.images.v1.ImageUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='containerd.services.images.v1.ImageUpdate.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='containerd.services.images.v1.ImageUpdate.labels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_IMAGEUPDATE_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=258,
  serialized_end=404,
)


_IMAGEDELETE = _descriptor.Descriptor(
  name='ImageDelete',
  full_name='containerd.services.images.v1.ImageDelete',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='containerd.services.images.v1.ImageDelete.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=406,
  serialized_end=433,
)

_IMAGECREATE_LABELSENTRY.containing_type = _IMAGECREATE
_IMAGECREATE.fields_by_name['labels'].message_type = _IMAGECREATE_LABELSENTRY
_IMAGEUPDATE_LABELSENTRY.containing_type = _IMAGEUPDATE
_IMAGEUPDATE.fields_by_name['labels'].message_type = _IMAGEUPDATE_LABELSENTRY
DESCRIPTOR.message_types_by_name['ImageCreate'] = _IMAGECREATE
DESCRIPTOR.message_types_by_name['ImageUpdate'] = _IMAGEUPDATE
DESCRIPTOR.message_types_by_name['ImageDelete'] = _IMAGEDELETE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageCreate = _reflection.GeneratedProtocolMessageType('ImageCreate', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _IMAGECREATE_LABELSENTRY,
    '__module__' : 'containerd.events.image_pb2'
    # @@protoc_insertion_point(class_scope:containerd.services.images.v1.ImageCreate.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _IMAGECREATE,
  '__module__' : 'containerd.events.image_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.images.v1.ImageCreate)
  })
_sym_db.RegisterMessage(ImageCreate)
_sym_db.RegisterMessage(ImageCreate.LabelsEntry)

ImageUpdate = _reflection.GeneratedProtocolMessageType('ImageUpdate', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _IMAGEUPDATE_LABELSENTRY,
    '__module__' : 'containerd.events.image_pb2'
    # @@protoc_insertion_point(class_scope:containerd.services.images.v1.ImageUpdate.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _IMAGEUPDATE,
  '__module__' : 'containerd.events.image_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.images.v1.ImageUpdate)
  })
_sym_db.RegisterMessage(ImageUpdate)
_sym_db.RegisterMessage(ImageUpdate.LabelsEntry)

ImageDelete = _reflection.GeneratedProtocolMessageType('ImageDelete', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEDELETE,
  '__module__' : 'containerd.events.image_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.images.v1.ImageDelete)
  })
_sym_db.RegisterMessage(ImageDelete)


DESCRIPTOR._options = None
_IMAGECREATE_LABELSENTRY._options = None
_IMAGEUPDATE_LABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)