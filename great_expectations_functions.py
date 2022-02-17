import great_expectations as ge
import great_expectations.jupyter_ux
from great_expectations.core.batch import BatchRequest
import pandas as pd
import numpy as np

# column_name = 'No'
def column_to_exist(series, column  ):
    return ge.from_pandas(series).expect_column_to_exist(column = column)['success']

def table_columns_to_match_ordered_list(series, columns= None ):
    """
    takes series and a list contain columns in order of desire
    """
    return ge.from_pandas(series).expect_table_columns_to_match_ordered_list(column_list = columns)

def table_row_count_to_be_between(series, min_value=None, max_value=None):
    return ge.from_pandas(series).expect_table_row_count_to_be_between( min_value = min_value, max_value = max_value)

def table_row_count_to_equal(series, row_count = None):
    return ge.from_pandas(series).expect_table_row_count_to_equal( value = row_count)

# def table_row_count_to_equal_other_table(series, column  ):
#     return ge.from_pandas(series).expect_table_row_count_to_equal_other_table(column = column)

def column_values_to_be_unique(series,column_name):
    return ge.from_pandas(series).expect_column_values_to_be_unique(column = column_name)

def column_values_to_not_be_null(series, column  ):
    return ge.from_pandas(series).expect_column_values_to_not_be_null(column = column)

def column_values_to_be_null(series, column  ):
    return ge.from_pandas(series).expect_column_values_to_be_null(column = column)

def column_values_to_be_of_type(series, column  ,type_defined = None ):
    return ge.from_pandas(series).expect_column_values_to_be_of_type(column = column, type_ = type_defined)

def column_values_to_be_between(series, column  ,min_value=None, max_value=None):
    return ge.from_pandas(series).expect_column_values_to_be_between(column = column , min_value = min_value , max_value = max_value)

def column_values_to_be_increasing(series, column  ):    
    return ge.from_pandas(series).expect_column_values_to_be_increasing(column = column)

def column_values_to_be_decreasing(series, column  ):
    return ge.from_pandas(series).expect_column_values_to_be_decreasing(column = column)

def column_value_lengths_to_be_between(series, column  ,min_value=None, max_value=None):
    return ge.from_pandas(series).expect_column_value_lengths_to_be_between(column = column, min_value=min_value, max_value = max_value)

def column_value_lengths_to_equal(series, column   , Length_value = None):
    """
    takes column: must be string and length of column desired
    """
    try:
        return ge.from_pandas(series).expect_column_value_lengths_to_equal(column = column,value = Length_value)
    except:
        return 'Column is not string'

def column_values_to_match_regex(series, column  ,regex = None):
    """
    takes column: must be string and length of column desired
    """
    try:
        return ge.from_pandas(series).expect_column_values_to_match_regex(column = column,regex = regex)
    except:
        return 'Column is not string'

def column_values_to_not_match_regex(series, column  ,regex = None):
    """
    takes column: must be string and length of column desired
    """
    try:
        return ge.from_pandas(series).expect_column_values_to_not_match_regex(column = column,regex = regex)
    except:
        return 'Column is not string'

def column_values_to_match_regex_list(series, column  , regex_list = None):
    """
    takes column: must be string and length of column desired
    """
    try:
        return ge.from_pandas(series).expect_column_values_to_match_regex_list(column = column, regex_list = regex_list)
    except:
        return 'Column is not string'

def column_values_to_not_match_regex_list(series, column  ,regex_list = None):
    """
    takes column: must be string and length of column desired
    """
    try:
        return ge.from_pandas(series).expect_column_values_to_not_match_regex_list(column = column,regex_list = regex_list)
    except:
        return 'Column is not string'
    

def column_values_to_match_strftime_format(series, column  , strftime_format = None):
    """
    takes column: must be string and length of column desired
    """
    try:
        return ge.from_pandas(series).expect_column_values_to_match_strftime_format(column = column, strftime_format = strftime_format)
    except Exception as err:
        return 'Column is not string{} or date format is not specified'.format(err)

def column_distinct_values_to_be_in_set(series, column ,set_list = None ):
    """
    takes a list in which values are declared
    """
    return ge.from_pandas(series).expect_column_distinct_values_to_be_in_set(column = column,value_set= set_list)

def column_distinct_values_to_contain_set(series, column  ,set_list =None):
    """
    takes a series and a list of values to compare them
    """
    return ge.from_pandas(series).expect_column_distinct_values_to_contain_set(column = column,value_set = set_list)

def column_distinct_values_to_equal_set(series, column  ,set_list =None):
    """
    takes a series and a list of values to compare them
    """
    return ge.from_pandas(series).expect_column_distinct_values_to_equal_set(column = column,value_set = set_list)

def column_distinct_values_to_equal_set(series, column  , set_list = None):
    """
    takes a series and a list of values to compare them
    """
    return ge.from_pandas(series).expect_column_distinct_values_to_equal_set(column = column, value_set = set_list)

def column_mean_to_be_between(series, column  , min_value=None, max_value = None):
    return ge.from_pandas(series).expect_column_mean_to_be_between(column = column,min_value=min_value, max_value = max_value)

def column_median_to_be_between(series, column  , min_value=None, max_value = None):
    return ge.from_pandas(series).expect_column_median_to_be_between(column = column,min_value=min_value, max_value = max_value)

def column_quantile_values_to_be_between(series, column  , min_value=None, max_value = None):
    return ge.from_pandas(series).expect_column_quantile_values_to_be_between(column = column,min_value=min_value, max_value = max_value)

def column_stdev_to_be_between(series, column  , min_value=None, max_value = None):
    return ge.from_pandas(series).expect_column_stdev_to_be_between(column = column,min_value=min_value, max_value = max_value)

def column_unique_value_count_to_be_between(series, column  , min_value=None, max_value = None):
    return ge.from_pandas(series).expect_column_unique_value_count_to_be_between(column = column,min_value=min_value, max_value = max_value)

def column_proportion_of_unique_values_to_be_between(series, column  , min_value=None, max_value = None):
    return ge.from_pandas(series).expect_column_proportion_of_unique_values_to_be_between(column = column,min_value=min_value, max_value = max_value)

# def column_most_common_value_to_be_in_set(series, column  ):
#     return ge.from_pandas(series).expect_column_most_common_value_to_be_in_set(column = column)

def column_max_to_be_between(series, column  , min_value=None, max_value = None):
    return ge.from_pandas(series).expect_column_max_to_be_between(column = column,min_value=min_value, max_value = max_value)

def column_min_to_be_between(series, column  ,min_value=None, max_value = None):
    return ge.from_pandas(series).expect_column_min_to_be_between(column = column,min_value=min_value, max_value = max_value)

def column_sum_to_be_between(series, column  ,min_value=None, max_value = None):
    return ge.from_pandas(series).expect_column_sum_to_be_between(column = column,min_value=min_value, max_value = max_value)

def column_pair_values_A_to_be_greater_than_B(series,column_A, column_B, or_equal=None):
    return ge.from_pandas(series).expect_column_pair_values_A_to_be_greater_than_B(column_A = column_A, column_B = column_B)

def column_pair_values_to_be_equal(series, column_A, column_B, or_equal=None):
    return ge.from_pandas(series).expect_column_pair_values_to_be_equal(column_A = column_A, column_B = column_B)

# def expect_select_column_values_to_be_unique_within_record(series, column  ):
#     return ge.from_pandas(series).expect_select_column_values_to_be_unique_within_record(column = column)

# def multicolumn_sum_to_equal(series, column  ):
#     return ge.from_pandas(series).expect_multicolumn_sum_to_equal(column = column)

# def compound_columns_to_be_unique(series, column  ):
#     return ge.from_pandas(series).expect_compound_columns_to_be_unique(column = column)

def column_kl_divergence_to_be_less_than(series, column_A = None, column_B = None, threshold = None):
    return ge.from_pandas(series).expect_column_kl_divergence_to_be_less_than(column_A = column_A, column_B = column_B, threshold = threshold)
    
# def expect_column_bootstrapped_ks_test_p_value_to_be_greater_than(series, column  ):
#     return ge.from_pandas(series).expect_column_bootstrapped_ks_test_p_value_to_be_greater_than(column = column)
    
# def expect_column_chisquare_test_p_value_to_be_greater_than(series, column  ):
#     return ge.from_pandas(series).expect_column_chisquare_test_p_value_to_be_greater_than(column = column)
    
# def expect_column_parameterized_distribution_ks_test_p_value_to_be_greater_than(series, column  ):
#     return ge.from_pandas(series).expect_column_parameterized_distribution_ks_test_p_value_to_be_greater_than(column = column)
    