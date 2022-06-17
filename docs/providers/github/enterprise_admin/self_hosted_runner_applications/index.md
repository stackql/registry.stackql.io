---
title: self_hosted_runner_applications
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
<tr><td><b>Name</b></td><td><code>github.enterprise_admin.self_hosted_runner_applications</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.enterprise_admin.self_hosted_runner_applications</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `os` | `string` |  |
| `sha256_checksum` | `string` |  |
| `temp_download_token` | `string` | A short lived bearer token used to download the runner, if needed. |
| `architecture` | `string` |  |
| `download_url` | `string` |  |
| `filename` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_runner_applications_for_enterprise` | `enterprise` | Lists binaries for the runner application that you can download and run.<br /><br />You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint. | SELECT |
