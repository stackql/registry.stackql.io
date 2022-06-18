---
title: okta
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
A description of the provider.  
    

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation
```bash
REGISTRY PULL okta v0.1.0;
```

## Authentication
```javascript
{
    "okta": {
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
AUTH='{ "okta": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json" }}
stackql shell --auth="${AUTH}"
```
## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/okta/application/index.md">application</a><br />
<a href="/providers/okta/authenticator/index.md">authenticator</a><br />
<a href="/providers/okta/authorizationserver/index.md">authorizationserver</a><br />
<a href="/providers/okta/domain/index.md">domain</a><br />
<a href="/providers/okta/eventhook/index.md">eventhook</a><br />
<a href="/providers/okta/feature/index.md">feature</a><br />
<a href="/providers/okta/group/index.md">group</a><br />
<a href="/providers/okta/groupschema/index.md">groupschema</a><br />
<a href="/providers/okta/identityprovider/index.md">identityprovider</a><br />
<a href="/providers/okta/inlinehook/index.md">inlinehook</a><br />
<a href="/providers/okta/linkedobject/index.md">linkedobject</a><br />
<a href="/providers/okta/log/index.md">log</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/okta/networkzone/index.md">networkzone</a><br />
<a href="/providers/okta/org/index.md">org</a><br />
<a href="/providers/okta/policy/index.md">policy</a><br />
<a href="/providers/okta/profilemapping/index.md">profilemapping</a><br />
<a href="/providers/okta/session/index.md">session</a><br />
<a href="/providers/okta/template/index.md">template</a><br />
<a href="/providers/okta/threatinsight/index.md">threatinsight</a><br />
<a href="/providers/okta/trustedorigin/index.md">trustedorigin</a><br />
<a href="/providers/okta/user/index.md">user</a><br />
<a href="/providers/okta/userfactor/index.md">userfactor</a><br />
<a href="/providers/okta/userschema/index.md">userschema</a><br />
<a href="/providers/okta/usertype/index.md">usertype</a><br />
</div>
</div>
