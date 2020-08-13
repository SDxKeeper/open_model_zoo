#!/usr/bin/env python3

# Copyright (c) 2019 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import json
import sys

from pathlib import Path

import common

def to_info(model):
    modelfiles = []
    input_shape = "unknown"
    if model.mo_args:
        for arg in model.mo_args:
            if "input_shape" in arg:
                shape_list = list(json.loads("[" + arg.split("=")[1]+"]"))

                input_strs=[]
                for input in shape_list:
                    input_strs.append("x".join(str(x) for x in input))
                input_shape = "_".join(input_strs)



    for modelfile in model.files:
        modelfiles.append(
            {
                'name': str(modelfile.name),
                'sha256': modelfile.sha256,
                'source': str(modelfile.source)
            })
    model_info = {
        'name': model.name,
        'model_id': f"{model.name}-fw_{model.framework}-input_{input_shape}",
        'files': modelfiles,
        'description': model.description,
        'framework': model.framework,
        'license_url': model.license_url,
        'precisions': sorted(model.precisions),
        'subdirectory': str(model.subdirectory),
        'task_type': str(model.task_type),
    }
    if model.postprocessing:
        model_info['postprocessing'] = True

    return model_info

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', metavar='PAT[,PAT...]',
        help='only dump info for models whose names match at least one of the specified patterns')
    parser.add_argument('--list', type=Path, metavar='FILE.LST',
        help='only dump info for models whose names match at least one of the patterns in the specified file')
    parser.add_argument('--all', action='store_true', help='dump info for all available models')
    parser.add_argument('--print_all', action='store_true', help='print all available models')
    args = parser.parse_args()

    models = common.load_models_from_args(parser, args)

    json.dump(list(map(to_info, models)), sys.stdout, indent=4)
    print() # add a final newline

if __name__ == '__main__':
    main()
