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
// 	protoc        v3.10.0
// source: feast/core/FeatureSource.proto

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

// Type of Feature Source.
type FeatureSourceSpec_SourceType int32

const (
	FeatureSourceSpec_INVALID        FeatureSourceSpec_SourceType = 0
	FeatureSourceSpec_BATCH_FILE     FeatureSourceSpec_SourceType = 1
	FeatureSourceSpec_BATCH_BIGQUERY FeatureSourceSpec_SourceType = 2
	FeatureSourceSpec_STREAM_KAFKA   FeatureSourceSpec_SourceType = 3
	FeatureSourceSpec_STREAM_KINESIS FeatureSourceSpec_SourceType = 4
)

// Enum value maps for FeatureSourceSpec_SourceType.
var (
	FeatureSourceSpec_SourceType_name = map[int32]string{
		0: "INVALID",
		1: "BATCH_FILE",
		2: "BATCH_BIGQUERY",
		3: "STREAM_KAFKA",
		4: "STREAM_KINESIS",
	}
	FeatureSourceSpec_SourceType_value = map[string]int32{
		"INVALID":        0,
		"BATCH_FILE":     1,
		"BATCH_BIGQUERY": 2,
		"STREAM_KAFKA":   3,
		"STREAM_KINESIS": 4,
	}
)

func (x FeatureSourceSpec_SourceType) Enum() *FeatureSourceSpec_SourceType {
	p := new(FeatureSourceSpec_SourceType)
	*p = x
	return p
}

func (x FeatureSourceSpec_SourceType) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (FeatureSourceSpec_SourceType) Descriptor() protoreflect.EnumDescriptor {
	return file_feast_core_FeatureSource_proto_enumTypes[0].Descriptor()
}

func (FeatureSourceSpec_SourceType) Type() protoreflect.EnumType {
	return &file_feast_core_FeatureSource_proto_enumTypes[0]
}

func (x FeatureSourceSpec_SourceType) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use FeatureSourceSpec_SourceType.Descriptor instead.
func (FeatureSourceSpec_SourceType) EnumDescriptor() ([]byte, []int) {
	return file_feast_core_FeatureSource_proto_rawDescGZIP(), []int{0, 0}
}

// File Format of the file containing the features
type FeatureSourceSpec_FileOptions_FileFormat int32

const (
	FeatureSourceSpec_FileOptions_INVALID FeatureSourceSpec_FileOptions_FileFormat = 0
	FeatureSourceSpec_FileOptions_PARQUET FeatureSourceSpec_FileOptions_FileFormat = 1
	FeatureSourceSpec_FileOptions_AVRO    FeatureSourceSpec_FileOptions_FileFormat = 2
)

// Enum value maps for FeatureSourceSpec_FileOptions_FileFormat.
var (
	FeatureSourceSpec_FileOptions_FileFormat_name = map[int32]string{
		0: "INVALID",
		1: "PARQUET",
		2: "AVRO",
	}
	FeatureSourceSpec_FileOptions_FileFormat_value = map[string]int32{
		"INVALID": 0,
		"PARQUET": 1,
		"AVRO":    2,
	}
)

func (x FeatureSourceSpec_FileOptions_FileFormat) Enum() *FeatureSourceSpec_FileOptions_FileFormat {
	p := new(FeatureSourceSpec_FileOptions_FileFormat)
	*p = x
	return p
}

func (x FeatureSourceSpec_FileOptions_FileFormat) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (FeatureSourceSpec_FileOptions_FileFormat) Descriptor() protoreflect.EnumDescriptor {
	return file_feast_core_FeatureSource_proto_enumTypes[1].Descriptor()
}

func (FeatureSourceSpec_FileOptions_FileFormat) Type() protoreflect.EnumType {
	return &file_feast_core_FeatureSource_proto_enumTypes[1]
}

func (x FeatureSourceSpec_FileOptions_FileFormat) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use FeatureSourceSpec_FileOptions_FileFormat.Descriptor instead.
func (FeatureSourceSpec_FileOptions_FileFormat) EnumDescriptor() ([]byte, []int) {
	return file_feast_core_FeatureSource_proto_rawDescGZIP(), []int{0, 1, 0}
}

// Defines a Feature Source that can be used source Feature data
type FeatureSourceSpec struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Type FeatureSourceSpec_SourceType `protobuf:"varint,1,opt,name=type,proto3,enum=feast.core.FeatureSourceSpec_SourceType" json:"type,omitempty"`
	// Defines mapping between fields in the sourced data
	// and feature names in parent FeatureTable.
	FieldMapping map[string]string `protobuf:"bytes,2,rep,name=field_mapping,json=fieldMapping,proto3" json:"field_mapping,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
	// Feature Source options.
	//
	// Types that are assignable to Options:
	//	*FeatureSourceSpec_FileOptions_
	//	*FeatureSourceSpec_BigqueryOptions
	//	*FeatureSourceSpec_KafkaOptions_
	//	*FeatureSourceSpec_KinesisOptions_
	Options isFeatureSourceSpec_Options `protobuf_oneof:"options"`
}

func (x *FeatureSourceSpec) Reset() {
	*x = FeatureSourceSpec{}
	if protoimpl.UnsafeEnabled {
		mi := &file_feast_core_FeatureSource_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *FeatureSourceSpec) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*FeatureSourceSpec) ProtoMessage() {}

func (x *FeatureSourceSpec) ProtoReflect() protoreflect.Message {
	mi := &file_feast_core_FeatureSource_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use FeatureSourceSpec.ProtoReflect.Descriptor instead.
func (*FeatureSourceSpec) Descriptor() ([]byte, []int) {
	return file_feast_core_FeatureSource_proto_rawDescGZIP(), []int{0}
}

func (x *FeatureSourceSpec) GetType() FeatureSourceSpec_SourceType {
	if x != nil {
		return x.Type
	}
	return FeatureSourceSpec_INVALID
}

func (x *FeatureSourceSpec) GetFieldMapping() map[string]string {
	if x != nil {
		return x.FieldMapping
	}
	return nil
}

func (m *FeatureSourceSpec) GetOptions() isFeatureSourceSpec_Options {
	if m != nil {
		return m.Options
	}
	return nil
}

func (x *FeatureSourceSpec) GetFileOptions() *FeatureSourceSpec_FileOptions {
	if x, ok := x.GetOptions().(*FeatureSourceSpec_FileOptions_); ok {
		return x.FileOptions
	}
	return nil
}

func (x *FeatureSourceSpec) GetBigqueryOptions() *FeatureSourceSpec_BigQueryOptions {
	if x, ok := x.GetOptions().(*FeatureSourceSpec_BigqueryOptions); ok {
		return x.BigqueryOptions
	}
	return nil
}

func (x *FeatureSourceSpec) GetKafkaOptions() *FeatureSourceSpec_KafkaOptions {
	if x, ok := x.GetOptions().(*FeatureSourceSpec_KafkaOptions_); ok {
		return x.KafkaOptions
	}
	return nil
}

func (x *FeatureSourceSpec) GetKinesisOptions() *FeatureSourceSpec_KinesisOptions {
	if x, ok := x.GetOptions().(*FeatureSourceSpec_KinesisOptions_); ok {
		return x.KinesisOptions
	}
	return nil
}

type isFeatureSourceSpec_Options interface {
	isFeatureSourceSpec_Options()
}

type FeatureSourceSpec_FileOptions_ struct {
	FileOptions *FeatureSourceSpec_FileOptions `protobuf:"bytes,11,opt,name=file_options,json=fileOptions,proto3,oneof"`
}

type FeatureSourceSpec_BigqueryOptions struct {
	BigqueryOptions *FeatureSourceSpec_BigQueryOptions `protobuf:"bytes,12,opt,name=bigquery_options,json=bigqueryOptions,proto3,oneof"`
}

type FeatureSourceSpec_KafkaOptions_ struct {
	KafkaOptions *FeatureSourceSpec_KafkaOptions `protobuf:"bytes,13,opt,name=kafka_options,json=kafkaOptions,proto3,oneof"`
}

type FeatureSourceSpec_KinesisOptions_ struct {
	KinesisOptions *FeatureSourceSpec_KinesisOptions `protobuf:"bytes,14,opt,name=kinesis_options,json=kinesisOptions,proto3,oneof"`
}

func (*FeatureSourceSpec_FileOptions_) isFeatureSourceSpec_Options() {}

func (*FeatureSourceSpec_BigqueryOptions) isFeatureSourceSpec_Options() {}

func (*FeatureSourceSpec_KafkaOptions_) isFeatureSourceSpec_Options() {}

func (*FeatureSourceSpec_KinesisOptions_) isFeatureSourceSpec_Options() {}

// Defines options for Feature source that sources features from a file
type FeatureSourceSpec_FileOptions struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	FileFormat FeatureSourceSpec_FileOptions_FileFormat `protobuf:"varint,1,opt,name=file_format,json=fileFormat,proto3,enum=feast.core.FeatureSourceSpec_FileOptions_FileFormat" json:"file_format,omitempty"`
	// Target URL of file to retrieve and source features from.
	// s3://path/to/file for AWS S3 storage
	// gs://path/to/file for GCP GCS storage
	// file:///path/to/file for local storage
	FileUrl string `protobuf:"bytes,2,opt,name=file_url,json=fileUrl,proto3" json:"file_url,omitempty"`
}

func (x *FeatureSourceSpec_FileOptions) Reset() {
	*x = FeatureSourceSpec_FileOptions{}
	if protoimpl.UnsafeEnabled {
		mi := &file_feast_core_FeatureSource_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *FeatureSourceSpec_FileOptions) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*FeatureSourceSpec_FileOptions) ProtoMessage() {}

func (x *FeatureSourceSpec_FileOptions) ProtoReflect() protoreflect.Message {
	mi := &file_feast_core_FeatureSource_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use FeatureSourceSpec_FileOptions.ProtoReflect.Descriptor instead.
func (*FeatureSourceSpec_FileOptions) Descriptor() ([]byte, []int) {
	return file_feast_core_FeatureSource_proto_rawDescGZIP(), []int{0, 1}
}

func (x *FeatureSourceSpec_FileOptions) GetFileFormat() FeatureSourceSpec_FileOptions_FileFormat {
	if x != nil {
		return x.FileFormat
	}
	return FeatureSourceSpec_FileOptions_INVALID
}

func (x *FeatureSourceSpec_FileOptions) GetFileUrl() string {
	if x != nil {
		return x.FileUrl
	}
	return ""
}

// Defines options for Feature source that sources features from a BigQuery Query
type FeatureSourceSpec_BigQueryOptions struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// GCP Project ID
	ProjectId string `protobuf:"bytes,1,opt,name=project_id,json=projectId,proto3" json:"project_id,omitempty"`
	// SQL Query used by BQ Source to query feature data.
	SqlQuery string `protobuf:"bytes,2,opt,name=sql_query,json=sqlQuery,proto3" json:"sql_query,omitempty"`
}

func (x *FeatureSourceSpec_BigQueryOptions) Reset() {
	*x = FeatureSourceSpec_BigQueryOptions{}
	if protoimpl.UnsafeEnabled {
		mi := &file_feast_core_FeatureSource_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *FeatureSourceSpec_BigQueryOptions) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*FeatureSourceSpec_BigQueryOptions) ProtoMessage() {}

func (x *FeatureSourceSpec_BigQueryOptions) ProtoReflect() protoreflect.Message {
	mi := &file_feast_core_FeatureSource_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use FeatureSourceSpec_BigQueryOptions.ProtoReflect.Descriptor instead.
func (*FeatureSourceSpec_BigQueryOptions) Descriptor() ([]byte, []int) {
	return file_feast_core_FeatureSource_proto_rawDescGZIP(), []int{0, 2}
}

func (x *FeatureSourceSpec_BigQueryOptions) GetProjectId() string {
	if x != nil {
		return x.ProjectId
	}
	return ""
}

func (x *FeatureSourceSpec_BigQueryOptions) GetSqlQuery() string {
	if x != nil {
		return x.SqlQuery
	}
	return ""
}

// Defines options for Feature source that sources features from Kafka messages.
// Each message should be a Protobuf that can be decoded with the generated
// Java Protobuf class at the given class path
type FeatureSourceSpec_KafkaOptions struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Comma separated list of Kafka bootstrap servers. Used for feature sets without a defined source host[:port]]
	BootstrapServers string `protobuf:"bytes,1,opt,name=bootstrap_servers,json=bootstrapServers,proto3" json:"bootstrap_servers,omitempty"`
	// Kafka topic to collect feature data from.
	Topic string `protobuf:"bytes,2,opt,name=topic,proto3" json:"topic,omitempty"`
	// Classpath to the generated Java Protobuf class that can be used to decode
	// Feature data from the obtained Kafka message
	ClassPath string `protobuf:"bytes,3,opt,name=class_path,json=classPath,proto3" json:"class_path,omitempty"`
}

func (x *FeatureSourceSpec_KafkaOptions) Reset() {
	*x = FeatureSourceSpec_KafkaOptions{}
	if protoimpl.UnsafeEnabled {
		mi := &file_feast_core_FeatureSource_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *FeatureSourceSpec_KafkaOptions) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*FeatureSourceSpec_KafkaOptions) ProtoMessage() {}

func (x *FeatureSourceSpec_KafkaOptions) ProtoReflect() protoreflect.Message {
	mi := &file_feast_core_FeatureSource_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use FeatureSourceSpec_KafkaOptions.ProtoReflect.Descriptor instead.
func (*FeatureSourceSpec_KafkaOptions) Descriptor() ([]byte, []int) {
	return file_feast_core_FeatureSource_proto_rawDescGZIP(), []int{0, 3}
}

func (x *FeatureSourceSpec_KafkaOptions) GetBootstrapServers() string {
	if x != nil {
		return x.BootstrapServers
	}
	return ""
}

func (x *FeatureSourceSpec_KafkaOptions) GetTopic() string {
	if x != nil {
		return x.Topic
	}
	return ""
}

func (x *FeatureSourceSpec_KafkaOptions) GetClassPath() string {
	if x != nil {
		return x.ClassPath
	}
	return ""
}

// Defines options for Feature source that sources features from Kinesis records.
// Each record should be a Protobuf that can be decoded with the generated
// Java Protobuf class at the given class path
type FeatureSourceSpec_KinesisOptions struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// AWS region of the Kinesis stream
	Region string `protobuf:"bytes,1,opt,name=region,proto3" json:"region,omitempty"`
	// Name of the Kinesis stream to obtain feature data from.
	StreamName string `protobuf:"bytes,2,opt,name=stream_name,json=streamName,proto3" json:"stream_name,omitempty"`
	// Classpath to the generated Java Protobuf class that can be used to decode
	// Feature data from the obtained Kinesis record
	ClassPath string `protobuf:"bytes,3,opt,name=class_path,json=classPath,proto3" json:"class_path,omitempty"`
}

func (x *FeatureSourceSpec_KinesisOptions) Reset() {
	*x = FeatureSourceSpec_KinesisOptions{}
	if protoimpl.UnsafeEnabled {
		mi := &file_feast_core_FeatureSource_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *FeatureSourceSpec_KinesisOptions) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*FeatureSourceSpec_KinesisOptions) ProtoMessage() {}

func (x *FeatureSourceSpec_KinesisOptions) ProtoReflect() protoreflect.Message {
	mi := &file_feast_core_FeatureSource_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use FeatureSourceSpec_KinesisOptions.ProtoReflect.Descriptor instead.
func (*FeatureSourceSpec_KinesisOptions) Descriptor() ([]byte, []int) {
	return file_feast_core_FeatureSource_proto_rawDescGZIP(), []int{0, 4}
}

func (x *FeatureSourceSpec_KinesisOptions) GetRegion() string {
	if x != nil {
		return x.Region
	}
	return ""
}

func (x *FeatureSourceSpec_KinesisOptions) GetStreamName() string {
	if x != nil {
		return x.StreamName
	}
	return ""
}

func (x *FeatureSourceSpec_KinesisOptions) GetClassPath() string {
	if x != nil {
		return x.ClassPath
	}
	return ""
}

var File_feast_core_FeatureSource_proto protoreflect.FileDescriptor

var file_feast_core_FeatureSource_proto_rawDesc = []byte{
	0x0a, 0x1e, 0x66, 0x65, 0x61, 0x73, 0x74, 0x2f, 0x63, 0x6f, 0x72, 0x65, 0x2f, 0x46, 0x65, 0x61,
	0x74, 0x75, 0x72, 0x65, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x12, 0x0a, 0x66, 0x65, 0x61, 0x73, 0x74, 0x2e, 0x63, 0x6f, 0x72, 0x65, 0x22, 0x8f, 0x09, 0x0a,
	0x11, 0x46, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x53, 0x70,
	0x65, 0x63, 0x12, 0x3c, 0x0a, 0x04, 0x74, 0x79, 0x70, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0e,
	0x32, 0x28, 0x2e, 0x66, 0x65, 0x61, 0x73, 0x74, 0x2e, 0x63, 0x6f, 0x72, 0x65, 0x2e, 0x46, 0x65,
	0x61, 0x74, 0x75, 0x72, 0x65, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x53, 0x70, 0x65, 0x63, 0x2e,
	0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x54, 0x79, 0x70, 0x65, 0x52, 0x04, 0x74, 0x79, 0x70, 0x65,
	0x12, 0x54, 0x0a, 0x0d, 0x66, 0x69, 0x65, 0x6c, 0x64, 0x5f, 0x6d, 0x61, 0x70, 0x70, 0x69, 0x6e,
	0x67, 0x18, 0x02, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x2f, 0x2e, 0x66, 0x65, 0x61, 0x73, 0x74, 0x2e,
	0x63, 0x6f, 0x72, 0x65, 0x2e, 0x46, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65, 0x53, 0x6f, 0x75, 0x72,
	0x63, 0x65, 0x53, 0x70, 0x65, 0x63, 0x2e, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x4d, 0x61, 0x70, 0x70,
	0x69, 0x6e, 0x67, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x52, 0x0c, 0x66, 0x69, 0x65, 0x6c, 0x64, 0x4d,
	0x61, 0x70, 0x70, 0x69, 0x6e, 0x67, 0x12, 0x4e, 0x0a, 0x0c, 0x66, 0x69, 0x6c, 0x65, 0x5f, 0x6f,
	0x70, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x18, 0x0b, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x29, 0x2e, 0x66,
	0x65, 0x61, 0x73, 0x74, 0x2e, 0x63, 0x6f, 0x72, 0x65, 0x2e, 0x46, 0x65, 0x61, 0x74, 0x75, 0x72,
	0x65, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x53, 0x70, 0x65, 0x63, 0x2e, 0x46, 0x69, 0x6c, 0x65,
	0x4f, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x48, 0x00, 0x52, 0x0b, 0x66, 0x69, 0x6c, 0x65, 0x4f,
	0x70, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x12, 0x5a, 0x0a, 0x10, 0x62, 0x69, 0x67, 0x71, 0x75, 0x65,
	0x72, 0x79, 0x5f, 0x6f, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x18, 0x0c, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x2d, 0x2e, 0x66, 0x65, 0x61, 0x73, 0x74, 0x2e, 0x63, 0x6f, 0x72, 0x65, 0x2e, 0x46, 0x65,
	0x61, 0x74, 0x75, 0x72, 0x65, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x53, 0x70, 0x65, 0x63, 0x2e,
	0x42, 0x69, 0x67, 0x51, 0x75, 0x65, 0x72, 0x79, 0x4f, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x48,
	0x00, 0x52, 0x0f, 0x62, 0x69, 0x67, 0x71, 0x75, 0x65, 0x72, 0x79, 0x4f, 0x70, 0x74, 0x69, 0x6f,
	0x6e, 0x73, 0x12, 0x51, 0x0a, 0x0d, 0x6b, 0x61, 0x66, 0x6b, 0x61, 0x5f, 0x6f, 0x70, 0x74, 0x69,
	0x6f, 0x6e, 0x73, 0x18, 0x0d, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x2a, 0x2e, 0x66, 0x65, 0x61, 0x73,
	0x74, 0x2e, 0x63, 0x6f, 0x72, 0x65, 0x2e, 0x46, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65, 0x53, 0x6f,
	0x75, 0x72, 0x63, 0x65, 0x53, 0x70, 0x65, 0x63, 0x2e, 0x4b, 0x61, 0x66, 0x6b, 0x61, 0x4f, 0x70,
	0x74, 0x69, 0x6f, 0x6e, 0x73, 0x48, 0x00, 0x52, 0x0c, 0x6b, 0x61, 0x66, 0x6b, 0x61, 0x4f, 0x70,
	0x74, 0x69, 0x6f, 0x6e, 0x73, 0x12, 0x57, 0x0a, 0x0f, 0x6b, 0x69, 0x6e, 0x65, 0x73, 0x69, 0x73,
	0x5f, 0x6f, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x18, 0x0e, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x2c,
	0x2e, 0x66, 0x65, 0x61, 0x73, 0x74, 0x2e, 0x63, 0x6f, 0x72, 0x65, 0x2e, 0x46, 0x65, 0x61, 0x74,
	0x75, 0x72, 0x65, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x53, 0x70, 0x65, 0x63, 0x2e, 0x4b, 0x69,
	0x6e, 0x65, 0x73, 0x69, 0x73, 0x4f, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x48, 0x00, 0x52, 0x0e,
	0x6b, 0x69, 0x6e, 0x65, 0x73, 0x69, 0x73, 0x4f, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x1a, 0x3f,
	0x0a, 0x11, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x4d, 0x61, 0x70, 0x70, 0x69, 0x6e, 0x67, 0x45, 0x6e,
	0x74, 0x72, 0x79, 0x12, 0x10, 0x0a, 0x03, 0x6b, 0x65, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x03, 0x6b, 0x65, 0x79, 0x12, 0x14, 0x0a, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x18, 0x02,
	0x20, 0x01, 0x28, 0x09, 0x52, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x3a, 0x02, 0x38, 0x01, 0x1a,
	0xb1, 0x01, 0x0a, 0x0b, 0x46, 0x69, 0x6c, 0x65, 0x4f, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x12,
	0x55, 0x0a, 0x0b, 0x66, 0x69, 0x6c, 0x65, 0x5f, 0x66, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x18, 0x01,
	0x20, 0x01, 0x28, 0x0e, 0x32, 0x34, 0x2e, 0x66, 0x65, 0x61, 0x73, 0x74, 0x2e, 0x63, 0x6f, 0x72,
	0x65, 0x2e, 0x46, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x53,
	0x70, 0x65, 0x63, 0x2e, 0x46, 0x69, 0x6c, 0x65, 0x4f, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x2e,
	0x46, 0x69, 0x6c, 0x65, 0x46, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x52, 0x0a, 0x66, 0x69, 0x6c, 0x65,
	0x46, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x12, 0x19, 0x0a, 0x08, 0x66, 0x69, 0x6c, 0x65, 0x5f, 0x75,
	0x72, 0x6c, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x07, 0x66, 0x69, 0x6c, 0x65, 0x55, 0x72,
	0x6c, 0x22, 0x30, 0x0a, 0x0a, 0x46, 0x69, 0x6c, 0x65, 0x46, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x12,
	0x0b, 0x0a, 0x07, 0x49, 0x4e, 0x56, 0x41, 0x4c, 0x49, 0x44, 0x10, 0x00, 0x12, 0x0b, 0x0a, 0x07,
	0x50, 0x41, 0x52, 0x51, 0x55, 0x45, 0x54, 0x10, 0x01, 0x12, 0x08, 0x0a, 0x04, 0x41, 0x56, 0x52,
	0x4f, 0x10, 0x02, 0x1a, 0x4d, 0x0a, 0x0f, 0x42, 0x69, 0x67, 0x51, 0x75, 0x65, 0x72, 0x79, 0x4f,
	0x70, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x12, 0x1d, 0x0a, 0x0a, 0x70, 0x72, 0x6f, 0x6a, 0x65, 0x63,
	0x74, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x70, 0x72, 0x6f, 0x6a,
	0x65, 0x63, 0x74, 0x49, 0x64, 0x12, 0x1b, 0x0a, 0x09, 0x73, 0x71, 0x6c, 0x5f, 0x71, 0x75, 0x65,
	0x72, 0x79, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x73, 0x71, 0x6c, 0x51, 0x75, 0x65,
	0x72, 0x79, 0x1a, 0x70, 0x0a, 0x0c, 0x4b, 0x61, 0x66, 0x6b, 0x61, 0x4f, 0x70, 0x74, 0x69, 0x6f,
	0x6e, 0x73, 0x12, 0x2b, 0x0a, 0x11, 0x62, 0x6f, 0x6f, 0x74, 0x73, 0x74, 0x72, 0x61, 0x70, 0x5f,
	0x73, 0x65, 0x72, 0x76, 0x65, 0x72, 0x73, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x10, 0x62,
	0x6f, 0x6f, 0x74, 0x73, 0x74, 0x72, 0x61, 0x70, 0x53, 0x65, 0x72, 0x76, 0x65, 0x72, 0x73, 0x12,
	0x14, 0x0a, 0x05, 0x74, 0x6f, 0x70, 0x69, 0x63, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x05,
	0x74, 0x6f, 0x70, 0x69, 0x63, 0x12, 0x1d, 0x0a, 0x0a, 0x63, 0x6c, 0x61, 0x73, 0x73, 0x5f, 0x70,
	0x61, 0x74, 0x68, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x63, 0x6c, 0x61, 0x73, 0x73,
	0x50, 0x61, 0x74, 0x68, 0x1a, 0x68, 0x0a, 0x0e, 0x4b, 0x69, 0x6e, 0x65, 0x73, 0x69, 0x73, 0x4f,
	0x70, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x12, 0x16, 0x0a, 0x06, 0x72, 0x65, 0x67, 0x69, 0x6f, 0x6e,
	0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x06, 0x72, 0x65, 0x67, 0x69, 0x6f, 0x6e, 0x12, 0x1f,
	0x0a, 0x0b, 0x73, 0x74, 0x72, 0x65, 0x61, 0x6d, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x02, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x0a, 0x73, 0x74, 0x72, 0x65, 0x61, 0x6d, 0x4e, 0x61, 0x6d, 0x65, 0x12,
	0x1d, 0x0a, 0x0a, 0x63, 0x6c, 0x61, 0x73, 0x73, 0x5f, 0x70, 0x61, 0x74, 0x68, 0x18, 0x03, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x09, 0x63, 0x6c, 0x61, 0x73, 0x73, 0x50, 0x61, 0x74, 0x68, 0x22, 0x63,
	0x0a, 0x0a, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x54, 0x79, 0x70, 0x65, 0x12, 0x0b, 0x0a, 0x07,
	0x49, 0x4e, 0x56, 0x41, 0x4c, 0x49, 0x44, 0x10, 0x00, 0x12, 0x0e, 0x0a, 0x0a, 0x42, 0x41, 0x54,
	0x43, 0x48, 0x5f, 0x46, 0x49, 0x4c, 0x45, 0x10, 0x01, 0x12, 0x12, 0x0a, 0x0e, 0x42, 0x41, 0x54,
	0x43, 0x48, 0x5f, 0x42, 0x49, 0x47, 0x51, 0x55, 0x45, 0x52, 0x59, 0x10, 0x02, 0x12, 0x10, 0x0a,
	0x0c, 0x53, 0x54, 0x52, 0x45, 0x41, 0x4d, 0x5f, 0x4b, 0x41, 0x46, 0x4b, 0x41, 0x10, 0x03, 0x12,
	0x12, 0x0a, 0x0e, 0x53, 0x54, 0x52, 0x45, 0x41, 0x4d, 0x5f, 0x4b, 0x49, 0x4e, 0x45, 0x53, 0x49,
	0x53, 0x10, 0x04, 0x42, 0x09, 0x0a, 0x07, 0x6f, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x42, 0x5b,
	0x0a, 0x10, 0x66, 0x65, 0x61, 0x73, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x63, 0x6f,
	0x72, 0x65, 0x42, 0x12, 0x46, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65, 0x53, 0x6f, 0x75, 0x72, 0x63,
	0x65, 0x50, 0x72, 0x6f, 0x74, 0x6f, 0x5a, 0x33, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63,
	0x6f, 0x6d, 0x2f, 0x66, 0x65, 0x61, 0x73, 0x74, 0x2d, 0x64, 0x65, 0x76, 0x2f, 0x66, 0x65, 0x61,
	0x73, 0x74, 0x2f, 0x73, 0x64, 0x6b, 0x2f, 0x67, 0x6f, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x73,
	0x2f, 0x66, 0x65, 0x61, 0x73, 0x74, 0x2f, 0x63, 0x6f, 0x72, 0x65, 0x62, 0x06, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x33,
}

var (
	file_feast_core_FeatureSource_proto_rawDescOnce sync.Once
	file_feast_core_FeatureSource_proto_rawDescData = file_feast_core_FeatureSource_proto_rawDesc
)

func file_feast_core_FeatureSource_proto_rawDescGZIP() []byte {
	file_feast_core_FeatureSource_proto_rawDescOnce.Do(func() {
		file_feast_core_FeatureSource_proto_rawDescData = protoimpl.X.CompressGZIP(file_feast_core_FeatureSource_proto_rawDescData)
	})
	return file_feast_core_FeatureSource_proto_rawDescData
}

var file_feast_core_FeatureSource_proto_enumTypes = make([]protoimpl.EnumInfo, 2)
var file_feast_core_FeatureSource_proto_msgTypes = make([]protoimpl.MessageInfo, 6)
var file_feast_core_FeatureSource_proto_goTypes = []interface{}{
	(FeatureSourceSpec_SourceType)(0),             // 0: feast.core.FeatureSourceSpec.SourceType
	(FeatureSourceSpec_FileOptions_FileFormat)(0), // 1: feast.core.FeatureSourceSpec.FileOptions.FileFormat
	(*FeatureSourceSpec)(nil),                     // 2: feast.core.FeatureSourceSpec
	nil,                                           // 3: feast.core.FeatureSourceSpec.FieldMappingEntry
	(*FeatureSourceSpec_FileOptions)(nil),         // 4: feast.core.FeatureSourceSpec.FileOptions
	(*FeatureSourceSpec_BigQueryOptions)(nil),     // 5: feast.core.FeatureSourceSpec.BigQueryOptions
	(*FeatureSourceSpec_KafkaOptions)(nil),        // 6: feast.core.FeatureSourceSpec.KafkaOptions
	(*FeatureSourceSpec_KinesisOptions)(nil),      // 7: feast.core.FeatureSourceSpec.KinesisOptions
}
var file_feast_core_FeatureSource_proto_depIdxs = []int32{
	0, // 0: feast.core.FeatureSourceSpec.type:type_name -> feast.core.FeatureSourceSpec.SourceType
	3, // 1: feast.core.FeatureSourceSpec.field_mapping:type_name -> feast.core.FeatureSourceSpec.FieldMappingEntry
	4, // 2: feast.core.FeatureSourceSpec.file_options:type_name -> feast.core.FeatureSourceSpec.FileOptions
	5, // 3: feast.core.FeatureSourceSpec.bigquery_options:type_name -> feast.core.FeatureSourceSpec.BigQueryOptions
	6, // 4: feast.core.FeatureSourceSpec.kafka_options:type_name -> feast.core.FeatureSourceSpec.KafkaOptions
	7, // 5: feast.core.FeatureSourceSpec.kinesis_options:type_name -> feast.core.FeatureSourceSpec.KinesisOptions
	1, // 6: feast.core.FeatureSourceSpec.FileOptions.file_format:type_name -> feast.core.FeatureSourceSpec.FileOptions.FileFormat
	7, // [7:7] is the sub-list for method output_type
	7, // [7:7] is the sub-list for method input_type
	7, // [7:7] is the sub-list for extension type_name
	7, // [7:7] is the sub-list for extension extendee
	0, // [0:7] is the sub-list for field type_name
}

func init() { file_feast_core_FeatureSource_proto_init() }
func file_feast_core_FeatureSource_proto_init() {
	if File_feast_core_FeatureSource_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_feast_core_FeatureSource_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*FeatureSourceSpec); i {
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
		file_feast_core_FeatureSource_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*FeatureSourceSpec_FileOptions); i {
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
		file_feast_core_FeatureSource_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*FeatureSourceSpec_BigQueryOptions); i {
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
		file_feast_core_FeatureSource_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*FeatureSourceSpec_KafkaOptions); i {
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
		file_feast_core_FeatureSource_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*FeatureSourceSpec_KinesisOptions); i {
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
	file_feast_core_FeatureSource_proto_msgTypes[0].OneofWrappers = []interface{}{
		(*FeatureSourceSpec_FileOptions_)(nil),
		(*FeatureSourceSpec_BigqueryOptions)(nil),
		(*FeatureSourceSpec_KafkaOptions_)(nil),
		(*FeatureSourceSpec_KinesisOptions_)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_feast_core_FeatureSource_proto_rawDesc,
			NumEnums:      2,
			NumMessages:   6,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_feast_core_FeatureSource_proto_goTypes,
		DependencyIndexes: file_feast_core_FeatureSource_proto_depIdxs,
		EnumInfos:         file_feast_core_FeatureSource_proto_enumTypes,
		MessageInfos:      file_feast_core_FeatureSource_proto_msgTypes,
	}.Build()
	File_feast_core_FeatureSource_proto = out.File
	file_feast_core_FeatureSource_proto_rawDesc = nil
	file_feast_core_FeatureSource_proto_goTypes = nil
	file_feast_core_FeatureSource_proto_depIdxs = nil
}