EarthquakeHub Release Notes
===========================

This page records notable capabilities added to the EarthquakeHub system. It is a historical summary, not a substitute for repository-specific API or deployment documentation. The current summary below is based on the remote project baselines checked on 2026-07-14:

- Documentation: ``upri-earthquake.github.io`` ``main``
- Hub backend/frontend, sender backend/frontend, and connectors: their remote ``dev`` baselines
- Deployment commons: deployed remote ``dep-improvements`` branch

## July 2026 — Current operational baseline

### Hub web application and backend

- Migrated service defaults and public integrations to ``earthquake.up.edu.ph``.
- Added richer earthquake detail pages with direct event loading, stable public event IDs, source/catalog comparison, source provenance, and cached place enrichment.
- Added candidate-station versus verified-recording-station states and FDSN-backed waveform availability checks.
- Added community reports with moderation states, pagination, anonymous/public-safe posting, image validation, helpful votes, private issue reports, and contribution-event tracking.
- Added cached GeoJSON overlay services for faults, plate boundaries, and the Philippine Area of Responsibility.
- Improved password reset, refresh-token, account/device recovery, and device-link lifecycle handling.
- Added administrator-only RShake alert routing and browser push-notification subscription management.

### Sender client

- Added sender health snapshots for network reachability, time synchronization, host resources, metrics, update state, watchdog state, disk alerts, token refresh state, and remote-tunnel state.
- Added admin-only RShake alerts for disk pressure, token refresh, watchdog recovery, and related delivery outcomes.
- Improved image-bundle update handling, digest tracking, rollback behavior, host-script synchronization, and watchdog recovery.
- Added protected default-ringserver behavior and automatic default-ringserver restoration after device linking or startup.
- Added reverse SSH-over-WebSocket support through ``wstunnel``, including automatic enrollment, operator SSH keys, path-prefix configuration, service status, and recovery tooling.

### Deployed commons stack

- Added the deployed ``wstunnel-server`` path behind nginx with restricted reverse-listener destinations and per-deployment WebSocket path prefixes.
- Added edge hardening for suspicious routes, service-prefix normalization, crawler controls, security headers, no-store/noindex service responses, and static-asset caching.
- Updated deployment defaults for the new public hostname, MongoDB 5.0, scoped token/email configuration, analytics settings, and SeisComP inventory-import workflows.

## 2026 — Event detail, contributor, and sender operations

- Introduced the dynamic earthquake detail experience with direct links, resilient loading, local detail caching, summaries, nearby stations, waveform access, and catalog-source enrichment.
- Added editable event summaries and a community-report carousel with responsive report cards and image viewing.
- Added dashboard controls for remote device capabilities, server listing/addition/removal, device recovery, alert preferences, protected ringserver targets, and clearer device states.
- Added password-reset flow, account recovery improvements, device refresh-token handling, released/unlinked-device tracking, and safer link/unlink cleanup.
- Added sender-side health checks, token-status visibility, automatic update timers, stack watchdogs, alert queues, and remote-tunnel enrollment foundations.

## 2025 — Monitoring UI and platform improvements

- Added map layer controls for OSM, Carto, and Esri basemaps, with fault-line and plate-boundary overlays and attribution handling.
- Improved real-time earthquake and station updates through SSE, station status markers, event/station selection synchronization, and live waveform views.
- Added event search, filtering, sorting, presets, map reset controls, clearer legends, depth-based marker colors, and responsive mobile layouts.
- Improved accessibility with keyboard navigation, labels, focus behavior, screen-reader support, and clearer operational state messaging.
- Added consent-aware Google Analytics and optional browser push notifications.
- Improved backend compression, safe GET caching, device-location caching, public event upsert behavior, and station-status messaging.

## 2024 — Public event and contributor foundations

- Added significant-earthquake persistence and retrieval workflows.
- Expanded device activity and station information returned by backend APIs.
- Continued the monitoring-console UI work around earthquake lists, station states, filters, and map interactions.

## 2023 — Initial network architecture

- Established the Docker-based EarthquakeHub commons stack with nginx, frontend, backend, MongoDB, ringserver, and SeisComP integration.
- Implemented JWT-based ringserver write authorization through the EarthquakeHub authentication API.
- Added ringserver support for redundant DataLink connections, duplicate-packet filtering, and SSE diagnostics for streams and connections.
- Added the sender path from Raspberry Shake SeedLink through ``slink2dali`` to the hub ringserver over DataLink.
- Added initial Raspberry Shake linking, ringserver configuration, FDSNWS access, metadata retrieval, and device installation guidance.

## Release-note maintenance

When adding an entry, include the approximate release date, the affected component, and whether the feature is deployed or only available on a development branch. Verify behavior against the relevant remote branch before publishing. Keep operational procedures in the dedicated tutorials and runbooks linked from the documentation index.
