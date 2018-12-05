# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/websecurityscanner_v1alpha/proto/finding.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.websecurityscanner_v1alpha.proto import (
    finding_addon_pb2 as google_dot_cloud_dot_websecurityscanner__v1alpha_dot_proto_dot_finding__addon__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/websecurityscanner_v1alpha/proto/finding.proto",
    package="google.cloud.websecurityscanner.v1alpha",
    syntax="proto3",
    serialized_pb=_b(
        '\n;google/cloud/websecurityscanner_v1alpha/proto/finding.proto\x12\'google.cloud.websecurityscanner.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x41google/cloud/websecurityscanner_v1alpha/proto/finding_addon.proto"\xf5\x05\n\x07\x46inding\x12\x0c\n\x04name\x18\x01 \x01(\t\x12R\n\x0c\x66inding_type\x18\x02 \x01(\x0e\x32<.google.cloud.websecurityscanner.v1alpha.Finding.FindingType\x12\x13\n\x0bhttp_method\x18\x03 \x01(\t\x12\x12\n\nfuzzed_url\x18\x04 \x01(\t\x12\x0c\n\x04\x62ody\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x18\n\x10reproduction_url\x18\x07 \x01(\t\x12\x11\n\tframe_url\x18\x08 \x01(\t\x12\x11\n\tfinal_url\x18\t \x01(\t\x12\x13\n\x0btracking_id\x18\n \x01(\t\x12R\n\x10outdated_library\x18\x0b \x01(\x0b\x32\x38.google.cloud.websecurityscanner.v1alpha.OutdatedLibrary\x12V\n\x12violating_resource\x18\x0c \x01(\x0b\x32:.google.cloud.websecurityscanner.v1alpha.ViolatingResource\x12\\\n\x15vulnerable_parameters\x18\r \x01(\x0b\x32=.google.cloud.websecurityscanner.v1alpha.VulnerableParameters\x12\x39\n\x03xss\x18\x0e \x01(\x0b\x32,.google.cloud.websecurityscanner.v1alpha.Xss"\xa1\x01\n\x0b\x46indingType\x12\x1c\n\x18\x46INDING_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rMIXED_CONTENT\x10\x01\x12\x14\n\x10OUTDATED_LIBRARY\x10\x02\x12\x11\n\rROSETTA_FLASH\x10\x05\x12\x10\n\x0cXSS_CALLBACK\x10\x03\x12\r\n\tXSS_ERROR\x10\x04\x12\x17\n\x13\x43LEAR_TEXT_PASSWORD\x10\x06\x42\x98\x01\n+com.google.cloud.websecurityscanner.v1alphaB\x0c\x46indingProtoP\x01ZYgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1alpha;websecurityscannerb\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_cloud_dot_websecurityscanner__v1alpha_dot_proto_dot_finding__addon__pb2.DESCRIPTOR,
    ],
)


_FINDING_FINDINGTYPE = _descriptor.EnumDescriptor(
    name="FindingType",
    full_name="google.cloud.websecurityscanner.v1alpha.Finding.FindingType",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="FINDING_TYPE_UNSPECIFIED", index=0, number=0, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="MIXED_CONTENT", index=1, number=1, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="OUTDATED_LIBRARY", index=2, number=2, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="ROSETTA_FLASH", index=3, number=5, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="XSS_CALLBACK", index=4, number=3, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="XSS_ERROR", index=5, number=4, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="CLEAR_TEXT_PASSWORD", index=6, number=6, options=None, type=None
        ),
    ],
    containing_type=None,
    options=None,
    serialized_start=798,
    serialized_end=959,
)
_sym_db.RegisterEnumDescriptor(_FINDING_FINDINGTYPE)


_FINDING = _descriptor.Descriptor(
    name="Finding",
    full_name="google.cloud.websecurityscanner.v1alpha.Finding",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="finding_type",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.finding_type",
            index=1,
            number=2,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="http_method",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.http_method",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="fuzzed_url",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.fuzzed_url",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="body",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.body",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.description",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="reproduction_url",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.reproduction_url",
            index=6,
            number=7,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="frame_url",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.frame_url",
            index=7,
            number=8,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="final_url",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.final_url",
            index=8,
            number=9,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="tracking_id",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.tracking_id",
            index=9,
            number=10,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="outdated_library",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.outdated_library",
            index=10,
            number=11,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="violating_resource",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.violating_resource",
            index=11,
            number=12,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="vulnerable_parameters",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.vulnerable_parameters",
            index=12,
            number=13,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="xss",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.xss",
            index=13,
            number=14,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_FINDING_FINDINGTYPE],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=202,
    serialized_end=959,
)

_FINDING.fields_by_name["finding_type"].enum_type = _FINDING_FINDINGTYPE
_FINDING.fields_by_name[
    "outdated_library"
].message_type = (
    google_dot_cloud_dot_websecurityscanner__v1alpha_dot_proto_dot_finding__addon__pb2._OUTDATEDLIBRARY
)
_FINDING.fields_by_name[
    "violating_resource"
].message_type = (
    google_dot_cloud_dot_websecurityscanner__v1alpha_dot_proto_dot_finding__addon__pb2._VIOLATINGRESOURCE
)
_FINDING.fields_by_name[
    "vulnerable_parameters"
].message_type = (
    google_dot_cloud_dot_websecurityscanner__v1alpha_dot_proto_dot_finding__addon__pb2._VULNERABLEPARAMETERS
)
_FINDING.fields_by_name[
    "xss"
].message_type = (
    google_dot_cloud_dot_websecurityscanner__v1alpha_dot_proto_dot_finding__addon__pb2._XSS
)
_FINDING_FINDINGTYPE.containing_type = _FINDING
DESCRIPTOR.message_types_by_name["Finding"] = _FINDING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Finding = _reflection.GeneratedProtocolMessageType(
    "Finding",
    (_message.Message,),
    dict(
        DESCRIPTOR=_FINDING,
        __module__="google.cloud.websecurityscanner_v1alpha.proto.finding_pb2",
        __doc__="""A Finding resource represents a vulnerability instance identified during
  a ScanRun.
  
  
  Attributes:
      name:
          Output only. The resource name of the Finding. The name
          follows the format of 'projects/{projectId}/scanConfigs/{scanC
          onfigId}/scanruns/{scanRunId}/findings/{findingId}'. The
          finding IDs are generated by the system.
      finding_type:
          Output only. The type of the Finding.
      http_method:
          Output only. The http method of the request that triggered the
          vulnerability, in uppercase.
      fuzzed_url:
          Output only. The URL produced by the server-side fuzzer and
          used in the request that triggered the vulnerability.
      body:
          Output only. The body of the request that triggered the
          vulnerability.
      description:
          Output only. The description of the vulnerability.
      reproduction_url:
          Output only. The URL containing human-readable payload that
          user can leverage to reproduce the vulnerability.
      frame_url:
          Output only. If the vulnerability was originated from nested
          IFrame, the immediate parent IFrame is reported.
      final_url:
          Output only. The URL where the browser lands when the
          vulnerability is detected.
      tracking_id:
          Output only. The tracking ID uniquely identifies a
          vulnerability instance across multiple ScanRuns.
      outdated_library:
          Output only. An addon containing information about outdated
          libraries.
      violating_resource:
          Output only. An addon containing detailed information
          regarding any resource causing the vulnerability such as
          JavaScript sources, image, audio files, etc.
      vulnerable_parameters:
          Output only. An addon containing information about request
          parameters which were found to be vulnerable.
      xss:
          Output only. An addon containing information reported for an
          XSS, if any.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1alpha.Finding)
    ),
)
_sym_db.RegisterMessage(Finding)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(
    descriptor_pb2.FileOptions(),
    _b(
        "\n+com.google.cloud.websecurityscanner.v1alphaB\014FindingProtoP\001ZYgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1alpha;websecurityscanner"
    ),
)
# @@protoc_insertion_point(module_scope)
