---
title: okta
hide_title: false
hide_table_of_contents: false
keywords:
  - okta
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
Authentication and authorization services.  

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
      * Type of authentication to use, suported values include:  api_key
      * @type String
      */
     "type": string, 
     /**
      * Environment variable name containing the api key or credentials.
      * @type String
      */
     "credentialsenvvar": string, 
    }
}
```
### Example (Mac/Linux)
```bash

OKTA_SECRET_KEY=yourapikey
AUTH='{ "okta": { "type": "api_key",  "credentialsenvvar": "OKTA_SECRET_KEY" }}'
stackql shell --auth="${AUTH}"

```
### Example (PowerShell)
```powershell

$env:OKTA_SECRET_KEY = "yourapikey"
$Auth = "{ 'okta': { 'type': 'api_key',  'credentialsenvvar': 'OKTA_SECRET_KEY' }}"
stackql.exe shell --auth=$Auth

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
