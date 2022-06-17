---
title: github
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
REGISTRY PULL github v0.3.1;
```

## Authentication
```javascript
{
    "github": {
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
AUTH='{ "github": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json" }}
stackql shell --auth="${AUTH}"
```
## Services
<div class="row">
<div class="providerDocColumn">
<a href="/docs/providers/github/actions">actions</a><br />
<a href="/docs/providers/github/activity">activity</a><br />
<a href="/docs/providers/github/apps">apps</a><br />
<a href="/docs/providers/github/billing">billing</a><br />
<a href="/docs/providers/github/checks">checks</a><br />
<a href="/docs/providers/github/code_scanning">code_scanning</a><br />
<a href="/docs/providers/github/codes_of_conduct">codes_of_conduct</a><br />
<a href="/docs/providers/github/codespaces">codespaces</a><br />
<a href="/docs/providers/github/dependabot">dependabot</a><br />
<a href="/docs/providers/github/enterprise_admin">enterprise_admin</a><br />
<a href="/docs/providers/github/gists">gists</a><br />
<a href="/docs/providers/github/git">git</a><br />
<a href="/docs/providers/github/gitignore">gitignore</a><br />
<a href="/docs/providers/github/interactions">interactions</a><br />
<a href="/docs/providers/github/issues">issues</a><br />
<a href="/docs/providers/github/licenses">licenses</a><br />
</div>
<div class="providerDocColumn">
<a href="/docs/providers/github/markdown">markdown</a><br />
<a href="/docs/providers/github/meta">meta</a><br />
<a href="/docs/providers/github/migrations">migrations</a><br />
<a href="/docs/providers/github/oauth_authorizations">oauth_authorizations</a><br />
<a href="/docs/providers/github/orgs">orgs</a><br />
<a href="/docs/providers/github/packages">packages</a><br />
<a href="/docs/providers/github/projects">projects</a><br />
<a href="/docs/providers/github/pulls">pulls</a><br />
<a href="/docs/providers/github/rate_limit">rate_limit</a><br />
<a href="/docs/providers/github/reactions">reactions</a><br />
<a href="/docs/providers/github/repos">repos</a><br />
<a href="/docs/providers/github/scim">scim</a><br />
<a href="/docs/providers/github/search">search</a><br />
<a href="/docs/providers/github/secret_scanning">secret_scanning</a><br />
<a href="/docs/providers/github/teams">teams</a><br />
<a href="/docs/providers/github/users">users</a><br />
</div>
</div>
