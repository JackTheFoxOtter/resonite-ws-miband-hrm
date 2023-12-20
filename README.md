# Resonite Websocket Miband HRM
This is a super rudimentary adapter to connect a ProtoFlux websocket client (or any websocket client really) to a heartbeat tracking wristband I quickly whippped together to help a user on Resonite.

It's based on https://vard88508.github.io/vrc-osc-miband-hrm/, which implements a browser interface that connects to the wristband via Bluetooth and then connects to the vrc-osc-hrm.exe via websocket, which forwards the messages as OSC to VRChat.
This script basically replaces that executable, so the website talks directly to the relay script, which will forward all messages it receives to every connected websocket client.

## How to use
1. Install required package with pip (pip install websockets)
2. Launch this script (python -m ./server.py)
3. Open https://vard88508.github.io/vrc-osc-miband-hrm/html/ in your browser, it should automatically connect to the relay (on ws://localhost:3228)
4. in your browser and connect your heartrate monitor
5. Connect a compatible websocket client (for example implemented in ProtoFlux for Resonite) to ws://localhost:3229

That's it! The websocket client should now receive every message sent by the heartbeat tracking wristband.
If you filter out everything that's not an integer, you now have the BPM readings to do whatever you want with!