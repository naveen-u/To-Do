#!/usr/bin/env python3

# "THE BEER-WARE LICENSE" (Revision 43~maze)

# <maze@pyth0n.org> wrote these files. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return.

import atexit
import math
import os
import random
import re
import sys
import time
from signal import signal, SIGPIPE, SIG_DFL

# override default handler so no exceptions on SIGPIPE
signal(SIGPIPE, SIG_DFL)

# Reset terminal colors at exit
def reset():
    sys.stdout.write('\x1b[0m')
    sys.stdout.flush()

atexit.register(reset)

STRIP_ANSI = re.compile(r'\x1b\[(\d+)(;\d+)?(;\d+)?[m|K]')
COLOR_ANSI = (
    (0x00, 0x00, 0x00), (0xcd, 0x00, 0x00),
    (0x00, 0xcd, 0x00), (0xcd, 0xcd, 0x00),
    (0x00, 0x00, 0xee), (0xcd, 0x00, 0xcd),
    (0x00, 0xcd, 0xcd), (0xe5, 0xe5, 0xe5),
    (0x7f, 0x7f, 0x7f), (0xff, 0x00, 0x00),
    (0x00, 0xff, 0x00), (0xff, 0xff, 0x00),
    (0x5c, 0x5c, 0xff), (0xff, 0x00, 0xff),
    (0x00, 0xff, 0xff), (0xff, 0xff, 0xff),
)

class LolCat(object):
    def __init__(self, options, output=sys.stdout):

        self.mode = options.mode or self.detect_mode()
        if options.spread <= 0.0:
            options.spread = 3.0
        self.seed = random.randint(0, 256) if options.seed <= 0 else options.seed
        self.output = output
        self.spread = options.spread
        self.freq = options.freq
        self.force = options.force

    def _distance(self, rgb1, rgb2):
        return sum(map(lambda c: (c[0] - c[1]) ** 2,
            zip(rgb1, rgb2)))

    def ansi(self, rgb):
        r, g, b = rgb

        if self.mode in (8, 16):
            colors = COLOR_ANSI[:self.mode]
            matches = [(self._distance(c, map(int, rgb)), i) for i, c in enumerate(colors)]
            matches.sort()
            color = matches[0][1]

            return '3%d' % (color,)
        else:
            gray_possible = True
            sep = 2.5

            while gray_possible:
                if r < sep or g < sep or b < sep:
                    gray = r < sep and g < sep and b < sep
                    gray_possible = False

                sep += 42.5

            if gray:
                color = 232 + int(float(sum(rgb) / 33.0))
            else:
                color = sum([16]+[int(6 * float(val)/256) * mod
                    for val, mod in zip(rgb, [36, 6, 1])])

            return '38;5;%d' % (color,)

    def wrap(self, *codes):
        return '\x1b[%sm' % (''.join(codes),)

    def rainbow(self, freq, i):
        r = math.sin(freq * i) * 127 + 128
        g = math.sin(freq * i + 2 * math.pi / 3) * 127 + 128
        b = math.sin(freq * i + 4 * math.pi / 3) * 127 + 128
        return [r, g, b]

    def cat(self, fd):
        for line in fd:
            self.seed += 1
            self.println(line)

    def println(self, s):
        s = s.rstrip()
        if self.force or self.output.isatty():
            s = STRIP_ANSI.sub('', s)

        self.println_plain(s)

        self.output.write('\n')
        self.output.flush()

    def println_plain(self, s):
        for i, c in enumerate(s):
            rgb = self.rainbow(self.freq, self.seed + i / self.spread)
            self.output.write(''.join([self.wrap(self.ansi(rgb)), c]))

    def detect_mode(self, term_hint='xterm-256color'):
        '''
        Poor-mans color mode detection.
        '''
        if 'ANSICON' in os.environ:
            return 16
        elif os.environ.get('ConEmuANSI', 'OFF') == 'ON':
            return 256
        else:
            term = os.environ.get('TERM', term_hint)
            if term.endswith('-256color') or term in ('xterm', 'screen'):
                return 256
            elif term.endswith('-color') or term in ('rxvt',):
                return 16
            else:
                return 256 # optimistic default
