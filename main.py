from google.cloud.aiplatform import pipeline_jobs
from config.config import PIPELINE_NAME
from flask import jsonify
import os
import sys

local_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(local_path, "config")
sys.path.append(config_path)


def run_pipeline_clustering(request) -> bool:
    job = pipeline_jobs.PipelineJob(
        display_name=f"{PIPELINE_NAME.replace('_', '-')}",
        template_path=f"{PIPELINE_NAME}.json",
        enable_caching=False,
    )
    job.submit()
    return True


def start_clustering(request):
    response = run_pipeline_clustering(request)
    return jsonify({"mensagem": response}), 200
