import logging
import posixpath
import sys
import unittest

from unicorn import *
from androidemu.utils import debug_utils
from androidemu.utils import cfg
from androidemu.utils.cfg import CodeBlock

class TestCfg(unittest.TestCase):

    def hex_addr_assert(self, a, b):
        self.assertEqual(a, b, "0x%08X != 0x%08X"%(a, b))
    #

    def test_cfg_libc_pthread_create(self):
        cbs = [CodeBlock(0x0000D218, 0x0000D268), CodeBlock(0x0000D268, 0x0000D274), 
        CodeBlock(0x0000D274, 0x0000D28C), CodeBlock(0x0000D28C, 0x0000D2C8), 
        CodeBlock(0x0000D2C8, 0x0000D2D4), CodeBlock(0x0000D2D4, 0x0000D314), CodeBlock(0x0000D314, 0x0000D32C), 
        CodeBlock(0x0000D32C, 0x0000D348), CodeBlock(0x0000D348, 0x0000D350), CodeBlock(0x0000D350, 0x0000D364), 
        CodeBlock(0x0000D364, 0x0000D378), CodeBlock(0x0000D378, 0x0000D3AC), CodeBlock(0x0000D3AC, 0x0000D3D8), 
        CodeBlock(0x0000D3D8, 0x0000D3E8), CodeBlock(0x0000D3E8, 0x0000D408), CodeBlock(0x0000D408, 0x0000D414), 
        CodeBlock(0x0000D414, 0x0000D454), CodeBlock(0x0000D454, 0x0000D468), CodeBlock(0x0000D468, 0x0000D47C), 
        CodeBlock(0x0000D47C, 0x0000D484), CodeBlock(0x0000D484, 0x0000D4B4), CodeBlock(0x0000D4B4, 0x0000D4C8), 
        CodeBlock(0x0000D4C8, 0x0000D4D8), CodeBlock(0x0000D4D8, 0x0000D518)]

        with open("vfs/system/lib/libc.so", "rb") as f:
            blocks = cfg.create_cfg(f, 0x0000D218, 768, False)
            #print(blocks[9])
            #print(blocks[9].parent)
            #print(blocks[9].childs)
            #print(blocks)
            self.assertTrue(len(cbs), len(blocks))
            for i in range(0, len(cbs)):
                self.hex_addr_assert(cbs[i].start, blocks[i].start)
                self.hex_addr_assert(cbs[i].end, blocks[i].end)
            #
            b = blocks[9]
            self.hex_addr_assert(b.start, 0x0000D350)
            self.hex_addr_assert(b.end, 0x0000D364)
            self.assertEqual(len(b.parent), 3)
            self.assertEqual(len(b.childs), 0)
        #
    #
#