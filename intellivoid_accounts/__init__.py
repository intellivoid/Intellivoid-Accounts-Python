
"""
Intellivoid Accounts COA Library
"""
__version__ = '1.0.0'
__author__ = 'Zi Xing'
__license__ = 'MIT'

from intellivoid_accounts.auth import COA
from intellivoid_accounts.exception import AuthenticationError
from intellivoid_accounts.objects import AuthenticationRequest, Permissions
from intellivoid_accounts.access import Access