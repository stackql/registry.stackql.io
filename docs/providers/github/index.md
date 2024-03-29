---
title: github
hide_title: false
hide_table_of_contents: false
keywords:
  - github
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
Web-based version-control and collaboration.    

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
      * Type of authentication to use, suported values include: basic
      * @type String
      */
    "type": string, 
    /**
      * Environment variable name containing the api key or credentials.
      * Variable value must be a base64 encoded string of the form: username:password
      * @type String
      */
    "credentialsenvvar": string, 
  }
}
```
### Example (Mac/Linux)
```bash

export GITHUB_CREDS=$(echo -n 'yourusername:ghp_YOURPERSONALACCESSTOKEN' | base64)
AUTH='{ "github": { "type": "basic", "credentialsenvvar": "GITHUB_CREDS" } }'
stackql shell --auth="${AUTH}"

```
### Example (PowerShell)
```powershell

$env:GITHUB_CREDS = [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes("yourusername:ghp_YOURPERSONALACCESSTOKEN"))
$Auth = "{ 'github': { 'type': 'basic', 'credentialsenvvar': 'GITHUB_CREDS' } }"
stackql shell --auth=$Auth

```
## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/github/actions/">actions</a><br />
<a href="/providers/github/activity/">activity</a><br />
<a href="/providers/github/apps/">apps</a><br />
<a href="/providers/github/billing/">billing</a><br />
<a href="/providers/github/checks/">checks</a><br />
<a href="/providers/github/code_scanning/">code_scanning</a><br />
<a href="/providers/github/codes_of_conduct/">codes_of_conduct</a><br />
<a href="/providers/github/codespaces/">codespaces</a><br />
<a href="/providers/github/dependabot/">dependabot</a><br />
<a href="/providers/github/enterprise_admin/">enterprise_admin</a><br />
<a href="/providers/github/gists/">gists</a><br />
<a href="/providers/github/git/">git</a><br />
<a href="/providers/github/gitignore/">gitignore</a><br />
<a href="/providers/github/interactions/">interactions</a><br />
<a href="/providers/github/issues/">issues</a><br />
<a href="/providers/github/licenses/">licenses</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/github/markdown/">markdown</a><br />
<a href="/providers/github/meta/">meta</a><br />
<a href="/providers/github/migrations/">migrations</a><br />
<a href="/providers/github/oauth_authorizations/">oauth_authorizations</a><br />
<a href="/providers/github/orgs/">orgs</a><br />
<a href="/providers/github/packages/">packages</a><br />
<a href="/providers/github/projects/">projects</a><br />
<a href="/providers/github/pulls/">pulls</a><br />
<a href="/providers/github/rate_limit/">rate_limit</a><br />
<a href="/providers/github/reactions/">reactions</a><br />
<a href="/providers/github/repos/">repos</a><br />
<a href="/providers/github/scim/">scim</a><br />
<a href="/providers/github/search/">search</a><br />
<a href="/providers/github/secret_scanning/">secret_scanning</a><br />
<a href="/providers/github/teams/">teams</a><br />
<a href="/providers/github/users/">users</a><br />
</div>
</div>
