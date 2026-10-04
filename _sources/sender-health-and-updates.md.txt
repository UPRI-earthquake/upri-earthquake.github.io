Sender Health, Updates, and Recovery
====================================

The sender-backend ``dev`` baseline includes health snapshots, automatic update state, watchdog recovery, token refresh reporting, and device-side alerting. These checks help distinguish a stopped container, a stale image, an expired token, and a broken network path.

## Health endpoints

From the Raspberry Shake, the sender backend listens on port ``5001``:

```bash
curl http://localhost:5001/health/network
curl http://localhost:5001/health/time
curl http://localhost:5001/health/resources
curl http://localhost:5001/health/sender-state
curl http://localhost:5001/health/metrics
```

``/health/sender-state`` reports persisted operational state when available, including token refresh, update, watchdog, disk-alert, and remote-tunnel state. ``/health/metrics`` reports request counters, alert outcomes, and health trend history.

## Update behavior

The host updater uses ``SENDER_BUNDLE_TAG`` (``latest`` by default) and resolves image tags to digests before recreating the sender containers. A published image tag alone does not prove that a device has updated. Confirm the device's update-state file and running container/image digest after the update cycle.

Existing devices may need the one-time bootstrap command:

```bash
bash <(curl -fsSL "https://raw.githubusercontent.com/UPRI-earthquake/sender-backend/dev/update.sh")
```

Normal operator commands remain available through ``sender-backend UPDATE_STACK`` and the installed update timer. Backend and frontend images should use the same bundle version when publishing a release.

## Watchdog and alerts

``sender-backend INSTALL_SERVICE`` installs the daily ``sender-backend-update.timer`` and periodic ``sender-stack-watchdog.timer``. The watchdog checks container state and can restart stopped services. Sender alerts cover disk pressure, token refresh outcomes, and watchdog actions; they are sent to the restricted backend alert endpoint and are intended for administrators.

## Recovery guidance

1. Check ``docker ps -a`` and the health endpoints.
2. Check ``sender-backend REMOTE_TUNNEL_STATUS`` if remote access is involved.
3. Inspect ``/var/lib/upri-sender/update-state.json`` for the last update result.
4. If the first update cycle only refreshed host scripts, allow the next cycle to run or perform the documented second-cycle recovery before reinstalling.
5. Reinstall only when the service state or local files cannot be recovered; preserve device identity and link information where possible.

Do not report a station as updated merely because GHCR contains a new ``latest`` image.
