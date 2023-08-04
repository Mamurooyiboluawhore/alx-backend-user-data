#!/usr/bin/env python3
''' 0. Regex-ing0.'''
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    ''' 0. Regex-ing'''
    return re.sub(r'({0}=)(.*?)(?={0}|$)'.format('|'.join(fields)),
                  r'\1{0}'.format(redaction), message)
