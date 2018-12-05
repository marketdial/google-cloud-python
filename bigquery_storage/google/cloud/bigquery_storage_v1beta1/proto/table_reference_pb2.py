# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/bigquery/storage_v1beta1/proto/table_reference.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/bigquery/storage_v1beta1/proto/table_reference.proto",
    package="google.cloud.bigquery.storage.v1beta1",
    syntax="proto3",
    serialized_pb=_b(
        '\nAgoogle/cloud/bigquery/storage_v1beta1/proto/table_reference.proto\x12%google.cloud.bigquery.storage.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto"J\n\x0eTableReference\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\x10\n\x08table_id\x18\x03 \x01(\t"C\n\x0eTableModifiers\x12\x31\n\rsnapshot_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x8e\x01\n)com.google.cloud.bigquery.storage.v1beta1B\x13TableReferenceProtoZLgoogle.golang.org/genproto/googleapis/cloud/bigquery/storage/v1beta1;storageb\x06proto3'
    ),
    dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR],
)


_TABLEREFERENCE = _descriptor.Descriptor(
    name="TableReference",
    full_name="google.cloud.bigquery.storage.v1beta1.TableReference",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="project_id",
            full_name="google.cloud.bigquery.storage.v1beta1.TableReference.project_id",
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
            name="dataset_id",
            full_name="google.cloud.bigquery.storage.v1beta1.TableReference.dataset_id",
            index=1,
            number=2,
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
            name="table_id",
            full_name="google.cloud.bigquery.storage.v1beta1.TableReference.table_id",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=141,
    serialized_end=215,
)


_TABLEMODIFIERS = _descriptor.Descriptor(
    name="TableModifiers",
    full_name="google.cloud.bigquery.storage.v1beta1.TableModifiers",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="snapshot_time",
            full_name="google.cloud.bigquery.storage.v1beta1.TableModifiers.snapshot_time",
            index=0,
            number=1,
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
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=217,
    serialized_end=284,
)

_TABLEMODIFIERS.fields_by_name[
    "snapshot_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name["TableReference"] = _TABLEREFERENCE
DESCRIPTOR.message_types_by_name["TableModifiers"] = _TABLEMODIFIERS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TableReference = _reflection.GeneratedProtocolMessageType(
    "TableReference",
    (_message.Message,),
    dict(
        DESCRIPTOR=_TABLEREFERENCE,
        __module__="google.cloud.bigquery.storage_v1beta1.proto.table_reference_pb2",
        __doc__="""Table reference that includes just the 3 strings needed to identify a
  table.
  
  
  Attributes:
      project_id:
          The assigned project ID of the project.
      dataset_id:
          The ID of the dataset in the above project.
      table_id:
          The ID of the table in the above dataset.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.bigquery.storage.v1beta1.TableReference)
    ),
)
_sym_db.RegisterMessage(TableReference)

TableModifiers = _reflection.GeneratedProtocolMessageType(
    "TableModifiers",
    (_message.Message,),
    dict(
        DESCRIPTOR=_TABLEMODIFIERS,
        __module__="google.cloud.bigquery.storage_v1beta1.proto.table_reference_pb2",
        __doc__="""All fields in this message optional.
  
  
  Attributes:
      snapshot_time:
          The snapshot time of the table. If not set, interpreted as
          now.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.bigquery.storage.v1beta1.TableModifiers)
    ),
)
_sym_db.RegisterMessage(TableModifiers)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(
    descriptor_pb2.FileOptions(),
    _b(
        "\n)com.google.cloud.bigquery.storage.v1beta1B\023TableReferenceProtoZLgoogle.golang.org/genproto/googleapis/cloud/bigquery/storage/v1beta1;storage"
    ),
)
# @@protoc_insertion_point(module_scope)
