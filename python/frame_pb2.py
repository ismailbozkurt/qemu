# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='frame.proto',
  package='',
  serialized_pb='\n\x0b\x66rame.proto\"\xed\x01\n\x05\x66rame\x12\x1d\n\tstd_frame\x18\x01 \x01(\x0b\x32\n.std_frame\x12%\n\rsyscall_frame\x18\x02 \x01(\x0b\x32\x0e.syscall_frame\x12)\n\x0f\x65xception_frame\x18\x03 \x01(\x0b\x32\x10.exception_frame\x12-\n\x11taint_intro_frame\x18\x04 \x01(\x0b\x32\x12.taint_intro_frame\x12%\n\rmodload_frame\x18\x05 \x01(\x0b\x32\x0e.modload_frame\x12\x1d\n\tkey_frame\x18\x06 \x01(\x0b\x32\n.key_frame\"1\n\x12operand_value_list\x12\x1b\n\x04\x65lem\x18\x01 \x03(\x0b\x32\r.operand_info\"\xb0\x01\n\x0coperand_info\x12\x35\n\x15operand_info_specific\x18\x01 \x02(\x0b\x32\x16.operand_info_specific\x12\x12\n\nbit_length\x18\x02 \x02(\x11\x12%\n\roperand_usage\x18\x03 \x02(\x0b\x32\x0e.operand_usage\x12\x1f\n\ntaint_info\x18\x04 \x02(\x0b\x32\x0b.taint_info\x12\r\n\x05value\x18\x05 \x02(\x0c\"]\n\x15operand_info_specific\x12!\n\x0bmem_operand\x18\x01 \x01(\x0b\x32\x0c.mem_operand\x12!\n\x0breg_operand\x18\x02 \x01(\x0b\x32\x0c.reg_operand\"\x1b\n\x0breg_operand\x12\x0c\n\x04name\x18\x01 \x02(\t\"\x1e\n\x0bmem_operand\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x02(\x04\"K\n\roperand_usage\x12\x0c\n\x04read\x18\x01 \x02(\x08\x12\x0f\n\x07written\x18\x02 \x02(\x08\x12\r\n\x05index\x18\x03 \x02(\x08\x12\x0c\n\x04\x62\x61se\x18\x04 \x02(\x08\"H\n\ntaint_info\x12\x10\n\x08no_taint\x18\x01 \x01(\x08\x12\x10\n\x08taint_id\x18\x02 \x01(\x04\x12\x16\n\x0etaint_multiple\x18\x03 \x01(\x08\"\xa0\x01\n\tstd_frame\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x02(\x04\x12\x11\n\tthread_id\x18\x02 \x02(\x04\x12\x10\n\x08rawbytes\x18\x03 \x02(\x0c\x12-\n\x10operand_pre_list\x18\x04 \x02(\x0b\x32\x13.operand_value_list\x12.\n\x11operand_post_list\x18\x05 \x01(\x0b\x32\x13.operand_value_list\"j\n\rsyscall_frame\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x02(\x04\x12\x11\n\tthread_id\x18\x02 \x02(\x04\x12\x0e\n\x06number\x18\x03 \x02(\x04\x12%\n\rargument_list\x18\x04 \x02(\x0b\x32\x0e.argument_list\"\x1d\n\rargument_list\x12\x0c\n\x04\x65lem\x18\x01 \x03(\x12\"b\n\x0f\x65xception_frame\x12\x18\n\x10\x65xception_number\x18\x01 \x02(\x04\x12\x11\n\tthread_id\x18\x02 \x01(\x04\x12\x11\n\tfrom_addr\x18\x03 \x01(\x04\x12\x0f\n\x07to_addr\x18\x04 \x01(\x04\"@\n\x11taint_intro_frame\x12+\n\x10taint_intro_list\x18\x01 \x02(\x0b\x32\x11.taint_intro_list\".\n\x10taint_intro_list\x12\x1a\n\x04\x65lem\x18\x01 \x03(\x0b\x32\x0c.taint_intro\"a\n\x0btaint_intro\x12\x0c\n\x04\x61\x64\x64r\x18\x01 \x02(\x04\x12\x10\n\x08taint_id\x18\x02 \x02(\x04\x12\r\n\x05value\x18\x03 \x01(\x0c\x12\x13\n\x0bsource_name\x18\x04 \x01(\t\x12\x0e\n\x06offset\x18\x05 \x01(\x04\"O\n\rmodload_frame\x12\x13\n\x0bmodule_name\x18\x01 \x02(\t\x12\x13\n\x0blow_address\x18\x02 \x02(\x04\x12\x14\n\x0chigh_address\x18\x03 \x02(\x04\"<\n\tkey_frame\x12/\n\x12tagged_value_lists\x18\x01 \x02(\x0b\x32\x13.tagged_value_lists\"6\n\x12tagged_value_lists\x12 \n\x04\x65lem\x18\x01 \x03(\x0b\x32\x12.tagged_value_list\"a\n\x11tagged_value_list\x12+\n\x10value_source_tag\x18\x01 \x02(\x0b\x32\x11.value_source_tag\x12\x1f\n\nvalue_list\x18\x02 \x02(\x0b\x32\x0b.value_list\";\n\x10value_source_tag\x12\x14\n\x0cno_thread_id\x18\x01 \x01(\x08\x12\x11\n\tthread_id\x18\x02 \x01(\x04\"\'\n\nvalue_list\x12\x19\n\x04\x65lem\x18\x01 \x03(\x0b\x32\x0b.value_info\"\x87\x01\n\nvalue_info\x12\x35\n\x15operand_info_specific\x18\x01 \x02(\x0b\x32\x16.operand_info_specific\x12\x12\n\nbit_length\x18\x02 \x02(\x11\x12\x1f\n\ntaint_info\x18\x03 \x01(\x0b\x32\x0b.taint_info\x12\r\n\x05value\x18\x04 \x02(\x0c')




_FRAME = descriptor.Descriptor(
  name='frame',
  full_name='frame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='std_frame', full_name='frame.std_frame', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='syscall_frame', full_name='frame.syscall_frame', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='exception_frame', full_name='frame.exception_frame', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='taint_intro_frame', full_name='frame.taint_intro_frame', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='modload_frame', full_name='frame.modload_frame', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='key_frame', full_name='frame.key_frame', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=16,
  serialized_end=253,
)


_OPERAND_VALUE_LIST = descriptor.Descriptor(
  name='operand_value_list',
  full_name='operand_value_list',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='elem', full_name='operand_value_list.elem', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=255,
  serialized_end=304,
)


_OPERAND_INFO = descriptor.Descriptor(
  name='operand_info',
  full_name='operand_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='operand_info_specific', full_name='operand_info.operand_info_specific', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bit_length', full_name='operand_info.bit_length', index=1,
      number=2, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='operand_usage', full_name='operand_info.operand_usage', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='taint_info', full_name='operand_info.taint_info', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='operand_info.value', index=4,
      number=5, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=307,
  serialized_end=483,
)


_OPERAND_INFO_SPECIFIC = descriptor.Descriptor(
  name='operand_info_specific',
  full_name='operand_info_specific',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='mem_operand', full_name='operand_info_specific.mem_operand', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='reg_operand', full_name='operand_info_specific.reg_operand', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=485,
  serialized_end=578,
)


_REG_OPERAND = descriptor.Descriptor(
  name='reg_operand',
  full_name='reg_operand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='reg_operand.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=580,
  serialized_end=607,
)


_MEM_OPERAND = descriptor.Descriptor(
  name='mem_operand',
  full_name='mem_operand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='address', full_name='mem_operand.address', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=609,
  serialized_end=639,
)


_OPERAND_USAGE = descriptor.Descriptor(
  name='operand_usage',
  full_name='operand_usage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='read', full_name='operand_usage.read', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='written', full_name='operand_usage.written', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='index', full_name='operand_usage.index', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='base', full_name='operand_usage.base', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=641,
  serialized_end=716,
)


_TAINT_INFO = descriptor.Descriptor(
  name='taint_info',
  full_name='taint_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='no_taint', full_name='taint_info.no_taint', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='taint_id', full_name='taint_info.taint_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='taint_multiple', full_name='taint_info.taint_multiple', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=718,
  serialized_end=790,
)


_STD_FRAME = descriptor.Descriptor(
  name='std_frame',
  full_name='std_frame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='address', full_name='std_frame.address', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='thread_id', full_name='std_frame.thread_id', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rawbytes', full_name='std_frame.rawbytes', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='operand_pre_list', full_name='std_frame.operand_pre_list', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='operand_post_list', full_name='std_frame.operand_post_list', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=793,
  serialized_end=953,
)


_SYSCALL_FRAME = descriptor.Descriptor(
  name='syscall_frame',
  full_name='syscall_frame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='address', full_name='syscall_frame.address', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='thread_id', full_name='syscall_frame.thread_id', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='number', full_name='syscall_frame.number', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='argument_list', full_name='syscall_frame.argument_list', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=955,
  serialized_end=1061,
)


_ARGUMENT_LIST = descriptor.Descriptor(
  name='argument_list',
  full_name='argument_list',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='elem', full_name='argument_list.elem', index=0,
      number=1, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1063,
  serialized_end=1092,
)


_EXCEPTION_FRAME = descriptor.Descriptor(
  name='exception_frame',
  full_name='exception_frame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='exception_number', full_name='exception_frame.exception_number', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='thread_id', full_name='exception_frame.thread_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='from_addr', full_name='exception_frame.from_addr', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='to_addr', full_name='exception_frame.to_addr', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1094,
  serialized_end=1192,
)


_TAINT_INTRO_FRAME = descriptor.Descriptor(
  name='taint_intro_frame',
  full_name='taint_intro_frame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='taint_intro_list', full_name='taint_intro_frame.taint_intro_list', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1194,
  serialized_end=1258,
)


_TAINT_INTRO_LIST = descriptor.Descriptor(
  name='taint_intro_list',
  full_name='taint_intro_list',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='elem', full_name='taint_intro_list.elem', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1260,
  serialized_end=1306,
)


_TAINT_INTRO = descriptor.Descriptor(
  name='taint_intro',
  full_name='taint_intro',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='addr', full_name='taint_intro.addr', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='taint_id', full_name='taint_intro.taint_id', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='taint_intro.value', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='source_name', full_name='taint_intro.source_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='offset', full_name='taint_intro.offset', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1308,
  serialized_end=1405,
)


_MODLOAD_FRAME = descriptor.Descriptor(
  name='modload_frame',
  full_name='modload_frame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='module_name', full_name='modload_frame.module_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='low_address', full_name='modload_frame.low_address', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='high_address', full_name='modload_frame.high_address', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1407,
  serialized_end=1486,
)


_KEY_FRAME = descriptor.Descriptor(
  name='key_frame',
  full_name='key_frame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='tagged_value_lists', full_name='key_frame.tagged_value_lists', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1488,
  serialized_end=1548,
)


_TAGGED_VALUE_LISTS = descriptor.Descriptor(
  name='tagged_value_lists',
  full_name='tagged_value_lists',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='elem', full_name='tagged_value_lists.elem', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1550,
  serialized_end=1604,
)


_TAGGED_VALUE_LIST = descriptor.Descriptor(
  name='tagged_value_list',
  full_name='tagged_value_list',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='value_source_tag', full_name='tagged_value_list.value_source_tag', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value_list', full_name='tagged_value_list.value_list', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1606,
  serialized_end=1703,
)


_VALUE_SOURCE_TAG = descriptor.Descriptor(
  name='value_source_tag',
  full_name='value_source_tag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='no_thread_id', full_name='value_source_tag.no_thread_id', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='thread_id', full_name='value_source_tag.thread_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1705,
  serialized_end=1764,
)


_VALUE_LIST = descriptor.Descriptor(
  name='value_list',
  full_name='value_list',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='elem', full_name='value_list.elem', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1766,
  serialized_end=1805,
)


_VALUE_INFO = descriptor.Descriptor(
  name='value_info',
  full_name='value_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='operand_info_specific', full_name='value_info.operand_info_specific', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bit_length', full_name='value_info.bit_length', index=1,
      number=2, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='taint_info', full_name='value_info.taint_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='value_info.value', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1808,
  serialized_end=1943,
)

_FRAME.fields_by_name['std_frame'].message_type = _STD_FRAME
_FRAME.fields_by_name['syscall_frame'].message_type = _SYSCALL_FRAME
_FRAME.fields_by_name['exception_frame'].message_type = _EXCEPTION_FRAME
_FRAME.fields_by_name['taint_intro_frame'].message_type = _TAINT_INTRO_FRAME
_FRAME.fields_by_name['modload_frame'].message_type = _MODLOAD_FRAME
_FRAME.fields_by_name['key_frame'].message_type = _KEY_FRAME
_OPERAND_VALUE_LIST.fields_by_name['elem'].message_type = _OPERAND_INFO
_OPERAND_INFO.fields_by_name['operand_info_specific'].message_type = _OPERAND_INFO_SPECIFIC
_OPERAND_INFO.fields_by_name['operand_usage'].message_type = _OPERAND_USAGE
_OPERAND_INFO.fields_by_name['taint_info'].message_type = _TAINT_INFO
_OPERAND_INFO_SPECIFIC.fields_by_name['mem_operand'].message_type = _MEM_OPERAND
_OPERAND_INFO_SPECIFIC.fields_by_name['reg_operand'].message_type = _REG_OPERAND
_STD_FRAME.fields_by_name['operand_pre_list'].message_type = _OPERAND_VALUE_LIST
_STD_FRAME.fields_by_name['operand_post_list'].message_type = _OPERAND_VALUE_LIST
_SYSCALL_FRAME.fields_by_name['argument_list'].message_type = _ARGUMENT_LIST
_TAINT_INTRO_FRAME.fields_by_name['taint_intro_list'].message_type = _TAINT_INTRO_LIST
_TAINT_INTRO_LIST.fields_by_name['elem'].message_type = _TAINT_INTRO
_KEY_FRAME.fields_by_name['tagged_value_lists'].message_type = _TAGGED_VALUE_LISTS
_TAGGED_VALUE_LISTS.fields_by_name['elem'].message_type = _TAGGED_VALUE_LIST
_TAGGED_VALUE_LIST.fields_by_name['value_source_tag'].message_type = _VALUE_SOURCE_TAG
_TAGGED_VALUE_LIST.fields_by_name['value_list'].message_type = _VALUE_LIST
_VALUE_LIST.fields_by_name['elem'].message_type = _VALUE_INFO
_VALUE_INFO.fields_by_name['operand_info_specific'].message_type = _OPERAND_INFO_SPECIFIC
_VALUE_INFO.fields_by_name['taint_info'].message_type = _TAINT_INFO
DESCRIPTOR.message_types_by_name['frame'] = _FRAME
DESCRIPTOR.message_types_by_name['operand_value_list'] = _OPERAND_VALUE_LIST
DESCRIPTOR.message_types_by_name['operand_info'] = _OPERAND_INFO
DESCRIPTOR.message_types_by_name['operand_info_specific'] = _OPERAND_INFO_SPECIFIC
DESCRIPTOR.message_types_by_name['reg_operand'] = _REG_OPERAND
DESCRIPTOR.message_types_by_name['mem_operand'] = _MEM_OPERAND
DESCRIPTOR.message_types_by_name['operand_usage'] = _OPERAND_USAGE
DESCRIPTOR.message_types_by_name['taint_info'] = _TAINT_INFO
DESCRIPTOR.message_types_by_name['std_frame'] = _STD_FRAME
DESCRIPTOR.message_types_by_name['syscall_frame'] = _SYSCALL_FRAME
DESCRIPTOR.message_types_by_name['argument_list'] = _ARGUMENT_LIST
DESCRIPTOR.message_types_by_name['exception_frame'] = _EXCEPTION_FRAME
DESCRIPTOR.message_types_by_name['taint_intro_frame'] = _TAINT_INTRO_FRAME
DESCRIPTOR.message_types_by_name['taint_intro_list'] = _TAINT_INTRO_LIST
DESCRIPTOR.message_types_by_name['taint_intro'] = _TAINT_INTRO
DESCRIPTOR.message_types_by_name['modload_frame'] = _MODLOAD_FRAME
DESCRIPTOR.message_types_by_name['key_frame'] = _KEY_FRAME
DESCRIPTOR.message_types_by_name['tagged_value_lists'] = _TAGGED_VALUE_LISTS
DESCRIPTOR.message_types_by_name['tagged_value_list'] = _TAGGED_VALUE_LIST
DESCRIPTOR.message_types_by_name['value_source_tag'] = _VALUE_SOURCE_TAG
DESCRIPTOR.message_types_by_name['value_list'] = _VALUE_LIST
DESCRIPTOR.message_types_by_name['value_info'] = _VALUE_INFO

class frame(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FRAME
  
  # @@protoc_insertion_point(class_scope:frame)

class operand_value_list(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OPERAND_VALUE_LIST
  
  # @@protoc_insertion_point(class_scope:operand_value_list)

class operand_info(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OPERAND_INFO
  
  # @@protoc_insertion_point(class_scope:operand_info)

class operand_info_specific(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OPERAND_INFO_SPECIFIC
  
  # @@protoc_insertion_point(class_scope:operand_info_specific)

class reg_operand(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REG_OPERAND
  
  # @@protoc_insertion_point(class_scope:reg_operand)

class mem_operand(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MEM_OPERAND
  
  # @@protoc_insertion_point(class_scope:mem_operand)

class operand_usage(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OPERAND_USAGE
  
  # @@protoc_insertion_point(class_scope:operand_usage)

class taint_info(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TAINT_INFO
  
  # @@protoc_insertion_point(class_scope:taint_info)

class std_frame(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STD_FRAME
  
  # @@protoc_insertion_point(class_scope:std_frame)

class syscall_frame(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SYSCALL_FRAME
  
  # @@protoc_insertion_point(class_scope:syscall_frame)

class argument_list(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ARGUMENT_LIST
  
  # @@protoc_insertion_point(class_scope:argument_list)

class exception_frame(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EXCEPTION_FRAME
  
  # @@protoc_insertion_point(class_scope:exception_frame)

class taint_intro_frame(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TAINT_INTRO_FRAME
  
  # @@protoc_insertion_point(class_scope:taint_intro_frame)

class taint_intro_list(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TAINT_INTRO_LIST
  
  # @@protoc_insertion_point(class_scope:taint_intro_list)

class taint_intro(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TAINT_INTRO
  
  # @@protoc_insertion_point(class_scope:taint_intro)

class modload_frame(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MODLOAD_FRAME
  
  # @@protoc_insertion_point(class_scope:modload_frame)

class key_frame(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _KEY_FRAME
  
  # @@protoc_insertion_point(class_scope:key_frame)

class tagged_value_lists(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TAGGED_VALUE_LISTS
  
  # @@protoc_insertion_point(class_scope:tagged_value_lists)

class tagged_value_list(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TAGGED_VALUE_LIST
  
  # @@protoc_insertion_point(class_scope:tagged_value_list)

class value_source_tag(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _VALUE_SOURCE_TAG
  
  # @@protoc_insertion_point(class_scope:value_source_tag)

class value_list(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _VALUE_LIST
  
  # @@protoc_insertion_point(class_scope:value_list)

class value_info(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _VALUE_INFO
  
  # @@protoc_insertion_point(class_scope:value_info)

# @@protoc_insertion_point(module_scope)
