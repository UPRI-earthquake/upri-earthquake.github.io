Web Application Features
========================

The current EarthquakeHub web application combines live seismic monitoring with event detail, station waveform access, account management, and contributor tools.

## Map and event views

The map supports multiple basemaps and operational overlays for stations, earthquakes, fault lines, plate boundaries, and the Philippine Area of Responsibility. Event filters and presets support time, magnitude, depth, and region-based browsing. Event details can include source/catalog comparisons, derived place information, candidate stations, recording stations, and recording-availability status.

Waveform downloads use the configured FDSNWS service. Availability states distinguish a station that is geographically near an event from a station whose waveform data has been confirmed.

## Accounts and device management

Contributor accounts can link and unlink Raspberry Shake devices, manage device location metadata, inspect device status, configure ringserver targets, and recover account access through password-reset email links. The default UPRI ringserver is protected from accidental removal by sender/backend policy.

Remote device actions and tunnel enrollment are restricted operations. See :doc:`remote-tunnel` for the server/device boundary and operator workflow.

## Community reports and notifications

Event pages can expose moderated community reports/comments with pagination and public-safe response shaping. The web application can also register browser push subscriptions through ``POST /api/notifications/subscribe``. Notification and analytics behavior should respect the application's consent and account settings.

## Backend endpoints for maintainers

The backend ``dev`` baseline includes these feature groups:

- ``/api/eq-events`` for event lists, direct event detail, summaries, and restricted enrichment maintenance.
- ``/api/overlays/faults``, ``/api/overlays/plates``, and ``/api/overlays/par`` for cached GeoJSON overlays.
- ``/api/comments`` for moderated event reports/comments.
- ``/api/accounts/reset-password`` for password recovery.
- ``/api/notifications/subscribe`` for web-push subscriptions.
- ``/api/device/tunnel/*`` and ``/api/device/remote-actions/*`` for restricted remote-device workflows.

API response fields and authorization requirements can change with the backend release. Treat the synchronized backend API schema as authoritative and do not copy credentials or restricted endpoint payloads into public examples.
