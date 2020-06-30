#!/usr/bin/env python3
# coding: utf-8
from flask import Blueprint, Response, jsonify

from dashi.const import GET_STATUS_CODE
from dashi.type import AllInformation, Parameters, ServiceInfo, Type, Version
from dashi.util import generate_service_info

app_bp = Blueprint("dashi", __name__)


@app_bp.route("/service-info", methods=["GET"])
def get_service_info() -> Response:
    """
    Response to the name and version of workflow engines to be used inside the
    API Service. Also, it may be possible to extract the type, version and
    parameters of a workflow without using workflow engines. Therefore,
    workflow types and versions supported by this service are also responded
    to. The logic for determining workflow type and version is completely
    implementation-dependent.
    """
    res_body: ServiceInfo = generate_service_info()
    response: Response = jsonify(res_body)
    response.status_code = GET_STATUS_CODE

    return response


@app_bp.route("/inspect-workflow", methods=["GET"])
def inspect_workflow() -> Response:
    """
    This endpoint is used to inspect workflow. The parameter should be
    used one of wf_url, wf_content or wf_file.
    """
    res_body: AllInformation = {}
    response: Response = jsonify(res_body)
    response.status_code = GET_STATUS_CODE

    return response


@app_bp.route("/inspect-workflow/type", methods=["GET"])
def inspect_workflow_type() -> Response:
    """
    This endpoint is used to inspect workflow type. The parameter should be
    used one of wf_url, wf_content or wf_file.
    """
    res_body: Type = {}
    response: Response = jsonify(res_body)
    response.status_code = GET_STATUS_CODE

    return response


@app_bp.route("/inspect-workflow/version", methods=["GET"])
def inspect_workflow_version() -> Response:
    """
    This endpoint is used to inspect workflow version. The parameter should be
    used one of wf_url, wf_content or wf_file.
    """
    res_body: Version = {}
    response: Response = jsonify(res_body)
    response.status_code = GET_STATUS_CODE

    return response


@app_bp.route("/inspect-workflow/parameters", methods=["GET"])
def inspect_workflow_parameters() -> Response:
    """
    This endpoint is used to inspect workflow parameters. The parameter should
    be used one of wf_url, wf_content or wf_file.
    """
    res_body: Parameters = {}
    response: Response = jsonify(res_body)
    response.status_code = GET_STATUS_CODE

    return response
