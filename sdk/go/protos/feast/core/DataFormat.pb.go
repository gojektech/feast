//
// Copyright 2020 The Feast Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     https://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.25.0
// 	protoc        v3.12.4
// source: feast/core/DataFormat.proto

package core

import (
	proto "github.com/golang/protobuf/proto"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// This is a compile-time assertion that a sufficiently up-to-date version
// of the legacy proto package is being used.
const _ = proto.ProtoPackageIsVersion4

// Defines the file format encoding the features/entity data in files
type FileFormat struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to Format:
	//	*FileFormat_ParquetFormat_
	Format isFileFormat_Format `protobuf_oneof:"format"`
}

func (x *FileFormat) Reset() {
	*x = FileFormat{}
	if protoimpl.UnsafeEnabled {
		mi := &file_feast_core_DataFormat_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *FileFormat) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*FileFormat) ProtoMessage() {}

func (x *FileFormat) ProtoReflect() protoreflect.Message {
	mi := &file_feast_core_DataFormat_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use FileFormat.ProtoReflect.Descriptor instead.
func (*FileFormat) Descriptor() ([]byte, []int) {
	return file_feast_core_DataFormat_proto_rawDescGZIP(), []int{0}
}

func (m *FileFormat) GetFormat() isFileFormat_Format {
	if m != nil {
		return m.Format
	}
	return nil
}

func (x *FileFormat) GetParquetFormat() *FileFormat_ParquetFormat {
	if x, ok := x.GetFormat().(*FileFormat_ParquetFormat_); ok {
		return x.ParquetFormat
	}
	return nil
}

type isFileFormat_Format interface {
	isFileFormat_Format()
}

type FileFormat_ParquetFormat_ struct {
	ParquetFormat *FileFormat_ParquetFormat `protobuf:"bytes,1,opt,name=parquet_format,json=parquetFormat,proto3,oneof"`
}

func (*FileFormat_ParquetFormat_) isFileFormat_Format() {}

// Defines the data format encoding features/entity data in data streams
type StreamFormat struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Specifies the data format and format specific options
	//
	// Types that are assignable to Format:
	//	*StreamFormat_AvroFormat_
	//	*StreamFormat_ProtoFormat_
	Format isStreamFormat_Format `protobuf_oneof:"format"`
}

func (x *StreamFormat) Reset() {
	*x = StreamFormat{}
	if protoimpl.UnsafeEnabled {
		mi := &file_feast_core_DataFormat_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *StreamFormat) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*StreamFormat) ProtoMessage() {}

func (x *StreamFormat) ProtoReflect() protoreflect.Message {
	mi := &file_feast_core_DataFormat_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use StreamFormat.ProtoReflect.Descriptor instead.
func (*StreamFormat) Descriptor() ([]byte, []int) {
	return file_feast_core_DataFormat_proto_rawDescGZIP(), []int{1}
}

func (m *StreamFormat) GetFormat() isStreamFormat_Format {
	if m != nil {
		return m.Format
	}
	return nil
}

func (x *StreamFormat) GetAvroFormat() *StreamFormat_AvroFormat {
	if x, ok := x.GetFormat().(*StreamFormat_AvroFormat_); ok {
		return x.AvroFormat
	}
	return nil
}

func (x *StreamFormat) GetProtoFormat() *StreamFormat_ProtoFormat {
	if x, ok := x.GetFormat().(*StreamFormat_ProtoFormat_); ok {
		return x.ProtoFormat
	}
	return nil
}

type isStreamFormat_Format interface {
	isStreamFormat_Format()
}

type StreamFormat_AvroFormat_ struct {
	AvroFormat *StreamFormat_AvroFormat `protobuf:"bytes,1,opt,name=avro_format,json=avroFormat,proto3,oneof"`
}

type StreamFormat_ProtoFormat_ struct {
	ProtoFormat *StreamFormat_ProtoFormat `protobuf:"bytes,2,opt,name=proto_format,json=protoFormat,proto3,oneof"`
}

func (*StreamFormat_AvroFormat_) isStreamFormat_Format() {}

func (*StreamFormat_ProtoFormat_) isStreamFormat_Format() {}

// Defines options for the Parquet data format
type FileFormat_ParquetFormat struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *FileFormat_ParquetFormat) Reset() {
	*x = FileFormat_ParquetFormat{}
	if protoimpl.UnsafeEnabled {
		mi := &file_feast_core_DataFormat_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *FileFormat_ParquetFormat) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*FileFormat_ParquetFormat) ProtoMessage() {}

func (x *FileFormat_ParquetFormat) ProtoReflect() protoreflect.Message {
	mi := &file_feast_core_DataFormat_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use FileFormat_ParquetFormat.ProtoReflect.Descriptor instead.
func (*FileFormat_ParquetFormat) Descriptor() ([]byte, []int) {
	return file_feast_core_DataFormat_proto_rawDescGZIP(), []int{0, 0}
}

// Defines options for the protobuf data format
type StreamFormat_ProtoFormat struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Classpath to the generated Java Protobuf class that can be used to decode
	// Feature data from the obtained stream message
	ClassPath string `protobuf:"bytes,1,opt,name=class_path,json=classPath,proto3" json:"class_path,omitempty"`
}

func (x *StreamFormat_ProtoFormat) Reset() {
	*x = StreamFormat_ProtoFormat{}
	if protoimpl.UnsafeEnabled {
		mi := &file_feast_core_DataFormat_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *StreamFormat_ProtoFormat) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*StreamFormat_ProtoFormat) ProtoMessage() {}

func (x *StreamFormat_ProtoFormat) ProtoReflect() protoreflect.Message {
	mi := &file_feast_core_DataFormat_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use StreamFormat_ProtoFormat.ProtoReflect.Descriptor instead.
func (*StreamFormat_ProtoFormat) Descriptor() ([]byte, []int) {
	return file_feast_core_DataFormat_proto_rawDescGZIP(), []int{1, 0}
}

func (x *StreamFormat_ProtoFormat) GetClassPath() string {
	if x != nil {
		return x.ClassPath
	}
	return ""
}

// Defines options for the avro data format
type StreamFormat_AvroFormat struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Optional if used in a File DataSource as schema is embedded in avro file.
	// Specifies the schema of the Avro message as JSON string.
	SchemaJson string `protobuf:"bytes,1,opt,name=schema_json,json=schemaJson,proto3" json:"schema_json,omitempty"`
}

func (x *StreamFormat_AvroFormat) Reset() {
	*x = StreamFormat_AvroFormat{}
	if protoimpl.UnsafeEnabled {
		mi := &file_feast_core_DataFormat_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *StreamFormat_AvroFormat) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*StreamFormat_AvroFormat) ProtoMessage() {}

func (x *StreamFormat_AvroFormat) ProtoReflect() protoreflect.Message {
	mi := &file_feast_core_DataFormat_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use StreamFormat_AvroFormat.ProtoReflect.Descriptor instead.
func (*StreamFormat_AvroFormat) Descriptor() ([]byte, []int) {
	return file_feast_core_DataFormat_proto_rawDescGZIP(), []int{1, 1}
}

func (x *StreamFormat_AvroFormat) GetSchemaJson() string {
	if x != nil {
		return x.SchemaJson
	}
	return ""
}

var File_feast_core_DataFormat_proto protoreflect.FileDescriptor

var file_feast_core_DataFormat_proto_rawDesc = []byte{
	0x0a, 0x1b, 0x66, 0x65, 0x61, 0x73, 0x74, 0x2f, 0x63, 0x6f, 0x72, 0x65, 0x2f, 0x44, 0x61, 0x74,
	0x61, 0x46, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x0a, 0x66,
	0x65, 0x61, 0x73, 0x74, 0x2e, 0x63, 0x6f, 0x72, 0x65, 0x22, 0x76, 0x0a, 0x0a, 0x46, 0x69, 0x6c,
	0x65, 0x46, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x12, 0x4d, 0x0a, 0x0e, 0x70, 0x61, 0x72, 0x71, 0x75,
	0x65, 0x74, 0x5f, 0x66, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32,
	0x24, 0x2e, 0x66, 0x65, 0x61, 0x73, 0x74, 0x2e, 0x63, 0x6f, 0x72, 0x65, 0x2e, 0x46, 0x69, 0x6c,
	0x65, 0x46, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x2e, 0x50, 0x61, 0x72, 0x71, 0x75, 0x65, 0x74, 0x46,
	0x6f, 0x72, 0x6d, 0x61, 0x74, 0x48, 0x00, 0x52, 0x0d, 0x70, 0x61, 0x72, 0x71, 0x75, 0x65, 0x74,
	0x46, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x1a, 0x0f, 0x0a, 0x0d, 0x50, 0x61, 0x72, 0x71, 0x75, 0x65,
	0x74, 0x46, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x42, 0x08, 0x0a, 0x06, 0x66, 0x6f, 0x72, 0x6d, 0x61,
	0x74, 0x22, 0x88, 0x02, 0x0a, 0x0c, 0x53, 0x74, 0x72, 0x65, 0x61, 0x6d, 0x46, 0x6f, 0x72, 0x6d,
	0x61, 0x74, 0x12, 0x46, 0x0a, 0x0b, 0x61, 0x76, 0x72, 0x6f, 0x5f, 0x66, 0x6f, 0x72, 0x6d, 0x61,
	0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x23, 0x2e, 0x66, 0x65, 0x61, 0x73, 0x74, 0x2e,
	0x63, 0x6f, 0x72, 0x65, 0x2e, 0x53, 0x74, 0x72, 0x65, 0x61, 0x6d, 0x46, 0x6f, 0x72, 0x6d, 0x61,
	0x74, 0x2e, 0x41, 0x76, 0x72, 0x6f, 0x46, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x48, 0x00, 0x52, 0x0a,
	0x61, 0x76, 0x72, 0x6f, 0x46, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x12, 0x49, 0x0a, 0x0c, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x5f, 0x66, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x24, 0x2e, 0x66, 0x65, 0x61, 0x73, 0x74, 0x2e, 0x63, 0x6f, 0x72, 0x65, 0x2e, 0x53, 0x74,
	0x72, 0x65, 0x61, 0x6d, 0x46, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x2e, 0x50, 0x72, 0x6f, 0x74, 0x6f,
	0x46, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x48, 0x00, 0x52, 0x0b, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x46,
	0x6f, 0x72, 0x6d, 0x61, 0x74, 0x1a, 0x2c, 0x0a, 0x0b, 0x50, 0x72, 0x6f, 0x74, 0x6f, 0x46, 0x6f,
	0x72, 0x6d, 0x61, 0x74, 0x12, 0x1d, 0x0a, 0x0a, 0x63, 0x6c, 0x61, 0x73, 0x73, 0x5f, 0x70, 0x61,
	0x74, 0x68, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x63, 0x6c, 0x61, 0x73, 0x73, 0x50,
	0x61, 0x74, 0x68, 0x1a, 0x2d, 0x0a, 0x0a, 0x41, 0x76, 0x72, 0x6f, 0x46, 0x6f, 0x72, 0x6d, 0x61,
	0x74, 0x12, 0x1f, 0x0a, 0x0b, 0x73, 0x63, 0x68, 0x65, 0x6d, 0x61, 0x5f, 0x6a, 0x73, 0x6f, 0x6e,
	0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0a, 0x73, 0x63, 0x68, 0x65, 0x6d, 0x61, 0x4a, 0x73,
	0x6f, 0x6e, 0x42, 0x08, 0x0a, 0x06, 0x66, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x42, 0x58, 0x0a, 0x10,
	0x66, 0x65, 0x61, 0x73, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x63, 0x6f, 0x72, 0x65,
	0x42, 0x0f, 0x44, 0x61, 0x74, 0x61, 0x46, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x50, 0x72, 0x6f, 0x74,
	0x6f, 0x5a, 0x33, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x66, 0x65,
	0x61, 0x73, 0x74, 0x2d, 0x64, 0x65, 0x76, 0x2f, 0x66, 0x65, 0x61, 0x73, 0x74, 0x2f, 0x73, 0x64,
	0x6b, 0x2f, 0x67, 0x6f, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x73, 0x2f, 0x66, 0x65, 0x61, 0x73,
	0x74, 0x2f, 0x63, 0x6f, 0x72, 0x65, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_feast_core_DataFormat_proto_rawDescOnce sync.Once
	file_feast_core_DataFormat_proto_rawDescData = file_feast_core_DataFormat_proto_rawDesc
)

func file_feast_core_DataFormat_proto_rawDescGZIP() []byte {
	file_feast_core_DataFormat_proto_rawDescOnce.Do(func() {
		file_feast_core_DataFormat_proto_rawDescData = protoimpl.X.CompressGZIP(file_feast_core_DataFormat_proto_rawDescData)
	})
	return file_feast_core_DataFormat_proto_rawDescData
}

var file_feast_core_DataFormat_proto_msgTypes = make([]protoimpl.MessageInfo, 5)
var file_feast_core_DataFormat_proto_goTypes = []interface{}{
	(*FileFormat)(nil),               // 0: feast.core.FileFormat
	(*StreamFormat)(nil),             // 1: feast.core.StreamFormat
	(*FileFormat_ParquetFormat)(nil), // 2: feast.core.FileFormat.ParquetFormat
	(*StreamFormat_ProtoFormat)(nil), // 3: feast.core.StreamFormat.ProtoFormat
	(*StreamFormat_AvroFormat)(nil),  // 4: feast.core.StreamFormat.AvroFormat
}
var file_feast_core_DataFormat_proto_depIdxs = []int32{
	2, // 0: feast.core.FileFormat.parquet_format:type_name -> feast.core.FileFormat.ParquetFormat
	4, // 1: feast.core.StreamFormat.avro_format:type_name -> feast.core.StreamFormat.AvroFormat
	3, // 2: feast.core.StreamFormat.proto_format:type_name -> feast.core.StreamFormat.ProtoFormat
	3, // [3:3] is the sub-list for method output_type
	3, // [3:3] is the sub-list for method input_type
	3, // [3:3] is the sub-list for extension type_name
	3, // [3:3] is the sub-list for extension extendee
	0, // [0:3] is the sub-list for field type_name
}

func init() { file_feast_core_DataFormat_proto_init() }
func file_feast_core_DataFormat_proto_init() {
	if File_feast_core_DataFormat_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_feast_core_DataFormat_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*FileFormat); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_feast_core_DataFormat_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*StreamFormat); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_feast_core_DataFormat_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*FileFormat_ParquetFormat); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_feast_core_DataFormat_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*StreamFormat_ProtoFormat); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_feast_core_DataFormat_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*StreamFormat_AvroFormat); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	file_feast_core_DataFormat_proto_msgTypes[0].OneofWrappers = []interface{}{
		(*FileFormat_ParquetFormat_)(nil),
	}
	file_feast_core_DataFormat_proto_msgTypes[1].OneofWrappers = []interface{}{
		(*StreamFormat_AvroFormat_)(nil),
		(*StreamFormat_ProtoFormat_)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_feast_core_DataFormat_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   5,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_feast_core_DataFormat_proto_goTypes,
		DependencyIndexes: file_feast_core_DataFormat_proto_depIdxs,
		MessageInfos:      file_feast_core_DataFormat_proto_msgTypes,
	}.Build()
	File_feast_core_DataFormat_proto = out.File
	file_feast_core_DataFormat_proto_rawDesc = nil
	file_feast_core_DataFormat_proto_goTypes = nil
	file_feast_core_DataFormat_proto_depIdxs = nil
}
