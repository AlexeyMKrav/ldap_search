import os
from dotenv import load_dotenv

load_dotenv()

LDAP_SERVER = os.environ.get("LDAP_SERVER")
LDAP_USER = os.environ.get("LDAP_USER")
LDAP_PASSWORD = os.environ.get("LDAP_PASSWORD")
LDAP_SEARCH_BASE = os.environ.get("LDAP_SEARCH_BASE")
