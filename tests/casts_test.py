#!/usr/bin/env python
#
# Copyright 2016 The Fabulous Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import unittest
from terminate import casts

class TestControl(unittest.TestCase):

    def test_casts_yes_no(self):
        self.failUnlessEqual(casts.yes_no('y'), True)
        self.failUnlessEqual(casts.yes_no('n'), False)
        self.failUnlessEqual(casts.yes_no('Yes'), True)
        self.failUnlessEqual(casts.yes_no('nO'), False)
        self.failUnlessRaises(ValueError, casts.yes_no, 'spam')
        
    def test_casts_file(self):
        self.failUnlessEqual( type(casts.file(__file__)), type(open(__file__)) )
        self.failUnlessRaises(ValueError, casts.file, '')
        

if __name__ == '__main__':
    unittest.main()
