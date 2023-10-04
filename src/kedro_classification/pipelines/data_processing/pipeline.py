"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.13
"""
from kedro.pipeline import Pipeline, node, pipeline
from .nodes import preprocess_companies, preprocess_shuttles,create_model_input_table


def create_pipeline(**kwargs) -> Pipeline:
    """_summary_

    Returns:
        Pipeline: _description_
    """
    return pipeline(
        [
            node(
                func=preprocess_companies,
                inputs="companies",
                outputs="preprocessed_companies",
                name="preprocess_companies_node",
            ),
            node(
                func=preprocess_shuttles,
                inputs="shuttles",
                outputs="preprocessed_shuttles",
                name="preprocess_shuttles_node",
            ),
            node(
                func=create_model_input_table,
                inputs=["preprocessed_shuttles", "preprocessed_companies", "reviews"],
                outputs="model_input_table",
                name="create_model_input_table_node",
),
        ]
    )
