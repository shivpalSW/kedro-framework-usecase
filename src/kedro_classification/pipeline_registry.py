"""Project pipelines."""
from __future__ import annotations

from typing import Dict
from kedro.pipeline import Pipeline
from kedro.framework.project import find_pipelines
from kedro_classification.pipelines import data_processing as dp
from kedro_classification.pipelines import data_science as ds


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    data_processing_pipeline = dp.create_pipeline()
    data_science_pipeline = ds.create_pipeline()
    #pipelines = find_pipelines()
    #pipelines["__default__"] = sum(pipelines.values())
    return {
        "__default__": data_processing_pipeline  + data_science_pipeline,
        "dp": data_processing_pipeline,
        "ds": data_science_pipeline,
    }


