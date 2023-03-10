"""
    Elastic Email REST API

    This API is based on the REST API architecture, allowing the user to easily manage their data with this resource-based approach.    Every API call is established on which specific request type (GET, POST, PUT, DELETE) will be used.    The API has a limit of 20 concurrent connections and a hard timeout of 600 seconds per request.    To start using this API, you will need your Access Token (available <a target=\"_blank\" href=\"https://app.elasticemail.com/marketing/settings/new/manage-api\">here</a>). Remember to keep it safe. Required access levels are listed in the given request’s description.    Downloadable library clients can be found in our Github repository <a target=\"_blank\" href=\"https://github.com/ElasticEmail?tab=repositories&q=%22rest+api%22+in%3Areadme\">here</a>  # noqa: E501

    The version of the OpenAPI document: 4.0.0
    Contact: support@elasticemail.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ElasticEmail.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from ElasticEmail.exceptions import ApiAttributeError


def lazy_import():
    from ElasticEmail.model.body_part import BodyPart
    from ElasticEmail.model.message_attachment import MessageAttachment
    from ElasticEmail.model.utm import Utm
    globals()['BodyPart'] = BodyPart
    globals()['MessageAttachment'] = MessageAttachment
    globals()['Utm'] = Utm


class EmailContent(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'body': ([BodyPart],),  # noqa: E501
            'merge': ({str: (str,)},),  # noqa: E501
            'attachments': ([MessageAttachment],),  # noqa: E501
            'headers': ({str: (str,)},),  # noqa: E501
            'postback': (str,),  # noqa: E501
            'envelope_from': (str,),  # noqa: E501
            '_from': (str,),  # noqa: E501
            'reply_to': (str,),  # noqa: E501
            'subject': (str,),  # noqa: E501
            'template_name': (str,),  # noqa: E501
            'attach_files': ([str],),  # noqa: E501
            'utm': (Utm,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'body': 'Body',  # noqa: E501
        'merge': 'Merge',  # noqa: E501
        'attachments': 'Attachments',  # noqa: E501
        'headers': 'Headers',  # noqa: E501
        'postback': 'Postback',  # noqa: E501
        'envelope_from': 'EnvelopeFrom',  # noqa: E501
        '_from': 'From',  # noqa: E501
        'reply_to': 'ReplyTo',  # noqa: E501
        'subject': 'Subject',  # noqa: E501
        'template_name': 'TemplateName',  # noqa: E501
        'attach_files': 'AttachFiles',  # noqa: E501
        'utm': 'Utm',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """EmailContent - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            body ([BodyPart]): List of e-mail body parts, with user-provided MIME types (text/html, text/plain etc). [optional]  # noqa: E501
            merge ({str: (str,)}): A key-value collection of custom merge fields, shared between recipients. Should be used in e-mail body like so: {firstname}, {lastname} etc.. [optional]  # noqa: E501
            attachments ([MessageAttachment]): Attachments provided by sending binary data. [optional]  # noqa: E501
            headers ({str: (str,)}): A key-value collection of custom e-mail headers.. [optional]  # noqa: E501
            postback (str): Postback header.. [optional]  # noqa: E501
            envelope_from (str): E-mail with an optional name to be used as the envelope from address (e.g.: John Doe <email@domain.com>). [optional]  # noqa: E501
            _from (str): Your e-mail with an optional name (e.g.: John Doe <email@domain.com>). [optional]  # noqa: E501
            reply_to (str): To what address should the recipients reply to (e.g. John Doe <email@domain.com>). [optional]  # noqa: E501
            subject (str): Default subject of email.. [optional]  # noqa: E501
            template_name (str): Name of template.. [optional]  # noqa: E501
            attach_files ([str]): Names of previously uploaded files that should be sent as downloadable attachments. [optional]  # noqa: E501
            utm (Utm): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', False)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """EmailContent - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            body ([BodyPart]): List of e-mail body parts, with user-provided MIME types (text/html, text/plain etc). [optional]  # noqa: E501
            merge ({str: (str,)}): A key-value collection of custom merge fields, shared between recipients. Should be used in e-mail body like so: {firstname}, {lastname} etc.. [optional]  # noqa: E501
            attachments ([MessageAttachment]): Attachments provided by sending binary data. [optional]  # noqa: E501
            headers ({str: (str,)}): A key-value collection of custom e-mail headers.. [optional]  # noqa: E501
            postback (str): Postback header.. [optional]  # noqa: E501
            envelope_from (str): E-mail with an optional name to be used as the envelope from address (e.g.: John Doe <email@domain.com>). [optional]  # noqa: E501
            _from (str): Your e-mail with an optional name (e.g.: John Doe <email@domain.com>). [optional]  # noqa: E501
            reply_to (str): To what address should the recipients reply to (e.g. John Doe <email@domain.com>). [optional]  # noqa: E501
            subject (str): Default subject of email.. [optional]  # noqa: E501
            template_name (str): Name of template.. [optional]  # noqa: E501
            attach_files ([str]): Names of previously uploaded files that should be sent as downloadable attachments. [optional]  # noqa: E501
            utm (Utm): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', False)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
