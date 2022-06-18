---
title: repricingrules
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
<tr><td><b>Name</b></td><td><code>repricingrules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.content.repricingrules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `repricingRules` | `array` | The rules from the specified merchant. |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `merchantId, ruleId` | Retrieves a repricing rule from your Merchant Center account. |
| `list` | `SELECT` | `merchantId` | Lists the repricing rules in your Merchant Center account. |
| `create` | `INSERT` | `merchantId` | Creates a repricing rule for your Merchant Center account. |
| `delete` | `DELETE` | `merchantId, ruleId` | Deletes a repricing rule in your Merchant Center account. |
| `patch` | `EXEC` | `merchantId, ruleId` | Updates a repricing rule in your Merchant Center account. All mutable fields will be overwritten in each update request. In each update, you must provide all required mutable fields, or an error will be thrown. If you do not provide an optional field in the update request, if that field currently exists, it will be deleted from the rule. |
