---
title: transactions
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
<tr><td><b>Name</b></td><td><code>transactions</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.userfactor.transactions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `_links` | `object` |
| `expiresAt` | `string` |
| `factorResult` | `string` |
| `factorResultMessage` | `string` |
| `_embedded` | `object` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get` | `SELECT` | `factorId, transactionId, userId` |
