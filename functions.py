import os, sys, json, pandas as pd
from math import ceil
from pystackql import StackQL
iql = StackQL(exe="./stackql")

def create_dir(dirName, verbose):
    if verbose:
        print("creating directory %s..." % dirName)
    try:
        os.mkdir(dirName)
    except FileExistsError:
        print("ERROR: directory already exists")
        #sys.exit(1)
    except:
        print("ERROR: unknown error")
        sys.exit(1)

def write_file(fileName, contents, verbose):
    if verbose:
        print("writing file %s..." % fileName)
    file = open(fileName, "w")
    file.write(contents)
    file.close

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
    
""" % (title, description)

def generate_see_also_links():
    return """
See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 
"""

def generate_installation_block(provider, version):
    return """
## Installation
```bash
REGISTRY PULL %s %s;
```
""" % (provider, version)

def generate_auth_block(provider):
    return """
## Authentication
```javascript
{
    "%s": {
        /**
            * Type of authentication to use, suported values include: service_account, api_key, basic
            * @type String
            */
        "type": string, 
        /**
            * path to service account key file.
            * @type String
            */
        "credentialsfilepath": string, 
        /**
            * Environment variable name containing the api key or credentials.
            * @type String
            */
        "credentialsenvvar": string, 
        /**
            * Value prepended to the request header, e.g. "Bearer "
            * @type String
            */
        "valuePrefix": string, 
    }
}
```
### Example
```bash
AUTH='{ "%s": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json" }}
stackql shell --auth="${AUTH}"
```
""" % (provider, provider)

def generate_two_col_list(provider, list_of_objects, service_name=None):
    num_objects = list_of_objects.shape[0]
    first_col_len = ceil(num_objects/2.0)
    output = '<div class="row">\n'
    # col1
    output = output + '<div class="providerDocColumn">\n'
    for ix, this_obj in list_of_objects.iterrows():
        if service_name is None:
            link = create_html_link("/docs/providers/%s/%s" % (provider, this_obj["name"]), this_obj["name"])
        else:
            link = create_html_link("/docs/providers/%s/%s/%s" % (provider, service_name, this_obj["name"]), this_obj["name"])
        if ix < first_col_len:
            output = output + link + "<br />\n"
    output = output + '</div>\n'
    # col2
    output = output + '<div class="providerDocColumn">\n'
    for ix, this_obj in list_of_objects.iterrows():
        if service_name is None:
            link = create_html_link("/docs/providers/%s/%s" % (provider, this_obj["name"]), this_obj["name"])
        else:
            link = create_html_link("/docs/providers/%s/%s/%s" % (provider, service_name, this_obj["name"]), this_obj["name"])
        if ix >= first_col_len:
            output = output + link + "<br />\n"
    output = output + '</div>\n'
    output = output + '</div>\n'
    return output

def generate_service_overview(provider, serviceObj):
    return """
## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>%s.%s</code></td></tr>
<tr><td><b>Title</b></td><td>%s</td></tr>
<tr><td><b>Description</b></td><td>%s</td></tr>
<tr><td><b>Id</b></td><td><code>%s</code></td></tr>
<tr><td><b>Version</b></td><td>%s</td></tr>
</tbody></table>

""" % (provider, serviceObj["name"], serviceObj["title"], serviceObj["description"], serviceObj["id"], serviceObj["version"])


def generate_resource_overview(provider, serviceName, resourceObj):
    return """
## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>%s.%s.%s</code></td></tr>
<tr><td><b>Id</b></td><td><code>%s</code></td></tr>
<tr><td><b>Description</b></td><td>%s</td></tr>
</tbody></table>

""" % (provider, serviceName, resourceObj["name"], resourceObj["id"], resourceObj["description"])

def generate_fields_table(fields):
    output = "## Fields\n"
    if fields.shape[0] > 1:
        output = output + "| Name | Datatype | Description |\n"
        output = output + "| ---- | -------- | ----------- |\n"
        for fieldIx, fieldRow in fields.iterrows():
            output = output + "| `%s` | `%s` | %s |\n" % (fieldRow["name"], fieldRow["type"], fieldRow["description"].replace("<", "&#x7B;").replace(">", "&#x7D;").replace("\n", "<br />").replace("|", "\|"))
    else:
        output = output + "`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  \n"
    return output

def generate_methods_table(methods):
    output = "## Methods\n"
    output = output + "| Name | Required Params | Description | Accessible by |\n"
    output = output + "| ---- | --------------- | ----------- | ------------- |\n"
    for methodIx, methodRow in methods.iterrows():
        output = output + "| `%s` | `%s` | %s | %s |\n" % (methodRow["MethodName"], methodRow["RequiredParams"], methodRow["description"].replace("<", "&#x7B;").replace(">", "&#x7D;").replace("\n", "<br />").replace("|", "\|"), methodRow["SQLVerb"])
    return output

def run_stackql_query(query, verbose, retries):
    if verbose:
        print("running %s..." % query)
    try:
        resp = iql.execute(query)
        resp_dict = json.loads(resp)
        return pd.DataFrame.from_dict(resp_dict)
    except:
        print("retrying [%s] (%s left)" % (query, retries))
        if retries > 0:
            return run_stackql_query(query, verbose, retries-1)
        else:
            print("ERROR [%s]" % query)
            return None

def create_html_link(url, title):
    return """<a href="%s">%s</a>""" % (url, title)