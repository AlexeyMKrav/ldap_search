from string import Template
from ldap3 import Server, Connection, SUBTREE
import config

attr = ['DisplayName', "Company", "mail", "Department", "Title", "SamAccountName"]
login = input()
domain_name, username = login.split('\\')
AD_SEARCH_TREE = Template(config.LDAP_SEARCH_BASE).safe_substitute(domain=domain_name)
conn = Connection(server=Server(config.LDAP_SERVER), user=config.LDAP_USER, password=config.LDAP_PASSWORD)
conn.bind()
conn.search(AD_SEARCH_TREE,
            f'(&(objectCategory=person)(objectClass=user)(sAMAccountName={username}))',
            SUBTREE,
            attributes=attr)
for item in conn.entries[0]:
    print(item)
