---
title: events
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
<tr><td><b>Name</b></td><td><code>events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gamesManagement.events</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `reset` | `EXEC` | `eventId` | Resets all player progress on the event with the given ID for the currently authenticated player. This method is only accessible to whitelisted tester accounts for your application. |
| `resetAll` | `EXEC` |  | Resets all player progress on all events for the currently authenticated player. This method is only accessible to whitelisted tester accounts for your application. |
| `resetAllForAllPlayers` | `EXEC` |  | Resets all draft events for all players. This method is only available to user accounts for your developer console. |
| `resetForAllPlayers` | `EXEC` | `eventId` | Resets the event with the given ID for all players. This method is only available to user accounts for your developer console. Only draft events can be reset. |
| `resetMultipleForAllPlayers` | `EXEC` |  | Resets events with the given IDs for all players. This method is only available to user accounts for your developer console. Only draft events may be reset. |