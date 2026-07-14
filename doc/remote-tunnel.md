Remote Device Tunnel (SSH over WebSocket)
=========================================

EarthquakeHub supports optional remote access to deployed Raspberry Shake devices through a reverse SSH tunnel carried over WebSocket by ``wstunnel``. The tunnel is intended for authorized operations staff and is separate from ordinary waveform streaming.

## Architecture

The deployed commons ``dep-improvements`` branch owns the server-side tunnel endpoint, bastion registry, and operator access path. The sender-backend ``dev`` branch owns the device-side service and enrollment helper. The backend ``dev`` branch provides the enrollment API.

The path is:

``RShake → sender-remote-tunnel.service → wstunnel WebSocket → nginx /api/ws-tunnel/<secret>/ → wstunnel-server → bastion port → device SSH``

The deployment uses ``earthquake.up.edu.ph``. The WebSocket path prefix contains a deployment-specific secret and must not be copied into public issue reports or documentation.

## Device-side setup

Install or refresh the sender service on the device, then use the helper supplied by sender-backend:

```bash
sudo sender-setup-remote-tunnel \
  --enroll-token "<sensor access token>" \
  --enroll-endpoint "https://earthquake.up.edu.ph/api/device/tunnel/enroll"
```

If the command is being run from a checkout, use ``sudo ./setup-remote-tunnel.sh`` instead. The helper can discover an existing sender token when ``--enroll-token`` is omitted, but explicit enrollment is preferred for first-time setup.

The helper writes ``/etc/upri/sender-remote-tunnel.env``, installs the service, and restarts it. Enrollment returns the device mapping and WebSocket settings. The device service is disabled by default until the environment file has ``REMOTE_TUNNEL_ENABLED=true`` and valid mapping data.

Useful device commands:

```bash
sudo sender-backend INSTALL_REMOTE_TUNNEL_SERVICE
sudo sender-backend REMOTE_TUNNEL_STATUS
sudo systemctl status sender-remote-tunnel.service
curl http://localhost:5001/health/sender-state
```

## Server-side enrollment and access

The backend routes are:

- ``POST /api/device/tunnel/enroll`` — sensor bearer token required.
- ``GET /api/device/tunnel/mappings`` — administrator session required.
- ``POST /api/device/tunnel/revoke`` — administrator session required.

The commons bastion scripts maintain the server-side registry:

- ``bastion/register-device.sh``
- ``bastion/revoke-device.sh``
- ``bastion/list-devices.sh``

After connecting to the approved VPN and bastion, an operator uses the assigned reverse port:

```bash
ssh -p <assigned-remote-port> myshake@127.0.0.1
```

Use ``sudo`` on the device only when required. Do not expose the bastion, registry, private keys, enrollment tokens, or secret WebSocket prefix publicly.

## Troubleshooting

- ``404`` during WebSocket connection usually means the sender path prefix does not match the nginx ``/api/ws-tunnel/<secret>/`` location.
- ``504`` usually means nginx cannot reach ``wstunnel-server`` on the configured host port.
- ``400 not allowed destination`` indicates that ``wstunnel-restrictions.yaml`` rejected the requested reverse listener.
- An enrollment success does not prove that the tunnel is connected; confirm ``REMOTE_TUNNEL_STATUS``, ``/health/sender-state``, and the service journal.

For deployment checks, use the commons runbook commands such as ``bastion-tunnel CHECK_WSTUNNEL`` and inspect ``docker logs --tail 80 wstunnel-server``. The sender-side implementation details remain in ``sender-backend/docs/remote-tunnel-runbook.md``.
