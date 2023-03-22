"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline, pipeline


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()

    for region in ["parasubicular", "parainsular"]:
        pipelines[f"{region}.data_processing"] = pipeline(
            pipelines["data_processing"], namespace=region
        )

    del pipelines["data_processing"]  # We don't want the non-namespaced pipeline.

    pipelines["__default__"] = sum(pipelines.values())
    return pipelines
