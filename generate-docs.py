import json, sys, shutil, os, pandas as pd
from functions import *

# python3 ./generate-docs.py github v0.3.1 true

provider = sys.argv[1]
provider_ver = sys.argv[2]
verbose = sys.argv[3]

if verbose == "true":
    verbose = True
else:
    verbose = False

if "." in provider:
    service_only = True
    provider = provider.split(".")[0]
    service = provider.split(".")[1]
else:
    service_only = False

# clean output dir
if service_only:
    shutil.rmtree("./docs/%s/%s" % (provider, service), ignore_errors=True)
else:
    shutil.rmtree("./docs/%s" % provider, ignore_errors=True)

#
# generate provider root doc
#

provider_doc = generate_front_matter(provider, "A description of the provider.")
provider_doc = provider_doc + generate_see_also_links()

# add install and auth blocks to provider doc
provider_doc = provider_doc + generate_installation_block(provider, provider_ver)
provider_doc = provider_doc + generate_auth_block(provider)

# get services and add to provider doc
iql_query = "SHOW EXTENDED SERVICES IN %s" % provider
services = run_stackql_query(iql_query, verbose, 5)
services = services.groupby("name", as_index=False).max()
provider_doc = provider_doc + "## Services\n"
provider_doc = provider_doc + generate_two_col_list(provider, services)

# create output dir
create_dir("./docs/%s" % provider, verbose)
    
# write provider doc
write_file("./docs/%s/index.md" % provider, provider_doc, verbose)

#
# create service and resource docs
#

for serviceIx, serviceRow in services.iterrows():
    
    serviceName = serviceRow["name"]

    # create service dir
    create_dir("./docs/%s/%s" % (provider, serviceName), verbose)

    # create service doc
    service_doc = generate_front_matter(serviceName, serviceRow["description"])
    service_doc = service_doc + generate_service_overview(provider, serviceRow)

    #
    # get resources
    #

    iql_query = "SHOW EXTENDED RESOURCES IN %s.%s" % (provider, serviceName)
    resources = run_stackql_query(iql_query, verbose, 5)

    service_doc = service_doc + "## Resources\n"
    service_doc = service_doc + generate_two_col_list(provider, resources, serviceName)

    # write service doc
    write_file("./docs/%s/%s/index.md" % (provider, serviceName), service_doc, verbose)

    for resourceIx, resourceRow in resources.iterrows():
        try:
            resourceName = resourceRow["name"]
        except:
            break

        # create resource dir
        create_dir("./docs/%s/%s/%s" % (provider, serviceName, resourceName), verbose)

        # create resource doc
        resource_doc = generate_front_matter(resourceName, resourceRow["description"])
        resource_doc = resource_doc + generate_resource_overview(provider, serviceName, resourceRow)

        # get fields
        iql_query = "DESCRIBE EXTENDED %s.%s.`%s`" % (provider, serviceName, resourceName)
        fields = run_stackql_query(iql_query, verbose, 5)
        resource_doc = resource_doc + generate_fields_table(fields)
        
        # get methods
        iql_query = "SHOW EXTENDED METHODS IN %s.%s.`%s`" % (provider, serviceName, resourceName)
        methods = run_stackql_query(iql_query, verbose, 5)
        resource_doc = resource_doc + generate_methods_table(methods)

        # write resource doc
        write_file("./docs/%s/%s/%s/index.md" % (provider, serviceName, resourceName), resource_doc, verbose)

    