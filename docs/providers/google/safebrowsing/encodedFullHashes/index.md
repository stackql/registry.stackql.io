---
title: encodedFullHashes
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
<tr><td><b>Name</b></td><td><code>encodedFullHashes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.safebrowsing.encodedFullHashes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `matches` | `array` | The full hashes that matched the requested prefixes. |
| `minimumWaitDuration` | `string` | The minimum duration the client must wait before issuing any find hashes request. If this field is not set, clients can issue a request as soon as they want. |
| `negativeCacheDuration` | `string` | For requested entities that did not match the threat list, how long to cache the response. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `encodedRequest` |
