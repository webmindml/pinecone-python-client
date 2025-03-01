# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.struct_pb2 import (
    Struct as google___protobuf___struct_pb2___Struct,
)

from typing import (
    Iterable as typing___Iterable,
    Mapping as typing___Mapping,
    MutableMapping as typing___MutableMapping,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class NdArray(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    buffer: builtin___bytes = ...
    shape: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    dtype: typing___Text = ...
    compressed: builtin___bool = ...

    def __init__(
        self,
        *,
        buffer: typing___Optional[builtin___bytes] = None,
        shape: typing___Optional[typing___Iterable[builtin___int]] = None,
        dtype: typing___Optional[typing___Text] = None,
        compressed: typing___Optional[builtin___bool] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "buffer", b"buffer", "compressed", b"compressed", "dtype", b"dtype", "shape", b"shape"
        ],
    ) -> None: ...

type___NdArray = NdArray

class ScoredResults(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def ids(self) -> type___NdArray: ...
    @property
    def scores(self) -> type___NdArray: ...
    @property
    def data(self) -> type___NdArray: ...
    @property
    def metadata(self) -> type___NdArray: ...
    def __init__(
        self,
        *,
        ids: typing___Optional[type___NdArray] = None,
        scores: typing___Optional[type___NdArray] = None,
        data: typing___Optional[type___NdArray] = None,
        metadata: typing___Optional[type___NdArray] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "data", b"data", "ids", b"ids", "metadata", b"metadata", "scores", b"scores"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "data", b"data", "ids", b"ids", "metadata", b"metadata", "scores", b"scores"
        ],
    ) -> None: ...

type___ScoredResults = ScoredResults

class UpsertRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    namespace: typing___Text = ...
    ids: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...

    @property
    def data(self) -> type___NdArray: ...
    @property
    def metadata(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___struct_pb2___Struct
    ]: ...
    def __init__(
        self,
        *,
        namespace: typing___Optional[typing___Text] = None,
        ids: typing___Optional[typing___Iterable[typing___Text]] = None,
        data: typing___Optional[type___NdArray] = None,
        metadata: typing___Optional[typing___Iterable[google___protobuf___struct_pb2___Struct]] = None,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal["data", b"data"]) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "data", b"data", "ids", b"ids", "metadata", b"metadata", "namespace", b"namespace"
        ],
    ) -> None: ...

type___UpsertRequest = UpsertRequest

class UpsertResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    upserted_count: builtin___int = ...

    def __init__(
        self,
        *,
        upserted_count: typing___Optional[builtin___int] = None,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal["upserted_count", b"upserted_count"]) -> None: ...

type___UpsertResponse = UpsertResponse

class DeleteRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    namespace: typing___Text = ...
    ids: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    delete_all: builtin___bool = ...

    def __init__(
        self,
        *,
        namespace: typing___Optional[typing___Text] = None,
        ids: typing___Optional[typing___Iterable[typing___Text]] = None,
        delete_all: typing___Optional[builtin___bool] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal["delete_all", b"delete_all", "ids", b"ids", "namespace", b"namespace"],
    ) -> None: ...

type___DeleteRequest = DeleteRequest

class DeleteResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(
        self,
    ) -> None: ...

type___DeleteResponse = DeleteResponse

class FetchRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    namespace: typing___Text = ...
    ids: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...

    def __init__(
        self,
        *,
        namespace: typing___Optional[typing___Text] = None,
        ids: typing___Optional[typing___Iterable[typing___Text]] = None,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal["ids", b"ids", "namespace", b"namespace"]) -> None: ...

type___FetchRequest = FetchRequest

class FetchResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    namespace: typing___Text = ...
    ids: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...

    @property
    def vectors(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___NdArray]: ...
    @property
    def metadata(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___struct_pb2___Struct
    ]: ...
    def __init__(
        self,
        *,
        namespace: typing___Optional[typing___Text] = None,
        ids: typing___Optional[typing___Iterable[typing___Text]] = None,
        vectors: typing___Optional[typing___Iterable[type___NdArray]] = None,
        metadata: typing___Optional[typing___Iterable[google___protobuf___struct_pb2___Struct]] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "ids", b"ids", "metadata", b"metadata", "namespace", b"namespace", "vectors", b"vectors"
        ],
    ) -> None: ...

type___FetchResponse = FetchResponse

class QueryRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    namespace: typing___Text = ...
    namespace_overrides: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    top_k: builtin___int = ...
    top_k_overrides: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    include_values: builtin___bool = ...
    include_metadata: builtin___bool = ...

    @property
    def filter(self) -> google___protobuf___struct_pb2___Struct: ...
    @property
    def filter_overrides(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___struct_pb2___Struct
    ]: ...
    @property
    def queries(self) -> type___NdArray: ...
    def __init__(
        self,
        *,
        namespace: typing___Optional[typing___Text] = None,
        namespace_overrides: typing___Optional[typing___Iterable[typing___Text]] = None,
        top_k: typing___Optional[builtin___int] = None,
        top_k_overrides: typing___Optional[typing___Iterable[builtin___int]] = None,
        filter: typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        filter_overrides: typing___Optional[typing___Iterable[google___protobuf___struct_pb2___Struct]] = None,
        include_values: typing___Optional[builtin___bool] = None,
        include_metadata: typing___Optional[builtin___bool] = None,
        queries: typing___Optional[type___NdArray] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["filter", b"filter", "queries", b"queries"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "filter",
            b"filter",
            "filter_overrides",
            b"filter_overrides",
            "include_metadata",
            b"include_metadata",
            "include_values",
            b"include_values",
            "namespace",
            b"namespace",
            "namespace_overrides",
            b"namespace_overrides",
            "queries",
            b"queries",
            "top_k",
            b"top_k",
            "top_k_overrides",
            b"top_k_overrides",
        ],
    ) -> None: ...

type___QueryRequest = QueryRequest

class QueryResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def matches(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___ScoredResults]: ...
    def __init__(
        self,
        *,
        matches: typing___Optional[typing___Iterable[type___ScoredResults]] = None,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal["matches", b"matches"]) -> None: ...

type___QueryResponse = QueryResponse

class DescribeIndexStatsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(
        self,
    ) -> None: ...

type___DescribeIndexStatsRequest = DescribeIndexStatsRequest

class NamespaceSummary(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    vector_count: builtin___int = ...

    def __init__(
        self,
        *,
        vector_count: typing___Optional[builtin___int] = None,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal["vector_count", b"vector_count"]) -> None: ...

type___NamespaceSummary = NamespaceSummary

class DescribeIndexStatsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    class NamespacesEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> type___NamespaceSummary: ...
        def __init__(
            self,
            *,
            key: typing___Optional[typing___Text] = None,
            value: typing___Optional[type___NamespaceSummary] = None,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal["value", b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal["key", b"key", "value", b"value"]) -> None: ...
    type___NamespacesEntry = NamespacesEntry

    dimension: builtin___int = ...

    @property
    def namespaces(self) -> typing___MutableMapping[typing___Text, type___NamespaceSummary]: ...
    def __init__(
        self,
        *,
        namespaces: typing___Optional[typing___Mapping[typing___Text, type___NamespaceSummary]] = None,
        dimension: typing___Optional[builtin___int] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["dimension", b"dimension", "namespaces", b"namespaces"]
    ) -> None: ...

type___DescribeIndexStatsResponse = DescribeIndexStatsResponse
