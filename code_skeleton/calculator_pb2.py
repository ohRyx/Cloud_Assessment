# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63\x61lculator.proto\x12\ncalculator\"\x1f\n\x07Request\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\"\x14\n\x05Reply\x12\x0b\n\x03res\x18\x01 \x01(\x05\x32\xd8\x01\n\nCalculator\x12/\n\x03\x41\x64\x64\x12\x13.calculator.Request\x1a\x11.calculator.Reply\"\x00\x12/\n\x03Sub\x12\x13.calculator.Request\x1a\x11.calculator.Reply\"\x00\x12\x34\n\x08Multiply\x12\x13.calculator.Request\x1a\x11.calculator.Reply\"\x00\x12\x32\n\x06\x44ivide\x12\x13.calculator.Request\x1a\x11.calculator.Reply\"\x00\x62\x06proto3')



_REQUEST = DESCRIPTOR.message_types_by_name['Request']
_REPLY = DESCRIPTOR.message_types_by_name['Reply']
Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:calculator.Request)
  })
_sym_db.RegisterMessage(Request)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), {
  'DESCRIPTOR' : _REPLY,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:calculator.Reply)
  })
_sym_db.RegisterMessage(Reply)

_CALCULATOR = DESCRIPTOR.services_by_name['Calculator']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=32
  _REQUEST._serialized_end=63
  _REPLY._serialized_start=65
  _REPLY._serialized_end=85
  _CALCULATOR._serialized_start=88
  _CALCULATOR._serialized_end=304
# @@protoc_insertion_point(module_scope)
