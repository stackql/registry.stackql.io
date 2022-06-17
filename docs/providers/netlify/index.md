---
title: netlify
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
REGISTRY PULL netlify v0.2.0;
```

## Authentication
```javascript
{
    "netlify": {
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
AUTH='{ "netlify": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json" }}
stackql shell --auth="${AUTH}"
```
## Services
<div class="row">
<div class="providerDocColumn">
<a href="/docs/providers/netlify/access_token">access_token</a><br />
<a href="/docs/providers/netlify/account_membership">account_membership</a><br />
<a href="/docs/providers/netlify/account_type">account_type</a><br />
<a href="/docs/providers/netlify/asset">asset</a><br />
<a href="/docs/providers/netlify/asset_public_signature">asset_public_signature</a><br />
<a href="/docs/providers/netlify/audit_log">audit_log</a><br />
<a href="/docs/providers/netlify/build">build</a><br />
<a href="/docs/providers/netlify/build_hook">build_hook</a><br />
<a href="/docs/providers/netlify/build_log_msg">build_log_msg</a><br />
<a href="/docs/providers/netlify/deploy">deploy</a><br />
<a href="/docs/providers/netlify/deploy_key">deploy_key</a><br />
<a href="/docs/providers/netlify/deployed_branch">deployed_branch</a><br />
<a href="/docs/providers/netlify/dns_zone">dns_zone</a><br />
<a href="/docs/providers/netlify/file">file</a><br />
<a href="/docs/providers/netlify/form">form</a><br />
</div>
<div class="providerDocColumn">
<a href="/docs/providers/netlify/function">function</a><br />
<a href="/docs/providers/netlify/hook">hook</a><br />
<a href="/docs/providers/netlify/hook_type">hook_type</a><br />
<a href="/docs/providers/netlify/member">member</a><br />
<a href="/docs/providers/netlify/metadata">metadata</a><br />
<a href="/docs/providers/netlify/payment_method">payment_method</a><br />
<a href="/docs/providers/netlify/service">service</a><br />
<a href="/docs/providers/netlify/service_instance">service_instance</a><br />
<a href="/docs/providers/netlify/site">site</a><br />
<a href="/docs/providers/netlify/sni_certificate">sni_certificate</a><br />
<a href="/docs/providers/netlify/snippet">snippet</a><br />
<a href="/docs/providers/netlify/split_test">split_test</a><br />
<a href="/docs/providers/netlify/submission">submission</a><br />
<a href="/docs/providers/netlify/ticket">ticket</a><br />
<a href="/docs/providers/netlify/user">user</a><br />
</div>
</div>