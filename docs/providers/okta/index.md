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
<a href="/providers/okta/application/">application</a><br />
<a href="/providers/okta/authenticator/">authenticator</a><br />
<a href="/providers/okta/authorizationserver/">authorizationserver</a><br />
<a href="/providers/okta/domain/">domain</a><br />
<a href="/providers/okta/eventhook/">eventhook</a><br />
<a href="/providers/okta/feature/">feature</a><br />
<a href="/providers/okta/group/">group</a><br />
<a href="/providers/okta/groupschema/">groupschema</a><br />
<a href="/providers/okta/identityprovider/">identityprovider</a><br />
<a href="/providers/okta/inlinehook/">inlinehook</a><br />
<a href="/providers/okta/linkedobject/">linkedobject</a><br />
<a href="/providers/okta/log/">log</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/okta/networkzone/">networkzone</a><br />
<a href="/providers/okta/org/">org</a><br />
<a href="/providers/okta/policy/">policy</a><br />
<a href="/providers/okta/profilemapping/">profilemapping</a><br />
<a href="/providers/okta/session/">session</a><br />
<a href="/providers/okta/template/">template</a><br />
<a href="/providers/okta/threatinsight/">threatinsight</a><br />
<a href="/providers/okta/trustedorigin/">trustedorigin</a><br />
<a href="/providers/okta/user/">user</a><br />
<a href="/providers/okta/userfactor/">userfactor</a><br />
<a href="/providers/okta/userschema/">userschema</a><br />
<a href="/providers/okta/usertype/">usertype</a><br />
</div>
</div>