import json, sys, shutil, os, pandas as pd
from math import ceil

# python3 ./generate-docs.py github v0.3.1

provider = sys.argv[1]
provider_ver = sys.argv[2]

sys.path.append("../")
from pystackql import StackQL
iql = StackQL(exe="./stackql")

def generate_front_matter(title, description):
    return """---
title: %s
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and Deploy Cloud Infrastructure and Resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
%s  
    
See also:   
[[` SHOW `]](/docs/language-spec/show) [[` DESCRIBE `]](/docs/language-spec/describe)  
* * * 
""" % (title, description)

def create_html_link(url, title):
    return """<a href="%s">%s</a>""" % (url, title)

#
# clean output dir
#
shutil.rmtree("./docs/%s" % provider, ignore_errors=True)

#
# get services
#

iql_query = "SHOW EXTENDED SERVICES IN %s" % provider

print("running %s..." % iql_query)
try:
    services = pd.read_json(iql.execute(iql_query))
except:
    print("ERROR [%s]" % iql_query)

#
# generate provider root doc
#
 
provider_doc = generate_front_matter("%s %s" % (provider, provider_ver), "A description of the provider.")

#
# add auth block to provider doc
# 

provider_doc = provider_doc + "## Authentication\n"

#
# add services to provider doc
# 

provider_doc = provider_doc + "## Services\n"

num_services = services.shape[0]
first_col_len = ceil(num_services/2.0)

provider_doc = provider_doc + '<div class="row">' + '\n'
# col1
provider_doc = provider_doc + '<div class="providerDocColumn">' + '\n'
for serviceIx, serviceRow in services.iterrows():
    if serviceIx < first_col_len:
        provider_doc = provider_doc + create_html_link("/docs/providers/%s/%s" % (provider, serviceRow["name"]), serviceRow["name"]) + "<br />\n"
provider_doc = provider_doc + '</div>' + '\n'
# col2
provider_doc = provider_doc + '<div class="providerDocColumn">' + '\n'
for serviceIx, serviceRow in services.iterrows():
    if serviceIx >= first_col_len:
        provider_doc = provider_doc + create_html_link("/docs/providers/%s/%s" % (provider, serviceRow["name"]), serviceRow["name"]) + "<br />\n"
provider_doc = provider_doc + "</div>\n</div>\n"

#
# create output dir
#
try:
    os.mkdir("./docs/%s" % provider)
except FileExistsError:
    print("directory already exists, skipping...")
except:
    print("ERROR: unknown error")
    sys.exit(1)
    
#
# write provider doc
#

file = open("./docs/%s/index.md" % provider, "w")
file.write(provider_doc)
file.close

#
# create service and resource docs
#

for serviceIx, serviceRow in services.iterrows():
    # create service dir
    try:
        os.mkdir("./docs/%s/%s" % (provider, serviceRow["name"]))
    except FileExistsError:
        print("directory already exists, skipping...")
    except:
        print("ERROR: unknown error")
        sys.exit(1)
    # create service doc
    service_doc = generate_front_matter(serviceRow["name"], serviceRow["description"])
    service_doc = service_doc + "## Overview\n"
    service_doc = service_doc + "<table><tbody>\n"
    service_doc = service_doc + "<tr><td><b>Name</b></td><td><code>%s.%s</code></td></tr>\n" % (provider, serviceRow["name"])
    service_doc = service_doc + "<tr><td><b>Title</b></td><td>%s</td></tr>\n" % serviceRow["title"]
    service_doc = service_doc + "<tr><td><b>Description</b></td><td>%s</td></tr>\n" % serviceRow["description"]
    service_doc = service_doc + "<tr><td><b>Id</b></td><td><code>%s</code></td></tr>\n" % serviceRow["id"]
    service_doc = service_doc + "<tr><td><b>Version</b></td><td>%s</td></tr>\n" % serviceRow["version"]
    service_doc = service_doc + "</tbody></table>\n\n"

    #
    # get resources
    #

    iql_query = "SHOW EXTENDED RESOURCES IN %s.%s" % (provider, serviceRow["name"])

    #print("running %s..." % iql_query)
    try:
        resources = pd.read_json(iql.execute(iql_query))
    except:
        print("ERROR [%s]" % iql_query)

    num_resources = resources.shape[0]
    first_col_len = ceil(num_resources/2.0)

    service_doc = service_doc + "## Resources\n"
    service_doc = service_doc + '<div class="row">' + '\n'
    # col1
    service_doc = service_doc + '<div class="providerDocColumn">' + '\n'
    for resourceIx, resourceRow in resources.iterrows():
        if resourceIx < first_col_len:
            service_doc = service_doc + create_html_link("/docs/providers/%s/%s/%s" % (provider, serviceRow["name"], resourceRow["name"]), resourceRow["name"]) + "<br />\n"
    service_doc = service_doc + '</div>' + '\n'
    # col2
    service_doc = service_doc + '<div class="providerDocColumn">' + '\n'
    for resourceIx, resourceRow in resources.iterrows():
        if resourceIx >= first_col_len:
            service_doc = service_doc + create_html_link("/docs/providers/%s/%s/%s" % (provider, serviceRow["name"], resourceRow["name"]), resourceRow["name"]) + "<br />\n"
    service_doc = service_doc + "</div>\n</div>\n"

    # write service doc
    file = open("./docs/%s/%s/index.md" % (provider, serviceRow["name"]), "w")
    file.write(service_doc)
    file.close

    for resourceIx, resourceRow in resources.iterrows():
        #
        # create resource dir
        #
        try:
            os.mkdir("./docs/%s/%s/%s" % (provider, serviceRow["name"], resourceRow["name"]))
        except FileExistsError:
            print("directory already exists, skipping...")
        except:
            print("ERROR: unknown error")
            sys.exit(1)
        # create resource doc
        resource_doc = generate_front_matter(resourceRow["name"], resourceRow["description"])
        resource_doc = resource_doc + "## Overview\n"
        resource_doc = resource_doc + "<table><tbody>\n"
        resource_doc = resource_doc + "<tr><td><b>Name</b></td><td><code>%s</code></td></tr>\n" % resourceRow["name"]
        resource_doc = resource_doc + "<tr><td><b>Id</b></td><td><code>%s</code></td></tr>\n" % resourceRow["id"]
        resource_doc = resource_doc + "<tr><td><b>Description</b></td><td>%s</td></tr>\n" % resourceRow["description"]
        resource_doc = resource_doc + "</tbody></table>\n\n"
        resource_doc = resource_doc + "## Fields\n"

        iql_query = "DESCRIBE EXTENDED %s.%s.%s" % (provider, serviceRow["name"], resourceRow["name"])

        #print("running %s..." % iql_query)
        try:
            fields = pd.read_json(iql.execute(iql_query))
        except:
            print("ERROR [%s]" % iql_query)

        if fields.shape[0] > 1:
            resource_doc = resource_doc + "| Name | Datatype | Description |\n"
            resource_doc = resource_doc + "| ---- | -------- | ----------- |\n"
            for fieldIx, fieldRow in fields.iterrows():
                resource_doc = resource_doc + "| `%s` | `%s` | %s |\n" % (fieldRow["name"], fieldRow["type"], fieldRow["description"].replace("<", "&#x7B;").replace(">", "&#x7D;").replace("\n", "<br />").replace("|", "\|"))
        else:
            resource_doc = resource_doc + "`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  \n"
        resource_doc = resource_doc + "## Methods\n"

        iql_query = "SHOW EXTENDED METHODS IN %s.%s.%s" % (provider, serviceRow["name"], resourceRow["name"])

        #print("running %s..." % iql_query)
        try:
            methods = pd.read_json(iql.execute(iql_query))
        except:
            print("ERROR [%s] retrying..." % iql_query)
            #methods = pd.read_json(iql.execute(iql_query))

        # for methodIx, methodRow in methods.iterrows():
        #     resource_doc = resource_doc + "<table><thead>\n"
        #     resource_doc = resource_doc + "<tr><td>Name</td></tr>\n"
        #     resource_doc = resource_doc + "<tr><td>Required Params</td></tr>\n"
        #     resource_doc = resource_doc + "<tr><td>Description</td></tr>\n"
        #     resource_doc = resource_doc + "<tr><td>Accessible by</td></tr>\n"
        #     resource_doc = resource_doc + "</thead><tbody>\n"
        #     resource_doc = resource_doc + "<tr><td><code>%s</code></td></tr>\n" % methodRow["MethodName"]
        #     resource_doc = resource_doc + "<tr><td><code>%s</code></td></tr>\n" % methodRow["RequiredParams"]
        #     resource_doc = resource_doc + "<tr><td>%s</td></tr>\n" % methodRow["SQLVerb"]
        #     resource_doc = resource_doc + "</tbody></table>\n\n"

        #
        # write resource doc
        #
        file = open("./docs/%s/%s/%s/index.md" % (provider, serviceRow["name"], resourceRow["name"]), "w")
        file.write(resource_doc)
        file.close

    