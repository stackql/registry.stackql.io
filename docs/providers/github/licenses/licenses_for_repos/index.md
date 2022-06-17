---
title: licenses_for_repos
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>github.licenses.licenses_for_repos</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.licenses.licenses_for_repos</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `name` | `string` |  |
| `license` | `object` | License Simple |
| `download_url` | `string` |  |
| `html_url` | `string` |  |
| `type` | `string` |  |
| `content` | `string` |  |
| `path` | `string` |  |
| `git_url` | `string` |  |
| `_links` | `object` |  |
| `url` | `string` |  |
| `size` | `integer` |  |
| `encoding` | `string` |  |
| `sha` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_for_repo` | `owner, repo` | This method returns the contents of the repository's license file, if one is detected.<br /><br />Similar to [Get repository content](https://docs.github.com/rest/reference/repos#get-repository-content), this method also supports [custom media types](https://docs.github.com/rest/overview/media-types) for retrieving the raw license content or rendered license HTML. | SELECT |
