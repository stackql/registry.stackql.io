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
<a href="/providers/netlify/access_token/index.md">access_token</a><br />
<a href="/providers/netlify/account_membership/index.md">account_membership</a><br />
<a href="/providers/netlify/account_type/index.md">account_type</a><br />
<a href="/providers/netlify/asset/index.md">asset</a><br />
<a href="/providers/netlify/asset_public_signature/index.md">asset_public_signature</a><br />
<a href="/providers/netlify/audit_log/index.md">audit_log</a><br />
<a href="/providers/netlify/build/index.md">build</a><br />
<a href="/providers/netlify/build_hook/index.md">build_hook</a><br />
<a href="/providers/netlify/build_log_msg/index.md">build_log_msg</a><br />
<a href="/providers/netlify/deploy/index.md">deploy</a><br />
<a href="/providers/netlify/deploy_key/index.md">deploy_key</a><br />
<a href="/providers/netlify/deployed_branch/index.md">deployed_branch</a><br />
<a href="/providers/netlify/dns_zone/index.md">dns_zone</a><br />
<a href="/providers/netlify/file/index.md">file</a><br />
<a href="/providers/netlify/form/index.md">form</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/netlify/function/index.md">function</a><br />
<a href="/providers/netlify/hook/index.md">hook</a><br />
<a href="/providers/netlify/hook_type/index.md">hook_type</a><br />
<a href="/providers/netlify/member/index.md">member</a><br />
<a href="/providers/netlify/metadata/index.md">metadata</a><br />
<a href="/providers/netlify/payment_method/index.md">payment_method</a><br />
<a href="/providers/netlify/service/index.md">service</a><br />
<a href="/providers/netlify/service_instance/index.md">service_instance</a><br />
<a href="/providers/netlify/site/index.md">site</a><br />
<a href="/providers/netlify/sni_certificate/index.md">sni_certificate</a><br />
<a href="/providers/netlify/snippet/index.md">snippet</a><br />
<a href="/providers/netlify/split_test/index.md">split_test</a><br />
<a href="/providers/netlify/submission/index.md">submission</a><br />
<a href="/providers/netlify/ticket/index.md">ticket</a><br />
<a href="/providers/netlify/user/index.md">user</a><br />
</div>
</div>
