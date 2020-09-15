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
    inputs = []

    # Extract inputs from MO Args
    if model.mo_args:
        # Find shapes argument
        mo_arg_input_shape = next((x[14:] for x in model.mo_args if "--input_shape=" in x), None)
        mo_arg_input_name = next((x[8:] for x in model.mo_args if "--input=" in x), None)
        #print(f"names: {mo_arg_input_name} and shapes: {mo_arg_input_shape}")
        if mo_arg_input_shape and mo_arg_input_name:
            input_shapes = json.loads("[" + mo_arg_input_shape + "]")
            input_names = mo_arg_input_name.split(",")
            for i in range(len(input_names)):
                input_entry = {}
                input_entry["name"] = input_names[i]
                input_entry["shape"] = input_shapes[i] # let it throw out of range
                input_entry["layout"] = "unknown"
                inputs.append(input_entry)

    for modelfile in model.files:
        modelfiles.append(
            {
                'name': str(modelfile.name),
                'sha256': modelfile.sha256,
                'source': {'url': str(modelfile.source), '$type': 'http'}
            })
    model_info = {
        'name': model.name,
        #'model_id': f"{model.name}-fw_{model.framework}-input_{input_shape}",
        'files': modelfiles,
        'description': model.description,
        'framework': {"name": model.framework},
        'license_url': model.license_url,
        'precisions': sorted(model.precisions),
        'subdirectory': str(model.subdirectory),
        'task_type': [str(model.task_type)],
        'model_optimizer_args': model.mo_args if model.mo_args else [],
        'inputs': inputs
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
