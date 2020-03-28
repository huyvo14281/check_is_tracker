from sqlalchemy import Column, BigInteger, Integer, String
from sqlalchemy.util import hybridproperty

from model.base import Base


class HttpRequests(Base):
    __tablename__ = 'http_requests'
    __id = Column('id', BigInteger, primary_key=True)
    __incognito = Column('incognito', Integer)
    __crawl_id = Column('crawl_id', Integer)
    __visit_id = Column('visit_id', Integer)
    __extension_session_uuid = Column('extension_session_uuid', String)
    __event_ordinal = Column('event_ordinal', Integer)
    __window_id = Column('window_id', Integer)
    __tab_id = Column('tab_id', Integer)
    __frame_id = Column('frame_id', Integer)
    __url = Column('url', String)
    __top_level_url = Column('top_level_url', String)
    __parent_frame_id = Column('parent_frame_id', Integer)
    __frame_ancestors = Column('frame_ancestors', String)
    __method = Column('method', String)
    ___referrer = Column('referrer', String)
    __headers = Column('headers', String)
    __request_id = Column('request_id', String)
    __is_xhr = Column('is_xhr', Integer)
    __is_frame_load = Column('is_frame_load', Integer)
    __is_full_page = Column('is_full_page', Integer)
    __is_third_party_channel = Column('is_third_party_channel', Integer)
    __is_third_party_to_top_window = Column('is_third_party_to_top_window', Integer)
    __triggering_origin = Column('triggering_origin', String)
    __loading_origin = Column('loading_origin', String)
    __loading_href = Column('loading_href', String)
    __req_call_stack = Column('req_call_stack', String)
    __resource_type = Column('resource_type', String)
    ___post_body = Column('post_body', String)
    __post_body_raw = Column('post_body_raw', String)
    __time_stamp = Column('time_stamp', BigInteger)

    def __init__(self,
                 incognito: int,
                 crawl_id: int,
                 visit_id: int,
                 extension_session_uuid: str,
                 event_ordinal: int,
                 window_id: int,
                 tab_id: int,
                 frame_id: int,
                 url: str,
                 top_level_url: str,
                 parent_frame_id: int,
                 frame_ancestors: str,
                 method: str,
                 referrer: str,
                 headers: str,
                 request_id: str,
                 is_xhr: int,
                 is_frame_load: int,
                 is_full_page: int,
                 is_third_party_channel: int,
                 is_third_party_to_top_window: int,
                 triggering_origin: str,
                 loading_origin: str,
                 loading_href: str,
                 req_call_stack: str,
                 resource_type: str,
                 post_body: str,
                 post_body_raw: str,
                 time_stamp: int):
        self.__incognito = incognito
        self.__crawl_id = crawl_id
        self.__visit_id = visit_id
        self.__extension_session_uuid = extension_session_uuid
        self.__event_ordinal = event_ordinal
        self.__window_id = window_id
        self.__tab_id = tab_id
        self.__frame_id = frame_id
        self.__url = url
        self.__top_level_url = top_level_url
        self.__parent_frame_id = parent_frame_id
        self.__frame_ancestors = frame_ancestors
        self.__method = method
        self.___referrer = referrer
        self.__headers = headers
        self.__request_id = request_id
        self.__is_xhr = is_xhr
        self.__is_frame_load = is_frame_load
        self.__is_full_page = is_full_page
        self.__is_third_party_channel = is_third_party_channel
        self.__is_third_party_to_top_window = is_third_party_to_top_window
        self.__triggering_origin = triggering_origin
        self.__loading_origin = loading_origin
        self.__loading_href = loading_href
        self.__req_call_stack = req_call_stack
        self.__resource_type = resource_type
        self.___post_body = post_body
        self.__post_body_raw = post_body_raw
        self.__time_stamp = time_stamp

    @hybridproperty
    def id(self):
        return self.__id

    @hybridproperty
    def incognito(self):
        return self.__incognito

    @hybridproperty
    def crawl_id(self):
        return self.__crawl_id

    @hybridproperty
    def visit_id(self):
        return self.__visit_id

    @hybridproperty
    def extension_session_uuid(self):
        return self.__extension_session_uuid

    @hybridproperty
    def event_ordinal(self):
        return self.__event_ordinal

    @hybridproperty
    def window_id(self):
        return self.__window_id

    @hybridproperty
    def tab_id(self):
        return self.__tab_id

    @hybridproperty
    def frame_id(self):
        return self.__frame_id

    @hybridproperty
    def url(self):
        return self.__url

    @hybridproperty
    def top_level_url(self):
        return self.__top_level_url

    @hybridproperty
    def parent_frame_id(self):
        return self.__parent_frame_id

    @hybridproperty
    def frame_ancestors(self):
        return self.__frame_ancestors

    @hybridproperty
    def method(self):
        return self.__method

    @hybridproperty
    def referrer(self):
        return self.___referrer

    @hybridproperty
    def headers(self):
        return self.__headers

    @hybridproperty
    def request_id(self):
        return self.__request_id

    @hybridproperty
    def is_xhr(self):
        return self.__is_xhr

    @hybridproperty
    def is_frame_load(self):
        return self.__is_frame_load

    @hybridproperty
    def is_full_page(self):
        return self.__is_full_page

    @hybridproperty
    def is_third_party_channel(self):
        return self.__is_third_party_channel

    @hybridproperty
    def is_third_party_to_top_window(self):
        return self.__is_third_party_to_top_window

    @hybridproperty
    def triggering_origin(self):
        return self.__triggering_origin

    @hybridproperty
    def loading_origin(self):
        return self.__loading_origin

    @hybridproperty
    def loading_href(self):
        return self.__loading_href

    @hybridproperty
    def req_call_stack(self):
        return self.__req_call_stack

    @hybridproperty
    def resource_type(self):
        return self.__resource_type

    @hybridproperty
    def post_body(self):
        return self.___post_body

    @hybridproperty
    def post_body_raw(self):
        return self.__post_body_raw

    @hybridproperty
    def time_stamp(self):
        return self.__time_stamp
