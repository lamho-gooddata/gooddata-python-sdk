# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from gooddata_afm_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from gooddata_afm_client.model.afm import AFM
from gooddata_afm_client.model.absolute_date_filter import AbsoluteDateFilter
from gooddata_afm_client.model.absolute_date_filter_absolute_date_filter import AbsoluteDateFilterAbsoluteDateFilter
from gooddata_afm_client.model.abstract_measure_value_filter import AbstractMeasureValueFilter
from gooddata_afm_client.model.afm_execution import AfmExecution
from gooddata_afm_client.model.afm_execution_response import AfmExecutionResponse
from gooddata_afm_client.model.afm_identifier import AfmIdentifier
from gooddata_afm_client.model.afm_local_identifier import AfmLocalIdentifier
from gooddata_afm_client.model.afm_object_identifier import AfmObjectIdentifier
from gooddata_afm_client.model.afm_object_identifier_attribute import AfmObjectIdentifierAttribute
from gooddata_afm_client.model.afm_object_identifier_attribute_identifier import AfmObjectIdentifierAttributeIdentifier
from gooddata_afm_client.model.afm_object_identifier_core import AfmObjectIdentifierCore
from gooddata_afm_client.model.afm_object_identifier_core_identifier import AfmObjectIdentifierCoreIdentifier
from gooddata_afm_client.model.afm_object_identifier_dataset import AfmObjectIdentifierDataset
from gooddata_afm_client.model.afm_object_identifier_dataset_identifier import AfmObjectIdentifierDatasetIdentifier
from gooddata_afm_client.model.afm_object_identifier_identifier import AfmObjectIdentifierIdentifier
from gooddata_afm_client.model.afm_object_identifier_label import AfmObjectIdentifierLabel
from gooddata_afm_client.model.afm_object_identifier_label_identifier import AfmObjectIdentifierLabelIdentifier
from gooddata_afm_client.model.afm_valid_objects_query import AfmValidObjectsQuery
from gooddata_afm_client.model.afm_valid_objects_response import AfmValidObjectsResponse
from gooddata_afm_client.model.arithmetic_measure_definition import ArithmeticMeasureDefinition
from gooddata_afm_client.model.arithmetic_measure_definition_arithmetic_measure import ArithmeticMeasureDefinitionArithmeticMeasure
from gooddata_afm_client.model.attribute_execution_result_header import AttributeExecutionResultHeader
from gooddata_afm_client.model.attribute_filter import AttributeFilter
from gooddata_afm_client.model.attribute_filter_elements import AttributeFilterElements
from gooddata_afm_client.model.attribute_header_out import AttributeHeaderOut
from gooddata_afm_client.model.attribute_header_out_attribute_header import AttributeHeaderOutAttributeHeader
from gooddata_afm_client.model.attribute_item import AttributeItem
from gooddata_afm_client.model.attribute_result_header import AttributeResultHeader
from gooddata_afm_client.model.comparison_measure_value_filter import ComparisonMeasureValueFilter
from gooddata_afm_client.model.comparison_measure_value_filter_comparison_measure_value_filter import ComparisonMeasureValueFilterComparisonMeasureValueFilter
from gooddata_afm_client.model.data_column_locator import DataColumnLocator
from gooddata_afm_client.model.data_column_locators import DataColumnLocators
from gooddata_afm_client.model.date_filter import DateFilter
from gooddata_afm_client.model.dimension import Dimension
from gooddata_afm_client.model.dimension_header import DimensionHeader
from gooddata_afm_client.model.element import Element
from gooddata_afm_client.model.elements_request import ElementsRequest
from gooddata_afm_client.model.elements_response import ElementsResponse
from gooddata_afm_client.model.execution_links import ExecutionLinks
from gooddata_afm_client.model.execution_response import ExecutionResponse
from gooddata_afm_client.model.execution_result import ExecutionResult
from gooddata_afm_client.model.execution_result_grand_total import ExecutionResultGrandTotal
from gooddata_afm_client.model.execution_result_header import ExecutionResultHeader
from gooddata_afm_client.model.execution_result_paging import ExecutionResultPaging
from gooddata_afm_client.model.execution_settings import ExecutionSettings
from gooddata_afm_client.model.filter_by import FilterBy
from gooddata_afm_client.model.filter_definition import FilterDefinition
from gooddata_afm_client.model.filter_definition_for_simple_measure import FilterDefinitionForSimpleMeasure
from gooddata_afm_client.model.header_group import HeaderGroup
from gooddata_afm_client.model.inline_filter_definition import InlineFilterDefinition
from gooddata_afm_client.model.inline_filter_definition_inline import InlineFilterDefinitionInline
from gooddata_afm_client.model.inline_measure_definition import InlineMeasureDefinition
from gooddata_afm_client.model.inline_measure_definition_inline import InlineMeasureDefinitionInline
from gooddata_afm_client.model.measure_definition import MeasureDefinition
from gooddata_afm_client.model.measure_execution_result_header import MeasureExecutionResultHeader
from gooddata_afm_client.model.measure_group_headers import MeasureGroupHeaders
from gooddata_afm_client.model.measure_header_out import MeasureHeaderOut
from gooddata_afm_client.model.measure_item import MeasureItem
from gooddata_afm_client.model.measure_result_header import MeasureResultHeader
from gooddata_afm_client.model.measure_value_filter import MeasureValueFilter
from gooddata_afm_client.model.negative_attribute_filter import NegativeAttributeFilter
from gooddata_afm_client.model.negative_attribute_filter_negative_attribute_filter import NegativeAttributeFilterNegativeAttributeFilter
from gooddata_afm_client.model.paging import Paging
from gooddata_afm_client.model.pop_dataset import PopDataset
from gooddata_afm_client.model.pop_dataset_measure_definition import PopDatasetMeasureDefinition
from gooddata_afm_client.model.pop_dataset_measure_definition_previous_period_measure import PopDatasetMeasureDefinitionPreviousPeriodMeasure
from gooddata_afm_client.model.pop_date import PopDate
from gooddata_afm_client.model.pop_date_measure_definition import PopDateMeasureDefinition
from gooddata_afm_client.model.pop_date_measure_definition_over_period_measure import PopDateMeasureDefinitionOverPeriodMeasure
from gooddata_afm_client.model.pop_measure_definition import PopMeasureDefinition
from gooddata_afm_client.model.positive_attribute_filter import PositiveAttributeFilter
from gooddata_afm_client.model.positive_attribute_filter_positive_attribute_filter import PositiveAttributeFilterPositiveAttributeFilter
from gooddata_afm_client.model.range_measure_value_filter import RangeMeasureValueFilter
from gooddata_afm_client.model.range_measure_value_filter_range_measure_value_filter import RangeMeasureValueFilterRangeMeasureValueFilter
from gooddata_afm_client.model.ranking_filter import RankingFilter
from gooddata_afm_client.model.ranking_filter_ranking_filter import RankingFilterRankingFilter
from gooddata_afm_client.model.relative_date_filter import RelativeDateFilter
from gooddata_afm_client.model.relative_date_filter_relative_date_filter import RelativeDateFilterRelativeDateFilter
from gooddata_afm_client.model.rest_api_identifier import RestApiIdentifier
from gooddata_afm_client.model.result_cache_metadata import ResultCacheMetadata
from gooddata_afm_client.model.result_dimension import ResultDimension
from gooddata_afm_client.model.result_dimension_header import ResultDimensionHeader
from gooddata_afm_client.model.result_spec import ResultSpec
from gooddata_afm_client.model.simple_measure_definition import SimpleMeasureDefinition
from gooddata_afm_client.model.simple_measure_definition_measure import SimpleMeasureDefinitionMeasure
from gooddata_afm_client.model.sort_key import SortKey
from gooddata_afm_client.model.sort_key_attribute import SortKeyAttribute
from gooddata_afm_client.model.sort_key_attribute_attribute import SortKeyAttributeAttribute
from gooddata_afm_client.model.sort_key_total import SortKeyTotal
from gooddata_afm_client.model.sort_key_total_total import SortKeyTotalTotal
from gooddata_afm_client.model.sort_key_value import SortKeyValue
from gooddata_afm_client.model.sort_key_value_value import SortKeyValueValue
from gooddata_afm_client.model.total import Total
from gooddata_afm_client.model.total_dimension import TotalDimension
from gooddata_afm_client.model.total_execution_result_header import TotalExecutionResultHeader
from gooddata_afm_client.model.total_result_header import TotalResultHeader
