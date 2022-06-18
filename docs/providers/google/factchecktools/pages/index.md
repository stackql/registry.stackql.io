---
title: pages
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
<tr><td><b>Name</b></td><td><code>pages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.factchecktools.pages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `claimReviewMarkupPages` | `array` | The result list of pages of `ClaimReview` markup. |
| `nextPageToken` | `string` | The next pagination token in the Search response. It should be used as the `page_token` for the following request. An empty value means no more results. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `pagesId` | Get all `ClaimReview` markup on a page. |
| `list` | `SELECT` |  | List the `ClaimReview` markup pages for a specific URL or for an organization. |
| `create` | `INSERT` |  | Create `ClaimReview` markup on a page. |
| `delete` | `DELETE` | `pagesId` | Delete all `ClaimReview` markup on a page. |
| `update` | `EXEC` | `pagesId` | Update for all `ClaimReview` markup on a page Note that this is a full update. To retain the existing `ClaimReview` markup on a page, first perform a Get operation, then modify the returned markup, and finally call Update with the entire `ClaimReview` markup as the body. |
