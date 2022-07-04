---
title: crawled_urls
hide_title: false
hide_table_of_contents: false
keywords:
  - crawled_urls
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
<tr><td><b>Name</b></td><td><code>crawled_urls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.websecurityscanner.crawled_urls</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `url` | `string` | Output only. The URL that was crawled. |
| `body` | `string` | Output only. The body of the request that was used to visit the URL. |
| `httpMethod` | `string` | Output only. The http method of the request that was used to visit the URL, in uppercase. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_scanConfigs_scanRuns_crawledUrls_list` | `SELECT` | `parent` |
