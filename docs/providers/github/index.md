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
<a href="/docs/providers/github/actions/index.md">actions</a><br />
<a href="/docs/providers/github/activity/index.md">activity</a><br />
<a href="/docs/providers/github/apps/index.md">apps</a><br />
<a href="/docs/providers/github/billing/index.md">billing</a><br />
<a href="/docs/providers/github/checks/index.md">checks</a><br />
<a href="/docs/providers/github/code_scanning/index.md">code_scanning</a><br />
<a href="/docs/providers/github/codes_of_conduct/index.md">codes_of_conduct</a><br />
<a href="/docs/providers/github/codespaces/index.md">codespaces</a><br />
<a href="/docs/providers/github/dependabot/index.md">dependabot</a><br />
<a href="/docs/providers/github/enterprise_admin/index.md">enterprise_admin</a><br />
<a href="/docs/providers/github/gists/index.md">gists</a><br />
<a href="/docs/providers/github/git/index.md">git</a><br />
<a href="/docs/providers/github/gitignore/index.md">gitignore</a><br />
<a href="/docs/providers/github/interactions/index.md">interactions</a><br />
<a href="/docs/providers/github/issues/index.md">issues</a><br />
<a href="/docs/providers/github/licenses/index.md">licenses</a><br />
</div>
<div class="providerDocColumn">
<a href="/docs/providers/github/markdown/index.md">markdown</a><br />
<a href="/docs/providers/github/meta/index.md">meta</a><br />
<a href="/docs/providers/github/migrations/index.md">migrations</a><br />
<a href="/docs/providers/github/oauth_authorizations/index.md">oauth_authorizations</a><br />
<a href="/docs/providers/github/orgs/index.md">orgs</a><br />
<a href="/docs/providers/github/packages/index.md">packages</a><br />
<a href="/docs/providers/github/projects/index.md">projects</a><br />
<a href="/docs/providers/github/pulls/index.md">pulls</a><br />
<a href="/docs/providers/github/rate_limit/index.md">rate_limit</a><br />
<a href="/docs/providers/github/reactions/index.md">reactions</a><br />
<a href="/docs/providers/github/repos/index.md">repos</a><br />
<a href="/docs/providers/github/scim/index.md">scim</a><br />
<a href="/docs/providers/github/search/index.md">search</a><br />
<a href="/docs/providers/github/secret_scanning/index.md">secret_scanning</a><br />
<a href="/docs/providers/github/teams/index.md">teams</a><br />
<a href="/docs/providers/github/users/index.md">users</a><br />
</div>
</div>
