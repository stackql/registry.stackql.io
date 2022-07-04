---
title: flowhooks
hide_title: false
hide_table_of_contents: false
keywords:
  - flowhooks
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
<tr><td><b>Name</b></td><td><code>flowhooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.flowhooks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | Description of the flow hook. |
| `continueOnError` | `boolean` | Optional. Flag that specifies whether execution should continue if the flow hook throws an exception. Set to `true` to continue execution. Set to `false` to stop execution if the flow hook throws an exception. Defaults to `true`. |
| `flowHookPoint` | `string` | Output only. Where in the API call flow the flow hook is invoked. Must be one of `PreProxyFlowHook`, `PostProxyFlowHook`, `PreTargetFlowHook`, or `PostTargetFlowHook`. |
| `sharedFlow` | `string` | Shared flow attached to this flow hook, or empty if there is none attached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_environments_flowhooks_get` | `SELECT` | `name` | Returns the name of the shared flow attached to the specified flow hook. If there's no shared flow attached to the flow hook, the API does not return an error; it simply does not return a name in the response. |
| `organizations_environments_flowhooks_attachSharedFlowToFlowHook` | `EXEC` | `name` | Attaches a shared flow to a flow hook. |
| `organizations_environments_flowhooks_detachSharedFlowFromFlowHook` | `EXEC` | `name` | Detaches a shared flow from a flow hook. |