# UJ CTF Challenges

This repository contains standalone web security challenges for CTF practice.

## Challenge Folders

- Blind Spot
- Cookies Badger
- Directory Dingo
- Orbital Uplink
- SpikeTheGuard
- The VIP Gate
- Trash Panda VIP

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) must be installed on your host machine.

## Run With Docker

Build and run from inside each challenge folder.

### Example 1: Running a Standard Challenge

```bash
cd "Blind Spot"
docker build -t blind-spot .
docker run --rm -p 5000:5000 blind-spot
```

**Next step:** Once the terminal shows the server is running, open your browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000)\*

**To stop:** Simply press `Ctrl+C` in your terminal. The container will automatically be removed.\*

## Dependencies

Each challenge contains its own `requirements.txt` and `Dockerfile`.

## Notes

- Challenge flags are intentionally included for CTF packaging.
- Apps bind to `0.0.0.0` and support the `PORT` environment variable defaults.

---

**Author**: Mohammad Al Musa
