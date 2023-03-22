"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.6
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import process


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([node(process, "data_right", "data_right_output")])
