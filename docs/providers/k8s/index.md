---
title: k8s
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
REGISTRY PULL k8s v0.1.0;
```

## Authentication
```javascript
{
    "k8s": {
        /**
            * Type of authentication to use, suported values include: api_key
            * @type String
            */
        "type": string, 
        /**
            * Environment variable name containing the api key or credentials.
            * @type String
            */
        "credentialsenvvar": string, 
        /**
            * Value prepended to the request header, e.g. "Bearer "
            * Must be set to "Bearer "
            * @type String
            */
        "valuePrefix": string, 
    }
}
```

:::note

__`cluster_addr`__ is a required paramter for all operations using the `k8s` provider, for example:  

```sql
SELECT name, namespace, uid, creationTimestamp 
FROM k8s.core_v1.service_account 
WHERE cluster_addr = '35.244.65.136' AND namespace = 'kube-system' 
ORDER BY name ASC;
```
:::

### Example
```bash
export K8S_TOKEN='eyJhbGciOiJ...'
AUTH='{ "k8s": { "type": "api_key", "valuePrefix": "Bearer ", "credentialsenvvar": "K8S_TOKEN" } }'
stackql shell --auth="${AUTH}"
```
## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/k8s/core/">core</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/k8s/core_v1/">core_v1</a><br />
</div>
</div>
