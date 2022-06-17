---
title: meta
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
<tr><td><b>Name</b></td><td><code>github.meta.meta</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.meta.meta</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `api` | `array` |  |
| `git` | `array` |  |
| `actions` | `array` |  |
| `dependabot` | `array` |  |
| `hooks` | `array` |  |
| `ssh_keys` | `array` |  |
| `pages` | `array` |  |
| `web` | `array` |  |
| `importer` | `array` |  |
| `packages` | `array` |  |
| `ssh_key_fingerprints` | `object` |  |
| `verifiable_password_authentication` | `boolean` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `` | Returns meta information about GitHub, including a list of GitHub's IP addresses. For more information, see "[About GitHub's IP addresses](https://docs.github.com/articles/about-github-s-ip-addresses/)."<br /><br />**Note:** The IP addresses shown in the documentation's response are only example values. You must always query the API directly to get the latest list of IP addresses. | SELECT |
| `get_octocat` | `` | Get the octocat as ASCII art | EXEC |
| `get_zen` | `` | Get a random sentence from the Zen of GitHub | EXEC |
| `root` | `` | Get Hypermedia links to resources accessible in GitHub's REST API | EXEC |
