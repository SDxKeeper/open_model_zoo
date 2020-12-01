#!/usr/bin/env python3

"""
 Copyright (c) 2020 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import sys
import argparse
from pathlib import Path

from omz_tools.downloader import main_body, get_argument_parser, DownloaderException

def main(argv=sys.argv[1:]):
    parser = get_argument_parser()
    args = parser.parse_args(argv)

    try:
        main_body(args)
    except ValueError as err:
        print("Error happened during download process: ", err)
        sys.exit(2)
    except DownloaderException as err:
        print("Error happened during download process: ", err)
        sys.exit(1)

if __name__ == '__main__':
    main()
