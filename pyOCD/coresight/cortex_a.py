"""
 mbed CMSIS-DAP debugger
 Copyright (c) 2006-2017 ARM Limited

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
from .cortex_target import CortexTarget

class CortexA(CortexTarget):
    def __init__(self, link, dp, ap, memoryMap=None, core_num=0):
        super(CortexA, self).__init__(link, dp, ap, memoryMap, core_num)

    DEBUG_BASE = 0x30070000