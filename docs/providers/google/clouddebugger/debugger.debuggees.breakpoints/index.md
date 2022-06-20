---
title: debugger.debuggees.breakpoints
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
<tr><td><b>Name</b></td><td><code>debugger.debuggees.breakpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.clouddebugger.debugger.debuggees.breakpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextWaitToken` | `string` | A wait token that can be used in the next call to `list` (REST) or `ListBreakpoints` (RPC) to block until the list of breakpoints has changes. |
| `breakpoints` | `array` | List of breakpoints matching the request. The fields `id` and `location` are guaranteed to be set on each breakpoint. The fields: `stack_frames`, `evaluated_expressions` and `variable_table` are cleared on each breakpoint regardless of its status. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `breakpointId, debuggeeId` | Gets breakpoint information. |
| `list` | `SELECT` | `debuggeeId` | Lists all breakpoints for the debuggee. |
| `delete` | `DELETE` | `breakpointId, debuggeeId` | Deletes the breakpoint from the debuggee. |
| `set` | `EXEC` | `debuggeeId` | Sets the breakpoint to the debuggee. |
