---
title: management.webPropertyAdWordsLinks
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
<tr><td><b>Name</b></td><td><code>management.webPropertyAdWordsLinks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.analytics.management.webPropertyAdWordsLinks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` | Entity Google Ads link ID |
| `name` | `string` | Name of the link. This field is required when creating a Google Ads link. |
| `profileIds` | `array` | IDs of linked Views (Profiles) represented as strings. |
| `selfLink` | `string` | URL link for this Google Analytics - Google Ads link. |
| `adWordsAccounts` | `array` | A list of Google Ads client accounts. These cannot be MCC accounts. This field is required when creating a Google Ads link. It cannot be empty. |
| `entity` | `object` | Web property being linked. |
| `kind` | `string` | Resource type for entity Google Ads link. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `accountId, webPropertyAdWordsLinkId, webPropertyId` | Returns a web property-Google Ads link to which the user has access. |
| `list` | `SELECT` | `accountId, webPropertyId` | Lists webProperty-Google Ads links for a given web property. |
| `insert` | `INSERT` | `accountId, webPropertyId` | Creates a webProperty-Google Ads link. |
| `delete` | `DELETE` | `accountId, webPropertyAdWordsLinkId, webPropertyId` | Deletes a web property-Google Ads link. |
| `patch` | `EXEC` | `accountId, webPropertyAdWordsLinkId, webPropertyId` | Updates an existing webProperty-Google Ads link. This method supports patch semantics. |
| `update` | `EXEC` | `accountId, webPropertyAdWordsLinkId, webPropertyId` | Updates an existing webProperty-Google Ads link. |
