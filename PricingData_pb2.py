# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PricingData.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="PricingData.proto",
    package="",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x11PricingData.proto"\xd7\x08\n\x0bPricingData\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\x02\x12\x0c\n\x04time\x18\x03 \x01(\x12\x12\x10\n\x08\x63urrency\x18\x04 \x01(\t\x12\x10\n\x08\x65xchange\x18\x05 \x01(\t\x12)\n\tquoteType\x18\x06 \x01(\x0e\x32\x16.PricingData.QuoteType\x12\x31\n\x0bmarketHours\x18\x07 \x01(\x0e\x32\x1c.PricingData.MarketHoursType\x12\x15\n\rchangePercent\x18\x08 \x01(\x02\x12\x11\n\tdayVolume\x18\t \x01(\x12\x12\x0f\n\x07\x64\x61yHigh\x18\n \x01(\x02\x12\x0e\n\x06\x64\x61yLow\x18\x0b \x01(\x02\x12\x0e\n\x06\x63hange\x18\x0c \x01(\x02\x12\x11\n\tshortName\x18\r \x01(\t\x12\x12\n\nexpireDate\x18\x0e \x01(\x12\x12\x11\n\topenPrice\x18\x0f \x01(\x02\x12\x15\n\rpreviousClose\x18\x10 \x01(\x02\x12\x13\n\x0bstrikePrice\x18\x11 \x01(\x02\x12\x18\n\x10underlyingSymbol\x18\x12 \x01(\t\x12\x14\n\x0copenInterest\x18\x13 \x01(\x12\x12,\n\x0boptionsType\x18\x14 \x01(\x0e\x32\x17.PricingData.OptionType\x12\x12\n\nminiOption\x18\x15 \x01(\x12\x12\x10\n\x08lastSize\x18\x16 \x01(\x12\x12\x0b\n\x03\x62id\x18\x17 \x01(\x02\x12\x0f\n\x07\x62idSize\x18\x18 \x01(\x12\x12\x0b\n\x03\x61sk\x18\x19 \x01(\x02\x12\x0f\n\x07\x61skSize\x18\x1a \x01(\x12\x12\x11\n\tpriceHint\x18\x1b \x01(\x12\x12\x10\n\x08vol_24hr\x18\x1c \x01(\x12\x12\x18\n\x10volAllCurrencies\x18\x1d \x01(\x12\x12\x14\n\x0c\x66romcurrency\x18\x1e \x01(\t\x12\x12\n\nlastMarket\x18\x1f \x01(\t\x12\x19\n\x11\x63irculatingSupply\x18  \x01(\x01\x12\x11\n\tmarketcap\x18! \x01(\x01"\x80\x02\n\tQuoteType\x12\x08\n\x04NONE\x10\x00\x12\r\n\tALTSYMBOL\x10\x05\x12\r\n\tHEARTBEAT\x10\x07\x12\n\n\x06\x45QUITY\x10\x08\x12\t\n\x05INDEX\x10\t\x12\x0e\n\nMUTUALFUND\x10\x0b\x12\x0f\n\x0bMONEYMARKET\x10\x0c\x12\n\n\x06OPTION\x10\r\x12\x0c\n\x08\x43URRENCY\x10\x0e\x12\x0b\n\x07WARRANT\x10\x0f\x12\x08\n\x04\x42OND\x10\x11\x12\n\n\x06\x46UTURE\x10\x12\x12\x07\n\x03\x45TF\x10\x14\x12\r\n\tCOMMODITY\x10\x17\x12\x0c\n\x08\x45\x43NQUOTE\x10\x1c\x12\x12\n\x0e\x43RYPTOCURRENCY\x10)\x12\r\n\tINDICATOR\x10*\x12\r\n\x08INDUSTRY\x10\xe8\x07"\x1f\n\nOptionType\x12\x08\n\x04\x43\x41LL\x10\x00\x12\x07\n\x03PUT\x10\x01"a\n\x0fMarketHoursType\x12\x0e\n\nPRE_MARKET\x10\x00\x12\x12\n\x0eREGULAR_MARKET\x10\x01\x12\x0f\n\x0bPOST_MARKET\x10\x02\x12\x19\n\x15\x45XTENDED_HOURS_MARKET\x10\x03\x62\x06proto3',
)


_PRICINGDATA_QUOTETYPE = _descriptor.EnumDescriptor(
    name="QuoteType",
    full_name="PricingData.QuoteType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="NONE",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ALTSYMBOL",
            index=1,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="HEARTBEAT",
            index=2,
            number=7,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="EQUITY",
            index=3,
            number=8,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INDEX",
            index=4,
            number=9,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MUTUALFUND",
            index=5,
            number=11,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MONEYMARKET",
            index=6,
            number=12,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="OPTION",
            index=7,
            number=13,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CURRENCY",
            index=8,
            number=14,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="WARRANT",
            index=9,
            number=15,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="BOND",
            index=10,
            number=17,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="FUTURE",
            index=11,
            number=18,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ETF",
            index=12,
            number=20,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="COMMODITY",
            index=13,
            number=23,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ECNQUOTE",
            index=14,
            number=28,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CRYPTOCURRENCY",
            index=15,
            number=41,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INDICATOR",
            index=16,
            number=42,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INDUSTRY",
            index=17,
            number=1000,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=745,
    serialized_end=1001,
)
_sym_db.RegisterEnumDescriptor(_PRICINGDATA_QUOTETYPE)

_PRICINGDATA_OPTIONTYPE = _descriptor.EnumDescriptor(
    name="OptionType",
    full_name="PricingData.OptionType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="CALL",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PUT",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1003,
    serialized_end=1034,
)
_sym_db.RegisterEnumDescriptor(_PRICINGDATA_OPTIONTYPE)

_PRICINGDATA_MARKETHOURSTYPE = _descriptor.EnumDescriptor(
    name="MarketHoursType",
    full_name="PricingData.MarketHoursType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="PRE_MARKET",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="REGULAR_MARKET",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="POST_MARKET",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="EXTENDED_HOURS_MARKET",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1036,
    serialized_end=1133,
)
_sym_db.RegisterEnumDescriptor(_PRICINGDATA_MARKETHOURSTYPE)


_PRICINGDATA = _descriptor.Descriptor(
    name="PricingData",
    full_name="PricingData",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="PricingData.id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="price",
            full_name="PricingData.price",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="time",
            full_name="PricingData.time",
            index=2,
            number=3,
            type=18,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="currency",
            full_name="PricingData.currency",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="exchange",
            full_name="PricingData.exchange",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="quoteType",
            full_name="PricingData.quoteType",
            index=5,
            number=6,
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
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="marketHours",
            full_name="PricingData.marketHours",
            index=6,
            number=7,
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
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="changePercent",
            full_name="PricingData.changePercent",
            index=7,
            number=8,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="dayVolume",
            full_name="PricingData.dayVolume",
            index=8,
            number=9,
            type=18,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="dayHigh",
            full_name="PricingData.dayHigh",
            index=9,
            number=10,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="dayLow",
            full_name="PricingData.dayLow",
            index=10,
            number=11,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="change",
            full_name="PricingData.change",
            index=11,
            number=12,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="shortName",
            full_name="PricingData.shortName",
            index=12,
            number=13,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="expireDate",
            full_name="PricingData.expireDate",
            index=13,
            number=14,
            type=18,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="openPrice",
            full_name="PricingData.openPrice",
            index=14,
            number=15,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="previousClose",
            full_name="PricingData.previousClose",
            index=15,
            number=16,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="strikePrice",
            full_name="PricingData.strikePrice",
            index=16,
            number=17,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="underlyingSymbol",
            full_name="PricingData.underlyingSymbol",
            index=17,
            number=18,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="openInterest",
            full_name="PricingData.openInterest",
            index=18,
            number=19,
            type=18,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="optionsType",
            full_name="PricingData.optionsType",
            index=19,
            number=20,
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
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="miniOption",
            full_name="PricingData.miniOption",
            index=20,
            number=21,
            type=18,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="lastSize",
            full_name="PricingData.lastSize",
            index=21,
            number=22,
            type=18,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="bid",
            full_name="PricingData.bid",
            index=22,
            number=23,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="bidSize",
            full_name="PricingData.bidSize",
            index=23,
            number=24,
            type=18,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="ask",
            full_name="PricingData.ask",
            index=24,
            number=25,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="askSize",
            full_name="PricingData.askSize",
            index=25,
            number=26,
            type=18,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="priceHint",
            full_name="PricingData.priceHint",
            index=26,
            number=27,
            type=18,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="vol_24hr",
            full_name="PricingData.vol_24hr",
            index=27,
            number=28,
            type=18,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="volAllCurrencies",
            full_name="PricingData.volAllCurrencies",
            index=28,
            number=29,
            type=18,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="fromcurrency",
            full_name="PricingData.fromcurrency",
            index=29,
            number=30,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="lastMarket",
            full_name="PricingData.lastMarket",
            index=30,
            number=31,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="circulatingSupply",
            full_name="PricingData.circulatingSupply",
            index=31,
            number=32,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="marketcap",
            full_name="PricingData.marketcap",
            index=32,
            number=33,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[
        _PRICINGDATA_QUOTETYPE,
        _PRICINGDATA_OPTIONTYPE,
        _PRICINGDATA_MARKETHOURSTYPE,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=22,
    serialized_end=1133,
)

_PRICINGDATA.fields_by_name["quoteType"].enum_type = _PRICINGDATA_QUOTETYPE
_PRICINGDATA.fields_by_name["marketHours"].enum_type = _PRICINGDATA_MARKETHOURSTYPE
_PRICINGDATA.fields_by_name["optionsType"].enum_type = _PRICINGDATA_OPTIONTYPE
_PRICINGDATA_QUOTETYPE.containing_type = _PRICINGDATA
_PRICINGDATA_OPTIONTYPE.containing_type = _PRICINGDATA
_PRICINGDATA_MARKETHOURSTYPE.containing_type = _PRICINGDATA
DESCRIPTOR.message_types_by_name["PricingData"] = _PRICINGDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PricingData = _reflection.GeneratedProtocolMessageType(
    "PricingData",
    (_message.Message,),
    {
        "DESCRIPTOR": _PRICINGDATA,
        "__module__": "PricingData_pb2"
        # @@protoc_insertion_point(class_scope:PricingData)
    },
)
_sym_db.RegisterMessage(PricingData)


# @@protoc_insertion_point(module_scope)
